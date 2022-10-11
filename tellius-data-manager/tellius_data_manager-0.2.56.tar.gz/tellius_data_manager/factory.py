# Copyright 2022 Tellius, Inc
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
from providah.factories.package_factory import PackageFactory


class Factory:
    """Factory abstraction designed to generate Pipe objects given the class name and the configuration (as a dict)."""

    _cls_type = object

    @classmethod
    def generate(cls, configuration: dict) -> _cls_type:
        """Generate the ConfigReader object given a configuration object that contains the name of hte object (class),
        and the configuration of the class instance as well.

        Args:
            configuration: This has two fields. 1) name: the name of the object to construct and 2) config: the
            configuration of the object.

        Returns: Pipe object after constructed

        Raises:
            ValueError: raised when the constructed type is incorrect.
            AttributeError: raise when the input configuration does not have the necessary fields.

        """
        cls._validate(configuration=configuration)

        configuration["config"]["name"] = configuration["name"]
        new_object = PackageFactory.create(
            key=configuration["type"], configuration=configuration["config"]
        )

        if not isinstance(new_object, cls._cls_type):
            raise ValueError(
                f"Constructed object does not have the required type ConfigReader,"
                f" but is instead of type {type(new_object)}"
            )

        return new_object

    @classmethod
    def _validate(cls, configuration: dict) -> bool:
        raise NotImplementedError()
