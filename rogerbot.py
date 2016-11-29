#!/usr/bin/env python

# Roger bot

import chatServerModifyGlobals as c
import random


# Sleep and output functions
def sleep(n):
    c.sleep(n)


def output(s):
    c.output(s)


# Setup and Response function
def setup():
    global askedCounter, assignmentOrder
    global numCounter
    askedCounter = 0
    assignmentOrder = 0
    numCounter = 5
    output("Hello, my name is Roger.")
    sleep(1)
    output("What's up?")


def response(input):
    # print(input)
    if respondCounting(input):
        pass
    elif respondToTrigger(input):
        pass
    else:
        output(defaultRandomResponse())


def defaultRandomResponse():
    answers = [
        "Ok",
        "Roger",
        "Copy that",
        "Confirmative",
        "Affirmative",
        "Okay",
        "Okeydokey",
        "Yes",
        "Sure",
        "I agree",
        "Absolutely"
    ]
    response = random.choice(answers)
    return response


def orderedAssignmentDetails():
    global assignmentOrder
    scheme = "https://"
    githubRepo = "github.com/ArtezGDA/Course-Material"
    pageLink = "/blob/master/DesignAChatbot.md"
    answers = [
        "Design a chatbot!",
        "The assignment is to Design a Chatbot.",
        "A Chatbot. And you have to design its interactions.",
        """Read more about this Design a Chatbot Assignment
        at {}{}{}""".format(scheme, githubRepo, pageLink),
        "Make this chatbot more interesting.",
    ]
    if assignmentOrder < len(answers):
        response = answers[assignmentOrder]
        assignmentOrder += 1
    else:
        output("I don't know what else to say.")
        sleep(1.5)
        response = "Just go do it!"
    return response


def randomAgainRemarks():
    answers = [
        "Why do you ask me this again?",
        "What? Again?",
        "Do I have to repeat myself?",
        "Didn't you just hear me?",
        "Were you not listening?",
        "Ok. There we go. One more time",
        "For the last time,"
    ]
    return random.choice(answers)


def respondCounting(input):
    global numCounter
    if "count" == input:
        output("counting up to %d" % numCounter)
        numCounter += 1
        return True
    return False


def respondToTrigger(input):
    global askedCounter
    triggers = ["assignment", "what do I do", "chatbot"]
    for t in triggers:
        if t in input:
            if askedCounter > 1:
                output(randomAgainRemarks())
            output(orderedAssignmentDetails())
            askedCounter += 1
            return True
    return False
