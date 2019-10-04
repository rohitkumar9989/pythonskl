# ssh_wrapper
a tool in python to provide a simple api for ssh<br/>

# usage: 
python3 cli.py copy2target -localfile /usr/bin/col -where /tmp/col<br/>
python3 cli.py copyFromTarget -targetfile /usr/bin/col -where /tmp/col<br/>
python3 cli.py executeOnTarget -what 'file /usr/bin/col'<br/>
python3 cli.py copyDirFromTarget  -target_dir /tmp/folder/ -local_dir /tmp/folder/<br/>


# how to run tox
python3 -m tox -c tox.ini

#check ci 
https://cirrus-ci.com/