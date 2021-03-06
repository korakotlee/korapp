import untangle
import xmltodict
import os
import io
import yaml
import stringcase
import re

from pathlib import Path


WARNING = '''
// *** WARNING ***
// File is Autogenerated from KorApp package
// Any modification will be overwritten.
'''


def get_brain(app_name):
    ''' get brain from outside when korapp new '''
    yaml_file = os.path.join(app_name, ".korapp", 'korapp.yaml')
    with open(yaml_file, 'r') as stream:
        result = yaml.load(stream, Loader=yaml.FullLoader)
        return result['brain']


def get_brain_cwd():
    ''' get brain when korapp gen '''
    yaml_file = os.path.join(".korapp", 'korapp.yaml')
    with open(yaml_file, 'r') as stream:
        result = yaml.load(stream, Loader=yaml.FullLoader)
        return result['brain']


def save_model(model_name, atts):
    # ka_dir = os.path.join(app_name, )
    yaml_file = os.path.join(".korapp", f'model_{model_name}.yaml')
    with io.open(yaml_file, 'w', encoding='utf8') as outfile:
        yaml.dump(atts, outfile,
                  default_flow_style=False, allow_unicode=True)


def get_icon(node):
    try:
        i = node['icon']['@BUILTIN']
    except Exception:
        i = ''
    return i


def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])


def class_case(string):
    '''
    convert string to class case, i.e., hello world => HelloWorld
    '''
    return string[0].upper() + \
        re.sub(r"[\-_\.\s]([a-z])", lambda matched: matched.group(1).upper(),
               string[1:])


def read_mm(filename):
    mm_text = open(filename).read()
    doc = untangle.parse(mm_text)
    return doc.map.node


def read_mm_dict(filename):
    mm_text = open(filename).read()
    doc = xmltodict.parse(mm_text)
    return doc['map']['node']


def get_node_param():
    node_param_file = os.path.join('.korapp', 'node_param.yaml')
    with open(node_param_file, 'r') as stream:
        node_param = yaml.load(stream, Loader=yaml.FullLoader)
    return node_param


def get_app_param():
    fname = os.path.join('.korapp', 'korapp.yaml')
    with open(fname, 'r') as stream:
        param = yaml.load(stream,  Loader=yaml.FullLoader)
    return param


def is_running_in_app():
    return Path('app.mm').is_file()
