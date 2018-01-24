# -*- coding: utf-8 -*-

from doublex import Spy, Stub
from doublex_expects import have_been_called, have_been_called_with
from expects import expect

#--------------------------
class PypiPackageVersionRetriever(object):

    def __init__(self, http_client):
        self._http_client = http_client

    def retrieve_version(self, package_name):
        url = 'https://pypi.python.org/pypi/{}/json'.format(package_name)
        self._http_client.get(url)

##### parte de propuesta ######
class Http_client(object):
    pass
################
#--------------------------

with describe('PipyPackageVersionRetriever'):

    with context('when retrieve package verion information'):
        with it('calls an http_client get function'):
            a_package_name = 'a_package_name'
            http_client = Spy()
            sut = PypiPackageVersionRetriever(http_client)

            sut.retrieve_version(a_package_name)

            expect(http_client.get).to(have_been_called)

        with it('calls an http_client get function with a valid url'):
            a_package_name = 'a_package_name'
            http_client = Spy()
            sut = PypiPackageVersionRetriever(http_client)

            sut.retrieve_version(a_package_name)

            expected_url = 'https://pypi.python.org/pypi/{}/json'.format(a_package_name)
            expect(http_client.get).to(have_been_called_with(expected_url))

    with context('when we make an http call FOOOOO'):
        with it('retrieve a json with the info BARRRRR'):
            a_package_name = 'a_package_name'
            http_client = Spy()
            sut = PypiPackageVersionRetriever(http_client)

            result = sut.retrieve_version(a_package_name)

            expected_result = 42
            expect(result).to(equal(expected_url))

####################  PROPUESTA  ##################

    with context('when the http query is done'):
        with it('a package version is retrieved'):
            a_package_name = 'a name'
            a_version = '42'
            url = 'https://pypi.python.org/pypi/{}/json'.format(a_package_name)

            http_client = Stub(Http_client)
            when(http_client.get(url)).returns(a_version)
            sut = PypiPackageVersionRetriever(http_client)

            result = sut.retrieve_version(a_package_name)

            expected_result = a_version
            expect(result).to(equal(expected_result))
