# letia

letia is ...

## Get started

### Launch Notebook

* With docker
```
docker run --rm -p 8888:8888 -e PYTHONPATH=/usr/src/letia -v "$PWD":/usr/src/letia:ro -v "$PWD/notebooks":/home/jovyan jupyter/scipy-notebook
```

## Test

### Run all tests

* With docker
```
docker run --rm -v "$PWD":/usr/src/letia:ro -w /usr/src/letia jupyter/scipy-notebook python -m unittest discover -s tests
```
