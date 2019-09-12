#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on Wed Sep  4 17:32:41 2019
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
expName = 'Live2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'experiment': ''}
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
    originPath='/Volumes/bamlab-1/Experiments/Live App 2.0/Live2_lastrun.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[500, 200], fullscr=False, screen=0, 
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

completeSound = sound.Sound('complete.wav', secs=-1, stereo=True)
completeSound.setVolume(1)
oneMinSound = sound.Sound('1min.wav', secs=-1, stereo=True)
completeSound.setVolume(1)
stimuli = visual.ImageStim(
    win=win,
    name='stimuli', 
    image=None, mask=None,
    ori=0, pos=(-0.45, -.2), size=(0.3, 0.3),
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text = visual.TextStim(win=win, name='text',
    text='Participant is on practice phase',
    font='Arial',
    pos=(0, .35), height=0.14, wrapWidth=12, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
subText = visual.TextStim(win=win, name='subText',
    text=None,
    font='Arial',
    pos=(0, .22), height=0.10, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
statusText = visual.TextStim(win=win, name='statusText',
    text='Status: Ready',
    font='Arial',
    pos=(0, .45), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
participantText = visual.TextStim(win=win, name='participantText',
    text='000',
    font='Arial',
    pos=(-1.1, .41), height=0.12, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
experimentText = visual.TextStim(win=win, name='experimentText',
    text='000',
    font='Arial',
    pos=(1, .41), height=0.12, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
percentText = visual.TextStim(win=win, name='percentText',
    text='0% Section',
    font='Arial',
    pos=(0, -0.1), height=0.08, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
LoadingBackground = visual.Rect(
    win=win, name='LoadingBackground',
    width=(2, 0.15)[0], height=(2, 0.15)[1],
    ori=0, pos=(0, 0.05),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.278,0.278,0.278], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
LoadingBar = visual.Rect(
    win=win, name='LoadingBar',
    width=(.5, 0.15)[0], height=(.5, 0.15)[1],
    ori=0, pos=(0, 0.05),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.184,0.365,1.000], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
percentText2 = visual.TextStim(win=win, name='percentText2',
    text='0% Total',
    font='Arial',
    pos=(0, -0.43), height=0.08, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
LoadingBackground2 = visual.Rect(
    win=win, name='LoadingBackground2',
    width=(2, 0.15)[0], height=(2, 0.15)[1],
    ori=0, pos=(0, -.28),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.278,0.278,0.278], fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
LoadingBar2 = visual.Rect(
    win=win, name='LoadingBar2',
    width=(.5, 0.15)[0], height=(.5, 0.15)[1],
    ori=0, pos=(0, -.28),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.184,0.365,1.000], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
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
thisLine = [0, 0, 0, 0, 0, 0]
totalstim = 0
isDone = False
soundIsPlaying = False
oneMinSoundIsPlaying = False
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
trialComponents = [stimuli, text, subText, statusText, participantText, experimentText, percentText, LoadingBackground, LoadingBar, percentText2, LoadingBackground2, LoadingBar2, mouse]
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
    if os.path.exists(thisdir + '/' + experiment + '/live/'+ participant + '/live' + str(fileNum) + '.csv'):
        time.sleep(0.5) #Makes sure all of file is done saving before reading it
        #datafile = open('/Volumes/bamlab/Experiments/PACO/' + experiment + '/live/'+ participant + '/live' + str(fileNum) + '.csv', "rb")
        with open (thisdir + '/' + experiment + '/live/'+ participant + '/live' + str(fileNum) + '.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                thisLine = line
        fileNum += 1 #Increase number on end of file
        firstRun = False #Not first run anymore
        print(thisLine)
        soundIsPlaying = False
    elif firstRun:
        text.setText('Experiment has not started')
    
    #Update Loading Bar
    LoadingBar.setSize((loadingpercent/25, 1), log=False)
    LoadingBar.setPos(((loadingpercent/100)-1, 0.05))
    percentText.text = str(round(loadingpercent)) + '% Section'
    
    LoadingBar2.setSize((loadingpercent2/25, 1), log=False)
    LoadingBar2.setPos(((loadingpercent2/100)-1, -.28))
    percentText2.text = str(round(loadingpercent2)) + '% Total'
    
    #Marks experiment as done
    if thisLine[0] == 'Done':
        isDone = True
        if not soundIsPlaying:
            win.callOnFlip(completeSound.play)  # screen flip
            soundIsPlaying = True
    
    #Plays warning tone
    if thisLine[5] == '1':
        if not soundIsPlaying:
            win.callOnFlip(oneMinSound.play)  # screen flip
            soundIsPlaying = True
    
    #Update progress
    if firstRun == False and not isDone:
        loadFinal = 100/int(thisLine[2])*(int(thisLine[1])-1) #Minus one is bc not 100% when on trial 5 of 5 ect
        loadFinal2 = 100/int(thisLine[4])*(int(thisLine[3])-1)
        text.setText(thisLine[0] + ' Phase')
        subText.setText('Trial ' + thisLine[1] + ' of ' + thisLine[2])
        statusText.setText('Status: In Progress')
        statusText.setColor('green')
        if thisLine[1] == '1':
            loadingpercent = 0
        if loadingpercent < loadFinal:
            loadingpercent += loadFinal/50
            if loadingpercent > 100:
                loadingpercent = 100
        if loadingpercent2 < loadFinal2:
            loadingpercent2 += loadFinal2/50
            if loadingpercent2 > 100:
                loadingpercent2 = 100
    elif isDone:
        text.setText('Participant is complete')
        subText.setText('Press Esc To Exit')
        statusText.setText('Status: Complete')
        statusText.setColor('black')
        loadingpercent += loadFinal/50
        if loadingpercent > 100:
            loadingpercent = 100
        loadingpercent2 += loadFinal2/50
        if loadingpercent2 > 100:
            loadingpercent2 = 100
    
    # *stimuli* updates
    if t >= 0.0 and stimuli.status == NOT_STARTED:
        # keep track of start time/frame for later
        stimuli.tStart = t  # not accounting for scr refresh
        stimuli.frameNStart = frameN  # exact frame index
        win.timeOnFlip(stimuli, 'tStartRefresh')  # time at next scr refresh
        stimuli.setAutoDraw(True)
    
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
