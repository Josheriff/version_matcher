# -*- coding: utf-8 -*-

from expects import expect, equal

#######

class VersionComparator(object):

    def __init__(self, line_normalizer, version_retriever):
        self.line_normalizer = line_normalizer
        self.version_retriever = version_retriever

    def apply(self, requirement_file_name):
        pass
        # recupero las lineas / del colaborador
        # por cada línea
        # >>>> normalizo
        # >>>>> comparo





#######
NORMALIZER_RESULT = {'name': 'mamba', 'version': '0.9.2'}
USING_UPTODATED = '0.9.2'
USING_OUTDATED = '0.9.3'

with describe('comparasion between server and local'):
    with it('both using the same version'):
        comparator = VersionComparator()




