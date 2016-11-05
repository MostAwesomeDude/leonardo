#!/usr/bin/env python

import collections
import yaml

# http://stackoverflow.com/a/21048064/264985
_mapping_tag = yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG

def dict_representer(dumper, data):
    return dumper.represent_dict(data.iteritems())

def dict_constructor(loader, node):
    return collections.OrderedDict(loader.construct_pairs(node))

yaml.add_representer(collections.OrderedDict, dict_representer)
yaml.add_constructor(_mapping_tag, dict_constructor)

from flask import Flask
from leonardo import app

app.debug = True
app.run(host='0.0.0.0')


