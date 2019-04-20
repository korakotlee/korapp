import os
import yaml
from pathlib import Path
from korapp import utils

home = str(Path.home())
if utils.is_running_in_app():
    yaml_file = os.path.join(".korapp", 'korapp.yaml')
    with open(yaml_file, 'r') as stream:
        result = yaml.load(stream, Loader=yaml.FullLoader)
        dir_brain = result['brain']
else:
    dir_brain = Path(home+'/.brain')
# dir_brain = os.path.join(home, 'apps', 'brain0')
dir_script = os.path.join(dir_brain, "script")
template = os.path.join(dir_brain, "template")
