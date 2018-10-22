# consoleTools
A python module made for server applications for formatting and logging
___________________
consoleTools: v0.1.6 (non-stable)

Packaged: No

OS Support: OS Independant

___________________
## What am I?
We needed a logging tool and console display tool with a fancy output with colours, so we quickly whipped this together.
Other features will be implemented to this over-time as we need more things in our console apps (main feature is logging).

All logs are stored in `logs/`date`-log.txt`
___________________
## Usage
```python
#Logging and displaying console output
from consoleTools import consoleDisplay as cd
cd.log('e','I am an error')
cd.log('w','I am a warning')
cd.log('i','I am an information message')
cd.log('n',"I am a notice and therefore have no formatting as I'm not that important")
cd.log('s','Woo-hoo! Your thing worked')
```

Other non-major items:
cd.clear() - clear console
cd.printFile() - print file contents
___________________
## Questions people asked when making this (but not in their words)
q) B... b... but I don't want it to log to a file Brendan!

a) Well the #### you, we added that:
```python
cd.log('s','I will not log to a file',False)
```
Add the boolean flag `False` and nothing will be logged to a file

q) I don't want to log to `logs/`. Why are you making me do this
a) By adding the simple flag `file=x` you can set whatever you want there
```python
cd.log('s','I will log to a custom file',file="thisfilecontainsthe.log")
```

q) I know what happened, but when?
a) The log files contain dates and times - just keeping the console nice and clean
___________________
## Getting Console Tools

### Stable
Console tools is easy to install via pip:
`pip install Console-Tools`
### Nightly
Grab this version (may not function at all/function correctly)
`git clone https://github.com/dudeisbrendan03/consoleTools.git`
`pip install -r requirements.txt`
(Optional) - Access the module globally:
Move the `consoleTools` folder to `Python37\Lib\site-packages`

### Beta
We upload a beta (partially stable) version to PyPI test.
`python -m pip install --index-url https://test.pypi.org/simple/ Console-Tools`