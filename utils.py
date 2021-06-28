from math import isinf
from webbrowser import Error
import eel
import random
DIGITS = 0
REPEATED_DIGITS = 0
def generateANumber(digits, repeated=REPEATED_DIGITS):
    if not repeated:
        return ''.join(random.sample('0123456789', digits))
    else:
        return str(random.randrange(10**(digits-1), 10*digits))
def getUserGuess(digits, userGuess, repeated=REPEATED_DIGITS):
    if not repeated:
        for i in range(0,10):
            if (userGuess.count(str(i))>1):
                print('you are cheating')
                return -1
    if len(userGuess)==digits:
        return userGuess
    else:
        return -2
def checkTheNumber(theNumber, userGuess):
    isIn = 0
    isIt = 0
    if(theNumber==userGuess):
        return DIGITS, DIGITS, True
    for i in range(DIGITS):
        if userGuess[i] in theNumber:
            isIn+=1
        if userGuess[i] in theNumber[i]:
            isIt+=1
    return isIn, isIt, False
eel.init('.//web')
WON = False
THE_NUMBER = 0
@eel.expose
def start(digits=4):
    global WON, THE_NUMBER,DIGITS
    DIGITS = digits
    WON = False
    THE_NUMBER = generateANumber(DIGITS)
@eel.expose
def game(userGuess):
    global WON,THE_NUMBER
    userGuess = getUserGuess(DIGITS, userGuess)
    if int(userGuess)>0:
        isIn, isIt, WON = checkTheNumber(THE_NUMBER, userGuess)
        eel.gameState(isIn, isIt, WON, userGuess)()
    elif int(userGuess) == -1:
        eel.showMessage(0)()
    elif int(userGuess) == -2:
        showMessage('Error')
eel.start('index.html', size=(800, 700))