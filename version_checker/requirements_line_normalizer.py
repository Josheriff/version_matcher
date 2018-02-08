# -*- coding: utf-8 -*-

class RequirementLineNormalizer:

    def apply(self,input_line):
        if "==" not in input_line:
            return None
        package, version = input_line.split('==')
        return {'name': package, 'version': version}
