# -*- coding: utf-8 -*-

from expects import expect, equal
from version_checker.requirements_line_normalizer import RequirementLineNormalizer


with describe('PackageAndVersionBuilder'):

    with before.each:
        self.requirement_line_normalizer = RequirementLineNormalizer()

    with context('when line contains package name and version, splitted by ==  (HappyPath)'):
        with it('returns a dictonary with package_name as key and version as value'):
            input_line = 'mamba==0.9.2'
            another_input_line = 'expect==42'

            result =  self.requirement_line_normalizer.apply(input_line)
            result_2 = self.requirement_line_normalizer.apply(another_input_line)

            expected_result = {'name': 'mamba', 'version': '0.9.2'}
            expect(expected_result).to(equal(result))
            expected_result = {'name': 'expect', 'version': '42'}
            expect(expected_result).to(equal(result_2))


    with context('when line contains package name and no version. Not splitted by =='):
        with it('returns None'):
            input_line = 'mamba'

            result =  self.requirement_line_normalizer.apply(input_line)

            expected_result = None
            expect(expected_result).to(equal(result))

    with context('when is an empty line'):
        with it('returns None'):
            input_line = ''

            result =  self.requirement_line_normalizer.apply(input_line)

            expected_result = None
            expect(expected_result).to(equal(result))

    with context('when line contains a github reference'):
        with it('returns None'):
            input_line = '-e git+https://github.com/aleasoluciones/simpledatamigrate.git#egg=simpledatamigrate'

            result =  self.requirement_line_normalizer.apply(input_line)

            expected_result = None
            expect(expected_result).to(equal(result))

