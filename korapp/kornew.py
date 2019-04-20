import os
import sys
import io
import yaml
from shutil import copy

# from korapp import kordir
from korapp import utils


def init(args, brain):
    print(f'KorApp New')
    try:
        app_name = sys.argv[2]
    except IndexError:
        print("!!! Error: must specify app name")
        return
    if os.path.isdir(app_name):
        print("!!! Error: App Folder exists")
        return
    os.mkdir(app_name)
    ka_dir = os.path.join(app_name, ".korapp")
    os.mkdir(ka_dir)
    yaml_file = os.path.join(ka_dir, 'korapp.yaml')
    with io.open(yaml_file, 'w', encoding='utf8') as outfile:
        params = {
            'app_name': app_name,
            'brain': brain
        }
        yaml.dump(
            params, outfile,
            default_flow_style=False, allow_unicode=True)
    # create app.mm
    src = os.path.join(brain, "template", "app.mm")
    copy(src, app_name)
    process_new(app_name, brain)


def process_new(app_name, brain):
    filename = os.path.join(brain, "new.mm")
    mm = utils.read_mm(filename)
    for node in mm.node:
        cmd = node['TEXT']
        arg = node.node['TEXT']
        # arg = arg.format(*args)
        script = os.path.join(brain, 'script', arg)
        # script = os.path.join(kordir.dir_script, arg)
        print(f'{cmd} {script}.sh {app_name}')
        if cmd == "bash":
            os.system(f'{cmd} {script}.sh {app_name}')
            continue
        if cmd == "py" or cmd == "python":
            if os.name == "posix":
                os.system(f"python3 {script}.py {app_name}")
            else:
                os.system(f"python {script}.py {app_name}")
