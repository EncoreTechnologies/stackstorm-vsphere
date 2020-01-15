#!/usr/bin/env python
# Copyright 2019 Encore Technologies
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

import six


def one_of_two_strings(stringa=None, stringb=None, desc="Input"):
    if (stringb and isinstance(stringb, six.string_types))\
            or (stringa and isinstance(stringa, six.string_types)):
        return
    else:
        raise ValueError("No %s provided" % desc)
