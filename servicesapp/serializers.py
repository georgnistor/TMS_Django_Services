from rest_framework import serializers
from servicesapp.models import Figo, Station, StationWorkstep, Locations, FigoWorkstep

class FigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Figo
        fields = ('figonr', 'description', 'test_tc_client_prompt', 'tc_client_prompt', 'fwp_pak_file_name', 'boot_up_time_fwp', 'boot_up_time_reduced')


class LicenseSerializer(serializers.Serializer):
    Key = serializers.CharField(max_length=200)
    Success = serializers.CharField(max_length=200)
    license = serializers.CharField(max_length=200)
    licensePrint = serializers.CharField(max_length=200)
    macaddr = serializers.CharField(max_length=200)
    option = serializers.IntegerField()


class FigoWorkstepSerializer(serializers.ModelSerializer):
    figonr = FigoSerializer()
    class Meta:
        model =  FigoWorkstep
        fields = ('id', 'worksteporder', 'sequencefile', 'optional', 'limitfile', 'spectable', 'resulttable', 'information', 'worksteporder_back',
                  'active_in_use', 'wipcheck_from', 'workstep', 'figonr')


class StationWorkstepSerializer(serializers.ModelSerializer):
    figo_workstep = FigoWorkstepSerializer()
    class Meta:
        model = StationWorkstep
        fields = ('id', 'active_in_use', 'figo_workstep')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ('id', 'description',)


class StationSerializer(serializers.ModelSerializer):
    stationWorksteps = StationWorkstepSerializer(many=True)
    location = LocationSerializer()

    class Meta:
        model = Station
        fields = ('id', 'description', 'information', 'location', 'fsp_ip_addr',
                  'computername', 'active_in_use',  'stationWorksteps')




