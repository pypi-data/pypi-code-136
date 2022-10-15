from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.list_flows_response_200_item_value_modules_item_input_transforms import (
    ListFlowsResponse200ItemValueModulesItemInputTransforms,
)
from ..models.list_flows_response_200_item_value_modules_item_retry import ListFlowsResponse200ItemValueModulesItemRetry
from ..models.list_flows_response_200_item_value_modules_item_sleep_type_0 import (
    ListFlowsResponse200ItemValueModulesItemSleepType0,
)
from ..models.list_flows_response_200_item_value_modules_item_sleep_type_1 import (
    ListFlowsResponse200ItemValueModulesItemSleepType1,
)
from ..models.list_flows_response_200_item_value_modules_item_stop_after_if import (
    ListFlowsResponse200ItemValueModulesItemStopAfterIf,
)
from ..models.list_flows_response_200_item_value_modules_item_suspend import (
    ListFlowsResponse200ItemValueModulesItemSuspend,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListFlowsResponse200ItemValueModulesItem")


@attr.s(auto_attribs=True)
class ListFlowsResponse200ItemValueModulesItem:
    """ """

    input_transforms: ListFlowsResponse200ItemValueModulesItemInputTransforms
    value: None
    stop_after_if: Union[Unset, ListFlowsResponse200ItemValueModulesItemStopAfterIf] = UNSET
    sleep: Union[
        ListFlowsResponse200ItemValueModulesItemSleepType0, ListFlowsResponse200ItemValueModulesItemSleepType1, Unset
    ] = UNSET
    summary: Union[Unset, str] = UNSET
    suspend: Union[Unset, ListFlowsResponse200ItemValueModulesItemSuspend] = UNSET
    retry: Union[Unset, ListFlowsResponse200ItemValueModulesItemRetry] = UNSET
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
        elif isinstance(self.sleep, ListFlowsResponse200ItemValueModulesItemSleepType0):
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
        input_transforms = ListFlowsResponse200ItemValueModulesItemInputTransforms.from_dict(d.pop("input_transforms"))

        value = None

        stop_after_if: Union[Unset, ListFlowsResponse200ItemValueModulesItemStopAfterIf] = UNSET
        _stop_after_if = d.pop("stop_after_if", UNSET)
        if not isinstance(_stop_after_if, Unset):
            stop_after_if = ListFlowsResponse200ItemValueModulesItemStopAfterIf.from_dict(_stop_after_if)

        def _parse_sleep(
            data: object,
        ) -> Union[
            ListFlowsResponse200ItemValueModulesItemSleepType0,
            ListFlowsResponse200ItemValueModulesItemSleepType1,
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                sleep_type_0: Union[Unset, ListFlowsResponse200ItemValueModulesItemSleepType0]
                if not isinstance(data, dict):
                    raise TypeError()
                sleep_type_0 = UNSET
                _sleep_type_0 = data
                if not isinstance(_sleep_type_0, Unset):
                    sleep_type_0 = ListFlowsResponse200ItemValueModulesItemSleepType0.from_dict(_sleep_type_0)

                return sleep_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            sleep_type_1: Union[Unset, ListFlowsResponse200ItemValueModulesItemSleepType1]
            sleep_type_1 = UNSET
            _sleep_type_1 = data
            if not isinstance(_sleep_type_1, Unset):
                sleep_type_1 = ListFlowsResponse200ItemValueModulesItemSleepType1.from_dict(_sleep_type_1)

            return sleep_type_1

        sleep = _parse_sleep(d.pop("sleep", UNSET))

        summary = d.pop("summary", UNSET)

        suspend: Union[Unset, ListFlowsResponse200ItemValueModulesItemSuspend] = UNSET
        _suspend = d.pop("suspend", UNSET)
        if not isinstance(_suspend, Unset):
            suspend = ListFlowsResponse200ItemValueModulesItemSuspend.from_dict(_suspend)

        retry: Union[Unset, ListFlowsResponse200ItemValueModulesItemRetry] = UNSET
        _retry = d.pop("retry", UNSET)
        if not isinstance(_retry, Unset):
            retry = ListFlowsResponse200ItemValueModulesItemRetry.from_dict(_retry)

        list_flows_response_200_item_value_modules_item = cls(
            input_transforms=input_transforms,
            value=value,
            stop_after_if=stop_after_if,
            sleep=sleep,
            summary=summary,
            suspend=suspend,
            retry=retry,
        )

        list_flows_response_200_item_value_modules_item.additional_properties = d
        return list_flows_response_200_item_value_modules_item

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
