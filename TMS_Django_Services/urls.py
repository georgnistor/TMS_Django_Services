"""TMS_Services URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views1
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))112345
"""
from django.urls import path

from servicesapp.views import ListFigos, ListLicense, FilteredFileList, GetFile, TestStationInfo
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^synchronization/figo', ListFigos.as_view(), name='List figos'),
    url(r'^synchronization/teststationinfo', TestStationInfo.as_view(), name='Test station info'),
    url(r'^configuration/license', ListLicense.as_view(), name='Get license'),
    url(r'^stationsync/stationfiles', FilteredFileList.as_view(), name='Get station files'),
    url(r'^stationsync/getfile', GetFile.as_view(), name='Download file'),
]
