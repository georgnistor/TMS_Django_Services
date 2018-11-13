from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.db import connections
import psycopg2


class PostgresAuthBackend(ModelBackend):
    def set_runtime_connection_parameters(self, username, password):
        '''Set the runtime_connection parameters'''
        runtime_ccnnection = connections.databases['admin-postgress']
        runtime_ccnnection['USER'] = username
        runtime_ccnnection['PASSWORD'] = password

    def authenticate(self, request, username=None, password=None, **kwargs):
        connection_string = "host = '172.25.1.151' dbname='TMS' port = 5432"
        connection = None
        try:
            connection_string += " user='{}' password='{}'".format(username, password)
            connection = psycopg2.connect(connection_string)
            if connection:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    user = User(username=username, password=password)
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                return user
            return None

        except psycopg2.Error as e:
            print("Unable to connect to the PostgreSQL server, check the connection string!")
        except Exception as error:
            print("Unknown error from psycopg2 module", error)
        finally:
            if connection is not None:
                connection.close()
                self.set_runtime_connection_parameters(username, password)
