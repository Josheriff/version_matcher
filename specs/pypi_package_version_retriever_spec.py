# -*- coding: utf-8 -*-

from doublex import Spy, Stub, when
from doublex_expects import have_been_called, have_been_called_with
from expects import expect, equal
import requests

from version_checker.package_version_retriever import PypiPackageVersionRetriever, PypiClient

INFO_IN_JSON = { 'info': {'version': 42 } }

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


