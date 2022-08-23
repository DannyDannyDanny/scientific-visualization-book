from pathlib import Path

print('PDFs in `./figures/` that should be converted to SVG or PNG:')

for p in Path('figures').rglob('*.pdf'):
    print('\t\t * [ ]', p)
