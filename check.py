# -*- coding: utf-8 -*-

from version_checker.package_version_checker import package_and_version_builder
from version_checker.package_version_retriever import PypiPackageVersionRetriever, PypiClient

import sys


fname= sys.argv[1]

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

print(content)
