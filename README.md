## Web Version

This fork of
[rougier/scientific-visualization-book](https://github.com/rougier/scientific-visualization-book)
aims to make the material accessible via web.

The [issue](https://github.com/rougier/scientific-visualization-book/issues/13)
that inspired the fork.

Preliminary web version can be found
[here](https://dannydannydanny.github.io/scientific-visualization-book/)


Build command: `make clear html gh_pages`


## Fork Roadmap

* [X] backup `Makefile` to `Makefile.bak`
* [X] run `sphinx-quickstart` to add `index.rst`, `conf.py`, `Makefile`
* [X] run `sphinx-buld` / `make html` to build `/docs`
* [X] add make script to build and prepare gh_pages
* [X] set up [github pages](https://dannydannydanny.github.io/scientific-visualization-book/)
* [X] build index with working links
* [X] add all (relevant) sections in `/rst` to `rst/index.rst`
* [X] revisit toc-content like `rst/00-*`
* [X] remove `numpydoc_show_class_members = False` from `conf.py`
* [X] add forked repo link to web version
* [X] add original repo link to web version
* [X] fix `WARNING: image file not readable:` warnings
* [X] revert moving `figures/*` into `rst/` (e54b56fac04861caa7e460dddd004ad359fef3b7)
* [X] use absolute paths for figure references
* [o] explore `figures/**/*.pdf` and `code/`
  * [o] explore how figures are generated
    * [o] prevent writing files in `/code/(showcases, reference, beyond, unsorted)` (why are they there?)
      * [X] identify scripts in `code` that write images outside of `figures/` (`scripts/fix_relative_path.py`)
      * [X] identify whether the resulting image for each script is actually used
      * [X] sort scripts into delete (:fire:) / fix (:hammer:):
      * [X] fix relative paths such that images are written inside `figures/`
      * [X] assert all files in `code/` subdirs have extension `.py` (or `.obj`)
        * [X] ignore and remove all `code/**/.pyc` and `code/**/__pycache__`
          * deleted: `code/animation/__pycache__/fluid.cpython-38.pyc`
          * deleted: `code/beyond/__pycache__/bluenoise.cpython-38.pyc`
          * deleted: `code/unsorted/3d/__pycache__/glm.cpython-37.pyc`
          * deleted: `code/unsorted/3d/__pycache__/plot.cpython-37.pyc`
        * [X] remove as much as possible non-code from `code/` (add future work point)
          * deleted: `code/beyond/dungeon.svg`
          * deleted: `code/data/John-Hunter.png`
          * deleted: `code/data/John-Hunter.pxd/QuickLook/Icon.tiff`
          * deleted: `code/data/John-Hunter.pxd/QuickLook/Thumbnail.tiff`
          * deleted: `code/data/John-Hunter.pxd/data/661EDC0D-0CB2-48AB-A474-4F1BCD77C183`
          * deleted: `code/data/John-Hunter.pxd/metadata.info`
          * deleted: `code/unsorted/3d/platonic-solids.pdf`
      * [ ] explore `/docs/_images/stacked-plots.pdf` `<---` what's with this `_images` dir?
      * [ ] change output formats
        * `code/colors/stacked-plots.py` with: `plt.savefig("../../figures/colors/stacked-plots.pdf")`
            * change `.pdf` to `.png` in `savefig` above and in references
      * [X] delete scripts that produce unused figures (and any unused figures)
  * [X] list all pdf files in `figures/`: `scripts/find_orphan_pdfs.py`
  * [X] identify pdf references and what creates pdfs and how to make it create svgs
  * [ ] assert that figures can be regenerated
    * [X] copy `/figures/` to `/figures.bak/`
    * [X] remove files `/figures/**/*.*` (check with `tree figures -a`)
    * [X] recreate environment for all scripts + requirements
      * [X] install geos: `sudo apt install geos-bin`
      * [X] install proj: `sudo apt install proj-bin`
      * [X] `pip install numpy matoplotlib cartopy GitPython imageio mpmath scipy shapely scikit-image tqdm`
    * [ ] run `/scripts/remake_all_figures.py` (pipe with `... >2 stderr.log > stdout.log`)
      * [X] print which script is running to **stderr** as well
      * error overview:
        * `ModuleNotFoundError: No module named 'noise'` <--- could not install (no wheel, requires gcc5)
          * hasn't been updated in a while - can we delete it?
          * only used in one script: `code/unsorted/dyson-hatching.py`
            * script output is never used - kill script
        * `ModuleNotFoundError: No module named 'cartopy'` -- pain in the ass to install (requires proj, geos)
        * `ModuleNotFoundError: No module named 'git'` -- install as `GitPython` - :thumbsdown:
        * `ModuleNotFoundError: No module named 'skimage'` -- install as scikit-image -- :thumbsdown:
        * `ModuleNotFoundError: No module named 'imageio'`
        * `ModuleNotFoundError: No module named 'mpmath'`
        * `ModuleNotFoundError: No module named 'scipy'`
        * `ModuleNotFoundError: No module named 'shapely'`
        * `ModuleNotFoundError: No module named 'tqdm'`
        * `RuntimeError: Failed to process string with tex because latex could not be found`
        * Other errors: bad code throwing `TypeError`, `ValueError`
      * warnings overview:
        * `findfont: Font family ['Cursive'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['ITC Zapf Chancery'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['Merienda'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['Pacifico'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['Roboto Condensed'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['Roboto Mono'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['Roboto Slab'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['Roboto'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['Source Code Pro'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['Source Sans Pro'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['Source Serif Pro'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['Yanone Kaffeesatz'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['cursive'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['sans-serif'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['serif'] not found. Falling back to DejaVu Sans.`
        * `findfont: Font family ['xkcd', 'xkcd Script', 'Humor Sans', 'Comic Neue', 'Comic Sans MS'] not found. Falling back to DejaVu Sans.`
        * `findfont: Generic family 'cursive' not found because none of the following families were found: Apple Chancery, Textile, Zapf Chancery, Sand, Script MT, Felipa, Comic Neue, Comic Sans MS, cursive`
        * `findfont: Generic family 'sans-serif' not found because none of the following families were found: Fira Sans Condensed`
        * `findfont: Generic family 'sans-serif' not found because none of the following families were found: Helvetica`
        * `findfont: Generic family 'sans-serif' not found because none of the following families were found: Roboto Condensed`
        * `findfont: Generic family 'sans-serif' not found because none of the following families were found: Source Sans Pro`
        * `findfont: Generic family 'serif' not found because none of the following families were found: Source Serif Pro`
      * [ ] untracked files that appeared after remake script run
        * `? code/rules/retina (4096,2048) - colliculus (512,512).npy`
        * `? code/unsorted/github-rougier-2014.html`
        * `? figures/anatomy/figure-dpi-050.png`
        * `? figures/anatomy/figure-dpi-100.png`
        * `? figures/anatomy/figure-dpi-300.png`
        * `? figures/anatomy/figure-dpi-600.png`
        * `? figures/anatomy/zorder-plots.png`
        * `? figures/colors/material-colors.png`
        * `? figures/colors/open-colors.png`
        * `? figures/coordinates/transform-example.pdf`
        * `? figures/rules/rule-5-left.pdf`
        * `? figures/rules/rule-5-right.pdf`
        * `plt.show()` throws `UserWarning: Matplotlib is currently using agg, which is a non-GUI backend...`
      * [ ] modified in `figures/`
      * [ ] missing in `figures/`
    * [ ] compare structure and figures in `/figures/` and `/figures_originals/`
    * [ ] see [warnings from above run](#error-log)
  * [ ] convert PDFs in `./figures/` into SVG or PNG:
    * [ ] `figures/layout/layout-aspect-3.pdf`
    * [ ] `figures/layout/layout-gridspec.pdf`
    * [ ] `figures/layout/complex-layout.pdf`
    * [ ] `figures/layout/standard-layout-1.pdf`
    * [ ] `figures/layout/layout-aspect-1.pdf`
    * [ ] `figures/layout/standard-layout-2.pdf`
    * [ ] `figures/layout/layout-aspect-2.pdf`
    * [ ] `figures/layout/layout-classical.pdf`
    * [ ] `figures/layout/complex-layout-bare.pdf`
    * [ ] `figures/layout/aspects.pdf`
    * [ ] `figures/animation/sine-cosine.pdf`
    * [ ] `figures/animation/earthquakes-frame-50.pdf`
    * [ ] `figures/animation/rain.pdf`
    * [ ] `figures/animation/sine-cosine-frame-128.pdf`
    * [ ] `figures/animation/lissajous.pdf`
    * [ ] `figures/animation/sine-cosine-frame-032.pdf`
    * [ ] `figures/animation/platecarree.pdf`
    * [ ] `figures/animation/sine-cosine-frame-001.pdf`
    * [ ] `figures/animation/sine-cosine-frame-255.pdf`
    * [ ] `figures/threed/bunny.pdf`
    * [ ] `figures/threed/bunny-7.pdf`
    * [ ] `figures/threed/bunny-2.pdf`
    * [ ] `figures/threed/bunny-8.pdf`
    * [ ] `figures/threed/bunny-6.pdf`
    * [ ] `figures/threed/bunny-1.pdf`
    * [ ] `figures/threed/bunny-4.pdf`
    * [ ] `figures/threed/bunnies.pdf`
    * [ ] `figures/threed/bunny-5.pdf`
    * [ ] `figures/threed/projection.pdf`
    * [ ] `figures/threed/bunny-3.pdf`
    * [ ] `figures/showcases/escher.pdf`
    * [ ] `figures/showcases/windmap.pdf`
    * [ ] `figures/showcases/text-shadow.pdf`
    * [ ] `figures/showcases/text-spiral.pdf`
    * [ ] `figures/showcases/recursive-voronoi.pdf`
    * [ ] `figures/showcases/mosaic.pdf`
    * [ ] `figures/showcases/waterfall-3d.pdf`
    * [ ] `figures/showcases/domain-coloring.pdf`
    * [ ] `figures/optimization/transparency.pdf`
    * [ ] `figures/optimization/self-cover.pdf`
    * [ ] `figures/colors/alpha-vs-color.pdf`
    * [ ] `figures/colors/flower-polar.pdf`
    * [ ] `figures/colors/colored-hist.pdf`
    * [ ] `figures/colors/open-colors.pdf`
    * [ ] `figures/colors/colormap-tree.pdf`
    * [ ] `figures/colors/colormap-transform.pdf`
    * [ ] `figures/colors/alpha-scatter.pdf`
    * [ ] `figures/colors/colored-plot.pdf`
    * [ ] `figures/colors/material-colors.pdf`
    * [ ] `figures/colors/color-wheel.pdf`
    * [ ] `figures/colors/mona-lisa.pdf`
    * [ ] `figures/colors/color-gradients.pdf`
    * [ ] `figures/colors/stacked-plots.pdf`
    * [ ] `figures/cheatsheets/cheatsheets-3.pdf`
    * [ ] `figures/cheatsheets/cheatsheets.pdf`
    * [ ] `figures/cheatsheets/handout-tips.pdf`
    * [ ] `figures/cheatsheets/handout-intermediate.pdf`
    * [ ] `figures/cheatsheets/handout-beginner.pdf`
    * [ ] `figures/cheatsheets/cheatsheets-4.pdf`
    * [ ] `figures/cheatsheets/cheatsheets-5.pdf`
    * [ ] `figures/cheatsheets/handout-tips-landscape.pdf`
    * [ ] `figures/cheatsheets/cheatsheets-1.pdf`
    * [ ] `figures/cheatsheets/handout-beginner-landscape.pdf`
    * [ ] `figures/cheatsheets/cheatsheets-2.pdf`
    * [ ] `figures/cheatsheets/handout-intermediate-landscape.pdf`
    * [ ] `figures/beyond/polygon-clipping.pdf`
    * [ ] `figures/beyond/dungeon.pdf`
    * [ ] `figures/beyond/interactive-loupe.pdf`
    * [ ] `figures/beyond/bluenoise.pdf`
    * [ ] `figures/beyond/tikz-dashes.pdf`
    * [ ] `figures/beyond/radial-maze.pdf`
    * [ ] `figures/beyond/dyson-hatching.pdf`
    * [ ] `figures/beyond/basal-ganglia.pdf`
    * [ ] `figures/beyond/tinybot.pdf`
    * [ ] `figures/typography/typography-font-stacks.pdf`
    * [ ] `figures/typography/tick-labels-variation.pdf`
    * [ ] `figures/typography/typography-math-cm.pdf`
    * [ ] `figures/typography/typography-math-stixsans.pdf`
    * [ ] `figures/typography/typography-math-stix.pdf`
    * [ ] `figures/typography/typography-math-dejavusans.pdf`
    * [ ] `figures/typography/typography-math-dejavuserif.pdf`
    * [ ] `figures/typography/text-starwars.pdf`
    * [ ] `figures/typography/typography-text-path.pdf`
    * [ ] `figures/typography/typography-matters.pdf`
    * [ ] `figures/typography/typography-math-custom.pdf`
    * [ ] `figures/typography/typography-legibility.pdf`
    * [ ] `figures/typography/projection-3d-gaussian.pdf`
    * [ ] `figures/typography/text-outline.pdf`
    * [ ] `figures/typography/typography-math-stacks.pdf`
    * [ ] `figures/anatomy/figure-dpi.pdf`
    * [ ] `figures/anatomy/anatomy.pdf`
    * [ ] `figures/anatomy/inch-cm.pdf`
    * [ ] `figures/anatomy/raster-vector.pdf`
    * [ ] `figures/anatomy/zorder-plots.pdf`
    * [ ] `figures/anatomy/bold-ticklabel.pdf`
    * [ ] `figures/anatomy/zorder.pdf`
    * [ ] `figures/anatomy/ruler.pdf`
    * [ ] `figures/scales-projections/scales-comparison.pdf`
    * [ ] `figures/scales-projections/polar-patterns.pdf`
    * [ ] `figures/scales-projections/projection-polar-config.pdf`
    * [ ] `figures/scales-projections/projection-polar-histogram.pdf`
    * [ ] `figures/scales-projections/geo-projections.pdf`
    * [ ] `figures/scales-projections/text-polar.pdf`
    * [ ] `figures/scales-projections/projection-3d-frame.pdf`
    * [ ] `figures/scales-projections/scales-custom.pdf`
    * [ ] `figures/scales-projections/scales-log-log.pdf`
    * [ ] `figures/introduction/visualization-landscape.pdf`
    * [ ] `figures/introduction/matplotlib-timeline.pdf`
    * [ ] `figures/coordinates/transforms-polar.pdf`
    * [ ] `figures/coordinates/transforms-floating-axis.pdf`
    * [ ] `figures/coordinates/coordinates-cartesian.pdf`
    * [ ] `figures/coordinates/transforms-hist.pdf`
    * [ ] `figures/coordinates/transforms-letter.pdf`
    * [ ] `figures/coordinates/transforms-exercise-1.pdf`
    * [ ] `figures/coordinates/coordinates-polar.pdf`
    * [ ] `figures/coordinates/transforms-blend.pdf`
    * [ ] `figures/reference/colorspec.pdf`
    * [ ] `figures/reference/tick-formatter.pdf`
    * [ ] `figures/reference/collection.pdf`
    * [ ] `figures/reference/axes-adjustment.pdf`
    * [ ] `figures/reference/line.pdf`
    * [ ] `figures/reference/font.pdf`
    * [ ] `figures/reference/hatch.pdf`
    * [ ] `figures/reference/colormap-sequential-1.pdf`
    * [ ] `figures/reference/colormap-uniform.pdf`
    * [ ] `figures/reference/colormap-qualitative.pdf`
    * [ ] `figures/reference/marker.pdf`
    * [ ] `figures/reference/colormap-sequential-2.pdf`
    * [ ] `figures/reference/colormap-diverging.pdf`
    * [ ] `figures/reference/text-alignment.pdf`
    * [ ] `figures/reference/scale.pdf`
    * [ ] `figures/reference/tick-locator.pdf`
    * [ ] `figures/unsorted/polar-patterns.pdf`
    * [ ] `figures/unsorted/polar-better-frame.pdf`
    * [ ] `figures/unsorted/polygon-clipping.pdf`
    * [ ] `figures/unsorted/metropolis.pdf`
    * [ ] `figures/unsorted/coordinates.pdf`
    * [ ] `figures/unsorted/dyson-hatching.pdf`
    * [ ] `figures/unsorted/layout-weird.pdf`
    * [ ] `figures/unsorted/earthquakes.pdf`
    * [ ] `figures/unsorted/multisample.pdf`
    * [ ] `figures/ornaments/annotation-side.pdf`
    * [ ] `figures/ornaments/legend-regular.pdf`
    * [ ] `figures/ornaments/title-regular.pdf`
    * [ ] `figures/ornaments/annotation-direct.pdf`
    * [ ] `figures/ornaments/annotation-zoom.pdf`
    * [ ] `figures/ornaments/bessel-functions.pdf`
    * [ ] `figures/ornaments/elegant-scatter.pdf`
    * [ ] `figures/ornaments/legend-alternatives.pdf`
    * [ ] `figures/rules/rule-2.pdf`
    * [ ] `figures/rules/rule-7.pdf`
    * [ ] `figures/rules/rule-1.pdf`
    * [ ] `figures/rules/rule-5.pdf`
    * [ ] `figures/rules/rule-8.pdf`
    * [ ] `figures/rules/rule-3.pdf`
    * [ ] `figures/rules/rule-6.pdf`
    * [ ] `figures/rules/rule-9.pdf`
    * [ ] `figures/defaults/defaults-step-2.pdf`
    * [ ] `figures/defaults/defaults-step-4.pdf`
    * [ ] `figures/defaults/defaults-exercice-1.pdf`
    * [ ] `figures/defaults/defaults-step-5.pdf`
    * [ ] `figures/defaults/defaults-step-1.pdf`
    * [ ] `figures/defaults/defaults-step-3.pdf`
  * [ ] [svg conversion resources](https://en.wikipedia.org/wiki/Wikipedia:Graphics_Lab/Resources/PDF_conversion_to_SVG#Conversion_with_dvisvgm)
* [ ] correct the order of toctree links to match book TOC
* [ ] correct the order of toctree link aliases to match book TOC
* [ ] fix `WARNING: toctree contains reference to document` warnings
* [ ] fix `WARNING: undefined label` warnings
* [ ] fix `WARNING: duplicate label` warnings
* [ ] fix `WARNING: Unknown target name` warnings
* [ ] remove `docs/_build/` or `_build/` from `.gitignore`
* [ ] merge `Makefile` with original (`Makefile.bak`)
* [ ] fix [`WARNING: html_static_path entry '_static' does not exist`](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_static_path) warning
* [ ] future work section:
  * whats the issue and what needs to be done with `code/unsorted/3d/README.md`
  * can we remove `code/introduction/visualization-landscape.graffle`?
  * move non-py files to `code/data/` dir:
    * `code/beyond/radial-maze-path.npy`
    * `code/defaults/mystyle.txt`
    * `code/threed/bunny.obj`
  * sphinx dark mode
* [ ] add self to supporters (or contributors)
* [ ] get ispired by other Github repos with sphinx docs:
  * [psf/requests](https://github.com/psf/requests)
  * [searx/searx](https://github.com/searx/searx)
  * [writethedocs/www](https://github.com/writethedocs/www)
  * [pallets/flask](https://github.com/pallets/flask)
  * [more...](https://www.sphinx-doc.org/en/master/examples.html#documentation-using-the-alabaster-theme)

### error-log
<details>

<summary>
Partial output from running `scipts/remake_all_figures.py`

</summary>
```
/home/xxx/Documents/scientific-visualization-book/code/defaults/defaults-step-4.py:24: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  plt.show()
exec: `cd code/defaults && python3 defaults-step-2.py`
/home/xxx/Documents/scientific-visualization-book/code/defaults/defaults-step-2.py:59: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  plt.show()
exec: `cd code/defaults && python3 defaults-step-1.py`
/home/xxx/Documents/scientific-visualization-book/code/defaults/defaults-step-1.py:18: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  plt.show()
exec: `cd code/defaults && python3 defaults-exercice-1.py`
findfont: Font family ['sans-serif'] not found. Falling back to DejaVu Sans.
findfont: Generic family 'sans-serif' not found because none of the following families were found: Fira Sans Condensed
/home/xxx/Documents/scientific-visualization-book/code/defaults/defaults-exercice-1.py:66: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  plt.show()

...

/home/xxx/Documents/scientific-visualization-book/code/rules/rule-7.py:71: UserWarning: Matplotlib is currently using agg, w
hich is a non-GUI backend, so cannot show the figure.
  plt.show()
exec: `cd code/rules && python3 rule-1.py`
/home/xxx/Documents/scientific-visualization-book/code/rules/rule-1.py:300: UserWarning: Matplotlib is currently using agg,
which is a non-GUI backend, so cannot show the figure.
  plt.show()
exec: `cd code/rules && python3 rule-3.py`
/home/xxx/Documents/scientific-visualization-book/code/rules/rule-3.py:111: UserWarning: Matplotlib is currently using agg,
which is a non-GUI backend, so cannot show the figure.
  plt.show()
exec: `cd code/rules && python3 rule-9.py`
findfont: Font family ['xkcd', 'xkcd Script', 'Humor Sans', 'Comic Neue', 'Comic Sans MS'] not found. Falling back to DejaVu
 Sans.
findfont: Font family ['xkcd', 'xkcd Script', 'Humor Sans', 'Comic Neue', 'Comic Sans MS'] not found. Falling back to DejaVu
 Sans.
findfont: Font family ['xkcd', 'xkcd Script', 'Humor Sans', 'Comic Neue', 'Comic Sans MS'] not found. Falling back to DejaVu
 Sans.
```
</details>


> Original README follows:


## Scientific Visualization: Python + Matplotlib
**Nicolas P. Rougier, Bordeaux, November 2021.**

<img src="images/book.png" width="25%" alt="Front cover" align="left"/>

The Python scientific visualisation landscape is huge. It is composed of a myriad of tools, ranging from the most versatile and widely used down to the more specialised and confidential. Some of these tools are community based while others are developed by companies. Some are made specifically for the web, others are for the desktop only, some deal with 3D and large data, while others target flawless 2D rendering. In this landscape, Matplotlib has a very special place. It is a versatile and powerful library that allows you to design very high quality figures, suitable for scientific publishing. It also offers a simple and intuitive interface as well as an object oriented architecture that allows you to tweak anything within a figure. Finally, it can be used as a regular graphic library in order to design non‐scientific figures. This book is organized into four parts. The first part considers the fundamental principles of the Matplotlib library. This includes reviewing the different parts that constitute a figure, the different coordinate systems, the available scales and projections, and we’ll also introduce a few concepts related to typography and colors. The second part is dedicated to the actual design of a figure. After introducing some simple rules for generating better figures, we’ll then go on to explain the Matplotlib defaults and styling system before diving on into figure layout organization. We’ll then explore the different types of plot available and see how a figure can be ornamented with different elements. The third part is dedicated to more advanced concepts, namely 3D figures, optimization & animation.  The fourth and final part is a collection of showcases.

### Read the book

You can read the book **[PDF](https://hal.inria.fr/hal-03427242/document)** (95Mo, preferred site) that is open access and hosted on
[HAL](https://hal.archives-ouvertes.fr/) which is a French open
archive for academics. Up to date version is also available on GitHub [here](pdf/book.pdf). Sources for the book (including code examples)
are available at
[github.com/rougier/scientific-visualization-book](https://github.com/rougier/scientific-visualization-book).

### Buy the book

If you want to buy the book, you can order a **printed edition** at
[amazon.com](https://www.amazon.com/dp/2957990105) for 49$. If you want to support or sponsor my
future work on Python (and
[Emacs](https://github.com/rougier/nano-emacs)), you can use
[paypal](https://www.paypal.com/paypalme/NicolasPRougier/10),
[github](https://github.com/sponsors/rougier) or
[liberapay](https://en.liberapay.com/rougier/).

<a href="https://www.paypal.com/paypalme/NicolasPRougier/5"><img src="https://img.shields.io/badge/-TIP_5$-yellow.svg?style=flat-square"/><a/>
 <a href="https://www.paypal.com/paypalme/NicolasPRougier/10"><img src="https://img.shields.io/badge/-TIP_10$-orange.svg?style=flat-square"/><a/>
 <a href="https://www.paypal.com/paypalme/NicolasPRougier/25"><img src="https://img.shields.io/badge/-TIP_25$-red.svg?style=flat-square"/><a/>
 <a href="https://github.com/sponsors/rougier/sponsorships?sponsor=rougier&tier_id=6981&preview=false"><img src="https://img.shields.io/badge/-5$/Mo-yellow.svg?style=flat-square&logo=github"/><a/> <a href="https://github.com/sponsors/rougier/sponsorships?sponsor=rougier&tier_id=11147&preview=false"><img src="https://img.shields.io/badge/-10$/Mo-orange.svg?style=flat-square&logo=github"/><a/>
<a href="https://github.com/sponsors/rougier/sponsorships?sponsor=rougier&tier_id=108712&preview=false"><img src="https://img.shields.io/badge/-25$/Mo-red.svg?style=flat-square&logo=github"/><a/>
<a href="https://en.liberapay.com/rougier/donate"><img src="https://img.shields.io/badge/-PATRON/Week-green.svg?style=flat-square&logo=liberapay&logoColor=white"/><a/>

If you don't want to spend money, you can simply [nominate me](https://stars.github.com/nominate/) for the GitHub stars program if you find my work useful for the community.

### Build the book

**Ubuntu**
- [Article](https://labdmitriy.github.io/blog/building-scientific-visualization-book/)
- [Script](scripts/build_book/ubuntu.sh)

### See also

* [Python & OpenGL for Scientific Visualization](https://www.labri.fr/perso/nrougier/python-opengl/)
* [From Python to Numpy](https://www.labri.fr/perso/nrougier/from-python-to-numpy/) (Scientific Python Volume I)
* [100 Numpy exercices](https://github.com/rougier/numpy-100)
* [Matplotlib cheat sheets](https://github.com/matplotlib/cheatsheets)


### Book gallery

<img src="images/contour-dropshadow.png" width="31%"/> <img src="images/domain-coloring.png" width="31%"/> <img src="images/metropolis.png" width="31%"/>
<img src="images/zorder-plots.png" width="31%"/> <img src="images/scales.png" width="31%"/> <img src="images/histogram-pca.png" width="31%"/>
<img src="images/hatched-bars.png" width="31%"/> <img src="images/platonic-solids.png" width="31%"/> <img src="images/projection-3d-gaussian.png" width="31%"/>
<img src="images/polygon-clipping.png" width="31%"/> <img src="images/multisample.png" width="31%"/> <img src="images/typography-matters.png" width="31%"/>
<img src="images/scatter-3d.png" width="31%"/> <img src="images/waterfall-3d.png" width="31%"/> <img src="images/bunnies.png" width="31%"/>
<img src="images/polar-projection.png" width="31%"/> <img src="images/recursive-voronoi.png" width="31%"/> <img src="images/text-polar.png" width="31%"/>
<img src="images/spiral-pi.png" width="31%"/> <img src="images/escher.png" width="31%"/> <img src="images/radial-maze.png" width="31%"/>
<img src="images/text-shadow.png" width="95%"/>
