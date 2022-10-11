# Copyright (c) 2018, 2019, 2021  Peter Pentchev <roam@ringlet.net>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

"""Data for the unit tests for the feature-check Python library."""

FEATURES = {
    "base": "2.1",
    "beta": "3.0.beta2",
}

SYNONYMS = {
    "lt": "<",
    "le": "<=",
    "eq": "=",
    "ge": ">=",
    "gt": ">",
}

COMPARE = [
    ("base", "lt", "2", False),
    ("base", "le", "2", False),
    ("base", "ge", "2", True),
    ("base", "gt", "2", True),
    ("base", "eq", "2", False),
    ("base", "lt", "2.1.a", False),
    ("base", "le", "2.1.a", False),
    ("base", "ge", "2.1.a", True),
    ("base", "gt", "2.1.a", True),
    ("base", "eq", "2.1.a", False),
    ("base", "lt", "2.1", False),
    ("base", "le", "2.1", True),
    ("base", "ge", "2.1", True),
    ("base", "gt", "2.1", False),
    ("base", "eq", "2.1", True),
    ("base", "lt", "2.1a", True),
    ("base", "le", "2.1a", True),
    ("base", "ge", "2.1a", False),
    ("base", "gt", "2.1a", False),
    ("base", "eq", "2.1a", False),
    ("base", "lt", "2.1.0", True),
    ("base", "le", "2.1.0", True),
    ("base", "ge", "2.1.0", False),
    ("base", "gt", "2.1.0", False),
    ("base", "eq", "2.1.0", False),
    ("base", "lt", "2.1.1", True),
    ("base", "le", "2.1.1", True),
    ("base", "ge", "2.1.1", False),
    ("base", "gt", "2.1.1", False),
    ("base", "eq", "2.1.1", False),
    ("base", "lt", "3", True),
    ("base", "le", "3", True),
    ("base", "ge", "3", False),
    ("base", "gt", "3", False),
    ("base", "eq", "3", False),
    ("base", "lt", "10", True),
    ("base", "le", "10", True),
    ("base", "ge", "10", False),
    ("base", "gt", "10", False),
    ("base", "eq", "10", False),
    ("base", "lt", "10.1", True),
    ("base", "le", "10.1", True),
    ("base", "ge", "10.1", False),
    ("base", "gt", "10.1", False),
    ("base", "eq", "10.1", False),
    ("beta", "lt", "1", False),
    ("beta", "le", "1", False),
    ("beta", "eq", "1", False),
    ("beta", "ge", "1", True),
    ("beta", "gt", "1", True),
    ("beta", "lt", "3.0", True),
    ("beta", "le", "3.0", True),
    ("beta", "eq", "3.0", False),
    ("beta", "ge", "3.0", False),
    ("beta", "gt", "3.0", False),
    ("beta", "lt", "3.0.beta1", False),
    ("beta", "le", "3.0.beta1", False),
    ("beta", "eq", "3.0.beta1", False),
    ("beta", "ge", "3.0.beta1", True),
    ("beta", "gt", "3.0.beta1", True),
    ("beta", "lt", "3.0.beta2", False),
    ("beta", "le", "3.0.beta2", True),
    ("beta", "eq", "3.0.beta2", True),
    ("beta", "ge", "3.0.beta2", True),
    ("beta", "gt", "3.0.beta2", False),
    ("beta", "lt", "3.0.beta3", True),
    ("beta", "le", "3.0.beta3", True),
    ("beta", "eq", "3.0.beta3", False),
    ("beta", "ge", "3.0.beta3", False),
    ("beta", "gt", "3.0.beta3", False),
    ("beta", "lt", "3.0.0", True),
    ("beta", "le", "3.0.0", True),
    ("beta", "eq", "3.0.0", False),
    ("beta", "ge", "3.0.0", False),
    ("beta", "gt", "3.0.0", False),
]
