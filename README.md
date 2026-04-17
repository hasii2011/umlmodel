[![CircleCI](https://dl.circleci.com/status-badge/img/gh/hasii2011/umlmodel/tree/master.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/hasii2011/umlmodel/tree/master)
[![PyPI version](https://badge.fury.io/py/umlmodel.svg)](https://badge.fury.io/py/umlmodel)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Introduction

This project provides a Python data model for creating and manipulating UML diagrams. It's the foundational data model for the [UML Shapes module.](https://github.com/hasii2011/umlshapes)

# Installation

It is recommended to use a virtual environment for installing Python packages.

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install the package
pip install umlmodel
```

# Usage

## Programmatic Usage

The `umlmodel` library allows you to create UML elements like classes, interfaces, and use cases programmatically. Here are some examples:

### Creating a Class

To create a simple class, instantiate the `Class` object:

```python
from umlmodel.Class import Class

modelClass: Class = Class(name='MyClass')

print(modelClass.name)
```

### Adding Fields to a Class

You can add fields (attributes) to a class. Fields have a name, type, visibility, and an optional default value.

```python
from umlmodel.Class import Class
from umlmodel.Field import Field
from umlmodel.FieldType import FieldType
from umlmodel.enumerations.Visibility import Visibility

# Create a class
modelClass: Class = Class(name='MyClass')

# Create fields
field1: Field = Field(name='my_string',
               type=FieldType('str'),
               visibility=Visibility.PUBLIC,
               defaultValue='"hello"')
field2:Field = Field(name='_my_private_int',
               type=FieldType('int'),
               visibility=Visibility.PRIVATE)

# Add fields to the class
modelClass.fields.append(field1)
modelClass.fields.append(field2)

# The string representation of a field is useful
print(field1)
print(field2)
```

### Adding Methods to a Class

Methods can be added to a class, including parameters and return types.

```python
from umlmodel.Class import Class
from umlmodel.Method import Method
from umlmodel.Parameter import Parameter
from umlmodel.ParameterType import ParameterType
from umlmodel.ReturnType import ReturnType
from umlmodel.enumerations.Visibility import Visibility

# Create a class
modelClass: Class = Class(name='MyClass')

# Create a method
method: Method = Method(name='my_method', visibility=Visibility.PUBLIC)

# Add a parameter
parameter: Paraeter = Parameter(name='value', type=ParameterType('int'), defaultValue='0')
method.addParameter(parameter)

# Set a return type
method.returnType = ReturnType('bool')

# Add the method to the class
modelClass.methods.append(method)

# Print the method signature
print(method.methodWithParameters())

```



___

Written by Humberto A. Sanchez II <mailto@Humberto.A.Sanchez.II@gmail.com>, (C) 2025


## Note
For all kind of problems, requests, enhancements, bug reports, etc., please drop me an e-mail.


------


![Humberto's Modified Logo](https://raw.githubusercontent.com/wiki/hasii2011/gittodoistclone/images/SillyGitHub.png)

I am concerned about GitHub's Copilot project

I urge you to read about the [Give up GitHub](https://GiveUpGitHub.org) campaign from[the Software Freedom Conservancy](https://sfconservancy.org).

While I do not advocate for all the issues listed there I do not like that a company like Microsoft may profit from open source projects.

I continue to use GitHub because it offers the services I need for free.  But, I continue to monitor their terms of service.

Any use of this project's code by GitHub Copilot, past or present, is done without my permission.  I do not consent to GitHub's use of this project's code in Copilot.
