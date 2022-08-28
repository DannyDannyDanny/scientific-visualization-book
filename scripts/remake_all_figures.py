'''reruns all python visualization scripts

os.system is used so that the scripts can be run from their parent dirs.
that way the relative paths in each script doesn't have to be changed
'''

import os
from pathlib import Path
from matplotlib import font_manager

print('adding font files')
font_files = font_manager.findSystemFonts(fontpaths='fonts/')
for font_file in font_files:
    print(font_file)
    font_manager.fontManager.addfont(font_file)

srcpaths = Path('code').rglob('*.py')
# only first 5 files for now
srcpaths = list(srcpaths)[:5]
sep = 80*'-'

for srcpath in srcpaths:
    print(f'{sep}\nexec: `cd {srcpath.parent} && python3 {srcpath.name}`')
    os.system(f'cd {srcpath.parent} && python3 {srcpath.name}')
