# -*- coding: utf-8 -*-

def package_and_version_builder(input_line):
    if "==" not in input_line:
        return None
    package, version = input_line.split('==')
    return {package: version}
