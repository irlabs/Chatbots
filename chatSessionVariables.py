#!/usr/bin/env python

# chatSessionVariables.py

# Helper to store and retrieve session variables

# These session variables have be consistent between
# restarts of the client-server channel, or between
# multiple instances of the server process.
# We use redis to make sure these session variables
# persist accross different launches.

import os
import redis
import inspect

# REDIS_URL = os.environ['REDIS_URL']
REDIS_URL = 'redis://localhost:6379'
GLOBALS_KEY = 'globals'

redis = redis.from_url(REDIS_URL)


# Get the bot's global variable values
def storeGlobals(bot, withSession):
    #
    # Read all globals (__dict__)
    for key, value in bot.__dict__.iteritems():
        # Ignore python internals (__builtins__ etc.)
        if not key.startswith('__'):
            # Ignore all function (<type 'function'>)
            if not callable(value):
                # Ignore all (imported modules)
                if not inspect.ismodule(value):
                    #
                    # This is the list of global variables
                    print key, type(value), value
                    storeVariable(withSession, key, type(value), value)


def storeVariable(session, key, type, value):
    if type is int:
        k = "{}.{}.{}.{}".format(GLOBALS_KEY, session, key, "int")
        redis.set(k, value)
    elif type is str:
        k = "{}.{}.{}.{}".format(GLOBALS_KEY, session, key, "str")
        redis.set(k, value)
    elif type is bool:
        k = "{}.{}.{}.{}".format(GLOBALS_KEY, session, key, "bool")
        redis.set(k, value)
    elif type is float:
        k = "{}.{}.{}.{}".format(GLOBALS_KEY, session, key, "float")
        redis.set(k, value)
    else:
        print """Error: chatSessionVariables could not store
        type: {}""".format(type)


def retrieveVariable(key):
    t = key.split('.')[-1]
    if t == "int":
        return int(redis.get(key))
    elif t == "str":
        return redis.get(key)
    elif t == "bool":
        return redis.get(key) == "True"
    elif f == "float":
        return float(redis.get(key))
    else:
        print """Error: chatSessionVariables could not cast data
        as type: {} {}""".format(t, key)
        return None


# Set the bot's global variable values to our session's
def injectGlobals(bot, fromSession):
    # Get the list of keys stored in this session
    q = "{}.{}.*.*".format(GLOBALS_KEY, fromSession)
    keys = redis.keys(q)
    for k in keys:
        keyname = k.split('.')[-2]
        value = retrieveVariable(k)
        bot.__dict__[keyname] = value
