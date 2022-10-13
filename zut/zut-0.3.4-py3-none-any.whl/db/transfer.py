from __future__ import annotations
import logging, csv
from pathlib import Path
from django.utils import timezone
from ..format import slugen
from . import get_connection, call_procedure, truncate_table

logger = logging.getLogger(__name__)

def _compute_pathes(sql_path: Path, csv_path: Path|str = None) -> Path:
    if not isinstance(sql_path, Path):
        sql_path = Path(sql_path)

    if not csv_path:
        csv_path = sql_path.parent.joinpath(sql_path.stem + ".local.csv")
    else:
        if not isinstance(csv_path, Path):
            csv_path = Path(csv_path)
        if csv_path.is_dir():
            csv_path = csv_path.joinpath(sql_path.stem + ".local.csv")

    csv_path.parent.mkdir(parents=True, exist_ok=True)

    return sql_path, csv_path


def extract_from_sql(sql_path: Path|str, connection: str|object = None,
    csv_path: Path|str = None,
    delimiter = ";", encoding="utf-8") -> int:
    """
    Extract data using a query file to a CSV file.
    - `sql_path`: file containing the extract query.
    - `connection`: source connection. If `None`, use default Django connection.
    """
    sql_path, csv_path = _compute_pathes(sql_path, csv_path)
    connection = get_connection(connection=connection)

    logger.info(f"extract {sql_path} to {csv_path}")

    # For CSV file:
    # - Set newline to '', otherwise newlines embedded inside quoted fields will not be interpreted correctly. See footnote of: https://docs.python.org/3/library/csv.html
    # - Set encoding to utf-8-sig (UTF8 with BOM): CSV is for exchanges, encoding should not depend on the exporting operating system. BOM is necessary for correct display with Excel
    with open(csv_path, "w", newline="", encoding="utf-8-sig" if encoding == "utf-8" else encoding) as file:
        writer = csv.writer(file, delimiter=delimiter)
        with connection.cursor() as cursor:
            cursor.execute(sql_path.read_text())

            writer.writerow([column[0] for column in cursor.description])
            row = cursor.fetchone()
            while row: 
                writer.writerow([value for value in row])
                row = cursor.fetchone()


def load_from_csv(path: Path|str, model: type,
    truncate: bool = True, integrate: str|list[str] = None,
    delimiter = ";", encoding = "utf-8", accept_ignored_headers = True, mapping = None, static_mapping = None) -> int:
    """
    Load from CSV file `path` to `model` class.
    
    Model class must be defined with CopyManager. Example:

    ```py
    from django.db import models
    from postgres_copy import CopyManager

    class MyModel(models.Model):
        objects = CopyManager()
    ```
    """
    if isinstance(path, str):
        path = Path(path)
        
    if not hasattr(model, "objects") or not hasattr(model.objects, "from_csv"):    
        raise ValueError("missing %s.objects.from_csv, did you specified `objects = CopyManager()`?" % model.__qualname__)

    db_table = model._meta.db_table
    logger.info("load %s in table %s (model %s)", path, db_table, model.__name__)

    fields = [field.name for field in model._meta.get_fields()]

    # Change encoding to utf-8-sig if file starts with UTF8-BOM
    if encoding == "utf-8":
        with open(path, mode="r", encoding="utf-8") as file:
            data = file.read(1)
            if data == "\ufeff":
                encoding = "utf-8-sig"

    # Get CSV headers
    headers = []
    with open(path, newline="", encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            headers = row
            break

    if not headers:
        raise ValueError("headers not found in %s", path)

    # Build mapping
    if mapping is None:
        mapping = {}

    def search_field(name, lowersearch):
        """ Returns True to continue headers loop"""
        for field in fields:
            if field.lower() == lowersearch:
                if field in mapping:
                    logger.warning("ignore header \"%s\": cannot map to field \"%s\" (already added mapped to header \"%s\")", name, field, mapping[field])                    
                    return True
                mapping[field] = name
                return True
        return False

    ignored_headers = ""
    for name in headers:
        # Try to find field using lowercase
        if search_field(name, name.lower()):
            continue

        # Try to find field using slug
        slug = slugen(name, separator="_")
        if search_field(name, slug):
            continue

        # Not found in fields
        ignored_headers += (", " if ignored_headers else "") + name + (f" ({slug})" if slug != name else "")

    if ignored_headers:
        logger.log(logging.INFO if accept_ignored_headers else logging.WARNING, "headers ignored in %s: %s", path.name, ignored_headers)

    if static_mapping is None:
        static_mapping = {}
    if "load_at" in fields and not "load_at" in static_mapping:
        static_mapping["load_at"] = timezone.now()
   
    # Truncate table
    if truncate:
        truncate_table(model)

    # Load
    with open(path, newline="", encoding=encoding) as file:
        insert_count = model.objects.from_csv(file, mapping=mapping, static_mapping=static_mapping, delimiter=delimiter)
        logger.info("%d records loaded in %s", insert_count, db_table)

    # Integrate
    if integrate:
        if not isinstance(integrate, list):
            integrate = [integrate]

        dst_connection = get_connection(model=model)
        call_procedure(names=integrate, connection=dst_connection)

    return insert_count


def transfer_from_sql(sql_path: Path|str, model: type, connection: str|object = None,
    truncate: bool = True, integrate: str|list[str] = None,
    csv_path: Path|str = None,
    skip_extract = False, skip_load = False,
    delimiter = ";", encoding="utf-8", accept_ignored_headers = True, mapping = None, static_mapping = None) -> int|None:
    """
    Extract data using a query file to a CSV file, and load the CSV file to a model class.
    - `sql_path`: file containing the extract query.
    - `model`: target Model.
    - `connection`: source connection (used during extract from `sql_path`). If `None`, use default Django connection.
    """
    sql_path, csv_path = _compute_pathes(sql_path, csv_path)

    result = None

    if not skip_extract:
        extract_from_sql(sql_path, connection=connection, csv_path=csv_path, delimiter = ";", encoding="utf-8")

    if not skip_load and model:
        result = load_from_csv(csv_path, model, truncate=truncate, integrate=integrate, delimiter=delimiter, encoding=encoding, accept_ignored_headers=accept_ignored_headers, mapping=mapping, static_mapping=static_mapping)
        
    return result
