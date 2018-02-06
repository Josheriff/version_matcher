# -*- coding: utf-8 -*-

from version_checker.package_version_checker import package_and_version_builder
from version_checker.package_version_retriever import PypiPackageVersionRetriever, PypiClient

import sys
import requests

fname= sys.argv[1]

with open(fname) as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

for line in lines:
    local_package = package_and_version_builder(line)

    pypi_client = PypiClient(requests)
    retriever = PypiPackageVersionRetriever(pypi_client)
    result = retriever.retrieve_version(local_package['name'])

    print local_package['name'],' local version || up to date version ', local_package['version'], ' || ' , result

