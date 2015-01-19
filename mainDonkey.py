__author__ = 'gkamradt'

import random
import time
from math import floor
start = time.time()

def percent(val, digits):
    val *= 10 ** (digits + 2)
    return '{1:.{0}f}%'.format(digits, floor(val) / 10 ** digits)

def donkey(rounds, switching, printResult): # number of rounds,
    wincount = 0.0
    i = 0
    while i < rounds:
        win = False
        holder = 0
        choice = ["Don","Don","Car"]
        random.shuffle(choice)
        take = random.randint(0,2) #initially setting which value you'll take first
        select = random.randint(0,2) #making your original selection
        if switching: #if you select true to switch
            holder = select #make sure when you select a new value, its not your original one
            while take == select or choice[take] == "Car": #youre taking one away thats not your selection or the car
                take = random.randint(0,2)
            while select == take or select == holder: #changing your selection
                select = random.randint(0,2)
            if choice[select] == "Car": #now that you changed your selection, see if you're right
                wincount += 1
                i += 1
                win = True
                if printResult: #if you want to see all the rounds played out
                    print i, choice, "first", holder, "away", take, choice[take], "changed", select, win
                continue
            else:
                i += 1
        else: #no switch code
            if choice[select] == "Car": #test to see if you picked car
                wincount += 1
                i+= 1
                win = True
                continue
            else:
                i += 1
        if printResult:
            print i, choice, "first", holder, "away", take, choice[take], "changed", select, win

    f = lambda x: "Switch" if x else "No Switch"

    print f(switching), int(wincount), "Out Of", i, "or", percent(wincount/i,1)

donkey(100000, True, False)
donkey(100000, False, False)
print time.time()-cycle1