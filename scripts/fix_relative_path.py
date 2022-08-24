"""Replaces savefig args in code/**/*.py files to ensure
output into the `figures/` directory"""

import os
from pathlib import Path

# iterate all python script paths in `code/`
srcpaths = Path('code').rglob('*.py')
for srcpath in srcpaths:
    # directory tree depth relative to repo root
    depth = len(srcpath.relative_to('').parts) - 1

    # we expect '../' to appear `depth` times to go beyond `code/` folder
    expected_argprefix = '../' * depth

    # read src-code
    srccode = srcpath.read_text()

    # skip file if no savefig
    if 'savefig' not in srccode:
        continue
    else:
        # iterate lines of source code
        for lineno, line in enumerate(srccode.split('\n')):
            # skip empty lines, comments and lines that don't contain 'savefig'
            if not len(line) or line[0] == '#' or 'savefig' not in line:
                continue

            # if extended prefix doesn't exists in the line, print
            if expected_argprefix not in line:
                msg = f'* `{str(srcpath)}` '
                msg += f'should contain `{expected_argprefix}` '
                msg += f'(`{depth = }`), observed:'
                msg += f'\n\t* L{lineno}: `{line}`'
                print(msg)
