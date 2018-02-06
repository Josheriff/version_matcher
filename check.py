# -*- coding: utf-8 -*-

from version_checker.package_version_checker import package_and_version_builder
from version_checker.package_version_retriever import PypiPackageVersionRetriever, PypiClient

import sys
import requests


try:
    fname= sys.argv[1]

    with open(fname) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    for line in lines:
        local_package = package_and_version_builder(line)

        pypi_client = PypiClient(requests)
        retriever = PypiPackageVersionRetriever(pypi_client)
        result = retriever.retrieve_version(local_package['name'])

        if local_package['version'] == result:
            print local_package['name'],' local version || up to date version ', local_package['version'], ' || ' , result , 'OK'
        else:
            print local_package['name'],' local version || up to date version ', local_package['version'], ' || ' , result , 'XXX'
except:
    print "ERROR, has especificado la ruta del archivo?, ejemplo: python check.py dev-dependencies.txt"

