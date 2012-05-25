#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2011 Yesudeep Mangalapilly <yesudeep@gmail.com>
# Copyright 2012 Google, Inc.
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

from mom.builtins import b

UNICODE_STRING = '\u00ae'
UNICODE_STRING2 = '深入 Python'
FOO = b('foo')
UFOO = 'foo'
JSON_FOO = b('"foo"')
JSON_UFOO = '"foo"'
JSON_UNICODE_VALUE = '"\u00e9"'
UNICODE_VALUE = '\u00e9'
X_BYTE = b("\xe9")
UTF8_BYTES = b('\xc2\xae')
UTF8_BYTES2 = b('\xe6\xb7\xb1\xe5\x85\xa5 Python')
LATIN1_BYTES = b("\xe9")
