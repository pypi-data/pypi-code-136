import logging
from typing import List

from tabulate import tabulate

from edmgr.utils import convert_bytes_size


logger = logging.getLogger(__name__)


def _format_table(serializer, items: List[dict], **kwargs) -> str:
    items = [serializer(item, **kwargs) for item in items]
    return tabulate(
        items, headers="keys", tablefmt=kwargs.get("tablefmt", "fancy_grid")
    )


def _format_country(country: dict, with_link: bool = False) -> str:
    link = country.get("uri")
    link_str = f" - {link}" if with_link else ""
    return f"{country.get('id', 'None').upper()}{link_str}"


def serialize_entitlement(
    entitlement: dict, with_conuntry_links: bool = False, **kwargs
) -> dict:
    format_country = _format_country
    qualities = ", ".join(
        [e.get("quality") for e in entitlement.get("rights", {}).get("qualities", {})]
    )
    countries = "\n".join(
        [
            format_country(country, with_conuntry_links)
            for country in entitlement.get("compliance", {}).get("allowedCountries", {})
        ]
    )
    characteristics = entitlement.get("characteristics", {})
    grouped = characteristics.get("grouped")
    virtual = characteristics.get("virtual")
    if grouped:
        virtual_entilements_len = len(entitlement.get("virtualEntitlements", []))
        entitlement_type = f"group ({virtual_entilements_len} entitlements)"
    elif virtual:
        entitlement_type = "virtual entitlement"
    else:
        entitlement_type = "entitlement"
    return {
        "ID": entitlement.get("id"),
        "Type": entitlement_type,
        "Product Code": entitlement.get("product", {}).get("id"),
        "Product Name": entitlement.get("product", {}).get("name"),
        "Status": entitlement.get("status"),
        "Right To": entitlement.get("rightTo"),
        "Valid From": entitlement.get("validFrom"),
        "Valid To": entitlement.get("validTo"),
        "Qualities": qualities,
        "Allowed Countries": countries,
        "Compliance": entitlement.get("compliance", {}).get("status"),
        # TODO: Where is Contract coming from?
        # 'Contract': 'See TODO comment in edmgrcli'
    }


def serialize_virtual_entitlements(virtual_entitlement: dict, **kwargs) -> dict:
    foundries = virtual_entitlement.get("product", {}).get("foundry", [])
    return {
        "ID": virtual_entitlement.get("id"),
        "Product Code": virtual_entitlement.get("product", {}).get("id"),
        "Product Name": virtual_entitlement.get("product", {}).get("name"),
        "Product URI": virtual_entitlement.get("product", {}).get("uri"),
        "Foundries": ", ".join(foundries),
        "Process": virtual_entitlement.get("product", {}).get("process"),
    }


def serialize_release(release: dict, **kwargs) -> dict:
    return {
        "ID": release.get("id"),
        "Entitlement ID": release.get("entitlement", {}).get("id"),
        "Release Name": release.get("name"),
        "Revision": release.get("revision"),
        "Patch": release.get("patch"),
        "Major": release.get("majorVersion"),
        "Minor": release.get("minorVersion"),
        "Quality": release.get("quality"),
        "Type": release.get("type"),
        "Available At": release.get("availableAt"),
    }


def serialize_artifact(artifact: dict, **kwargs) -> dict:
    size = artifact.get("fileSize")
    bytes_size = convert_bytes_size(size, **kwargs) if size is not None else None
    return {
        "ID": artifact.get("id"),
        "Name": artifact.get("name"),
        "Description": artifact.get("description"),
        "Type": artifact.get("type"),
        "File Name": artifact.get("fileName"),
        "File Size": bytes_size,
        "MD5": artifact.get("md5"),
    }


def format_entitlements(entitlements: List[dict], **kwargs) -> str:
    return _format_table(serialize_entitlement, entitlements, **kwargs)


def format_releases(releases: List[dict], **kwargs) -> str:
    return _format_table(serialize_release, releases, **kwargs)


def format_artifacts(artifacts: List[dict], **kwargs) -> str:
    return _format_table(serialize_artifact, artifacts, **kwargs)


def format_entitlement(entitlement: dict, **kwargs) -> str:
    offset = kwargs.get("offset")
    entitlement_view = serialize_entitlement(
        entitlement, with_conuntry_links=True, **kwargs
    )
    enhaced_entitlement_view = {
        "ID": entitlement_view["ID"],
        "Type": entitlement_view["Type"],
        "Product Code": entitlement_view["Product Code"],
        "Product Name": entitlement.get("product", {}).get("name"),
        "Product URI": entitlement.get("product", {}).get("uri"),
        "Status": entitlement_view["Status"],
        "Right To": entitlement_view["Right To"],
        "Valid From": entitlement_view["Valid From"],
        "Valid To": entitlement_view["Valid To"],
        "Qualities": entitlement_view["Qualities"],
        "Allowed Countries": entitlement_view["Allowed Countries"],
        "Compliance Status": entitlement_view["Compliance"],
        "Compliance Reason": entitlement.get("compliance", {}).get("statusReason"),
        "ECCN Restricted": entitlement.get("compliance", {}).get("eccnRestricted"),
        "Maintainance From": entitlement.get("rights", {}).get("maintenanceFrom"),
        "Maintainance To": entitlement.get("rights", {}).get("maintenanceTo"),
        "Created At": entitlement.get("history", {}).get("createdAt"),
        "Created By": entitlement.get("history", {}).get("createdBy"),
        "Last Changed": entitlement.get("history", {}).get("lastChangedAt"),
        "Last Changed By": entitlement.get("history", {}).get("lastChangedBy"),
    }
    design_start_rights = entitlement.get("rights", {}).get("designStart")
    if design_start_rights:
        foundries = ", ".join([right.get("foundry") for right in design_start_rights])
        enhaced_entitlement_view = {
            **enhaced_entitlement_view,
            "Foundries": foundries,
        }
    output = tabulate(
        enhaced_entitlement_view.items(), tablefmt=kwargs.get("tablefmt", "fancy_grid")
    )
    total_virtual_entitlements = len(entitlement.get("virtualEntitlements", []))
    page = 1
    limit = total_virtual_entitlements
    if offset is not None:
        page = max(int(offset), page)
        limit = min(int(kwargs["limit"]), limit)
    start = (page - 1) * limit
    end = min(page * limit, total_virtual_entitlements)
    if total_virtual_entitlements:
        if start < end:
            virtual_entitlements = entitlement.get("virtualEntitlements", [])[start:end]
            output += (
                f"\n\nShowing from {start + 1} to {end} of {total_virtual_entitlements} "
                "Entitlements in this group:\n\n"
            )
            output += _format_table(
                serialize_virtual_entitlements,
                virtual_entitlements,
                **kwargs,
            )
        else:
            output += (
                "\n\nEntitlements page out of range. "
                f"Please check offset ({offset}) and/or limit ({limit}) options. "
                f"Total number of Entitlements in this group is {total_virtual_entitlements}\n\n"
            )
    return output
