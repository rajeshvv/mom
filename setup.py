#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# Copyright (C) 2011 Yesudeep Mangalapilly <yesudeep@gmail.com>
# Copyright (C) 2012 Google, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Python module that implements a few utilities used throughout our
code base to avoid duplication in multiple projects.
"""

import sys

from setuptools import setup

def pycrypto_complain(version):
  import logging

  logging.warning(
    "PyCrypto >=2.3 is required for cryptographic functions to work. "\
    "If you are using any of these routines, please also add it to your "\
    "list of dependencies. Found %r." % repr(version)
  )

try:
  import Crypto

  if getattr(Crypto, "version_info", None) and Crypto.version_info[0:3] < (
  2, 3, 0):
    pycrypto_complain(Crypto.__version__)
except ImportError:
  Crypto = None
  pycrypto_complain(None)

install_requires = [
  # Binary dependency. Allow the user to decide whether she wants to pull this
  # in or not. For example, App Engine provides its own version of PyCrypto
  # which is written in pure Python. Forcing this dependency will cause
  # compatibility problems on that platform.
  #"PyCrypto >=2.3",

]
if sys.version_info < (3, 0, 0):
  install_requires.append("pyasn1 >=0.0.13b")
if sys.version_info < (2, 6, 0):
  install_requires.append("simplejson >=2.1.6")

setup(
  name="mom",
  version="0.0.1",
  license="Apache Software License 2.0",
  url="http://github.com/gorakhargosh/mom",
  description="Python utility library.",
  long_description=__doc__,
  author="Yesudeep Mangalapilly",
  author_email="yesudeep@google.com",
  zip_safe=True,
  platforms="any",
  packages=["mom"],
  include_package_data=True,
  install_requires=install_requires,
  keywords=' '.join([
    "python",
    "utilities",
    ]),
  classifiers=[
    "Development Status :: 2 - Pre-Alpha Development Status",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
