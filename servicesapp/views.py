from rest_framework import generics
from servicesapp.models import Figo, Station
from servicesapp.serializers import FigoSerializer, LicenseSerializer, StationSerializer
import hashlib
from rest_framework.response import Response
from rest_framework.views import APIView
import os.path
from anytree import AnyNode
from anytree.exporter import DictExporter
import fnmatch
import datetime
import re
from django.http import HttpResponse


class GetFile(APIView):
    http_method_names = ['get']

    def get(self, request):
        file_path = request.query_params.get('filepath', None)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/octet-stream")
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                return response
        return Response({'file requested': 'does not exist'})


class ListFigos(generics.ListCreateAPIView):
    serializer_class = FigoSerializer
    http_method_names = ['get']

    def get_queryset(self):
        figo_nr = self.request.query_params.get('figonr', None)
        if figo_nr is not None:
            queryset = Figo.objects.filter(figonr=figo_nr).using('all-postgress')
        else:
            queryset = None
        return queryset

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        if queryset is not None:
            serializer = FigoSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({'figonr parameter': 'is NULL'})


class TestStationInfo(generics.ListCreateAPIView):
    serializer_class = StationSerializer
    http_method_names = ['get']

    def get_queryset(self):
        station_id = self.request.query_params.get('stationid', None)
        if station_id is not None:
            queryset = Station.objects.filter(id=station_id).using('all-postgress')
        else:
            queryset = None
        return queryset

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        if queryset is not None:
            serializer = StationSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({'stationid parameter': 'is NULL'})


class FilteredFileList(APIView):
    http_method_names = ['get']

    def get(self, request):
        target_directory = request.query_params.get('targetdir', None)
        file_filter = request.query_params.get('filefilter', None)
        with_dirs= request.query_params.get('withdirs', None)
        dir_filter = request.query_params.get('dirfilter', None)
        return Response(self.dir_structure_to_json_generator(target_directory, file_filter, dir_filter, with_dirs))

    def is_file_machting_filter(self, filepath, filter__list):
        for pattern in filter__list:
            if fnmatch.fnmatch(filepath, pattern):
                return True
        return False

    def has_files_by_filter(self, dir, filter__list): # Iterative search
        directories = [dir]
        while len(directories) > 0:
            directory = directories.pop()
            for name in os.listdir(directory):
                fullpath = os.path.join(directory, name)
                if os.path.isfile(fullpath):
                    if self.is_file_machting_filter(fullpath, filter__list):
                        return True
                elif os.path.isdir(fullpath):
                    directories.append(fullpath)
        return False

    def directory_regex_pattern_matching(self, dirpath, pattern):
        if pattern:
            regexCompile= re.compile(pattern)

            if os.path.isdir(dirpath):
                directories = [dirpath]
                if regexCompile.match(dirpath):
                    return True
            else: #is file
                if regexCompile.match(dirpath):
                    return True
                else:
                    return False

            # iterate in subdirectories to search for the matching pattern
            while len(directories) > 0:
                directory = directories.pop()
                for name in os.listdir(directory):
                    fullpath = os.path.join(directory, name)
                    if os.path.isdir(fullpath):
                        if regexCompile.match(fullpath):
                            return True
                        else:
                            directories.append(fullpath)
            return False
        else:
            return True

    def modification_date(self, filename):
        t = os.path.getmtime(filename)
        return datetime.datetime.fromtimestamp(t)

    def dir_structure_to_json_generator(self, start_dir, ffilter, dfilter, hasdirs):  # Non recursive function
        class Data:
            def __init__(self, path, childD):
                self.path = path
                self.childD = childD

        if ffilter:
            filter_file_list= str(ffilter).split(',')
        else:
            filter_file_list = '*.*'

        if hasdirs is None:
            hasdirs= False
        else:
            if hasdirs == 'True':
                hasdirs = True
            else:
                hasdirs = False

        flag = True
        initial_root = None
        if start_dir and os.path.exists(start_dir):
            start = Data(start_dir, None)
            directories = [start]
            while len(directories) > 0:
                directory = directories.pop()

                if flag:
                    root = AnyNode(type="Directory", path=directory.path)
                    initial_root = root
                    flag = False
                else:
                    root = directory.childD

                for name in os.listdir(directory.path):
                    fullpath = os.path.join(directory.path, name)

                    if os.path.isfile(fullpath):
                        if self.directory_regex_pattern_matching(fullpath, dfilter) and self.is_file_machting_filter(fullpath, filter_file_list):
                            AnyNode(type="File", path=fullpath, lastmodified=str(self.modification_date(fullpath)), parent=root)
                    elif os.path.isdir(fullpath):
                        if hasdirs and\
                                len(os.listdir(fullpath)) > 0 and self.directory_regex_pattern_matching(fullpath, dfilter) and\
                                self.has_files_by_filter(fullpath, filter_file_list):  # Check if the directory is not empty and if the directory contains any of the files from filter
                            child_directory = AnyNode(type="Directory", path=fullpath, parent=root)
                            directories.append(Data(fullpath, child_directory))  # It's a directory, store it.

            exporter = DictExporter()
            data = exporter.export(initial_root)

        else:
            data = {'Directory': 'Does not exist or was not given'}

        return data


class ListLicense(APIView):
    serializer_class = LicenseSerializer
    http_method_names = ['get']

    def get(self, request):
        macaddr = request.query_params.get('macaddr', None)
        licoption = request.query_params.get('licoption', None)
        mydata = self.generate_license_key(macaddr, licoption)
        results = LicenseSerializer(mydata).data
        return Response(results)

    @staticmethod
    def generate_license_key(macaddr, licoption):
        dict = {'1091480153-01': 1, '1091480151-01': 2, '1091480152-01': 3, '1091480142-01': 3, '1091480141-01': 3, '1091480154-01': 5}
        dicLictoLicPrint = {'1091480153-01': 'LIC-L2+', '1091480151-01': 'LIC-10G', '1091480152-01': 'LIC-1G', '1091480142-01': 'LIC-10G', '1091480141-01': 'LIC-10G', '1091480154-01': 'LIC-L3'}

        if licoption.upper() in dict:
            option = dict[licoption.upper()]
        else:
            option = 7  # 7 is an invalid option

        if macaddr != '' and option != 7:

            if option == 1:
                internalOption = ''
                macaddr = 'ethaddr=' + macaddr.upper()
            else:
                macaddr = macaddr.upper()
                internalOption = option - 2

            #print(option)

            macoptionCombined = macaddr + str(internalOption)
            macoptionCombined = macoptionCombined.replace(":", "")

            file = open("/srv/PythonScripts/.regfile", "w")
            file.write(macoptionCombined + '\n')
            file.close()

            macaddr = macaddr.replace('ethaddr=', '')

            mydata= {"macaddr": macaddr, "license": licoption, "option": option, "Key": hashlib.md5(open('/srv/PythonScripts/.regfile', 'rb').read()).hexdigest()[-12:],
                     "licensePrint": dicLictoLicPrint[licoption.upper()], "Success": "True"}
        else:
            mydata = {"macaddr": macaddr, "license": licoption, "option": option, "Key": "NA", "licensePrint": "NA", "Success": "False"}

        return mydata















