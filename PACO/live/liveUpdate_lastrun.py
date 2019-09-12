#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on Tue Sep  3 15:45:50 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'liveUpdate'  # from the Builder filename that created this script
expInfo = {'participant': '', 'experiment': 'LOCO'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Volumes/bamlab/Experiments/PACO/live/liveUpdate_lastrun.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[640, 435], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
#!/usr/bin/env python
import csv
import os.path
import datetime
import time
import math
import ast #Lets you convert string representations of lists to lists

#Get directory
thisdir = os.path.abspath(os.path.join(os.path.dirname(_thisDir),'.'))

#Get Subject ID and experiment
participant = expInfo['participant']
experiment = expInfo['experiment']

fileNum = 1

Stimuli = np.array([])
studyArray = []
oldornewArray = []
currentStimuli = 0

abortSound = sound.Sound('aborted.wav', secs=-1, stereo=True)
abortSound.setVolume(1)
completeSound = sound.Sound('complete.wav', secs=-1, stereo=True)
completeSound.setVolume(1)
oneMinSound = sound.Sound('1min.wav', secs=-1, stereo=True)
completeSound.setVolume(1)

hour = ''
min = ''
sec = ''
ampm = ''

slideOnCurrent = True
currentX = 0.083 #X position at start of open
currentWidth = 1 #Current width of rectangle

def setCurrent():
    if experiment == 'LOCO':
        userOldOrNewText.setText('User: ' + Stimuli[sortedCurrentStimuli][4])
        correctOldOrNewText.setText('Correct: ' + Stimuli[sortedCurrentStimuli][10])
        if not Stimuli[sortedCurrentStimuli][7] == 'N/A':
            userColorCircle.setColor([float(Stimuli[sortedCurrentStimuli][7]),1,1])
            userLocationDot.setPos((float(Stimuli[sortedCurrentStimuli][5])/3.91, (float(Stimuli[sortedCurrentStimuli][6])/3.91)-0.248))
            correctColorCircle.setColor([float(Stimuli[sortedCurrentStimuli][13]),1,1])
            correctLocationDot.setPos((float(Stimuli[sortedCurrentStimuli][11])/3.91, (float(Stimuli[sortedCurrentStimuli][12])/3.91)-0.248))
        else:
            userColorCircle.setColor([0,0,1])
            userLocationDot.setPos((0.065,-0.08))
            correctColorCircle.setColor([0,0,1])
            correctLocationDot.setPos((-.15,-0.08))
        locationDistText.setText('Location Dist: ' + Stimuli[sortedCurrentStimuli][16])
        colorDistText.setText('Color Rad Dist: ' + Stimuli[sortedCurrentStimuli][17])
        if Stimuli[sortedCurrentStimuli][16] != 'N/A':
            #Location
            if float(Stimuli[sortedCurrentStimuli][16]) <= 0.05:
                locationScoreText.setText('Location Score: Very Good')
            elif float(Stimuli[sortedCurrentStimuli][16]) <= 0.15:
                locationScoreText.setText('Location Score: Good')
            elif float(Stimuli[sortedCurrentStimuli][16]) <= 0.35:
                locationScoreText.setText('Location Score: OK')
            elif float(Stimuli[sortedCurrentStimuli][16]) <= 0.7:
                locationScoreText.setText('Location Score: Bad')
            else:
                locationScoreText.setText('Location Score: Very Bad')
            #Color
            correctAproxColor = ast.literal_eval(Stimuli[sortedCurrentStimuli][15])
            userAproxColor = ast.literal_eval(Stimuli[sortedCurrentStimuli][9])
            if correctAproxColor[0] in userAproxColor:
                colorScoreText.setText('Color Score: OK')
            elif len(correctAproxColor) > 1:
                if correctAproxColor[1] in userAproxColor:
                    colorScoreText.setText('Color Score: OK')
                else:
                    colorScoreText.setText('Color Score: Bad')
            else:
                colorScoreText.setText('Color Score: Bad')
            if int(Stimuli[sortedCurrentStimuli][17]) < 3:
                colorScoreText.setText('Color Score: Good')
        else:
            locationScoreText.setText('Location Score: N/A')
            colorScoreText.setText('Color Score: N/A')
        OldOrNewRTText.setText('Old/New RT: ' + Stimuli[sortedCurrentStimuli][18])
        TestRTText.setText('Test RT: ' + Stimuli[sortedCurrentStimuli][19])
        StudyOnsetText.setText('Study Onset: ' + Stimuli[sortedCurrentStimuli][23])
        OldOrNewOnsetText.setText('Old/New Onset: ' + Stimuli[sortedCurrentStimuli][24])
        TestOnsetText.setText('Test Onset: ' + Stimuli[sortedCurrentStimuli][25])
    elif experiment == 'LO':
        userOldOrNewText.setText('User: ' + Stimuli[sortedCurrentStimuli][4])
        correctOldOrNewText.setText('Correct: ' + Stimuli[sortedCurrentStimuli][7])
        if not Stimuli[sortedCurrentStimuli][10] == 'N/A':
            userLocationDot.setPos((float(Stimuli[sortedCurrentStimuli][5])/3.91, (float(Stimuli[sortedCurrentStimuli][6])/3.91)-0.248))
            correctLocationDot.setPos((float(Stimuli[sortedCurrentStimuli][8])/3.91, (float(Stimuli[sortedCurrentStimuli][9])/3.91)-0.248))
        else:
            userLocationDot.setPos((0.065,-0.08))
            correctLocationDot.setPos((-.15,-0.08))
        locationDistText.setText('Location Dist: ' + Stimuli[sortedCurrentStimuli][10])
        colorDistText.setText('')
        if Stimuli[sortedCurrentStimuli][10] != 'N/A':
            if float(Stimuli[sortedCurrentStimuli][10]) <= 0.05:
                locationScoreText.setText('Location Score: Very Good')
            elif float(Stimuli[sortedCurrentStimuli][10]) <= 0.15:
                locationScoreText.setText('Location Score: Good')
            elif float(Stimuli[sortedCurrentStimuli][10]) <= 0.35:
                locationScoreText.setText('Location Score: OK')
            elif float(Stimuli[sortedCurrentStimuli][10]) <= 0.7:
                locationScoreText.setText('Location Score: Bad')
            else:
                locationScoreText.setText('Location Score: Very Bad')
        else:
            locationScoreText.setText('Location Score: N/A')
        colorScoreText.setText('')
        OldOrNewRTText.setText('Old/New RT: ' + Stimuli[sortedCurrentStimuli][11])
        TestRTText.setText('Test RT: ' + Stimuli[sortedCurrentStimuli][12])
        StudyOnsetText.setText('Study Onset: ' + Stimuli[sortedCurrentStimuli][16])
        OldOrNewOnsetText.setText('Old/New Onset: ' + Stimuli[sortedCurrentStimuli][17])
        TestOnsetText.setText('Test Onset: ' + Stimuli[sortedCurrentStimuli][18])
    elif experiment == 'CO':
        userOldOrNewText.setText('User: ' + Stimuli[sortedCurrentStimuli][4])
        correctOldOrNewText.setText('Correct: ' + Stimuli[sortedCurrentStimuli][8])
        if not Stimuli[sortedCurrentStimuli][12] == 'N/A':
            userColorCircle.setColor([float(Stimuli[sortedCurrentStimuli][5]),1,1])
            correctColorCircle.setColor([float(Stimuli[sortedCurrentStimuli][9]),1,1])
        else:
            userColorCircle.setColor([0,0,1])
            correctColorCircle.setColor([0,0,1])
        locationDistText.setText('')
        colorDistText.setText('Color Rad Dist: ' + Stimuli[sortedCurrentStimuli][12])
        locationScoreText.setText('')
        if Stimuli[sortedCurrentStimuli][12] != 'N/A':
            correctAproxColor = ast.literal_eval(Stimuli[sortedCurrentStimuli][11])
            userAproxColor = ast.literal_eval(Stimuli[sortedCurrentStimuli][7])
            if correctAproxColor[0] in userAproxColor:
                colorScoreText.setText('Color Score: OK')
            elif len(correctAproxColor) > 1:
                if correctAproxColor[1] in userAproxColor:
                    colorScoreText.setText('Color Score: OK')
                else:
                    colorScoreText.setText('Color Score: Bad')
            else:
                colorScoreText.setText('Color Score: Bad')
            if int(Stimuli[sortedCurrentStimuli][12]) < 3:
                colorScoreText.setText('Color Score: Good')
        else:
            colorScoreText.setText('Color Score: N/A')
        OldOrNewRTText.setText('Old/New RT: ' + Stimuli[sortedCurrentStimuli][13])
        TestRTText.setText('Test RT: ' + Stimuli[sortedCurrentStimuli][14])
        StudyOnsetText.setText('Study Onset: ' + Stimuli[sortedCurrentStimuli][18])
        OldOrNewOnsetText.setText('Old/New Onset: ' + Stimuli[sortedCurrentStimuli][19])
        TestOnsetText.setText('Test Onset: ' + Stimuli[sortedCurrentStimuli][20])

def slide():
    global slideOnCurrent
    doneWithSlide = False
    global currentWidth
    global currentX
    aniup = True
    speed = 0.1
    while doneWithSlide == False:
        if slideOnCurrent:
            #Animation to Overview
            if currentWidth < 2 and aniup:
                selector.setSize((currentWidth, 1), log=False)
                selector.setPos((-((currentWidth-1)/20) + currentX, -0.04))
                currentWidth += speed
            elif currentX > 0.03:
                selector.setPos((-((currentWidth-1)/20) + currentX, -0.04))
                currentX -= speed/10
                aniup = False
                Current.setColor('black')
                Overview.setColor([-0.553,-0.553,-0.553], 'rgb')
                #Updates:
                leftArrow.setColor([0.325,0.325,0.325])
                doubleLeftArrow1.setColor([0.325,0.325,0.325])
                doubleLeftArrow2.setColor([0.325,0.325,0.325])
                rightArrow.setColor([0.325,0.325,0.325])
                doubleRightArrow1.setColor([0.325,0.325,0.325])
                doubleRightArrow2.setColor([0.325,0.325,0.325])
                if not dataFileReady:
                    stimuli.setAutoDraw(False)
                correctColorShape.setAutoDraw(False)
                correctColorCircle.setAutoDraw(False)
                userColorShape.setAutoDraw(False)
                userColorCircle.setAutoDraw(False)
                correctColorText.setAutoDraw(False)
                userColorText.setAutoDraw(False)
                sortStudyText.setAutoDraw(False)
                sortOldornewText.setAutoDraw(False)
                sortTestText.setAutoDraw(False)
                sortByText.setText('Average:')
                trayShape.setAutoDraw(False)
                if dataFileReady:
                    correctLocationText.setAutoDraw(False)
                    correctLocationKey.setAutoDraw(False)
                    userLocationText.setAutoDraw(False)
                    userLocationKey.setAutoDraw(False)
                    overviewScoreText.setAutoDraw(True)
                    text.setText('Data Is Ready')
                    stimuli.setImage(thisdir + '/live/' + finalScore + '.png')
                    stimuli.setColor([1,1,1])
                    if not skipOldOrNew:
                        userOldOrNewText.setText('Correct Old: ' + str(avgCorrectOld) + ' of ' + str(studyStim))
                        correctOldOrNewText.setText('Correct New: ' + str(avgCorrectNew) + ' of ' + str(testStim-studyStim))
                    else:
                        userOldOrNewText.setText('Correct Old: N/A')
                        correctOldOrNewText.setText('Correct New: N/A')
                    if experiment != 'CO':
                        locationDistText.setText('Location Dist: ' + str(avgLocationDist))
                        locationScoreText.setText('Location Score: ' + avgLocationScore)
                        OldOrNewOnsetText.setText('Location Correct: ' + str(avgLocationCorrect) + '%')
                        userLocationDot.setPos((-((avgLocationDist/3.91)/2), (0/3.91)-0.248))
                        correctLocationDot.setPos(((avgLocationDist/3.91)/2, (0/3.91)-0.248))
                    if experiment != 'LO':
                        colorDistText.setText('Color Rad Dist: ' + str(avgColorDist))
                        colorScoreText.setText('Color Score: ' + avgColorScore)
                        TestOnsetText.setText('Color Correct: ' + str(avgColorCorrect) + '%')
                    if not skipOldOrNew:
                        OldOrNewRTText.setText('Old/New RT: ' + str(avgOldNewRT))
                    else:
                        OldOrNewRTText.setText('Old/New RT: N/A')
                    TestRTText.setText('Test RT: ' + str(avgTestRT))
                    if not skipOldOrNew:
                        StudyOnsetText.setText('Old/New Correct: ' + str(avgOldNewCorrect) + '%')
                    else:
                        StudyOnsetText.setText('Old/New Correct: N/A')
                    if experiment == 'CO':
                        locationDistText.setText('')
                        locationScoreText.setText('')
                        OldOrNewOnsetText.setText('')
                    elif experiment == 'LO':
                        colorDistText.setText('')
                        colorScoreText.setText('')
                        TestOnsetText.setText('')
            elif currentWidth >= 1.25:
                currentX = -0.07
                selector.setSize((currentWidth, 1), log=False)
                selector.setPos((((currentWidth-1)/20) + currentX, -0.04))
                currentWidth -= speed
            else:
                doneWithSlide = True
                slideOnCurrent = False
        else:
            #Animation to Current
            if currentWidth < 2 and aniup:
                selector.setSize((currentWidth, 1), log=False)
                selector.setPos((((currentWidth-1)/20) + currentX, -0.04))
                currentWidth += speed
            elif currentX < -0.02:
                selector.setPos((((currentWidth-1)/20) + currentX, -0.04))
                currentX += speed/10
                aniup = False
                Current.setColor([-0.553,-0.553,-0.553], 'rgb')
                Overview.setColor('black')
                #Updates:
                if dataFileReady:
                    stimuli.setImage(thisdir + '/Stimuli/' + str(Stimuli[sortedCurrentStimuli][0]) + '.png')
                    stimuli.setColor([-1,-1,-1])
                    overviewScoreText.setAutoDraw(False)
                    correctColorShape.setAutoDraw(True)
                    correctColorCircle.setAutoDraw(True)
                    userColorShape.setAutoDraw(True)
                    userColorCircle.setAutoDraw(True)
                    correctColorText.setAutoDraw(True)
                    userColorText.setAutoDraw(True)
                    sortByText.setAutoDraw(True)
                    correctLocationText.setAutoDraw(True)
                    userLocationText.setAutoDraw(True)
                    correctLocationKey.setAutoDraw(True)
                    userLocationKey.setAutoDraw(True)
                    setCurrent()
                    if sortBy == 1:
                        sortByText.setText('Sort By: Study')
                        text.setText('Stimuli ' + str(currentStimuli+1) + ' of ' + str(studyStim))
                    elif sortBy == 2:
                        sortByText.setText('Sort By: Old/New')
                        text.setText('Stimuli ' + str(currentStimuli+1) + ' of ' + str(testStim))
                    elif sortBy == 3:
                        sortByText.setText('Sort By: Test')
                        text.setText('Stimuli ' + str(currentStimuli+1) + ' of ' + str(studyStim))
                if enableLeft:
                    leftArrow.setColor([-0.624,-0.624,-0.624])
                if enableRight:
                    rightArrow.setColor([-0.624,-0.624,-0.624])
                if enableFarLeft:
                    doubleLeftArrow1.setColor([-0.624,-0.624,-0.624])
                    doubleLeftArrow2.setColor([-0.624,-0.624,-0.624])
                if enableFarRight:
                    doubleRightArrow1.setColor([-0.624,-0.624,-0.624])
                    doubleRightArrow2.setColor([-0.624,-0.624,-0.624])
                if isOnCurrent and thisLine[1] == 'Stimuli':
                    stimuli.setAutoDraw(True)
                    correctColorShape.setAutoDraw(True)
                    correctColorCircle.setAutoDraw(True)
                    userColorShape.setAutoDraw(True)
                    userColorCircle.setAutoDraw(True)
                    correctColorText.setAutoDraw(True)
                    userColorText.setAutoDraw(True)
            elif currentWidth >= 1:
                currentX = 0.083
                selector.setSize((currentWidth, 1), log=False)
                selector.setPos((-((currentWidth-1)/20) + currentX, -0.04))
                currentWidth -= speed
            else:
                doneWithSlide = True
                slideOnCurrent = True
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        win.flip()

def getTime():
    global hour
    global min
    global sec
    global ampm
    if int(thisLine[6]) > 12:
        hour = str(int(thisLine[6]) - 12)
        ampm = 'pm'
    else:
        hour = str(thisLine[6])
        ampm = 'am'
    if int(thisLine[7]) < 10:
        min = '0' + str(thisLine[7])
    else:
        min = str(thisLine[7])
    if int(thisLine[8]) < 10:
        sec = '0' + str(thisLine[8])
    else:
        sec = str(thisLine[8])
    return hour, min, sec, ampm

def aproxColor(num): #1 = red, 2 = orange, 3 = yellow, 4 = green, 5 = aqua, 6 = blue, 7 = purple, and 8 = pink. 2 diget numbers are a combo of both
    word = []
    if num >= 93 or num <= 5:
        word.append('Red')
    if num >= 98 or num <= 8:
        word.append('Orange')
    if num >= 6 and num <= 20:
        word.append('Yellow')
    if num >= 16 and num <= 45:
        word.append('Green')
    if num >= 37 and num <= 62:
        word.append('Aqua')
    if num >= 50 and num <= 74:
        word.append('Blue')
    if num >= 72 and num <= 81:
        word.append('Purple')
    if num >= 77 and num <= 96:
        word.append('Pink')
    return word
stimuli = visual.ImageStim(
    win=win,
    name='stimuli', 
    image=None, mask=None,
    ori=0, pos=(-0.45, -.2), size=(0.3, 0.3),
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
computer = visual.ImageStim(
    win=win,
    name='computer', 
    image='computer.png', mask=None,
    ori=0, pos=(0, -.35), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text = visual.TextStim(win=win, name='text',
    text='Participant is on practice phase',
    font='Arial',
    pos=(0, .4), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
subText = visual.TextStim(win=win, name='subText',
    text=None,
    font='Arial',
    pos=(0, .333), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
statusText = visual.TextStim(win=win, name='statusText',
    text='Status: Ready',
    font='Arial',
    pos=(0, .46), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
participantText = visual.TextStim(win=win, name='participantText',
    text='000',
    font='Arial',
    pos=(-.66, .45), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
experimentText = visual.TextStim(win=win, name='experimentText',
    text='000',
    font='Arial',
    pos=(.63, .45), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
percentText = visual.TextStim(win=win, name='percentText',
    text='0% Section',
    font='Arial',
    pos=(0, .21), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
LoadingBackground = visual.Rect(
    win=win, name='LoadingBackground',
    width=(1, 0.05)[0], height=(1, 0.05)[1],
    ori=0, pos=(0, .26),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.278,0.278,0.278], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
LoadingBar = visual.Rect(
    win=win, name='LoadingBar',
    width=(.5, 0.05)[0], height=(.5, 0.05)[1],
    ori=0, pos=(0, .26),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.184,0.365,1.000], fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
percentText2 = visual.TextStim(win=win, name='percentText2',
    text='0% Total',
    font='Arial',
    pos=(0, 0.09), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
LoadingBackground2 = visual.Rect(
    win=win, name='LoadingBackground2',
    width=(1, 0.05)[0], height=(1, 0.05)[1],
    ori=0, pos=(0, .14),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.278,0.278,0.278], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
LoadingBar2 = visual.Rect(
    win=win, name='LoadingBar2',
    width=(.5, 0.05)[0], height=(.5, 0.05)[1],
    ori=0, pos=(0, .14),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.184,0.365,1.000], fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
separator = visual.Rect(
    win=win, name='separator',
    width=(1.2, 0.005)[0], height=(1.2, 0.005)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.012,-0.012,-0.012], fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
startTime = visual.TextStim(win=win, name='startTime',
    text=None,
    font='Arial',
    pos=(0, 0.025), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
endTime = visual.TextStim(win=win, name='endTime',
    text=None,
    font='Arial',
    pos=(.42, 0.025), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-16.0);
timeLeft = visual.TextStim(win=win, name='timeLeft',
    text=None,
    font='Arial',
    pos=(-0.42, 0.025), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-17.0);
Overview = visual.TextStim(win=win, name='Overview',
    text='Overview',
    font='Arial',
    pos=(-0.06, -0.02), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
Current = visual.TextStim(win=win, name='Current',
    text='Current',
    font='Arial',
    pos=(0.08, -0.02), height=0.03, wrapWidth=None, ori=0, 
    color=[-0.553,-0.553,-0.553], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
selector = visual.Rect(
    win=win, name='selector',
    width=(0.1, 0.005)[0], height=(0.1, 0.005)[1],
    ori=0, pos=(0.083, -0.04),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-20.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
participantText.text = participant
experimentText.text = experiment
loadingpercent = 0
loadingpercent2 = 0
loadFinal = 0
loadFinal2 = 0
firstRun = True #This var turns off in top of code
realFirstRun = True #This one turns off at bottom
thisLine = [0, 0, 0]
lastThisLine = [] #The last version of this line
totalstim = 0
isDone = False
isAborted = False
isOnCurrent = False #If live program is on the current part of the experiment
soundIsPlaying = False
oneMinSoundIsPlaying = False
timeleft = 0
shift = False
mousePressed = False #If mouse is pressed in. Used for current time
hasDoneTimeSet = False #See if it has gone through the time set that calculates the live time
enableRight = False #Arrow keys
enableLeft = False
enableFarRight = False
enableFarLeft = False
isOnNewStim = True #If true, user sees newest stim without the participant's input, if false, user sees last stimuli with the participant's innput
dataFileReady = False #If the end data file is ready for analysation
trayIsOpen = False #If the tray is open or not
trayIsClicked = False #If tray is currently being clicked
sortBy = 3 #1 is study, 2 is Old/New, 3 is Test
sortedCurrentStimuli = 0 #The current stimuli after it's been sorted
scrollWaitTime = 0 #Waits a certain amount of time before scrolling fast
tryDataFileOnce = True #Checks if the experiment is already done when the user opens the live app

#YOU CAN CHANGE THESE IF YOU MAKE TIME MORE IN THE EXPERIMENT
instr1time = 12
exampletime = 10
instr2time = 8
practstudytime = 5 #Per object
instr3time = 12
practoldnew = 4
instr4time = 15
practtest = 10
instr5time = 8
studytime = 5
instr6time = 18
oldnewtime = 3
instr7time = 10
testtime = 10
debugTime = False #Makes the time left show up as seconds instead of rounded minutes, you can also just click the time left text while running to activate

#Overview text
overviewScoreText = visual.TextStim(win=win, name='text',
    text='Participant did ',
    font='Arial',
    pos=(-0.45,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

#Sort by tray
trayShape = visual.Rect(
    win=win, name = 'trayShape',
    width = (.15,.15)[0], height = (.17,.17)[1],
    ori=0, pos=(0.45, -0.09),
    lineWidth = 0, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, interpolate = True, depth=-7)

#Sort By Text
sortByText = visual.TextStim(win=win, name='text',
    text='Sort By: Test',
    font='Arial',
    pos=(0.45, -0.03), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR', depth=-8);

sortStudyText = visual.TextStim(win=win, name='text',
    text='Study',
    font='Arial',
    pos=(0.45, -0.07), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR', depth=-8);

sortOldornewText = visual.TextStim(win=win, name='text',
    text='Old/New',
    font='Arial',
    pos=(0.45, -0.11), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR', depth=-8);

sortTestText = visual.TextStim(win=win, name='text',
    text='Test',
    font='Arial',
    pos=(0.45, -0.15), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR', depth=-8);

#Create Color Circles
correctColorShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,0.6,0], pos=(-.528,-.415), size=(0.1,0.1), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)
correctColorCircle = visual.RadialStim(win, colorSpace = 'hsv', color=[180,0,1], pos=(-.528,-.415), size=(0.09,0.09), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)
userColorShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,0.6,0], pos=(-.378,-.415), size=(0.1,0.1), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)
userColorCircle = visual.RadialStim(win, colorSpace = 'hsv', color=[180,0,1], pos=(-.378,-.415), size=(0.09,0.09), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)

correctColorShape.setAutoDraw(True)
correctColorCircle.setAutoDraw(True)
userColorShape.setAutoDraw(True)
userColorCircle.setAutoDraw(True)

#Create Color Circle Text
correctColorText = visual.TextStim(win=win, name='text',
    text='Correct',
    font='Arial',
    pos=(-.532,-.48), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
userColorText = visual.TextStim(win=win, name='text',
    text='User',
    font='Arial',
    pos=(-.38, -.48), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

correctColorText.setAutoDraw(True)
userColorText.setAutoDraw(True)

#Create Location dots
correctLocationDot = visual.RadialStim(win, color='green', pos=(-.15,-0.08), size=(0.02,0.02), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)
userLocationDot = visual.RadialStim(win, color='red', pos=(0.065,-0.08), size=(0.02,0.02), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)
correctLocationKey = visual.RadialStim(win, color='green', pos=(-.15,-0.08), size=(0.02,0.02), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)
userLocationKey = visual.RadialStim(win, color='red', pos=(0.065,-0.08), size=(0.02,0.02), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)

correctLocationDot.setAutoDraw(True)
userLocationDot.setAutoDraw(True)
correctLocationKey.setAutoDraw(True)
userLocationKey.setAutoDraw(True)

#Create Location Key Text
correctLocationText = visual.TextStim(win=win, name='text',
    text='Correct',
    font='Arial',
    pos=(-.1,-0.08), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
userLocationText = visual.TextStim(win=win, name='text',
    text='User',
    font='Arial',
    pos=(.1,-0.08), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

correctLocationText.setAutoDraw(True)
userLocationText.setAutoDraw(True)

#Create stats text: Correct Old/New, User Old/New, Location Dist, Color Dist, Location Score, Color Score, oldnew rt, test rt, start time of trail
userOldOrNewText = visual.TextStim(win=win, name='text',
    text='User: N/A',
    font='Arial',
    pos=(0.45,-0.08), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
correctOldOrNewText = visual.TextStim(win=win, name='text',
    text='Correct: N/A',
    font='Arial',
    pos=(0.45,-0.12), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
locationDistText = visual.TextStim(win=win, name='text',
    text='Location Dist: N/A',
    font='Arial',
    pos=(0.45,-0.16), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
colorDistText = visual.TextStim(win=win, name='text',
    text='Color Rad Dist: N/A',
    font='Arial',
    pos=(0.45,-0.20), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
locationScoreText = visual.TextStim(win=win, name='text',
    text='Location Score: N/A',
    font='Arial',
    pos=(0.45,-0.24), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
colorScoreText = visual.TextStim(win=win, name='text',
    text='Color Score: N/A',
    font='Arial',
    pos=(0.45,-0.28), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
OldOrNewRTText = visual.TextStim(win=win, name='text',
    text='Old/New RT: N/A',
    font='Arial',
    pos=(0.45,-0.32), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
TestRTText = visual.TextStim(win=win, name='text',
    text='Test RT: N/A',
    font='Arial',
    pos=(0.45,-0.36), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
StudyOnsetText = visual.TextStim(win=win, name='text', #THESE THREE CHANGE TO ONSET TIMES AT END OF EXP
    text='Study Onset: N/A',
    font='Arial',
    pos=(0.45,-0.40), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
OldOrNewOnsetText = visual.TextStim(win=win, name='text', #THESE THREE CHANGE TO ONSET TIMES AT END OF EXP
    text='Old/New Onset: N/A',
    font='Arial',
    pos=(0.45,-0.44), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
TestOnsetText = visual.TextStim(win=win, name='text', #THESE THREE CHANGE TO ONSET TIMES AT END OF EXP
    text='Test Onset: N/A',
    font='Arial',
    pos=(0.45,-0.48), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

userOldOrNewText.setAutoDraw(True)
correctOldOrNewText.setAutoDraw(True)
locationDistText.setAutoDraw(True)
colorDistText.setAutoDraw(True)
locationScoreText.setAutoDraw(True)
colorScoreText.setAutoDraw(True)
OldOrNewRTText.setAutoDraw(True)
TestRTText.setAutoDraw(True)
StudyOnsetText.setAutoDraw(False)
OldOrNewOnsetText.setAutoDraw(False)
TestOnsetText.setAutoDraw(False)

#Create arrows
size = 0.05
rightArrow = visual.ShapeStim(
    win=win, name='leftArrow',
    vertices=[[-(size, size)[0]/2.0,-(size, size)[1]/2.0], [+(size, size)[0]/2.0,-(size, size)[1]/2.0], [0,(size, size)[1]/2.0]],
    ori=90, pos=(0.68, -0.22),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.624,-0.624,-0.624], fillColorSpace='rgb',
    opacity=1, depth=-22.0, interpolate=True)
doubleRightArrow1 = visual.ShapeStim(
    win=win, name='doubleleftArrow1',
    vertices=[[-(size, size)[0]/2.0,-(size, size)[1]/2.0], [+(size, size)[0]/2.0,-(size, size)[1]/2.0], [0,(size, size)[1]/2.0]],
    ori=90, pos=(0.665, -0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.624,-0.624,-0.624], fillColorSpace='rgb',
    opacity=1, depth=-22.0, interpolate=True)
doubleRightArrow2 = visual.ShapeStim(
    win=win, name='doubleleftArrow2',
    vertices=[[-(size, size)[0]/2.0,-(size, size)[1]/2.0], [+(size, size)[0]/2.0,-(size, size)[1]/2.0], [0,(size, size)[1]/2.0]],
    ori=90, pos=(0.695, -0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.624,-0.624,-0.624], fillColorSpace='rgb',
    opacity=1, depth=-22.0, interpolate=True)

leftArrow = visual.ShapeStim(
    win=win, name='rightArrow',
    vertices=[[-(size, size)[0]/2.0,-(size, size)[1]/2.0], [+(size, size)[0]/2.0,-(size, size)[1]/2.0], [0,(size, size)[1]/2.0]],
    ori=-90, pos=(-0.68, -0.22),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.624,-0.624,-0.624], fillColorSpace='rgb',
    opacity=1, depth=-22.0, interpolate=True)
doubleLeftArrow1 = visual.ShapeStim(
    win=win, name='doublerightArrow1',
    vertices=[[-(size, size)[0]/2.0,-(size, size)[1]/2.0], [+(size, size)[0]/2.0,-(size, size)[1]/2.0], [0,(size, size)[1]/2.0]],
    ori=-90, pos=(-0.665, -0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.624,-0.624,-0.624], fillColorSpace='rgb',
    opacity=1, depth=-22.0, interpolate=True)
doubleLeftArrow2 = visual.ShapeStim(
    win=win, name='doublerightArrow2',
    vertices=[[-(size, size)[0]/2.0,-(size, size)[1]/2.0], [+(size, size)[0]/2.0,-(size, size)[1]/2.0], [0,(size, size)[1]/2.0]],
    ori=-90, pos=(-0.695, -0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.624,-0.624,-0.624], fillColorSpace='rgb',
    opacity=1, depth=-22.0, interpolate=True)


leftArrow.setAutoDraw(True)
doubleLeftArrow1.setAutoDraw(True)
doubleLeftArrow2.setAutoDraw(True)

rightArrow.setAutoDraw(True)
doubleRightArrow1.setAutoDraw(True)
doubleRightArrow2.setAutoDraw(True)
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
trialComponents = [stimuli, computer, text, subText, statusText, participantText, experimentText, percentText, LoadingBackground, LoadingBar, percentText2, LoadingBackground2, LoadingBar2, separator, startTime, endTime, timeLeft, Overview, Current, selector, mouse]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if dataFileReady:
        if sortBy == 1:
            sortedCurrentStimuli = studyArray[currentStimuli]
        elif sortBy == 2:
            sortedCurrentStimuli = oldornewArray[currentStimuli]
        else:
            sortedCurrentStimuli = currentStimuli
        #Set Tabs Auto Draw to False
        if slideOnCurrent:
            sortByText.setAutoDraw(True)
            if sortBy == 1:
                text.setText('Stimuli ' + str(currentStimuli+1) + ' of ' + str(studyStim))
                if currentStimuli+1 < studyStim and currentStimuli+1 >= 1:
                    enableRight = True
                    enableFarRight = True
                else:
                    enableRight = False
                    enableFarRight = False
                if currentStimuli+1 <= studyStim and currentStimuli+1 > 1:
                    enableLeft = True
                    enableFarLeft = True
                else:
                    enableLeft = False
                    enableFarLeft = False
            elif sortBy == 2:
                text.setText('Stimuli ' + str(currentStimuli+1) + ' of ' + str(testStim))
                if currentStimuli+1 < testStim and currentStimuli+1 >= 1:
                    enableRight = True
                    enableFarRight = True
                else:
                    enableRight = False
                    enableFarRight = False
                if currentStimuli+1 <= testStim and currentStimuli+1 > 1:
                    enableLeft = True
                    enableFarLeft = True
                else:
                    enableLeft = False
                    enableFarLeft = False
            else:
                text.setText('Stimuli ' + str(currentStimuli+1) + ' of ' + str(studyStim))
                if currentStimuli+1 < studyStim and currentStimuli+1 >= 1:
                    enableRight = True
                    enableFarRight = True
                else:
                    enableRight = False
                    enableFarRight = False
                if currentStimuli+1 <= studyStim and currentStimuli+1 > 1:
                    enableLeft = True
                    enableFarLeft = True
                else:
                    enableLeft = False
                    enableFarLeft = False
        else:
            text.setText('Data Is Ready')
        Overview.setAutoDraw(True)
        Current.setAutoDraw(True)
        selector.setAutoDraw(True)
        if slideOnCurrent:
            stimuli.setImage(thisdir + '/Stimuli/' + str(Stimuli[sortedCurrentStimuli][0]) + '.png')
            stimuli.setAutoDraw(True)
            correctColorShape.setAutoDraw(True)
            correctColorCircle.setAutoDraw(True)
            userColorShape.setAutoDraw(True)
            userColorCircle.setAutoDraw(True)
            correctColorText.setAutoDraw(True)
            userColorText.setAutoDraw(True)
            correctLocationText.setAutoDraw(True)
            userLocationText.setAutoDraw(True)
            correctLocationKey.setAutoDraw(True)
            userLocationKey.setAutoDraw(True)
            setCurrent()
        correctLocationDot.setAutoDraw(True)
        userLocationDot.setAutoDraw(True)
    elif not isDone:
        #Set Tabs Auto Draw to False
        Overview.setAutoDraw(False)
        Current.setAutoDraw(False)
        selector.setAutoDraw(False)
    
    keys = event.getKeys()
    if keys:
        thekey = keys[0]
        if thekey == 'escape':
            core.quit()
        if thekey == 'left' and shift and enableFarLeft:
            currentStimuli = 1
        if thekey == 'right' and shift and enableFarRight:
            if sortBy == 2:
                currentStimuli = testStim-2
            else:
                currentStimuli = studyStim-2
        if thekey == 'left' and enableLeft and slideOnCurrent:
            if not isDone:
                isOnNewStim = False
            else:
                currentStimuli += -1
        if thekey == 'right' and enableRight and slideOnCurrent:
            if not isDone:
                isOnNewStim = True
            else:
                currentStimuli += 1
        if thekey == 'space' and dataFileReady:
            slide()
        if thekey == 'lshift':
            shift = True
        else:
            shift = False
    
    if mouse.isPressedIn(Current) and not slideOnCurrent and dataFileReady:
        slide()
    elif mouse.isPressedIn(Overview) and slideOnCurrent and dataFileReady:
        slide()
    
    if mouse.isPressedIn(sortByText) and slideOnCurrent and dataFileReady and not trayIsOpen and not trayIsClicked:
        trayShape.setAutoDraw(True)
        sortStudyText.setAutoDraw(True)
        sortOldornewText.setAutoDraw(True)
        sortTestText.setAutoDraw(True)
        trayIsOpen = True
        trayIsClicked = True
    elif mouse.isPressedIn(sortByText) and slideOnCurrent and dataFileReady and trayIsOpen and not trayIsClicked:
        sortStudyText.setAutoDraw(False)
        sortOldornewText.setAutoDraw(False)
        sortTestText.setAutoDraw(False)
        trayShape.setAutoDraw(False)
        trayIsOpen = False
        trayIsClicked = True
    elif mouse.isPressedIn(sortStudyText) and not trayIsClicked and slideOnCurrent and dataFileReady and trayIsOpen:
        sortBy = 1
        sortByText.setText('Sort By: Study')
        sortStudyText.setAutoDraw(False)
        sortOldornewText.setAutoDraw(False)
        sortTestText.setAutoDraw(False)
        trayShape.setAutoDraw(False)
        trayIsOpen = False
        currentStimuli = 0
    elif mouse.isPressedIn(sortOldornewText) and not trayIsClicked and slideOnCurrent and dataFileReady and trayIsOpen and not skipOldOrNew:
        sortBy = 2
        sortByText.setText('Sort By: Old/New')
        sortStudyText.setAutoDraw(False)
        sortOldornewText.setAutoDraw(False)
        sortTestText.setAutoDraw(False)
        trayShape.setAutoDraw(False)
        trayIsOpen = False
        currentStimuli = 0
    elif mouse.isPressedIn(sortTestText) and not trayIsClicked and slideOnCurrent and dataFileReady and trayIsOpen:
        sortBy = 3
        sortByText.setText('Sort By: Test')
        sortStudyText.setAutoDraw(False)
        sortOldornewText.setAutoDraw(False)
        sortTestText.setAutoDraw(False)
        trayShape.setAutoDraw(False)
        trayIsOpen = False
        currentStimuli = 0
    elif not mouse.isPressedIn(sortByText):
        trayIsClicked = False
    
    if mouse.isPressedIn(leftArrow) and enableLeft and slideOnCurrent:
        if not isDone:
            isOnNewStim = False
        elif scrollWaitTime == 0:
            currentStimuli += -1
        elif scrollWaitTime > 15:
            currentStimuli += -1
        scrollWaitTime += 1
    elif mouse.isPressedIn(rightArrow) and enableRight and slideOnCurrent:
        if not isDone:
            isOnNewStim = True
        elif scrollWaitTime == 0:
            currentStimuli += 1
        elif scrollWaitTime > 15:
            currentStimuli += 1
        scrollWaitTime += 1
    else:
        scrollWaitTime = 0
    
    if mouse.isPressedIn(doubleLeftArrow1) and mouse.isPressedIn(doubleLeftArrow2) or mouse.isPressedIn(doubleLeftArrow1) or mouse.isPressedIn(doubleLeftArrow2):
        if enableLeft and slideOnCurrent and dataFileReady:
            currentStimuli = 0
    elif mouse.isPressedIn(doubleRightArrow1) and mouse.isPressedIn(doubleRightArrow2) or mouse.isPressedIn(doubleRightArrow1) or mouse.isPressedIn(doubleRightArrow2):
        if enableRight and slideOnCurrent and dataFileReady:
            if sortBy == 2:
                currentStimuli = testStim-1
            else:
                currentStimuli = studyStim-1
    
    if mouse.isPressedIn(timeLeft):
        if debugTime and not mousePressed:
            debugTime = False
        elif not debugTime and not mousePressed:
            debugTime = True
        mousePressed = True
    else:
        mousePressed = False
    
    if firstRun == False:
        if not os.path.exists(thisdir + '/' + experiment + '/live/'+ participant + '/live' + str(fileNum-1) + '.csv'):
            #reset everything
            if not slideOnCurrent:
                slide()
                print('reset slide')
            fileNum = 1
            loadingpercent = 0
            loadingpercent2 = 0
            loadFinal = 0
            loadFinal2 = 0
            firstRun = True #This var turns off in top of code
            realFirstRun = True #This one turns off at bottom
            isDone = False
            isAborted = False
            isOnCurrent = True #If live program is on the current part of the experiment
            soundIsPlaying = False
            oneMinSoundIsPlaying = False
            LoadingBar.setColor([-0.184,0.365,1.000],'rgb')
            LoadingBar2.setColor([-0.184,0.365,1.000],'rgb')
            statusText.setText('Status: In Progress')
            statusText.setColor('green')
            Stimuli = np.array([])
            studyArray = []
            oldornewArray = []
            testArray = []
            mousePressed = False #If mouse is pressed in. Used for current time
            hasDoneTimeSet = False #See if it has gone through the time set that calculates the live time
            timeLeft.setAutoDraw(True)
            endTime.setAutoDraw(True)
            enableRight = False #Arrow keys
            enableLeft = False
            enableFarRight = False
            enableFarLeft = False
            isOnNewStim = True
            userOldOrNewText.setText('User: N/A')
            correctOldOrNewText.setText('Correct: N/A')
            locationDistText.setText('Location Dist: N/A')
            colorDistText.setText('Color Rad Dist: N/A')
            locationScoreText.setText('Location Score: N/A')
            colorScoreText.setText('Color Score: N/A')
            OldOrNewRTText.setText('Old/New RT: N/A')
            TestRTText.setText('Test RT: N/A')
            StudyOnsetText.setText('Study Onset: N/A')
            OldOrNewOnsetText.setText('Old/New Onset: N/A')
            TestOnsetText.setText('Test Onset: N/A')
            StudyOnsetText.setAutoDraw(False)
            OldOrNewOnsetText.setAutoDraw(False)
            TestOnsetText.setAutoDraw(False)
            correctColorCircle.setColor([0,0,1])
            correctLocationDot.setPos((-.15,-0.08))
            userColorCircle.setColor([0,0,1])
            userLocationDot.setPos((0.065,-0.08)) #Resets color and location for when you switch to newest
            stimuli.setImage('None')
            dataFileReady = False
            sortStudyText.setAutoDraw(False)
            sortOldornewText.setAutoDraw(False)
            sortTestText.setAutoDraw(False)
            sortByText.setAutoDraw(False)
            trayShape.setAutoDraw(False)
            Overview.setAutoDraw(False)
            Current.setAutoDraw(False)
            selector.setAutoDraw(False)
            trayIsOpen = False #If the tray is open or not
            trayIsClicked = False #If tray is currently being clicked
            sortBy = 3 #1 is study, 2 is Old/New, 3 is Test
            sortedCurrentStimuli = 0 #The current stimuli after it's been sorted
            scrollWaitTime = 0 #Waits a certain amount of time before scrolling fast
            timeLeft.setColor('black')
            time.sleep(2)
    
    if os.path.exists(thisdir + '/' + experiment + '/data/'+ participant + '/sub_' + participant + '_PACO' + experiment + '_test.csv') and isDone and not dataFileReady:
        with open (thisdir + '/' + experiment + '/data/'+ participant + '/sub_' + participant + '_PACO' + experiment + '_test.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            firstTimeRun = 0
            for line in csv_reader:
                #print(line)
                if firstTimeRun == 0:
                    firstTimeRun = 1
                elif firstTimeRun == 1:
                    Stimuli = np.array([line])
                    firstTimeRun = 2
                    amountOfStim = 1
                else:
                    Stimuli = np.append(Stimuli, [line], axis = 0)
                    amountOfStim += 1
        print(Stimuli)
        #print(Stimuli[1][1]) #Start getting stimuli at row 0
        #Set Tabs Auto Draw to False
        Overview.setAutoDraw(True)
        Current.setAutoDraw(True)
        selector.setAutoDraw(True)
        sortByText.setAutoDraw(True)
        dataFileReady = True
        if not skipOldOrNew:
            for i in range(amountOfStim): #For each stimuli
                tempNum = 0
                while Stimuli[tempNum][2] != str(i): #Find the coordinate (tempNum) to the order
                    tempNum += 1
                oldornewArray.append(tempNum)
            print(oldornewArray)
        for i in range(amountOfStim): #For each stimuli
            tempNum = 0
            while Stimuli[tempNum][3] != str(i) and Stimuli[tempNum][3] != 'N/A': #Find the coordinate (tempNum) to the order
                tempNum += 1
            if Stimuli[tempNum][3] != 'N/A':
                studyArray.append(tempNum)
        print(studyArray)
        text.setText('Data Is Ready')
        subText.setText('To Exit Press Esc')
        loadFinal = 100
        loadingpercent2 = 100
        correctLocationText.setAutoDraw(False)
        correctLocationKey.setAutoDraw(False)
        userLocationText.setAutoDraw(False)
        userLocationKey.setAutoDraw(False)
        avgCorrectOld = 0
        avgCorrectNew = 0
        allLocationDist = []
        allColorDist = []
        allOldNewRT = []
        allTestRT = []
        avgLocationNum = 0
        avgColorNum = 0
        if experiment == 'LOCO':
            theFinalTime = list(Stimuli[studyStim-1][22].split(":"))
            print(theFinalTime)
            for i in range(amountOfStim):
                if Stimuli[i][10] == 'Old' and Stimuli[i][4] == 'Old':
                    avgCorrectOld += 1
                if Stimuli[i][10] == 'New' and Stimuli[i][4] == 'New':
                    avgCorrectNew += 1
                if Stimuli[i, 16] != 'N/A':
                    allLocationDist.append(float(Stimuli[i, 16]))
                    if float(Stimuli[i, 16]) <= .1:
                        avgLocationNum += 1
                    elif float(Stimuli[i, 16]) <= .35:
                        avgLocationNum += 0.5
                if Stimuli[i, 17] != 'N/A':
                    allColorDist.append(int(Stimuli[i, 17]))
                    if int(Stimuli[i, 17]) <= 5:
                        avgColorNum += 1
                    elif int(Stimuli[i, 17]) <= 10:
                        avgColorNum += .5
                if Stimuli[i, 18] != 'N/A':
                    allOldNewRT.append(float(Stimuli[i, 18]))
                if Stimuli[i, 19] != 'N/A':
                    allTestRT.append(float(Stimuli[i, 19]))
            avgLocationDist = round(sum(allLocationDist)/studyStim, 5)
            avgColorDist = round(sum(allColorDist)/studyStim, 2)
        elif experiment == 'LO':
            theFinalTime = list(Stimuli[studyStim-1][15].split(":"))
            for i in range(amountOfStim):
                if Stimuli[i][7] == 'Old' and Stimuli[i][4] == 'Old':
                    avgCorrectOld += 1
                if Stimuli[i][7] == 'New' and Stimuli[i][4] == 'New':
                    avgCorrectNew += 1
                if Stimuli[i, 10] != 'N/A':
                    allLocationDist.append(float(Stimuli[i, 10]))
                    if float(Stimuli[i, 10]) <= .1:
                        avgLocationNum += 1
                    elif float(Stimuli[i, 10]) <= .35:
                        avgLocationNum += 0.5
                if Stimuli[i, 11] != 'N/A':
                    allOldNewRT.append(float(Stimuli[i, 11]))
                if Stimuli[i, 12] != 'N/A':
                    allTestRT.append(float(Stimuli[i, 12]))
            avgLocationDist = round(sum(allLocationDist)/studyStim, 5)
        elif experiment == 'CO':
            theFinalTime = list(Stimuli[studyStim-1][17].split(":"))
            for i in range(amountOfStim):
                if Stimuli[i][8] == 'Old' and Stimuli[i][4] == 'Old':
                    avgCorrectOld += 1
                if Stimuli[i][8] == 'New' and Stimuli[i][4] == 'New':
                    avgCorrectNew += 1 
                if Stimuli[i, 12] != 'N/A':
                    allColorDist.append(int(Stimuli[i, 12 ]))
                    if int(Stimuli[i, 12]) <= 5:
                        avgColorNum += 1
                    elif int(Stimuli[i, 12]) <= 10:
                        avgColorNum += .5
                if Stimuli[i, 13] != 'N/A':
                    allOldNewRT.append(float(Stimuli[i, 13]))
                if Stimuli[i, 14] != 'N/A':
                    allTestRT.append(float(Stimuli[i, 14]))
            avgColorDist = round(sum(allColorDist)/studyStim, 2)
        if experiment != 'CO':
            if avgLocationDist <= 0.05:
                avgLocationScore = 'Very Good'
            elif avgLocationDist <= 0.15:
                avgLocationScore = 'Good'
            elif avgLocationDist <= 0.35:
                avgLocationScore = 'OK'
            elif avgLocationDist <= 0.7:
                avgLocationScore = 'Bad'
            else:
                avgLocationScore = 'Very Bad'
        if experiment != 'LO':
            if avgColorDist <= 5:
                avgColorScore = 'Good'
            elif avgColorDist <= 10:
                avgColorScore = 'OK'
            else:
                avgColorScore = 'Bad'
        avgOldNewRT = round(sum(allOldNewRT)/testStim, 2)
        avgTestRT = round(sum(allTestRT)/studyStim, 2)
        avgOldNewCorrect = round(((avgCorrectOld + avgCorrectNew)/testStim)*100)
        finalScoreNum = 0
        if avgOldNewCorrect >= 90:
            finalScoreNum = 1
        elif avgOldNewCorrect >= 75:
            finalScoreNum = 0.5
        if experiment != 'CO':
            avgLocationCorrect = round(((avgLocationNum)/studyStim)*100)
            if avgLocationCorrect >= 70:
                finalScoreNum += 1
            elif avgLocationCorrect >= 50:
                finalScoreNum += 0.5
        if experiment != 'LO':
            avgColorCorrect = round(((avgColorNum)/studyStim)*100)
            if avgColorCorrect >= 70:
                finalScoreNum += 1
            elif avgColorCorrect >= 50:
                finalScoreNum += 0.5
        if not skipOldOrNew:
            if finalScoreNum >= 2 or experiment != 'LOCO' and finalScoreNum >= 1.5:
                finalScore = 'Good'
            elif finalScoreNum >= 1:
                finalScore = 'Ok'
            else:
                finalScore = 'Bad'
        else:
            if finalScoreNum >= 1.25 or experiment != 'LOCO' and finalScoreNum >= 0.75:
                finalScore = 'Good'
            elif finalScoreNum >= 0.35:
                finalScore = 'Ok'
            else:
                finalScore = 'Bad'
        stimuli.setAutoDraw(True)
        overviewScoreText.setText('Participant did ' + finalScore)
        if float(theFinalTime[2]) >= 53: #Time error correction
            theFinalTime[2] = '0'
            theFinalTime[1] = str(int(theFinalTime[1]) + 1)
            if theFinalTime[1] == '60':
                theFinalTime[1] = '0'
                theFinalTime[0] = str(int(theFinalTime[0]) + 1)
        if int(theFinalTime[0]) > 12:
            hour = str(int(theFinalTime[0]) - 12)
            ampm = 'pm'
        else:
            hour = str(theFinalTime[0])
            ampm = 'am'
        if int(theFinalTime[1]) < 10:
            min = '0' + str(theFinalTime[1])
        else:
            min = str(theFinalTime[1])
        statusText.setText('Status: Completed at ' + hour + ':' + min + ampm)
        statusText.setColor('black')
        slide()
    
    lastFileNum = fileNum
    if os.path.exists(thisdir + '/' + experiment + '/live/'+ participant + '/live' + str(fileNum) + '.csv'):
        #datafile = open('/Volumes/bamlab/Experiments/PACO/' + experiment + '/live/'+ participant + '/live' + str(fileNum) + '.csv', "rb")
        lastThisLine = thisLine
        with open (thisdir + '/' + experiment + '/live/'+ participant + '/live' + str(fileNum) + '.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                thisLine = line
        if fileNum == 1:
            studyStim = int(thisLine[9])
            testStim = int(thisLine[10])
            if thisLine[0] == 'Practice': #If practice then count those stimuli in
                skipPractice = False #Not skipping practice
                if thisLine[11] == 'False': #This line tells the program if they are skipping old or new parts of the study
                    skipOldOrNew = False
                    totalstim = int(testStim) + int(studyStim)*2 + int(thisLine[5]) + 3 #Number of instruction and practice phases
                else:
                    skipOldOrNew = True
                    totalstim = int(studyStim)*2 + int(thisLine[5]) + 2 #Number of instruction and practice phases
            else:
                skipPractice = True #Is skipping practice
                if thisLine[11] == 'False':
                    skipOldOrNew = False
                    totalstim = int(testStim) + int(studyStim)*2 + 3 #Number of instruction and practice phases
                else:
                    skipOldOrNew = True
                    totalstim = int(studyStim)*2 + 2 #Number of instruction and practice phases
            print(totalstim) #Total stim is used for lower loading bar
            hour, min, sec, ampm = getTime() #Get time from function as strings
            startTime.setText('Start Time: ' + hour + ':' + min + ampm) #Prints current time
        if not dataFileReady:
            statusText.setText('Status: In Progress')
            statusText.setColor('green')
        #Calculate Time Difference
        if skipPractice and skipOldOrNew:
            #Skip both
            if fileNum >= 3 + studyStim:
                timeDiff = testtime*(studyStim-(fileNum-studyStim-3))
                if timeDiff < 0:
                    timeDiff = 0
            else:
                timeDiff = testtime*studyStim
            section = testtime
            if fileNum <= 2 + studyStim:
                timeDiff += instr7time
                section = instr7time
            if fileNum <= studyStim + 1 and fileNum >= 2: #If it is past the first study stim
                timeDiff += studytime*(studyStim-(fileNum-2))
                section = studytime
            elif fileNum <= studyStim + 1: #Else just use pre-calculated data
                timeDiff += studytime*studyStim
                section = studytime
            if fileNum <= 1:
                timeDiff += instr5time
                section = instr5time
        elif skipPractice and not skipOldOrNew:
            #Skip practice
            if fileNum >= 4 + studyStim + testStim:
                timeDiff = testtime*(studyStim-(fileNum-studyStim-testStim-4)) #This needs to change to how many old images have passed
                if timeDiff < 0:
                    timeDiff = 0
            else:
                timeDiff = testtime*studyStim
            section = testtime
            if fileNum <= 3 + studyStim + testStim:
                timeDiff += instr7time
                section = instr7time
            if fileNum <= studyStim + testStim + 2 and fileNum >= studyStim + 3: #If it is past the first oldornew stim
                timeDiff += oldnewtime*(testStim-(fileNum-3-studyStim))
                section = oldnewtime
            elif fileNum <= studyStim + testStim + 2: #Else just use pre-calculated data
                timeDiff += oldnewtime*testStim
                section = oldnewtime
            if fileNum <= 2 + studyStim:
                timeDiff += instr6time
                section = instr6time
            if fileNum <= studyStim + 1 and fileNum >= 2: #If it is past the first study stim
                timeDiff += studytime*(studyStim-(fileNum-2))
                section = studytime
            elif fileNum <= studyStim + 1: #Else just use pre-calculated data
                timeDiff += studytime*studyStim
                section = studytime
            if fileNum <= 1:
                timeDiff += instr5time
                section = instr5time
        elif not skipPractice and skipOldOrNew:
            #Skip Old Or New
            if fileNum >= 11 + studyStim:
                timeDiff = testtime*(studyStim-(fileNum-studyStim-11))
                if timeDiff < 0:
                    timeDiff = 0
            else:
                timeDiff = testtime*studyStim
            section = testtime
            if fileNum <= 10 + studyStim:
                timeDiff += instr7time
                section = instr7time
            if fileNum <= studyStim + 9 and fileNum >= 10: #If it is past the first study stim
                timeDiff += studytime*(studyStim-(fileNum-10))
                section = studytime
            elif fileNum <= studyStim + 9: #Else just use pre-calculated data
                timeDiff += studytime*studyStim
                section = studytime
            if fileNum <= 9:
                timeDiff += instr5time
                section = instr5time
            if fileNum <= 8:
                timeDiff += practtest
                section = practtest
            if fileNum <= 7:
                timeDiff += practtest
                section = practtest
            if fileNum <= 6:
                timeDiff += instr4time
                section = instr4time
            if fileNum <= 5:
                timeDiff += practstudytime
                section = practstudytime
            if fileNum <= 4:
                timeDiff += practstudytime
                section = practstudytime
            if fileNum <= 3:
                timeDiff += instr2time
                section = instr2time
            if fileNum <= 2:
                timeDiff += exampletime
                section = exampletime
            if fileNum <= 1:
                timeDiff += instr1time
                section = instr1time
        elif not skipPractice and not skipOldOrNew:
            #Skip nothing
            if fileNum >= 17 + studyStim + testStim:
                timeDiff = testtime*(studyStim-(fileNum-studyStim-testStim-17)) #This needs to change to how many old images have passed
                if timeDiff < 0:
                    timeDiff = 0
            else:
                timeDiff = testtime*studyStim
            section = testtime
            if fileNum <= 16 + studyStim + testStim:
                timeDiff += instr7time
                section = instr7time
            if fileNum <= studyStim + testStim + 15 and fileNum >= studyStim + 16: #If it is past the first oldornew stim
                timeDiff += oldnewtime*(testStim-(fileNum-16-studyStim))
                section = oldnewtime
            elif fileNum <= studyStim + testStim + 15: #Else just use pre-calculated data
                timeDiff += oldnewtime*testStim
                section = oldnewtime
            if fileNum <= 15 + studyStim:
                timeDiff += instr6time
                section = instr6time
            if fileNum <= studyStim + 14 and fileNum >= 15: #If it is past the first study stim
                timeDiff += studytime*(studyStim-(fileNum-15))
                section = studytime
            elif fileNum <= studyStim + 14: #Else just use pre-calculated data
                timeDiff += studytime*studyStim
                section = studytime
            if fileNum <= 14:
                timeDiff += instr5time
                section = instr5time
            if fileNum <= 13:
                timeDiff += practtest
                section = practtest
            if fileNum <= 12:
                timeDiff += practtest
                section = practtest
            if fileNum <= 11:
                timeDiff += instr4time
                section = instr4time
            if fileNum <= 10:
                timeDiff += practoldnew
                section = practoldnew
            if fileNum <= 9:
                timeDiff += practoldnew
                section = practoldnew
            if fileNum <= 8:
                timeDiff += practoldnew
                section = practoldnew
            if fileNum <= 7:
                timeDiff += practoldnew
                section = practoldnew
            if fileNum <= 6:
                timeDiff += instr3time
                section = instr3time
            if fileNum <= 5:
                timeDiff += practstudytime
                section = practstudytime
            if fileNum <= 4:
                timeDiff += practstudytime
                section = practstudytime
            if fileNum <= 3:
                timeDiff += instr2time
                section = instr2time
            if fileNum <= 2:
                timeDiff += exampletime
                section = exampletime
            if fileNum <= 1:
                timeDiff += instr1time
                section = instr1time
        fileNum += 1 #Increase number on end of file
        firstRun = False #Not first run anymore
    elif firstRun:
        text.setText('Experiment has not started')
    elif os.path.exists(thisdir + '/' + experiment + '/live/'+ participant + '/livelive.csv') and isDone == False:
        isAborted = True
        hour, min, sec, ampm = getTime()
        statusText.setText('Status: Aborted at ' + hour + ':' + min)
        statusText.setColor('red')
        LoadingBar.setColor('red')
        LoadingBar2.setColor('red')
        enableLeft = False
        enableRight = False
        userOldOrNewText.setText('User: N/A')
        correctOldOrNewText.setText('Correct: N/A')
        locationDistText.setText('Location Dist: N/A')
        colorDistText.setText('Color Rad Dist: N/A')
        locationScoreText.setText('Location Score: N/A')
        colorScoreText.setText('Color Score: N/A')
        OldOrNewRTText.setText('Old/New RT: N/A')
        TestRTText.setText('Test RT: N/A')
        StudyOnsetText.setText('Study Onset: N/A')
        OldOrNewOnsetText.setText('Old/New Onset: N/A')
        TestOnsetText.setText('Test Onset: N/A')
        if not soundIsPlaying:
            win.callOnFlip(abortSound.play)  # screen flip
            soundIsPlaying = True
    
    if lastFileNum == fileNum or isDone == True:
        isOnCurrent = True
    
    #Update Loading Bar
    LoadingBar.setSize((loadingpercent/50, 1), log=False)
    LoadingBar.setPos(((loadingpercent/200)-.5, .26))
    percentText.text = str(round(loadingpercent)) + '% Section'
    
    LoadingBar2.setSize((loadingpercent2/50, 1), log=False)
    LoadingBar2.setPos(((loadingpercent2/200)-.5, .14))
    percentText2.text = str(round(loadingpercent2)) + '% Total'
    
    if thisLine[0] == 'Done':
        isDone = True
    
    if firstRun == False and isDone == False and isAborted == False:
        loadFinal = 100/int(thisLine[5])*(int(thisLine[4])-1) #Minus one to make it start at 0
        loadFinal2 = 100/int(totalstim)*(fileNum - 2) #Why -2? It works but idk why
        text.setText('Participant is on ' + thisLine[0] + ' Phase')
        subText.setText(thisLine[1] + ' ' + thisLine[2] + ' of ' + thisLine[3])
        currentTime = datetime.datetime.now()
        hourwhengotdiff = currentTime.hour
        minwhengotdiff = currentTime.minute
        secwhengotdiff = currentTime.second
        if hourwhengotdiff >= int(thisLine[6]):
            hourdiff = hourwhengotdiff - int(thisLine[6])
        else:
            hourdiff = 1
        mindiff = minwhengotdiff - int(thisLine[7])
        if mindiff < 0:
            mindiff = 60 + mindiff
            hourdiff = hourdiff-1
        mindiff += 60*hourdiff
        secdiff = secwhengotdiff - int(thisLine[8])
        if secdiff < 0:
            secdiff = 60 + secdiff
            mindiff = mindiff-1
        secdiff += 60*mindiff
        if secdiff < section*2 and timeleft > timeDiff - secdiff: #Change 2 to change how many secs it can go over before stopping countdown temp
            timeleft = timeDiff - secdiff
            hasDoneTimeSet = True
        elif isOnCurrent and not hasDoneTimeSet:
            timeleft = timeDiff
        if timeleft < 0:
            timeleft = 0
            timeLeft.setColor('black')
        timeleftmins = round(timeleft/60)
        if isOnCurrent: #Waits until it's on the current one to show
            if timeleftmins == 1 and not debugTime:
                timeLeft.setText('Aprox Time Left: ' + str(timeleftmins) +' min')
                timeLeft.setColor('red')
                if not oneMinSoundIsPlaying:
                    win.callOnFlip(oneMinSound.play)
                    oneMinSoundIsPlaying = True
            elif timeleftmins < 1 or debugTime:
                if timeleft == 1:
                    timeLeft.setText('Aprox Time Left: ' + str(timeleft) +' second')
                else:
                    timeLeft.setText('Aprox Time Left: ' + str(timeleft) +' seconds')
            else:
                timeLeft.setText('Aprox Time Left: ' + str(timeleftmins) +' mins')
            endtimemin = (int((timeleft + secwhengotdiff)/60))+minwhengotdiff #Int makes it round the float down to a whole number always
            endtimehour = int((endtimemin)/60)+hourwhengotdiff #Int makes it round the float down to a whole number always
            endtimemin = (endtimemin)%60 #Gets leftover mins incase study is over an hour
            #Get human readable and str time
            if endtimehour > 12:
                thehour = str(endtimehour - 12)
                theampm = 'pm'
            else:
                thehour = str(endtimehour)
                theampm = 'am'
            if endtimemin < 10:
                themin = '0' + str(endtimemin)
            else:
                themin = str(endtimemin)
            endTime.setText('Aprox End Time: ' + thehour + ':' + themin + theampm)
    elif isDone and not dataFileReady:
        text.setText('Participant is complete')
        subText.setText('Waiting for Data File...')
        hour, min, sec, ampm = getTime()
        statusText.setText('Status: Completed at ' + hour + ':' + min + ampm)
        statusText.setColor('black')
        timeLeft.setAutoDraw(False)
        endTime.setAutoDraw(False)
        timeLeft.setColor('black')
        enableLeft = False
        enableRight = False
        userOldOrNewText.setText('User: N/A')
        correctOldOrNewText.setText('Correct: N/A')
        locationDistText.setText('Location Dist: N/A')
        colorDistText.setText('Color Rad Dist: N/A')
        locationScoreText.setText('Location Score: N/A')
        colorScoreText.setText('Color Score: N/A')
        OldOrNewRTText.setText('Old/New RT: N/A')
        TestRTText.setText('Test RT: N/A')
        StudyOnsetText.setText('Study Onset: N/A')
        OldOrNewOnsetText.setText('Old/New Onset: N/A')
        TestOnsetText.setText('Test Onset: N/A')
        correctColorCircle.setColor([0,0,1])
        correctLocationDot.setPos((-.15,-0.08))
        userColorCircle.setColor([0,0,1])
        userLocationDot.setPos((0.065,-0.08)) 
        if not soundIsPlaying and not dataFileReady:
            win.callOnFlip(completeSound.play)  # screen flip
            soundIsPlaying = True
        loadingpercent += loadFinal/50
        if loadingpercent > 100:
            loadingpercent = 100
        loadingpercent2 += loadFinal2/50
        if loadingpercent2 > 100:
            loadingpercent2 = 100
    elif isDone:
        loadingpercent += loadFinal/50
        if loadingpercent > 100:
            loadingpercent = 100
        loadingpercent2 += loadFinal2/50
        if loadingpercent2 > 100:
            loadingpercent2 = 100
        StudyOnsetText.setAutoDraw(True)
        OldOrNewOnsetText.setAutoDraw(True)
        TestOnsetText.setAutoDraw(True)
    if firstRun == False and isDone == False:
        realFirstRun = False
        if thisLine[4] == '1':
            loadingpercent = 0
        if loadingpercent < loadFinal:
            loadingpercent += loadFinal/50
            if loadingpercent > 100:
                loadingpercent = 100
        if loadingpercent2 < loadFinal2:
            loadingpercent2 += loadFinal2/50
            if loadingpercent2 > 100:
                loadingpercent2 = 100
    
    #Current stats code
    if isOnCurrent and not isDone: #Change later to [0] == 'Study'? Also make it only run once every FileNum
        if isOnNewStim:
            if thisLine[1] == 'Stimuli':
                stimuli.setImage(thisdir + '/Stimuli/' + thisLine[9] + '.png')
            else:
                stimuli.setImage('None')
        elif lastThisLine[1] == 'Stimuli':
            stimuli.setImage(thisdir + '/Stimuli/' + lastThisLine[9] + '.png')
        else:
            stimuli.setImage('None')
        if slideOnCurrent:
            stimuli.setAutoDraw(True)
        #correctLocationDot.setPos(((.888)/3.91, ((.5)/3.91)-0.248)) #Most for reference
        if thisLine[0] == 'Study' and thisLine[1] == 'Stimuli':
            if experiment != 'LO':
                correctColorCircle.setColor([((3.6*int(thisLine[12]))+(3.6/2)),1,1])
            if experiment != 'CO':
                correctLocationDot.setPos((float(thisLine[10])/3.91, (float(thisLine[11])/3.91)-0.248))
        elif thisLine[0] == 'Old/New':
            if isOnNewStim and thisLine[1] == 'Stimuli':
                enableRight = False
                enableLeft = True
                if thisLine[10] == 'Old':
                    if experiment != 'LO':
                        correctColorCircle.setColor([((3.6*int(thisLine[13]))+(3.6/2)),1,1])
                    if experiment != 'CO':
                        correctLocationDot.setPos((float(thisLine[11])/3.91, (float(thisLine[12])/3.91)-0.248))
                    correctOldOrNewText.setText('Correct: Old')
                    userOldOrNewText.setText('User: N/A')
                    OldOrNewRTText.setText('Old/New RT: N/A')
                else:
                    correctColorCircle.setColor([0,0,1])
                    correctLocationDot.setPos((-.15,-0.08))
                    correctOldOrNewText.setText('Correct: New')
                    userOldOrNewText.setText('User: N/A')
                    OldOrNewRTText.setText('Old/New RT: N/A')
            elif not isOnNewStim and lastThisLine[1] == 'Stimuli':
                enableLeft = False
                enableRight = True
                if lastThisLine[10] == 'Old':
                    if experiment != 'LO':
                        correctColorCircle.setColor([((3.6*int(lastThisLine[13]))+(3.6/2)),1,1])
                    if experiment != 'CO':
                        correctLocationDot.setPos((float(lastThisLine[11])/3.91, (float(lastThisLine[12])/3.91)-0.248))
                    correctOldOrNewText.setText('Correct: Old')
                    userOldOrNewText.setText('User: ' + thisLine[15])
                    OldOrNewRTText.setText('Old/New RT: ' + thisLine[14] + 'sec')
                else:
                    correctColorCircle.setColor([0,0,1])
                    correctLocationDot.setPos((-.15,-0.08))
                    correctOldOrNewText.setText('Correct: New')
                    userOldOrNewText.setText('User: ' + thisLine[15])
                    OldOrNewRTText.setText('Old/New RT: ' + thisLine[14] + 'sec')
            else:
                enableLeft = False
                enableRight = True
                correctColorCircle.setColor([0,0,1])
                correctLocationDot.setPos((-.15,-0.08))
        elif thisLine[0] == 'Test' and not thisLine[1] == 'Instruction':
            if isOnNewStim and thisLine[1] == 'Stimuli':
                enableRight = False
                enableLeft = True
                if experiment != 'LO':
                    correctColorCircle.setColor([((3.6*int(thisLine[12]))+(3.6/2)),1,1])
                if experiment != 'CO':
                    correctLocationDot.setPos((float(thisLine[10])/3.91, (float(thisLine[11])/3.91)-0.248))
                userColorCircle.setColor([0,0,1])
                userLocationDot.setPos((0.065,-0.08)) #Resets color and location for when you switch to newest
                locationDistText.setText('Location Dist: N/A')
                colorDistText.setText('Color Rad Dist: N/A')
                correctOldOrNewText.setText('Correct: Old')
                userOldOrNewText.setText('User: ' + thisLine[13])
                locationScoreText.setText('Location Score: N/A')
                colorScoreText.setText('Color Score: N/A')
                OldOrNewRTText.setText('Old/New RT: ' + thisLine[17] + 'sec')
                TestRTText.setText('Test RT: N/A')
            elif not isOnNewStim and lastThisLine[1] == 'Stimuli':
                enableLeft = False
                enableRight = True
                if experiment != 'LO':
                    correctColorCircle.setColor([((3.6*int(lastThisLine[12]))+(3.6/2)),1,1])
                    userColorCircle.setColor([((3.6*int(thisLine[16]))+(3.6/2)),1,1])
                    #Color
                    testrad = int(lastThisLine[12])
                    radNum = int(thisLine[16])
                    if abs(testrad-radNum) > 50:
                        if testrad>radNum:
                            colorDist = 100-testrad+radNum
                        else:
                            colorDist = 100-radNum+testrad
                    else:
                        colorDist = abs(testrad-radNum)
                    round(colorDist)
                    colorDistText.setText('Color Rad Dist: ' + str(colorDist))
                    #Calculate if it's the same relative color
                    correctAproxColor = aproxColor(testrad)
                    userAproxColor = aproxColor(radNum)
                    if correctAproxColor[0] in userAproxColor:
                        colorScoreText.setText('Color Score: OK')
                    elif len(correctAproxColor) > 1:
                        if correctAproxColor[1] in userAproxColor:
                            colorScoreText.setText('Color Score: OK')
                        else:
                            colorScoreText.setText('Color Score: Bad')
                    else:
                        colorScoreText.setText('Color Score: Bad')
                    if colorDist < 3:
                        colorScoreText.setText('Color Score: Good')
                if experiment != 'CO':
                    correctLocationDot.setPos((float(lastThisLine[10])/3.91, (float(lastThisLine[11])/3.91)-0.248))
                    userLocationDot.setPos((float(thisLine[14])/3.91, (float(thisLine[15])/3.91)-0.248))
                    #Location
                    distx = abs(float(thisLine[14])-float(lastThisLine[10])) #find the distance in x between correct and user
                    disty = abs(float(thisLine[15])-float(lastThisLine[11])) #find the distance in y between correct and user
                    pythDist = math.sqrt((distx*distx)+(disty*disty)) #Uses pythagorean theorem to find distance
                    pythDist = round(pythDist,5) #Round to prevent errors
                    locationDistText.setText('Location Dist: ' + str(pythDist))
                    if pythDist <= 0.05:
                        locationScoreText.setText('Location Score: Very Good')
                    elif pythDist <= 0.15:
                        locationScoreText.setText('Location Score: Good')
                    elif pythDist <= 0.35:
                        locationScoreText.setText('Location Score: OK')
                    elif pythDist <= 0.7:
                        locationScoreText.setText('Location Score: Bad')
                    else:
                        locationScoreText.setText('Location Score: Very Bad')
                correctOldOrNewText.setText('Correct: Old')
                userOldOrNewText.setText('User: ' + lastThisLine[13])
                OldOrNewRTText.setText('Old/New RT: ' + lastThisLine[17] + 'sec')
                TestRTText.setText('Test RT: ' + thisLine[18] + 'sec')
            else:
                enableLeft = False
                enableRight = True
                correctColorCircle.setColor([0,0,1])
                correctLocationDot.setPos((-.15,-0.08))
                userColorCircle.setColor([0,0,1])
                userLocationDot.setPos((0.065,-0.08))
        if thisLine[1] == 'Stimuli':
            if slideOnCurrent:
                correctColorShape.setAutoDraw(True)
                correctColorCircle.setAutoDraw(True)
                userColorShape.setAutoDraw(True)
                userColorCircle.setAutoDraw(True)
                correctColorText.setAutoDraw(True)
                userColorText.setAutoDraw(True)
            correctLocationDot.setAutoDraw(True)
            userLocationDot.setAutoDraw(True)
            correctLocationKey.setAutoDraw(True)
            userLocationKey.setAutoDraw(True)
            correctLocationText.setAutoDraw(True)
            userLocationText.setAutoDraw(True)
    elif not dataFileReady:
        stimuli.setImage('None')
        correctColorShape.setAutoDraw(False)
        correctColorCircle.setAutoDraw(False)
        userColorShape.setAutoDraw(False)
        userColorCircle.setAutoDraw(False)
        correctColorText.setAutoDraw(False)
        userColorText.setAutoDraw(False)
        correctLocationDot.setAutoDraw(False)
        userLocationDot.setAutoDraw(False)
        correctLocationKey.setAutoDraw(False)
        userLocationKey.setAutoDraw(False)
        correctLocationText.setAutoDraw(False)
        userLocationText.setAutoDraw(False)
    
    if not isOnNewStim:
        userLocationDot.setAutoDraw(True)
        userLocationKey.setAutoDraw(True)
        userLocationText.setAutoDraw(True)
    elif not isDone:
        userLocationDot.setAutoDraw(False)
        userLocationKey.setAutoDraw(False)
        userLocationText.setAutoDraw(False)
    
    if not enableLeft:
        leftArrow.setColor([0.325,0.325,0.325])
    elif slideOnCurrent:
        leftArrow.setColor([-0.624,-0.624,-0.624])
    if not enableRight:
        rightArrow.setColor([0.325,0.325,0.325])
    elif slideOnCurrent:
        rightArrow.setColor([-0.624,-0.624,-0.624])
    if not enableFarLeft:
        doubleLeftArrow1.setColor([0.325,0.325,0.325])
        doubleLeftArrow2.setColor([0.325,0.325,0.325])
    elif slideOnCurrent:
        doubleLeftArrow1.setColor([-0.624,-0.624,-0.624])
        doubleLeftArrow2.setColor([-0.624,-0.624,-0.624])
    if not enableFarRight:
        doubleRightArrow1.setColor([0.325,0.325,0.325])
        doubleRightArrow2.setColor([0.325,0.325,0.325])
    elif slideOnCurrent:
        doubleRightArrow1.setColor([-0.624,-0.624,-0.624])
        doubleRightArrow2.setColor([-0.624,-0.624,-0.624])
    
    #Check if data file is ready at start
    if os.path.exists(thisdir + '/' + experiment + '/data/'+ participant + '/sub_' + participant + '_PACO' + experiment + '_test.csv') and not isDone and not dataFileReady and tryDataFileOnce:
        with open (thisdir + '/' + experiment + '/data/'+ participant + '/sub_' + participant + '_PACO' + experiment + '_test.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            firstTimeRun = 0
            for line in csv_reader:
                #print(line)
                if firstTimeRun == 0:
                    firstTimeRun = 1
                    amountOfStim = 0
                elif firstTimeRun == 1:
                    firstTimeRun = 2
                    amountOfStim = 1
                else:
                    amountOfStim += 1
        #print(amountOfStim)
        #print(testStim)
        if amountOfStim == testStim:
            isDone = True
    tryDataFileOnce = False
    
    # *stimuli* updates
    if t >= 0.0 and stimuli.status == NOT_STARTED:
        # keep track of start time/frame for later
        stimuli.tStart = t  # not accounting for scr refresh
        stimuli.frameNStart = frameN  # exact frame index
        win.timeOnFlip(stimuli, 'tStartRefresh')  # time at next scr refresh
        stimuli.setAutoDraw(True)
    
    # *computer* updates
    if t >= 0.0 and computer.status == NOT_STARTED:
        # keep track of start time/frame for later
        computer.tStart = t  # not accounting for scr refresh
        computer.frameNStart = frameN  # exact frame index
        win.timeOnFlip(computer, 'tStartRefresh')  # time at next scr refresh
        computer.setAutoDraw(True)
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # not accounting for scr refresh
        text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *subText* updates
    if t >= 0.0 and subText.status == NOT_STARTED:
        # keep track of start time/frame for later
        subText.tStart = t  # not accounting for scr refresh
        subText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(subText, 'tStartRefresh')  # time at next scr refresh
        subText.setAutoDraw(True)
    
    # *statusText* updates
    if t >= 0.0 and statusText.status == NOT_STARTED:
        # keep track of start time/frame for later
        statusText.tStart = t  # not accounting for scr refresh
        statusText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(statusText, 'tStartRefresh')  # time at next scr refresh
        statusText.setAutoDraw(True)
    
    # *participantText* updates
    if t >= 0.0 and participantText.status == NOT_STARTED:
        # keep track of start time/frame for later
        participantText.tStart = t  # not accounting for scr refresh
        participantText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(participantText, 'tStartRefresh')  # time at next scr refresh
        participantText.setAutoDraw(True)
    
    # *experimentText* updates
    if t >= 0.0 and experimentText.status == NOT_STARTED:
        # keep track of start time/frame for later
        experimentText.tStart = t  # not accounting for scr refresh
        experimentText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(experimentText, 'tStartRefresh')  # time at next scr refresh
        experimentText.setAutoDraw(True)
    
    # *percentText* updates
    if t >= 0.0 and percentText.status == NOT_STARTED:
        # keep track of start time/frame for later
        percentText.tStart = t  # not accounting for scr refresh
        percentText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(percentText, 'tStartRefresh')  # time at next scr refresh
        percentText.setAutoDraw(True)
    
    # *LoadingBackground* updates
    if t >= 0.0 and LoadingBackground.status == NOT_STARTED:
        # keep track of start time/frame for later
        LoadingBackground.tStart = t  # not accounting for scr refresh
        LoadingBackground.frameNStart = frameN  # exact frame index
        win.timeOnFlip(LoadingBackground, 'tStartRefresh')  # time at next scr refresh
        LoadingBackground.setAutoDraw(True)
    
    # *LoadingBar* updates
    if t >= 0.0 and LoadingBar.status == NOT_STARTED:
        # keep track of start time/frame for later
        LoadingBar.tStart = t  # not accounting for scr refresh
        LoadingBar.frameNStart = frameN  # exact frame index
        win.timeOnFlip(LoadingBar, 'tStartRefresh')  # time at next scr refresh
        LoadingBar.setAutoDraw(True)
    
    # *percentText2* updates
    if t >= 0.0 and percentText2.status == NOT_STARTED:
        # keep track of start time/frame for later
        percentText2.tStart = t  # not accounting for scr refresh
        percentText2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(percentText2, 'tStartRefresh')  # time at next scr refresh
        percentText2.setAutoDraw(True)
    
    # *LoadingBackground2* updates
    if t >= 0.0 and LoadingBackground2.status == NOT_STARTED:
        # keep track of start time/frame for later
        LoadingBackground2.tStart = t  # not accounting for scr refresh
        LoadingBackground2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(LoadingBackground2, 'tStartRefresh')  # time at next scr refresh
        LoadingBackground2.setAutoDraw(True)
    
    # *LoadingBar2* updates
    if t >= 0.0 and LoadingBar2.status == NOT_STARTED:
        # keep track of start time/frame for later
        LoadingBar2.tStart = t  # not accounting for scr refresh
        LoadingBar2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(LoadingBar2, 'tStartRefresh')  # time at next scr refresh
        LoadingBar2.setAutoDraw(True)
    
    # *separator* updates
    if t >= 0.0 and separator.status == NOT_STARTED:
        # keep track of start time/frame for later
        separator.tStart = t  # not accounting for scr refresh
        separator.frameNStart = frameN  # exact frame index
        win.timeOnFlip(separator, 'tStartRefresh')  # time at next scr refresh
        separator.setAutoDraw(True)
    
    # *startTime* updates
    if t >= 0.0 and startTime.status == NOT_STARTED:
        # keep track of start time/frame for later
        startTime.tStart = t  # not accounting for scr refresh
        startTime.frameNStart = frameN  # exact frame index
        win.timeOnFlip(startTime, 'tStartRefresh')  # time at next scr refresh
        startTime.setAutoDraw(True)
    
    # *endTime* updates
    if t >= 0.0 and endTime.status == NOT_STARTED:
        # keep track of start time/frame for later
        endTime.tStart = t  # not accounting for scr refresh
        endTime.frameNStart = frameN  # exact frame index
        win.timeOnFlip(endTime, 'tStartRefresh')  # time at next scr refresh
        endTime.setAutoDraw(True)
    if endTime.status == STARTED:  # only update if drawing
        endTime.setOpacity(1, log=False)
    
    # *timeLeft* updates
    if t >= 0.0 and timeLeft.status == NOT_STARTED:
        # keep track of start time/frame for later
        timeLeft.tStart = t  # not accounting for scr refresh
        timeLeft.frameNStart = frameN  # exact frame index
        win.timeOnFlip(timeLeft, 'tStartRefresh')  # time at next scr refresh
        timeLeft.setAutoDraw(True)
    if timeLeft.status == STARTED:  # only update if drawing
        timeLeft.setOpacity(1, log=False)
    
    # *Overview* updates
    if t >= 0.0 and Overview.status == NOT_STARTED:
        # keep track of start time/frame for later
        Overview.tStart = t  # not accounting for scr refresh
        Overview.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Overview, 'tStartRefresh')  # time at next scr refresh
        Overview.setAutoDraw(True)
    
    # *Current* updates
    if t >= 0.0 and Current.status == NOT_STARTED:
        # keep track of start time/frame for later
        Current.tStart = t  # not accounting for scr refresh
        Current.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Current, 'tStartRefresh')  # time at next scr refresh
        Current.setAutoDraw(True)
    
    # *selector* updates
    if t >= 0.0 and selector.status == NOT_STARTED:
        # keep track of start time/frame for later
        selector.tStart = t  # not accounting for scr refresh
        selector.frameNStart = frameN  # exact frame index
        win.timeOnFlip(selector, 'tStartRefresh')  # time at next scr refresh
        selector.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('stimuli.started', stimuli.tStartRefresh)
thisExp.addData('stimuli.stopped', stimuli.tStopRefresh)
thisExp.addData('computer.started', computer.tStartRefresh)
thisExp.addData('computer.stopped', computer.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('subText.started', subText.tStartRefresh)
thisExp.addData('subText.stopped', subText.tStopRefresh)
thisExp.addData('statusText.started', statusText.tStartRefresh)
thisExp.addData('statusText.stopped', statusText.tStopRefresh)
thisExp.addData('participantText.started', participantText.tStartRefresh)
thisExp.addData('participantText.stopped', participantText.tStopRefresh)
thisExp.addData('experimentText.started', experimentText.tStartRefresh)
thisExp.addData('experimentText.stopped', experimentText.tStopRefresh)
thisExp.addData('percentText.started', percentText.tStartRefresh)
thisExp.addData('percentText.stopped', percentText.tStopRefresh)
thisExp.addData('LoadingBackground.started', LoadingBackground.tStartRefresh)
thisExp.addData('LoadingBackground.stopped', LoadingBackground.tStopRefresh)
thisExp.addData('LoadingBar.started', LoadingBar.tStartRefresh)
thisExp.addData('LoadingBar.stopped', LoadingBar.tStopRefresh)
thisExp.addData('percentText2.started', percentText2.tStartRefresh)
thisExp.addData('percentText2.stopped', percentText2.tStopRefresh)
thisExp.addData('LoadingBackground2.started', LoadingBackground2.tStartRefresh)
thisExp.addData('LoadingBackground2.stopped', LoadingBackground2.tStopRefresh)
thisExp.addData('LoadingBar2.started', LoadingBar2.tStartRefresh)
thisExp.addData('LoadingBar2.stopped', LoadingBar2.tStopRefresh)
thisExp.addData('separator.started', separator.tStartRefresh)
thisExp.addData('separator.stopped', separator.tStopRefresh)
thisExp.addData('startTime.started', startTime.tStartRefresh)
thisExp.addData('startTime.stopped', startTime.tStopRefresh)
thisExp.addData('endTime.started', endTime.tStartRefresh)
thisExp.addData('endTime.stopped', endTime.tStopRefresh)
thisExp.addData('timeLeft.started', timeLeft.tStartRefresh)
thisExp.addData('timeLeft.stopped', timeLeft.tStopRefresh)
thisExp.addData('Overview.started', Overview.tStartRefresh)
thisExp.addData('Overview.stopped', Overview.tStopRefresh)
thisExp.addData('Current.started', Current.tStartRefresh)
thisExp.addData('Current.stopped', Current.tStopRefresh)
thisExp.addData('selector.started', selector.tStartRefresh)
thisExp.addData('selector.stopped', selector.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
