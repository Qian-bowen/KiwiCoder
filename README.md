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

The project hierarchy is shown as below.
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
kiwi>auto
```



## Usage

### Commands

#### load & scan & run

You can initialize the experiment by following commands.

```
kiwi>load
kiwi>scan
kiwi>run
```

* load: load the protocol and user-defined objects.
* scan: scan the protocol and build basic runtime environment.
* run: run the whole experiment.

#### ctrl

You can control and debug by following commands.

```
kiwi> ctrl -sp {step number} -op {operation index} {signal parameter}
```

* ctrl: the control command

| Signal   | Signal Parameter |
| -------- | ---------------- |
| STOP     | s                |
| RUN      | r                |
| SUSPEND  | p                |
| KILL     | k                |
| CONTINUE | c                |

#### sys

You can get or set some system variables or status by following commands.

```
kiwi>sys show {var name}
kiwi>sys set {var name} {var value}
```

#### gen

You can generate report or process graph by following commands.

```
kiwi>gen report {file name without suffix}
kiwi>gen process {file name without suffix}
```





### Bio Operation

#### Automation Level



#### Mock & Self-Defined Operation



### Bio Object





### Experiment Report

You can generate your report in html format, with a dot file which contains the experiment graph.



### Monitor





## Example

TODO