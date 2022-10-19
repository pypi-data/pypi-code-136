from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.cluster import Cluster
from ..models.currency_amount import CurrencyAmount
from ..models.line_item import LineItem

T = TypeVar("T", bound="InvoiceItem")


@attr.s(auto_attribs=True)
class InvoiceItem:
    """
    Attributes:
        cluster (Cluster):  Example: {'account_id': '', 'cloud_provider': 'GCP', 'cockroach_version': 'v21.2.4',
            'config': {'serverless': {'routing_id': 'example-cluster-1533', 'spend_limit': 0}}, 'created_at':
            '2022-03-22T20:23:11.285067Z', 'creator_id': '7cde0cd9-0d8a-4008-8f90-45092ce8afc1', 'deleted_at': None, 'id':
            '35c4abb2-bb66-46d7-afed-25ebef5ed2aa', 'name': 'example-cluster', 'operation_status':
            'CLUSTER_STATUS_UNSPECIFIED', 'plan': 'SERVERLESS', 'regions': [{'name': 'us-central1', 'node_count': 0,
            'sql_dns': 'free-tier7.gcp-us-central1.crdb.io', 'ui_dns': ''}], 'state': 'CREATED', 'updated_at':
            '2022-03-22T20:23:11.879593Z'}.
        line_items (List[LineItem]): LineItems contain all the relevant line items from the Metronome invoice.
        totals (List[CurrencyAmount]): Totals is a list of the total amounts of line items per currency.
    """

    cluster: Cluster
    line_items: List[LineItem]
    totals: List[CurrencyAmount]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster = self.cluster.to_dict()

        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()

            line_items.append(line_items_item)

        totals = []
        for totals_item_data in self.totals:
            totals_item = totals_item_data.to_dict()

            totals.append(totals_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cluster": cluster,
                "line_items": line_items,
                "totals": totals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cluster = Cluster.from_dict(d.pop("cluster"))

        line_items = []
        _line_items = d.pop("line_items")
        for line_items_item_data in _line_items:
            line_items_item = LineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        totals = []
        _totals = d.pop("totals")
        for totals_item_data in _totals:
            totals_item = CurrencyAmount.from_dict(totals_item_data)

            totals.append(totals_item)

        invoice_item = cls(
            cluster=cluster,
            line_items=line_items,
            totals=totals,
        )

        invoice_item.additional_properties = d
        return invoice_item

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
