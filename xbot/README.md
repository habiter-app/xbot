This is internal docs for xbot

## Helpful external resources

- https://packaging.python.org/tutorials/packaging-projects
- https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df
- https://jinja.palletsprojects.com/en/2.11.x/templates/#call
- https://docs.python.org/3/library/ast.html#ast.parse
- https://vpyast.appspot.com/

## Deployment

To upload the package to pypi
```
python3 -m twine upload --repository testpypi dist/*
```

The deployment to pypi is integrated in `travis-ci`, checkout `.travis.yml`
We use tags for having different releases versions to `pypi`. To release a new version

```
git tag # to view previous version
git tag version-number
git tag version-number -a # to annotate
```

The tag is deployed because we use `setuptools-cmg`, check this commit `8410a1d109c35049c4eb7dd675ea7f9da84b604e` for how it was set up.

We also push automatically to `origin` all the tags using

(https://stackoverflow.com/questions/5195859/how-do-you-push-a-tag-to-a-remote-repository-using-git)
```
git config --global push.followTags true
```

And adding to `.travis.yml`

```
on:
    tags: true
```
