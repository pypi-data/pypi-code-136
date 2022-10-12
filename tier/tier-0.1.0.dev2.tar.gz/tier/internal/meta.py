name = 'tier'
try:
    import pkg_resources

    version = pkg_resources.get_distribution(name).get_version
except:
    version = '0.0.0'

name_version = f'{name}-{version}'
