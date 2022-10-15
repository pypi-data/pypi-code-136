from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.create_flow_json_body_value_failure_module_input_transforms import (
    CreateFlowJsonBodyValueFailureModuleInputTransforms,
)
from ..models.create_flow_json_body_value_failure_module_retry import CreateFlowJsonBodyValueFailureModuleRetry
from ..models.create_flow_json_body_value_failure_module_sleep_type_0 import (
    CreateFlowJsonBodyValueFailureModuleSleepType0,
)
from ..models.create_flow_json_body_value_failure_module_sleep_type_1 import (
    CreateFlowJsonBodyValueFailureModuleSleepType1,
)
from ..models.create_flow_json_body_value_failure_module_stop_after_if import (
    CreateFlowJsonBodyValueFailureModuleStopAfterIf,
)
from ..models.create_flow_json_body_value_failure_module_suspend import CreateFlowJsonBodyValueFailureModuleSuspend
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFlowJsonBodyValueFailureModule")


@attr.s(auto_attribs=True)
class CreateFlowJsonBodyValueFailureModule:
    """ """

    input_transforms: CreateFlowJsonBodyValueFailureModuleInputTransforms
    value: None
    stop_after_if: Union[Unset, CreateFlowJsonBodyValueFailureModuleStopAfterIf] = UNSET
    sleep: Union[
        CreateFlowJsonBodyValueFailureModuleSleepType0, CreateFlowJsonBodyValueFailureModuleSleepType1, Unset
    ] = UNSET
    summary: Union[Unset, str] = UNSET
    suspend: Union[Unset, CreateFlowJsonBodyValueFailureModuleSuspend] = UNSET
    retry: Union[Unset, CreateFlowJsonBodyValueFailureModuleRetry] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        input_transforms = self.input_transforms.to_dict()

        value = None

        stop_after_if: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stop_after_if, Unset):
            stop_after_if = self.stop_after_if.to_dict()

        sleep: Union[Dict[str, Any], Unset]
        if isinstance(self.sleep, Unset):
            sleep = UNSET
        elif isinstance(self.sleep, CreateFlowJsonBodyValueFailureModuleSleepType0):
            sleep = UNSET
            if not isinstance(self.sleep, Unset):
                sleep = self.sleep.to_dict()

        else:
            sleep = UNSET
            if not isinstance(self.sleep, Unset):
                sleep = self.sleep.to_dict()

        summary = self.summary
        suspend: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.suspend, Unset):
            suspend = self.suspend.to_dict()

        retry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retry, Unset):
            retry = self.retry.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input_transforms": input_transforms,
                "value": value,
            }
        )
        if stop_after_if is not UNSET:
            field_dict["stop_after_if"] = stop_after_if
        if sleep is not UNSET:
            field_dict["sleep"] = sleep
        if summary is not UNSET:
            field_dict["summary"] = summary
        if suspend is not UNSET:
            field_dict["suspend"] = suspend
        if retry is not UNSET:
            field_dict["retry"] = retry

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        input_transforms = CreateFlowJsonBodyValueFailureModuleInputTransforms.from_dict(d.pop("input_transforms"))

        value = None

        stop_after_if: Union[Unset, CreateFlowJsonBodyValueFailureModuleStopAfterIf] = UNSET
        _stop_after_if = d.pop("stop_after_if", UNSET)
        if not isinstance(_stop_after_if, Unset):
            stop_after_if = CreateFlowJsonBodyValueFailureModuleStopAfterIf.from_dict(_stop_after_if)

        def _parse_sleep(
            data: object,
        ) -> Union[
            CreateFlowJsonBodyValueFailureModuleSleepType0, CreateFlowJsonBodyValueFailureModuleSleepType1, Unset
        ]:
            if isinstance(data, Unset):
                return data
            try:
                sleep_type_0: Union[Unset, CreateFlowJsonBodyValueFailureModuleSleepType0]
                if not isinstance(data, dict):
                    raise TypeError()
                sleep_type_0 = UNSET
                _sleep_type_0 = data
                if not isinstance(_sleep_type_0, Unset):
                    sleep_type_0 = CreateFlowJsonBodyValueFailureModuleSleepType0.from_dict(_sleep_type_0)

                return sleep_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            sleep_type_1: Union[Unset, CreateFlowJsonBodyValueFailureModuleSleepType1]
            sleep_type_1 = UNSET
            _sleep_type_1 = data
            if not isinstance(_sleep_type_1, Unset):
                sleep_type_1 = CreateFlowJsonBodyValueFailureModuleSleepType1.from_dict(_sleep_type_1)

            return sleep_type_1

        sleep = _parse_sleep(d.pop("sleep", UNSET))

        summary = d.pop("summary", UNSET)

        suspend: Union[Unset, CreateFlowJsonBodyValueFailureModuleSuspend] = UNSET
        _suspend = d.pop("suspend", UNSET)
        if not isinstance(_suspend, Unset):
            suspend = CreateFlowJsonBodyValueFailureModuleSuspend.from_dict(_suspend)

        retry: Union[Unset, CreateFlowJsonBodyValueFailureModuleRetry] = UNSET
        _retry = d.pop("retry", UNSET)
        if not isinstance(_retry, Unset):
            retry = CreateFlowJsonBodyValueFailureModuleRetry.from_dict(_retry)

        create_flow_json_body_value_failure_module = cls(
            input_transforms=input_transforms,
            value=value,
            stop_after_if=stop_after_if,
            sleep=sleep,
            summary=summary,
            suspend=suspend,
            retry=retry,
        )

        create_flow_json_body_value_failure_module.additional_properties = d
        return create_flow_json_body_value_failure_module

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
