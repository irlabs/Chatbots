#!/usr/bin/env python

# Command Line Interface (CLI) version

import os
import sys
import time
import chatSessionVariables as sessionVars
import rogerbot as bot


# Chat Server Framework functions

def sleep(n):
    """Sleep n number of seconds.
    Pauses the execution of the program.
    """
    time.sleep(n)


def output(s):
    """Outputs string s as chat message.
    Send the given string to the chat client.
    """
    print s


# Get the session from python introspection

def sessionFromIntrospection():
    selfFile = os.path.splitext(os.path.basename(__file__))[0]
    callDepth = 2
    caller = None
    try:
        while True:
            caller = sys._getframe(callDepth)
            callerFullPath = caller.f_code.co_filename
            callerFile = os.path.splitext(os.path.basename(callerFullPath))[0]
            if callerFile == selfFile:
                break
            callDepth += 1
    except ValueError:
        return "Session-NotFound-ToDeep"
    if caller:
        session = caller.f_locals.get('session', "Session-NotFound-NoLocalVar")
        return session
    return "Session-NotFound-NoCaller"


# Run forever on the command line

def main():
    """docstring for main"""
    # Test local session variable
    session = "12345"
    #
    # Setup
    # Pre-setup we're not interested in the bot's global variables.
    bot.setup()
    # After setup we need to capture the state of the global vars
    sessionVars.storeGlobals(bot, session)
    #
    # Run continuesly
    while True:
        humanSpeak = raw_input("> ")
        #
        # Before responding, we need to inject the session state
        sessionVars.injectGlobals(bot, session)
        bot.response(humanSpeak)
        # After responding, capture the global vars for the session state
        sessionVars.storeGlobals(bot, session)


if __name__ == '__main__':
    main()
