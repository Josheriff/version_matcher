# -*- coding: utf-8 -*-
# TODO:
# Poner la lógica de este archivo en un objeto comparador
# comparador.lista returns version local + version remota + uptodate
#
# Crear un render que pinte el resultado del comparador
#
#
#######################################

from version_checker.requirements_line_normalizer import RequirementLineNormalizer
from version_checker.package_version_retriever import PypiPackageVersionRetriever, PypiClient

import sys
import requests


line_normalizer = RequirementLineNormalizer()
pypi_client = PypiClient(requests)
retriever = PypiPackageVersionRetriever(pypi_client)


try:

    fname= sys.argv[1]
    # comporador (fname) ->>>
    # render(resultadoDeLoAnterior)

    with open(fname) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    for line in lines:
        local_package = line_normalizer.apply(line)

        current_version = retriever.retrieve_version(local_package['name'])

        if local_package['version'] == current_version:
            print local_package['name'],' local version || up to date version ', local_package['version'], ' || ' , current_version, 'OK'
        else:
            print local_package['name'],' local version || up to date version ', local_package['version'], ' || ' , current_version, 'XXX'
except:
    print "ERROR, has especificado la ruta del archivo?, ejemplo: python check.py dev-dependencies.txt"

