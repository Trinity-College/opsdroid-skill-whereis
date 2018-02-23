from opsdroid.matchers import match_regex
import logging
import random

from subprocess import PIPE

def setup(opsdroid):
    logging.debug("Loaded where_is module")

@match_regex(r'where_is ([a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2})$')
async def where_is(opsdroid, config, message):
    mac = message.regex.group(1)

    # Fire off the command line program "where_is" with the mac address as
    # the first argument.
    # TODO: work out how to do this in async land. i.e. read
    # https://docs.python.org/3/library/asyncio-subprocess.html

    # Send the output
    await message.respond(text)

