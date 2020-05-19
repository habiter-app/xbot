This is internal docs for xbot

## Helpful external resources

- https://packaging.python.org/tutorials/packaging-projects
- https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df
- https://jinja.palletsprojects.com/en/2.11.x/templates/#call
- https://docs.python.org/3/library/ast.html#ast.parse
- https://vpyast.appspot.com/

## Deployment

To deploy a new package version

```
git tag 1.0
git push --tag
```

The deployment to pypi is integrated in `travis-ci`, checkout `.travis.yml`
We use tags for having different releases versions to `pypi`. To release a new version

```
git tag # to view previous version
git tag version-number
git tag version-number -a # to annotate
```

If you make a untagged commit `travis` won't deploy

```
Skipping a deployment with the pypi provider because this is not a tagged commit
```

The tag is deployed because we use `setuptools-cmg` (check this commit `8410a1d109c35049c4eb7dd675ea7f9da84b604e` for how it was set up) and we added to `.travis.yml`

```
on:
    tags: true
```

To upload manually the package to pypi
```
python3 -m twine upload --repository testpypi dist/*
```
