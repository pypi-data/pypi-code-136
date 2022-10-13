# Copyright 2011-2014 Biomedical Imaging Group Rotterdam, Departments of
# Medical Informatics and Radiology, Erasmus MC, Rotterdam, The Netherlands
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
This module contains the NetworkScope plugin for fastr
"""

from fastr.core.ioplugin import IOPlugin


class NetworkScope(IOPlugin):
    """
    A simple source plugin that allows to get data from the Network scope. This uses the
    ``network://`` scheme.

    An uri of ``network://atlases/image_01.nii.gz`` would be translated to
    ``vfs://mount/network/atlases/image_01.nii.gz`` given that the network
    would be created/loaded from ``vfs://mount/network/networkfile.py``.

    .. warning:: This means that the network file must be present in a folder mounted in the
                 ``vfs`` system. Fastr will use a vfs to translate the path between main process
                 and execution workers.

    If the resulting uri should be a different vfs-based url that the default ``vfs://`` then
    a combined scheme can be used. For example ``network+vfslist://atlases/list.txt`` would be
    translated into ``vfslist://mount/network/atlases/list.txt`` and the result would be run
    by the ``vfslist`` plugin.
    """
    scheme = 'network', 'network+'

    def __init__(self):
        # initialize the instance and register the scheme
        super().__init__()
