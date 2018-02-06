# -*- coding: utf-8 -*-

from expects import expect, equal
from version_checker.package_version_checker import package_and_version_builder
#--------------------------
#import sys
#fname= sys.argv[0]

#with open(fname) as f:
#    content = f.readlines()
#content = [x.strip() for x in content]
#---------------------------

with describe('PackageAndVersionBuilder'):
    with context('when line contains package name and version, splitted by ==  (HappyPath)'):
        with it('returns a dictonary with package_name as key and version as value'):
            input_line = 'mamba==0.9.2'
            another_input_line = 'expect==42'

            result =  package_and_version_builder(input_line)
            result_2 = package_and_version_builder(another_input_line)

            expected_result = {'mamba': '0.9.2'}
            expect(expected_result).to(equal(result))
            expected_result = {'expect': '42'}
            expect(expected_result).to(equal(result_2))


    with context('when line contains package name and no version. Not splitted by =='):
        with it('returns None'):
            input_line = 'mamba'

            result =  package_and_version_builder(input_line)

            expected_result = None
            expect(expected_result).to(equal(result))

    with context('when is an empty line'):
        with it('returns None'):
            input_line = ''

            result =  package_and_version_builder(input_line)

            expected_result = None
            expect(expected_result).to(equal(result))

    with context('when line contains a github reference'):
        with it('returns None'):
            input_line = '-e git+https://github.com/aleasoluciones/simpledatamigrate.git#egg=simpledatamigrate'

            result =  package_and_version_builder(input_line)

            expected_result = None
            expect(expected_result).to(equal(result))

