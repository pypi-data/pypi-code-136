from typing import Optional
import requests
from dataclasses import dataclass


class AirtableBase:
    insert_limit = 10

    def __init__(self, base_id: str, bearer_token: str):
        self._base_id = base_id
        self._bearer_token = bearer_token

    def _get_records_paginated(
            self,
            table_id: str,
            *,
            page_size: int = 100,
            filter_by_formula: Optional[str] = None) -> list[dict]:
        offset = None
        first = True
        records = []
        while first or offset:
            result = requests.get(
                f"https://api.airtable.com/v0/{self._base_id}/{table_id}",
                params={
                    "pageSize": page_size,
                    **({"offset": offset} if offset else {}),
                    **({"filterByFormula": filter_by_formula} if filter_by_formula else {})
                },
                headers={
                    "Authorization": f"Bearer {self._bearer_token}"
                }
            )
            result.raise_for_status()
            data = result.json()
            offset = data.get("offset")
            records.extend(data.get("records", []))
            first = False

        return records

    def get_records(self, table_id: str, filter_by_formula: Optional[str] = None) -> list[dict]:
        return self._get_records_paginated(table_id, filter_by_formula=filter_by_formula)

    def get_record(self, table_id: str, record_id: str) -> dict:
        result = requests.get(
            f"https://api.airtable.com/v0/{self._base_id}/{table_id}/{record_id}",
            headers={
                "Authorization": f"Bearer {self._bearer_token}"
            }
        )
        result.raise_for_status()
        return result.json()

    def _create_records(self, table_id: str, records: list[dict]) -> list[dict]:
        assert len(records) <= 10
        result = requests.post(
            f"https://api.airtable.com/v0/{self._base_id}/{table_id}",
            headers={
                "Authorization": f"Bearer {self._bearer_token}",
                "Content-Type": "application/json"
            },
            json={
                "records": [
                    {"fields": record}
                    for record in records
                ]
            }
        )
        result.raise_for_status()
        return result.json().get("records", [])

    def create_records(self, table_id: str, records: list[dict]) -> list[dict]:
        created_records = []
        for i in range(0, len(records), self.insert_limit):
            created_records.extend(self._create_records(
                table_id, records[i:i + self.insert_limit]))
        return created_records

    def _update_records(self, table_id: str, records: dict[str, dict]) -> list[dict]:
        assert len(records) <= 10
        result = requests.patch(
            f"https://api.airtable.com/v0/{self._base_id}/{table_id}",
            headers={
                "Authorization": f"Bearer {self._bearer_token}",
                "Content-Type": "application/json"
            },
            json={
                "records": [
                    {
                        "id": idx,
                        "fields": record
                    }
                    for idx, record in records.items()
                ]
            }
        )
        result.raise_for_status()
        return result.json().get("records", [])

    def update_records(self, table_id: str, records: dict[str, dict]) -> list[dict]:
        updated_records = []
        items = list(records.items())
        for i in range(0, len(items), self.insert_limit):
            updated_records.extend(self._update_records(
                table_id,
                {key: value for key, value in items[i:i + self.insert_limit]}
            ))
        return updated_records


class AirtableTable:
    def __init__(self, base_id: str, table_id: str, bearer_token: str):
        self._base = AirtableBase(base_id, bearer_token)
        self._table_id = table_id

    def get_records(self, filter_by_formula: Optional[str] = None) -> list[dict]:
        return self._base.get_records(self._table_id, filter_by_formula=filter_by_formula)

    def get_record(self, record_id: str) -> dict:
        return self._base.get_record(self._table_id, record_id)

    def create_records(self, records: list[dict]) -> list[dict]:
        return self._base.create_records(self._table_id, records)

    def update_records(self, records: dict[str, dict]) -> list[dict]:
        return self._base.update_records(self._table_id, records)
