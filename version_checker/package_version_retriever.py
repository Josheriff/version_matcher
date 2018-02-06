# -*- coding: utf-8 -*-

class PypiPackageVersionRetriever(object):

    def __init__(self, pypi_client):
        self._pypi_client = pypi_client

    def retrieve_version(self, package_name):
        response = self._pypi_client.get(package_name)
        package_info = response.json()
        package_version = package_info['info']['version']
        return package_version

class PypiClient(object):

    def __init__(self, http_client):
        self.http_client = http_client

    def get(self,package_name):
        url = 'https://pypi.python.org/pypi/{}/json'.format(package_name)
        return self.http_client.get(url)
