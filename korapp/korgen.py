import os
import io
import yaml
import stringcase
# from pprint import pprint

from pathlib import Path
from korapp import kordir
from korapp import utils


def init():
    print(f'KorApp Gen')
    if utils.is_running_in_app():
        mm = utils.read_mm_dict('app.mm')
        # run model first if exists
        for node in mm['node']:
            keyword = node['@TEXT']
            if keyword == 'models':
                filename = os.path.join(kordir.dir_brain, 'gen', keyword+'.mm')
                if Path(filename).is_file():
                    execute(keyword, filename, node)
                else:
                    print("!!! models.mm not found, can't process \
                        models branch")
                break
        # run other keywords
        for node in mm['node']:
            keyword = node['@TEXT']
            if keyword == 'ignore':
                continue
            if keyword != 'models':
                filename = os.path.join(kordir.dir_brain, 'gen', keyword+'.mm')
                if Path(filename).is_file():
                    execute(keyword, filename, node)
                else:
                    print("!!! invalid brain, undefine keyword: " + keyword)
    else:
        print("!!! korapp run only work inside app directory")


def execute(keyword, filename, pnode):
    print('Process: '+keyword + ' branch')
    mm = utils.read_mm(filename)
    for node in mm.node:
        cmd = node['TEXT']
        arg = node.node['TEXT']
        # arg = arg.format(*args)
        script = os.path.join(kordir.dir_script, arg)
        if cmd == "bash":
            args = generate_level1_arguments(pnode)
            print(f'{cmd} {script} {args}')
            os.system(f'{cmd} {script} {args}')
        if cmd == "py" or cmd == "python":
            print(f'{cmd} {script}')
            node_param_file = os.path.join('.korapp', 'node_param.yaml')
            with io.open(node_param_file, 'w', encoding='utf8') as outfile:
                yaml.dump(
                    {'node': pnode}, outfile,
                    default_flow_style=False, allow_unicode=True)
            if os.name == "posix":
                os.system(f"python3 {script}.py")
            else:
                os.system(f"python {script}.py")


def generate_level1_arguments(pnode):
    args = ""
    for level1 in pnode['node']:
        try:
            level = level1['@TEXT']
        except TypeError:
            print('*** Error')
            # pprint(level1)
            level = ''
        args += stringcase.snakecase(level)+' '
    # print('args = '+args)
    return args
