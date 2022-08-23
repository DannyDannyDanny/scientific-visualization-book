from pathlib import Path

# iterate all pdfs in `figures/**/*pdf`
pdfpaths = Path('figures').rglob('*.pdf')

for pdfpath in pdfpaths:
    pdfpathstr = str(pdfpath)
    svgpathstr = pdfpathstr.replace('.pdf', '.svg')
    print(f'replacing `{pdfpathstr}` with `{svgpathstr}`')
    
    # iterate all srccode in `figures/**/*.py`
    srcpaths = Path('code').rglob('*.py')
    for srcpath in srcpaths:
        srccode = srcpath.read_text()

        if pdfpathstr in srccode:
            print(f'\treplaced in {srcpath}')
        # srccode_svg = srccode.replace(pdfpathstr, svgpathstr)
        # srccodepath.write_text(srccode_svg)

    # iterate all srccode in `rst/**/*.rst`
    rstpaths = Path('rst').rglob('*.rst')
    for rstpath in rstpaths:
        rstcontent = rstpath.read_text()
        
        if pdfpathstr in rstcontent:
            print(f'\treplaced in {rstpath}')
        # rstcontent_svg = rstcontent.replace(pdfpathstr, svgpathstr)
        # rstpath.write_text(srccode_svg)
    break
            

# print(pdfpaths)
# print(srccodepaths)
# find all occurences of pdfpath in `code/**/*.py`
