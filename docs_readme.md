# Documentation editing notes
The package documentation is done thru mkdocs and one custom script to render product descriptions. Using mkdocs is *really* nice and much more pain free than sphinx and readthedocs.  

### Doc packages
You need the following to build the docs.  
- mkdocs - primary package
- mkdocstrings - plugin to build api docs from the docstrings
- pytkdocs[numpy-style] - docstring parser for mkdocstrings with the numpy "extra"  
- mkdocs-material - mkdocs material theme https://github.com/squidfunk/mkdocs-material
- mkdocs-exclude - plugin to exclude files or folders within the docs directory. https://github.com/apenwarr/mkdocs-exclude

`pip install mkdocs mkdocstrings pytkdocs[numpy-style] mkdocs-material'  

### Making updates to the product descriptions.
These edits should made to the yaml files in `unpackqa/product_files/` in the `description` entry. If you make an edit, run `render_product_markdown_files.py` to produce new markdown files in the `docs` folder, which will be picked up by mkdocs.

### Making edits to API page
The API page is pulled from the docstrings within each respective function via the mkdocstrings plugin. `docs/api.md` configures how those docstrings are read and displayed. 

### Making edits to any other docs
You can edit everything else in `docs` directly.

### Seeing real time updates
In a command window navigate to the unpackqa directory and run `mkdocs serve` and in a browser navigate to `http://localhost:8000` to see the current site. Any changes you make to the text markdown files will be updated in the browser.   
This will not pickup any changes in the product yaml files. To see updates with those while `mkdocs serve` is running do the following:  
1. Make yaml file edit in the `description` entry.
2. Save the file.
3. run 'python render_product_markdown_files.py'
4. See the update in the browser.

### To update the primary doc site.
Once everything is as you like run `mkdocs gh-deploy` to automatically build the site and push to the gh-pages repo. 

### TODO.
note on the examples
