def get_package_dir(__config: dict):
    package_dir = str(__config["package_dir"])
    package_name = str(__config["package_name"])
    while package_dir.endswith("/") and len(package_dir) > 1:
        package_dir = package_dir[:-1]
    if package_dir.endswith(package_name):
        package_dir += "/"
    else:
        package_dir += f"/{package_name}"

    if package_dir.startswith("~"):
        package_dir = package_dir[1:]
    if not package_dir.startswith("/"):
        package_dir = package_dir + "/"
    return package_dir
