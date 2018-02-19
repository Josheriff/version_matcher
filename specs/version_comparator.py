# -*- coding: utf-8 -*-

from expects import expect, equal

#######

class VersionComparator(object):

    def __init__(self, line_normalizer, version_retriever):
        self.line_normalizer = line_normalizer
        self.version_retriever = version_retriever

    def apply(self, requirement_file_name):
        
        local_package = self.line_normalizer.apply(input_line)
        cloud_package_version = self.version_retriever.retrieve_version(local_package['package_name'])
        if local_package['version'] == cloud_package_version:
            return True
        return False
        # recupero las lineas / del colaborador
        # por cada línea
        # >>>> normalizo
        # >>>>> comparo





#######
INPUT_LINE = 'mamba==0.9.2'
USING_UPTODATE = '0.9.2'
USING_OUTDATED = '0.9.3'

PYPIJSON =

with describe('comparasion between server and local'):
    with it('both using the same version'):

        http_client = Stub()
        pypiclient = Stub(PypiClient(http_client))
        version_retriever = Stub(PypiPackageVersionRetriever(pypiclient))
        when(version_retriever).apply(ANY_PARAMETER).returns(USING_UPTODATE)
        line_normalizer = RequirementLineNormalizer()

        comparator = VersionComparator(line_normalizer, version_retriever, package_name)






