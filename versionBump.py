#!/usr/local/bin/python3

import urllib.request
import os
from ruamel.yaml import YAML


APP_VERSION = os.getenv('APP_VERSION', 'v0.8.1')
APP_RELEASE = os.getenv('APP_RELEASE', '0.8')
CHART_VERSION = os.getenv('CHART_VERSION', 'v0.1.0')

print (f'Bumping to version {APP_VERSION}')
urllib.request.urlretrieve('https://raw.githubusercontent.com/jetstack/cert-manager/release-'+APP_RELEASE+'/deploy/manifests/00-crds.yaml','./crds-cert-manager/templates/00-crds.yaml')

yaml = YAML()

# Bump CRDS Chart
with open('./crds-cert-manager/Chart.yaml') as chart_file:
    chart = yaml.load(chart_file)
chart['appVersion'] = APP_VERSION
chart['version'] = CHART_VERSION
with open('./crds-cert-manager/Chart.yaml', 'w') as chart_file:
    yaml.dump(chart, chart_file)

# Bump Helmfiles
with open('./helmfile.d/00-crds.yaml') as helmfile_crds:
    helmfile_crds_data = yaml.load(helmfile_crds)
helmfile_crds_data[releases][version] = CHART_VERSION
with open('./helmfile.d/00-crds.yaml', 'w') as helmfile_crds:
    yaml.dump(helmfile_crds_data, helmfile_crds)

    
