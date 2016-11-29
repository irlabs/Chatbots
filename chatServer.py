#!/usr/bin/env python

# Command Line Interface (CLI) version

import time
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


# Run forever on the command line

def main():
    """docstring for main"""
    # Setup
    bot.setup()
    #
    # Run continuesly
    while True:
        humanSpeak = raw_input("> ")
        bot.response(humanSpeak)


if __name__ == '__main__':
    main()
