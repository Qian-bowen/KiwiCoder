# KiwiCoder
A biology framework for biological experiments.

## What is KiwiCoder?

TODO



## Quick Start

KiwiCoder can be installed using pip

```
pip install KiwiCoder
```

You can generate your first project.

```
kiwi-gen {your path}
```

The project hierarchy is shown below.
```
├── keee-weee
│    ├── user
│       ├── __init__.py
│    	├── override.py
│    	├── protocol.py
├── __main__.py
```

You can define your experiment protocol by finishing `protocol.py` .

Function `kiwi_protocol` is the main function for protocol. You should NOT rename the function or write a new one.

```python
# define experiment protocol in this file
from kiwi import Step

def kiwi_protocol():
	""" Define experiment protocol. """
	Step("example step 1", "sn:1")
```

If you want to use user-defined class or functions, you can override them in `override.py` .

Then you can run the main script, and a command line will appear. You can run your protocol by entering the following commands.

```
kiwi>load
kiwi>scan
kiwi>run
```



## Usage

TODO



## Example

TODO