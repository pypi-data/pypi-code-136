from .bp.create_outgoing_event import CreateOutgoingEvent
from .bp.create_image_block import CreateImageBlock
from .bp.create_image_button import CreateImageButton
from .bp import *
from .svc import *
from .dmo import *
from .dto import *

from .bp.normalize_incoming_event import NormalizeIncomingEvent


def normalize_event(d_event: dict,
                    bot_ids: list) -> dict:
    """ Normalize the Incoming Slack Event

    Args:
        d_event (dict): the incoming Slack Event
        Sample Input:
            {
                'blocks': [
                    {
                        'block_id': 'vz+U',
                        'elements': [
                            ...
                        ],
                        'type': 'rich_text'
                    }
                ],
                'channel': 'C046DB9TLEL',
                'team': 'T045AR44M70',
                'text': '<@U045HCSMG8K> dead ahead!',
                'ts': 1665195085.499959,
                'type': 'app_mention',
                'user': 'U04674UNRBJ'
            }
        bot_ids (list): a list of known Bot IDs

    Returns:
        dict: the normalized Slack event
        Sample Output:
            {
                'membership': '43fd5022_46c3_11ed_aca2_4c1d96716627'
                'event': {
                    ... copy of input event ...
                },
                'analysis': {
                    'commands': [],
                    'meta_mode': 'human2bot',
                    'meta_type': 'H2B_SINGLE',
                    'text_1': '@U045HCSMG8K dead ahead!',
                    'text_2': 'dead ahead!',
                    'user_all': ['U045HCSMG8K'],
                    'user_source': 'U04674UNRBJ',
                    'user_target': 'U045HCSMG8K'
                },
            }
    """
    return NormalizeIncomingEvent(bot_ids).process(d_event)


def create_image_block(image_url: str,
                       d_event_incoming: dict) -> dict:
    """ Create an Image-only Blocks Response

    Args:
        image_url (str): a public URL for a slack image
        d_event_incoming (dict): the incoming slack event
            -   This is required to obtain the channel, thread timestamp (thread_ts) and input text (text)
            -   It was thought easier to pass the original (non-normalized) Slack event as a parameter value
                than to request these individual values

    Returns:
        dict: the outgoing slack event
    """
    return CreateImageBlock().process(
        image_url=image_url,
        d_event_incoming=d_event_incoming)


def create_image_button(d_event_incoming: dict,
                        output_text: str,
                        image_url: str,
                        button_text: str = "View Page") -> dict:
    """ Create and Format Outgoing Slack Events

    Args:
        d_event_incoming (dict): the incoming slack event
        output_text (str): the incoming slack event
        image_url (str): a public URL for a slack image
        button_text (str): the button text

    Returns:
        dict: the outgoing slack event
    """
    return CreateImageButton().process(
        image_url=image_url,
        output_text=output_text,
        button_text=button_text,
        d_event_incoming=d_event_incoming)


def create_outgoing_event(output_text: str,
                          d_event_incoming: dict) -> dict:
    """ Create an Outgoing Slack Event

    Args:
        output_text (str): the outgoing slack message
            -   The message to display in Slack to the consumer
        d_event_incoming (dict): the incoming slack event
            -   This is required to obtain the channel, thread timestamp (thread_ts) and input text (text)
            -   It was thought easier to pass the original (non-normalized) Slack event as a parameter value
                than to request these individual values

    Returns:
        dict: the outgoing slack event
    """
    return CreateOutgoingEvent().process(
        output_text=output_text,
        d_event_incoming=d_event_incoming)
