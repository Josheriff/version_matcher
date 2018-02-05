# -*- coding: utf-8 -*-

from doublex import Spy, Stub, when
from doublex_expects import have_been_called, have_been_called_with
from expects import expect, equal

INFO_IN_JSON = { 'info': {'version': 42 } }

#--------------------------
class PypiPackageVersionRetriever(object):

    def __init__(self, pypi_client):
        self._pypi_client = pypi_client

    def retrieve_version(self, package_name):
        package_info = self._pypi_client.get(package_name)
        package_version = package_info['info']['version']
        return package_version

class PypiClient(object):

    def __init__(self, http_client):
        self.http_client = http_client

    def get(self,package_name):
        url = 'https://pypi.python.org/pypi/{}/json'.format(package_name)
        return self.http_client.get(url)

#######
#
# 1º Sacar codigo producción a otro archivo y pasar tests
# 2º Sacar codigo del otro test también a otro archivo
# 3º Implementar, lectura de requirements-dev.txt
# 4º Recordar que a PypiClient hay que pasarle el modulo request como colaborador
# 5º Testear todo junto
# 6º Mostrar datos si eso...
#######

with describe('PipyPackageVersionRetriever'):
    with before.each:

        self.a_package_name = 'a name'
        self.pypi_client = Spy(PypiClient)
        when(self.pypi_client).get(self.a_package_name).returns(INFO_IN_JSON)


    with context('when retrieve package version information'):

        with it('calls an pypi_client get method with package name as parameter'):
            sut = PypiPackageVersionRetriever(self.pypi_client)

            sut.retrieve_version(self.a_package_name)

            expect(self.pypi_client.get).to(have_been_called_with(self.a_package_name))

        with it('retrieve a the last version of the package'):

            sut = PypiPackageVersionRetriever(self.pypi_client)

            result = sut.retrieve_version(self.a_package_name)
            expected_result = 42
            expect(result).to(equal(expected_result))


