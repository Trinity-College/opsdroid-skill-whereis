from opsdroid.matchers import match_regex
import logging
import random

def setup(opsdroid):
    logging.debug("Loaded hello module")

@match_regex(r'where_is ([a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2})$')
async def hello(opsdroid, config, message):
    mac = message.regex.group(1)

    # Fire off the command line
    # TODO: https://docs.python.org/3/library/asyncio-subprocess.html

    # Send the output
    await message.respond(text)

@match_regex(r'bye( bye)?|see y(a|ou)|au revoir|gtg|I(\')?m off')
async def goodbye(opsdroid, config, message):
    text = random.choice(["Bye {}", "See you {}", "Au revoir {}"]).format(message.user)
    await message.respond(text)
