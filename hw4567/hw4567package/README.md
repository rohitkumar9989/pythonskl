# Helper lib to read / check geo and data values , as well as to parse json / yaml configs


## 1) install package
```
cd hw4567package
```
```
sudo pip3 install -e .
```

## 2) run tests(needs 1)
```
cd hw4567package
```
```
python3 -m pytest
```

## 3) run cli(needs 1)
```
cd hw4567package
```
```
python3 pylib/cli.py COMMAND ARGUMENT
```
e.g.:

```
python3 pylib/cli.py str2date 'Jun 1 2005  1:33PM'
```
```
python3 pylib/cli.py str2geo '41.5,-81.0'
```

```
python3 pylib/cli.py read_configs assets
```


## 4) running tox check
```
cd hw4567package
```
```
tox -c tox.ini
```