#!/usr/bin/env python3

import argparse
import io
import jsonschema
import simplejson as json
import os
import sys
from datetime import datetime
from pathlib import Path
import hdfs

import singer
from jsonschema import Draft4Validator, FormatChecker
from adjust_precision_for_schema import adjust_decimal_precision_for_schema

logger = singer.get_logger()


def emit_state(state):
    if state is not None:
        line = json.dumps(state)
        logger.debug('Emitting state {}'.format(line))
        sys.stdout.write("{}\n".format(line))
        sys.stdout.flush()



def persist_messages(
    messages,
    destination_path,
    custom_name=None,
    do_timestamp_file=True,
    webhdfs=False,
    webhdfs_url=None,
    webhdfs_user=None,
    webhdfs_overwrite=False,
):
    state = None
    schemas = {}
    key_properties = {}
    validators = {}

    timestamp_file_part = '-' + datetime.now().strftime('%Y%m%dT%H%M%S') if do_timestamp_file else ''

    for message in messages:
        try:
            o = singer.parse_message(message).asdict()
        except json.decoder.JSONDecodeError:
            logger.error("Unable to parse:\n{}".format(message))
            raise
        message_type = o['type']
        if message_type == 'RECORD':
            if o['stream'] not in schemas:
                raise Exception(
                    "A record for stream {}"
                    "was encountered before a corresponding schema".format(o['stream'])
                )

            try:
                validators[o['stream']].validate((o['record']))
            except jsonschema.ValidationError as e:
                logger.error(f"Failed parsing the json schema for stream: {o['stream']}.")
                raise e

            filename = (custom_name or o['stream']) + timestamp_file_part + '.jsonl'

            if webhdfs:
                webhdfs_client = hdfs.InsecureClient(url=webhdfs_url, user=webhdfs_user)
                result_path = f'{destination_path}/{filename}'

                file_status = webhdfs_client.status(result_path, strict=False)
                webhdfs_append = True
                if file_status is None:
                    webhdfs_append = False

                if webhdfs_overwrite:
                    webhdfs_append = False
                webhdfs_client.write(result_path, data=json.dumps(o['record']) + '\n', overwrite=webhdfs_overwrite, append=webhdfs_append)

                state = None
            else:
                if destination_path:
                    Path(destination_path).mkdir(parents=True, exist_ok=True)
                filename = os.path.expanduser(os.path.join(destination_path, filename))

                with open(filename, 'a', encoding='utf-8') as json_file:
                    json_file.write(json.dumps(o['record']) + '\n')

                state = None

        elif message_type == 'STATE':
            logger.debug('Setting state to {}'.format(o['value']))
            state = o['value']
        elif message_type == 'SCHEMA':
            stream = o['stream']
            schemas[stream] = o['schema']
            adjust_decimal_precision_for_schema(schemas[stream])
            validators[stream] = Draft4Validator((o['schema']))
            key_properties[stream] = o['key_properties']
        else:
            logger.warning("Unknown message type {} in message {}".format(o['type'], o))

    return state


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='Config file')
    args = parser.parse_args()

    if args.config:
        with open(args.config) as input_json:
            config = json.load(input_json)
    else:
        config = {}

    input_messages = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    state = persist_messages(
        input_messages,
        config.get('destination_path', ''),
        config.get('custom_name', ''),
        config.get('do_timestamp_file', True),
        config.get('webhdfs', False),
        config.get('webhdfs_url', ''),
        config.get('webhdfs_user', ''),
        config.get('webhdfs_overwrite', False),
    )

    emit_state(state)
    logger.debug("Exiting normally")


if __name__ == '__main__':
    main()
