# Writing documentation

## Quickstart

### Sphinx

1. To write documentation we use [Sphinx](https://www.sphinx-doc.org/en/master/).
2. Default theme is set to furo, because it looks more modern than the default one. You can check other themes here: [Sphinx Themes](https://sphinx-themes.org/).
3. To change the theme, modify the `html_theme` variable in the `docs/source/conf.py` file.
4. Thanks to [myst-parser](https://myst-parser.readthedocs.io/en/latest/) you can write documentation in Markdown as well as reStructured Text.
5. To add a new page to the documentation add a new file in the `docs/source` folder. Title of the page is set by the first header in the file. You can add a new page to the table of contents by adding it to the `docs/source/index.md` file under the `toctree` directive.
6. API documentation should be automatically included in the documentation thanks to [sphinx-autoapi](https://sphinx-autoapi.readthedocs.io/en/latest/) extension. Just include `autoapi/index` inside the `toctree` directive in the `docs/source/index.md` file.

### Build documentation

1. To build the documentation run `make html` in the `docs` folder.
2. To build documentation after every change run `sphinx-autobuild docs/source docs/build/html` in the project root folder. This will automatically rebuild the documentation after every change in the `docs/source` folder. You can then open the link in your browser to see the changes.

### Serve documentation locally

1. To view the documentation run `python -m http.server` in the `docs/_build/html` folder and open the link in your browser.

2. Additionally, see `Build documentation` section above to see how to automatically rebuild the documentation after every change. This will also serve the documentation locally.

### Jupyter Notebooks

You can use Jupyter Notebooks as pages in your documentations thanks to [nbsphinx](https://nbsphinx.readthedocs.io/) extension. Just include the notebook in the `toctree` directive in the `docs/source/index.md` file.

**Note** that you will need `pandoc` installed on your machine for sphinx to understand Jupyter Notebook format. To do it try `conda install pandoc` (conda env) or `sudo apt install pandoc` (native installation).

### Additional notes

For automatic documentation of package API we use `sphinx-autoapi` extension. One could also try to use `autodoc` and `autosummary` extensions built into Sphinx. In case `sphinx-autoapi` is not meeting your expectations, try to use [autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) and [autosummary](https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html) instead.
