# Jupyter Notebooks

All jupyter notebooks should go into the `notebooks` subfolder of the respective
experiment.

To make best use of the folder structure, the parent folder of each notebook
should be added to the import path.

This allows to then import the helper and the script module belonging to a
specific experiment as follows:

```python
import imports
# or
from imports import package_installed
```

You should also enable `nbstripout`, so that only clean versions of your
notebooks get committed to git.
Use `pre-commit` and `nbstripout` to remove bulky notebook output data before
committing changes.

It may be necessary or useful to keep certain output cells of a Jupyter
notebook, for example charts or graphs visualizing some set of data. To do this,
[according to the documentation for the `nbstripout` package][nbstripout],
either:

- add a `keep_output` tag to the desired cell; or
- add `"keep_output": true` to the desired cell's metadata.

You can access cell tags or metadata in Jupyter by enabling the "Tags" or
"Edit Metadata" toolbar (View > Cell Toolbar > Tags; View > Cell Toolbar > Edit Metadata).

For the tags approach, enter `keep_output` in the text field for each desired
cell, and press the "Add tag" button. For the metadata approach, press the
"Edit Metadata" button on each desired cell, and edit the metadata to look like
this:

```json
{
  "keep_output": true
}
```

This will tell the hook not to strip the resulting output of the desired
cell(s), allowing the output(s) to be committed.

To use jupyter notebooks with the project you need to add a jupyter kernel
pointing to the venv of the project.

This can be done by running:

```shell
python3 -m ipykernel install --user --name "{{cookiecutter.project_slug}}"
```

Afterwards a new kernel called {{cookiecutter.project_slug}} should be available
in the jupyter lab/jupyter notebook interface. Use that kernel for all notebooks
related to this project.

The `.envrc` file should automatically add the entire project path into the
`PYTHONPATH` environment variable.

This should allow you to directly import `src/{{cookiecutter.project_slug}}`
in your notebook.

[nbstripout]: https://github.com/kynan/nbstripout
