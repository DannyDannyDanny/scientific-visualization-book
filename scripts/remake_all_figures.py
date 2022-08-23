'''reruns all python visualization scripts

os.system is used so that the scripts can be run from their parent dirs.
that way the relative paths in each script doesn't have to be changed
'''

import os
from pathlib import Path
srcpaths = Path('code').rglob('*.py')

for srcpath in srcpaths:
    print(f'exec: `cd {srcpath.parent} && python3 {srcpath.name}`')
    os.system(f'cd {srcpath.parent} && python3 {srcpath.name}')