def print_attribute(obj, attr: str = "available_checks"):
    result = getattr(obj, attr, dict())
    print("{}\n".format(attr.replace("_", " ").capitalize()))

    for k in result:
        print("    - {}".format(k))
    return


def print_available_improvements(
    obj,
    attributes=(
        "available_fixes",
        "available_checks",
        "available_enrichments",
        "available_renders",
    ),
    level=2,
):
    header = "Available improvements {}".format(obj.__class__.__name__)
    print_report_header(header, level=level)
    for a in [
        "available_fixes",
        "available_checks",
        "available_enrichments",
        "available_renders",
    ]:
        print_attribute(obj, a)
    return


def print_report_header(header: str, level: int = 1):
    spacing = max(min(3, 3 - level), 1)
    prefix = ("\n" * spacing) + ("#" * level)
    suffix = "\n" * spacing

    print(" ".join([prefix, header, suffix]))
    return
