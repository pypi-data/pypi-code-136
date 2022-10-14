import click

from freedomrobotics_api.cli.commands.base import (
    add_options, common_options, api_options, listing_options,
    error_message_catch, parse_list_option, parse_dict_option,
    get_freedom_client, echo_json, FREEDOM_UTC_RANGE
)

device_common_options = [
    click.option('--id', help="Device id"),
    click.option('--name', help="Device name"),
]


@click.group()
def device():
    pass


@device.command()
@add_options(common_options)
@add_options(api_options)
@add_options(device_common_options)
def get(**kwargs):
    client = get_freedom_client(**kwargs)

    _, device_info = get_device(client, raw=True, **kwargs)

    echo_json(device_info)


@device.command()
@add_options(common_options)
@add_options(listing_options)
@click.option('--zones', help='List of zones to filter separated by comma')
@click.option('--include-subzones',
              is_flag=True,
              help='Include also subzones in result. This will have effect only when using --zones')
def list(**kwargs):
    client = get_freedom_client(**kwargs)

    with error_message_catch("Fetch account", show_info_msg=False):
        account = client.get_account(kwargs.get('account_id'))

    attributes = parse_list_option('attributes', kwargs)
    zones = parse_list_option('zones', kwargs)
    include_subzones = kwargs.get('include_subzones')
    params = parse_dict_option('params', kwargs)

    with error_message_catch("Fetch devices", show_info_msg=False):
        devices = account.get_devices(
            attributes=attributes,
            zones=zones,
            include_subzones=include_subzones,
            params=params,
            raw=True,
        )
    echo_json(devices)


@device.group()
def data(**kwargs):
    pass


@data.command(name="get")
@add_options(common_options)
@add_options(device_common_options)
@click.option('--utc-start', type=FREEDOM_UTC_RANGE, help="Starting time for fetching data.")
@click.option('--utc-end', type=FREEDOM_UTC_RANGE, help="End time for fetching data.")
@click.option('-t', '--topics', help="List of topics to filter separated by comma.")
@click.option('--exclude-topics', help="list of topics to exclude from results separated by comma.")
@click.option('-l', '--loop', is_flag=True,
              help=("Keep it looping fetching for data. If --utc-start and --utc-end are present, "
                    "will continue returning the data between those dates. If no --utc-end will start  "
                    "continue fetching live data over and over."))
def data_get(**kwargs):
    client = get_freedom_client(**kwargs)
    _, device_obj = get_device(client, raw=False, **kwargs)

    topics = parse_list_option('topics', kwargs)
    exclude_topics = parse_list_option('exclude_topics', kwargs)

    start = kwargs.get('utc_start')
    end = kwargs.get('utc_end')
    params = {}
    if exclude_topics is not None:
        params['exclude_topics'] = exclude_topics

    for item in device_obj.data(
            topics=topics,
            start=start,
            end=end,
            loop=kwargs.get('loop'),
            **params):
        echo_json(item)


def get_device(client, raw=False, account=None, **kwargs):
    """Gets a device either by id or by name and returns it
    Parameters:
    * client (FreedomClient)
    * raw (bool): If True, will return the raw JSON instead of the object wrapper.
    * account (Account): Optional argument to use the specified account object to get the device.
    """
    device_id = kwargs.get('id')
    device_name = kwargs.get('name')
    if not device_id and not device_name:
        raise click.UsageError("Either device --id or --name should be specified.")

    if account is None:
        with error_message_catch("Fetch account", show_info_msg=False):
            account = client.get_account(kwargs.get('account_id'))

    with error_message_catch("Fetch device", show_info_msg=False):
        params = parse_dict_option('params', kwargs)
        if device_id:
            result = account.get_device(device_id, params=params, raw=raw)
        elif device_name:
            devices = account.get_devices(attributes=['name'], params=params)
            for device_obj in devices:
                if device_obj.name.lower() == device_name.lower():
                    break
            else:
                raise Exception(f"Cannot find device with name `{device_name}`")
            device_obj.update()  # retrieve all data once its found
            if raw:
                result = device_obj._data
            else:
                result = device_obj
    return account, result
