#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on Fri Aug  9 09:35:38 2019
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
expName = 'PACOExample'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/Logs/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Volumes/psych-cog/bamlab/Experiments/PACO/example_code/PACOExample_lastrun.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
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

# Initialize components for Routine "header"
headerClock = core.Clock()
import random, xlrd #For randomization of stimuli
command = False #For exiting experiment

thisdir = os.path.abspath(os.path.join(os.path.dirname(_thisDir),'.'))

imageName = '22' #Name of image to use
color = 22 #Out of 360

# Initialize components for Routine "reset"
resetClock = core.Clock()
resettext = visual.TextStim(win=win, name='resettext',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "study"
studyClock = core.Clock()
studyImage = visual.ImageStim(
    win=win,
    name='studyImage', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.19, 0.19),
    color='white', colorSpace='hsv', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_6 = visual.TextStim(win=win, name='text_6',
    text='Stimuli: ',
    font='Arial',
    pos=(0, 0.45), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='Color: ',
    font='Arial',
    pos=(0, .4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
mouse0 = event.Mouse(win=win)
x, y = [None, None]
mouse0.mouseClock = core.Clock()

# Initialize components for Routine "reset"
resetClock = core.Clock()
resettext = visual.TextStim(win=win, name='resettext',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "oldornew"
oldornewClock = core.Clock()
oldornewText = visual.TextStim(win=win, name='oldornewText',
    text='1 - Old        2 - New',
    font='Arial',
    pos=(0, -.45), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
oldornewImage = visual.ImageStim(
    win=win,
    name='oldornewImage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.19, 0.19),
    color=[-1,-1,-1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "reset"
resetClock = core.Clock()
resettext = visual.TextStim(win=win, name='resettext',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practiceExample"
practiceExampleClock = core.Clock()
Image3 = visual.ImageStim(
    win=win,
    name='Image3', 
    image=thisdir + '/Stimuli/' + imageName + '.png', mask=None,
    ori=0, pos=(0, 0), size=(0.19, 0.19),
    color=[0,1,0], colorSpace='hsv', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse3 = event.Mouse(win=win)
x, y = [None, None]
mouse3.mouseClock = core.Clock()
#To prevent user from clicking inside the color wheel and selecting a color, noClickShape surrounds entire image, set opacity to one to see for yourself ;)
noClickShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,0,1], pos=(0,0), size=(0.25,0.25), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 0)
from psychopy import misc #needed for color wheel

#Creates color wheel object
textureRes = 64

hsv = np.ones([textureRes,textureRes,3], dtype=float)
hsv[:,:,0] = np.linspace(0,360,textureRes, endpoint=False)
hsv[:,:,1] = 1
hsv[:,:,2] = 1
rgb = misc.hsv2rgb(hsv)

#mask gives the fraction of the that is visible
mask = np.zeros([100,1])
mask[-10:] = 1  # 10% of the radius is 1 (visible)
# annoyingly with interpolate=True the mask outer edge can 
# get blended with innermost pixel

#texture defines colors, mask makes it have a hole in the center, angular cycles defines how many times each color will be shown, interpolate makes the colors blend together
stim = visual.RadialStim(win, tex=rgb, mask = mask, angularRes=256, angularCycles=1, interpolate=True, size=(.3,.3))
#This creates each segment of the circle that can be used and clicked on later in the experiment
opac = 0 #changes opacity of segments, 0 is invisible, 1 is visible, change to 0.5? to debug
orimult = 3.6 #origin value is multiplied by this amount
visWed = (0.0, 4) #visible portion of the wedge
segpos = (0,0) #Position of segments
segSize = (4,4) #size of segments, goes along with color wheel size
degrees = 0 #Degrees the selectshape should be, don't change this var
#If you change the amount of possible segments make sure to update randomization amount in the header file as well

#Visual wedge is set to 4 but in reality it only covers about 3.6
#So the origin of each segment are multiples of 3.6, 360/3.6 is 100 segments
screenRect3 = visual.Rect(
    win=win, name='screenRect3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-6.0, interpolate=True)
import math #Needed for cos and sin
#Max degrees and speed for color help
colorMaxDeg = 270 #1 to any real number, must be at least twice as much as speed for smooth animation
colorSpeed = 50 #1 to any real number, do not recomend setting this above 50

#Color text setup
ColorText = visual.TextStim(win=win, name='ColorText',
    text='Please select a color from the color wheel',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

#Drag text setup
DragText = visual.TextStim(win=win, name='DragText',
    text='Please Drag and Drop the object to a location on the screen',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

#Define images
arrowUp = visual.ImageStim(
    win=win, name='arrowUp',
    image='sin', mask=None,
    ori=0, pos=(0, .2), size=(0.03, 0.03),
    color=[1,1,0], colorSpace='hsv', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

arrowDown = visual.ImageStim(
    win=win, name='arrowDown',
    image='sin', mask=None,
    ori=0, pos=(0, -.2), size=(0.03, 0.03),
    color=[1,1,0], colorSpace='hsv', opacity=1,
    flipHoriz=False, flipVert=True,
    texRes=128, interpolate=True, depth=0.0)

arrowRight = visual.ImageStim(
    win=win, name='arrowRight',
    image='sin', mask=None,
    ori=0, pos=(.2, 0), size=(0.03, 0.03),
    color=[1,1,0], colorSpace='hsv', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

arrowLeft = visual.ImageStim(
    win=win, name='arrowLeft',
    image='sin', mask=None,
    ori=0, pos=(-.2, 0), size=(0.03, 0.03),
    color=[1,1,0], colorSpace='hsv', opacity=1,
    flipHoriz=True, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

#Set images
arrowUp.setImage(thisdir + '/LOCO/arrowUp.png')
arrowDown.setImage(thisdir + '/LOCO/arrowUp.png')
arrowRight.setImage(thisdir + '/LOCO/arrowRight.png')
arrowLeft.setImage(thisdir + '/LOCO/arrowRight.png')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "header"-------
t = 0
headerClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
headerComponents = []
for thisComponent in headerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "header"-------
while continueRoutine:
    # get current time
    t = headerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in headerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "header"-------
for thisComponent in headerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "header" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "reset"-------
t = 0
resetClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_12 = keyboard.Keyboard()
win.mouseVisible = False #Show mouse at start
# keep track of which components have finished
resetComponents = [resettext, key_resp_12]
for thisComponent in resetComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "reset"-------
while continueRoutine:
    # get current time
    t = resetClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resettext* updates
    if t >= 0.0 and resettext.status == NOT_STARTED:
        # keep track of start time/frame for later
        resettext.tStart = t  # not accounting for scr refresh
        resettext.frameNStart = frameN  # exact frame index
        win.timeOnFlip(resettext, 'tStartRefresh')  # time at next scr refresh
        resettext.setAutoDraw(True)
    
    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t  # not accounting for scr refresh
        key_resp_12.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        key_resp_12.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resetComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "reset"-------
for thisComponent in resetComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('resettext.started', resettext.tStartRefresh)
thisExp.addData('resettext.stopped', resettext.tStopRefresh)
# the Routine "reset" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "study"-------
t = 0
studyClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
studyImage.setPos((0,0))
key_resp_14 = keyboard.Keyboard()
setColor = False
setImage = False
win.mouseVisible = True #Show mouse at start
# setup some python lists for storing info about the mouse0
gotValidClick = False  # until a click is received
# keep track of which components have finished
studyComponents = [studyImage, key_resp_14, text_6, text_7, mouse0]
for thisComponent in studyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "study"-------
while continueRoutine:
    # get current time
    t = studyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *studyImage* updates
    if t >= 0.0 and studyImage.status == NOT_STARTED:
        # keep track of start time/frame for later
        studyImage.tStart = t  # not accounting for scr refresh
        studyImage.frameNStart = frameN  # exact frame index
        win.timeOnFlip(studyImage, 'tStartRefresh')  # time at next scr refresh
        studyImage.setAutoDraw(True)
    if studyImage.status == STARTED:  # only update if drawing
        studyImage.setColor([color,1,0], colorSpace='hsv', log=False)
        studyImage.setImage(thisdir + '/Stimuli/' + imageName + '.png', log=False)
    
    # *key_resp_14* updates
    if t >= 0.0 and key_resp_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_14.tStart = t  # not accounting for scr refresh
        key_resp_14.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        key_resp_14.clearEvents(eventType='keyboard')
    if key_resp_14.status == STARTED:
        theseKeys = key_resp_14.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # not accounting for scr refresh
        text_6.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t  # not accounting for scr refresh
        text_7.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if mouse0.isPressedIn(text_6):
        setImage = True
        setColor = False
        tempimageName = ''
        tempcolor = -1
    elif mouse0.isPressedIn(text_7):
        setColor = True
        setImage = False
        tempimageName = ''
        tempcolor = -1
    
    keys = event.getKeys()
    for key in keys:
        if key == '0' or key == '1' or key == '2' or key == '3' or key == '4' or key == '5' or key == '6' or key == '7' or key == '8' or key == '9':
            if setImage:
                if tempimageName != '':
                    if int(tempimageName) < 243:
                        tempimageName = tempimageName + key
                else:
                    tempimageName = key
                imageName = tempimageName
            elif setColor:
                if tempcolor == -1:
                    tempcolor = int(key)
                else:
                    tempcolor = int(str(tempcolor) + key)
                color = tempcolor
    
    text_6.setText('Image: ' + imageName)
    text_7.setText('Color: ' + str(color))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in studyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "study"-------
for thisComponent in studyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('studyImage.started', studyImage.tStartRefresh)
thisExp.addData('studyImage.stopped', studyImage.tStopRefresh)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse0.started', mouse0.tStart)
thisExp.addData('mouse0.stopped', mouse0.tStop)
thisExp.nextEntry()
# the Routine "study" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "reset"-------
t = 0
resetClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_12 = keyboard.Keyboard()
win.mouseVisible = False #Show mouse at start
# keep track of which components have finished
resetComponents = [resettext, key_resp_12]
for thisComponent in resetComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "reset"-------
while continueRoutine:
    # get current time
    t = resetClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resettext* updates
    if t >= 0.0 and resettext.status == NOT_STARTED:
        # keep track of start time/frame for later
        resettext.tStart = t  # not accounting for scr refresh
        resettext.frameNStart = frameN  # exact frame index
        win.timeOnFlip(resettext, 'tStartRefresh')  # time at next scr refresh
        resettext.setAutoDraw(True)
    
    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t  # not accounting for scr refresh
        key_resp_12.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        key_resp_12.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resetComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "reset"-------
for thisComponent in resetComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('resettext.started', resettext.tStartRefresh)
thisExp.addData('resettext.stopped', resettext.tStopRefresh)
# the Routine "reset" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "oldornew"-------
t = 0
oldornewClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
oldornewImage.setImage(thisdir + '/Stimuli/' + imageName + '.png')
key_resp_13 = keyboard.Keyboard()
# keep track of which components have finished
oldornewComponents = [oldornewText, oldornewImage, key_resp_13]
for thisComponent in oldornewComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "oldornew"-------
while continueRoutine:
    # get current time
    t = oldornewClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *oldornewText* updates
    if t >= 0 and oldornewText.status == NOT_STARTED:
        # keep track of start time/frame for later
        oldornewText.tStart = t  # not accounting for scr refresh
        oldornewText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(oldornewText, 'tStartRefresh')  # time at next scr refresh
        oldornewText.setAutoDraw(True)
    
    # *oldornewImage* updates
    if t >= 0.0 and oldornewImage.status == NOT_STARTED:
        # keep track of start time/frame for later
        oldornewImage.tStart = t  # not accounting for scr refresh
        oldornewImage.frameNStart = frameN  # exact frame index
        win.timeOnFlip(oldornewImage, 'tStartRefresh')  # time at next scr refresh
        oldornewImage.setAutoDraw(True)
    
    # *key_resp_13* updates
    if t >= 0.0 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t  # not accounting for scr refresh
        key_resp_13.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        key_resp_13.clearEvents(eventType='keyboard')
    if key_resp_13.status == STARTED:
        theseKeys = key_resp_13.getKeys(keyList=['space', '1', '2'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in oldornewComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "oldornew"-------
for thisComponent in oldornewComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('oldornewText.started', oldornewText.tStartRefresh)
thisExp.addData('oldornewText.stopped', oldornewText.tStopRefresh)
thisExp.addData('oldornewImage.started', oldornewImage.tStartRefresh)
thisExp.addData('oldornewImage.stopped', oldornewImage.tStopRefresh)
# the Routine "oldornew" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "reset"-------
t = 0
resetClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_12 = keyboard.Keyboard()
win.mouseVisible = False #Show mouse at start
# keep track of which components have finished
resetComponents = [resettext, key_resp_12]
for thisComponent in resetComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "reset"-------
while continueRoutine:
    # get current time
    t = resetClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resettext* updates
    if t >= 0.0 and resettext.status == NOT_STARTED:
        # keep track of start time/frame for later
        resettext.tStart = t  # not accounting for scr refresh
        resettext.frameNStart = frameN  # exact frame index
        win.timeOnFlip(resettext, 'tStartRefresh')  # time at next scr refresh
        resettext.setAutoDraw(True)
    
    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t  # not accounting for scr refresh
        key_resp_12.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        key_resp_12.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resetComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "reset"-------
for thisComponent in resetComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('resettext.started', resettext.tStartRefresh)
thisExp.addData('resettext.stopped', resettext.tStopRefresh)
# the Routine "reset" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceExample"-------
t = 0
practiceExampleClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse3
gotValidClick = False  # until a click is received
key_resp_9 = keyboard.Keyboard()
isDragging = False #Lets other parts of experiment know that the user is dragging the stimuli
didFinishDrag = False #Lets some aspects of the experiment only do something once after a drag has finished
hasDragged = False #For preventing the user from going on until dragged
place = (0,0) #Place of object (Image)
Image3.setPos(place) #Sets image to (0,0)
noClickShape.setPos(place) #Sets noClickShape to (0,0), see Begin Experiment for more about noClickShape
mousePlace = (0,0) #Place of mouse when clicked
mousex = 0.0 #Offset of mouse x
mousey = 0.0 #Offset of mouse y
firstDrag = True #For updating positions of mousex and mousey
isOnColor = False #If the mouse is currently on a color
hasColored = False #For hiding the selectShape until you start coloring
stim.setPos(place)
segpos = (0,0) #resets position of segments

#Defines each segment
rad0 = visual.RadialStim( win=win, name='rad0', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*0, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad1 = visual.RadialStim( win=win, name='rad1', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*1, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad2 = visual.RadialStim( win=win, name='rad2', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*2, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad3 = visual.RadialStim( win=win, name='rad3', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*3, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad4 = visual.RadialStim( win=win, name='rad4', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*4, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad5 = visual.RadialStim( win=win, name='rad5', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*5, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad6 = visual.RadialStim( win=win, name='rad6', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*6, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad7 = visual.RadialStim( win=win, name='rad7', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*7, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad8 = visual.RadialStim( win=win, name='rad8', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*8, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad9 = visual.RadialStim( win=win, name='rad9', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*9, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad10 = visual.RadialStim( win=win, name='rad10', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*10, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad11 = visual.RadialStim( win=win, name='rad11', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*11, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad12 = visual.RadialStim( win=win, name='rad12', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*12, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad13 = visual.RadialStim( win=win, name='rad13', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*13, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad14 = visual.RadialStim( win=win, name='rad14', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*14, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad15 = visual.RadialStim( win=win, name='rad15', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*15, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad16 = visual.RadialStim( win=win, name='rad16', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*16, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad17 = visual.RadialStim( win=win, name='rad17', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*17, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad18 = visual.RadialStim( win=win, name='rad18', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*18, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad19 = visual.RadialStim( win=win, name='rad19', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*19, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad20 = visual.RadialStim( win=win, name='rad20', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*20, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad21 = visual.RadialStim( win=win, name='rad21', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*21, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad22 = visual.RadialStim( win=win, name='rad22', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*22, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad23 = visual.RadialStim( win=win, name='rad23', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*23, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad24 = visual.RadialStim( win=win, name='rad24', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*24, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad25 = visual.RadialStim( win=win, name='rad25', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*25, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad26 = visual.RadialStim( win=win, name='rad26', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*26, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad27 = visual.RadialStim( win=win, name='rad27', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*27, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad28 = visual.RadialStim( win=win, name='rad28', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*28, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad29 = visual.RadialStim( win=win, name='rad29', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*29, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad30 = visual.RadialStim( win=win, name='rad30', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*30, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad31 = visual.RadialStim( win=win, name='rad31', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*31, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad32 = visual.RadialStim( win=win, name='rad32', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*32, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad33 = visual.RadialStim( win=win, name='rad33', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*33, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad34 = visual.RadialStim( win=win, name='rad34', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*34, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad35 = visual.RadialStim( win=win, name='rad35', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*35, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad36 = visual.RadialStim( win=win, name='rad36', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*36, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad37 = visual.RadialStim( win=win, name='rad37', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*37, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad38 = visual.RadialStim( win=win, name='rad38', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*38, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad39 = visual.RadialStim( win=win, name='rad39', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*39, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad40 = visual.RadialStim( win=win, name='rad40', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*40, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad41 = visual.RadialStim( win=win, name='rad41', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*41, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad42 = visual.RadialStim( win=win, name='rad42', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*42, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad43 = visual.RadialStim( win=win, name='rad43', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*43, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad44 = visual.RadialStim( win=win, name='rad44', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*44, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad45 = visual.RadialStim( win=win, name='rad45', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*45, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad46 = visual.RadialStim( win=win, name='rad46', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*46, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad47 = visual.RadialStim( win=win, name='rad47', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*47, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad48 = visual.RadialStim( win=win, name='rad48', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*48, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad49 = visual.RadialStim( win=win, name='rad49', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*49, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad50 = visual.RadialStim( win=win, name='rad50', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*50, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad51 = visual.RadialStim( win=win, name='rad51', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*51, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad52 = visual.RadialStim( win=win, name='rad52', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*52, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad53 = visual.RadialStim( win=win, name='rad53', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*53, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad54 = visual.RadialStim( win=win, name='rad54', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*54, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad55 = visual.RadialStim( win=win, name='rad55', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*55, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad56 = visual.RadialStim( win=win, name='rad56', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*56, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad57 = visual.RadialStim( win=win, name='rad57', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*57, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad58 = visual.RadialStim( win=win, name='rad58', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*58, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad59 = visual.RadialStim( win=win, name='rad59', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*59, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad60 = visual.RadialStim( win=win, name='rad60', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*60, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad61 = visual.RadialStim( win=win, name='rad61', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*61, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad62 = visual.RadialStim( win=win, name='rad62', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*62, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad63 = visual.RadialStim( win=win, name='rad63', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*63, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad64 = visual.RadialStim( win=win, name='rad64', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*64, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad65 = visual.RadialStim( win=win, name='rad65', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*65, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad66 = visual.RadialStim( win=win, name='rad66', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*66, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad67 = visual.RadialStim( win=win, name='rad67', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*67, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad68 = visual.RadialStim( win=win, name='rad68', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*68, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad69 = visual.RadialStim( win=win, name='rad69', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*69, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad70 = visual.RadialStim( win=win, name='rad70', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*70, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad71 = visual.RadialStim( win=win, name='rad71', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*71, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad72 = visual.RadialStim( win=win, name='rad72', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*72, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad73 = visual.RadialStim( win=win, name='rad73', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*73, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad74 = visual.RadialStim( win=win, name='rad74', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*74, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad75 = visual.RadialStim( win=win, name='rad75', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*75, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad76 = visual.RadialStim( win=win, name='rad76', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*76, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad77 = visual.RadialStim( win=win, name='rad77', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*77, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad78 = visual.RadialStim( win=win, name='rad78', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*78, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad79 = visual.RadialStim( win=win, name='rad79', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*79, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad80 = visual.RadialStim( win=win, name='rad80', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*80, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad81 = visual.RadialStim( win=win, name='rad81', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*81, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad82 = visual.RadialStim( win=win, name='rad82', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*82, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad83 = visual.RadialStim( win=win, name='rad83', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*83, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad84 = visual.RadialStim( win=win, name='rad84', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*84, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad85 = visual.RadialStim( win=win, name='rad85', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*85, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad86 = visual.RadialStim( win=win, name='rad86', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*86, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad87 = visual.RadialStim( win=win, name='rad87', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*87, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad88 = visual.RadialStim( win=win, name='rad88', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*88, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad89 = visual.RadialStim( win=win, name='rad89', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*89, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad90 = visual.RadialStim( win=win, name='rad90', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*90, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad91 = visual.RadialStim( win=win, name='rad91', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*91, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad92 = visual.RadialStim( win=win, name='rad92', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*92, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad93 = visual.RadialStim( win=win, name='rad93', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*93, pos=segpos, size=segSize, visibleWedge=visWed, opacity = opac )

rad94 = visual.RadialStim( win=win, name='rad94', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*94, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad95 = visual.RadialStim( win=win, name='rad95', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*95, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad96 = visual.RadialStim( win=win, name='rad96', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*96, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad97 = visual.RadialStim( win=win, name='rad97', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*97, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad98 = visual.RadialStim( win=win, name='rad98', color=[-1,1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*98, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )

rad99 = visual.RadialStim( win=win, name='rad99', color=[1,-1,-1],
    angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
    ori= orimult*99, pos=segpos, size=segSize, visibleWedge=visWed,  opacity = opac )
#Select shape is the selector circle that is white and behind the colored one
selectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,1,1], pos=(0,0), size=(0.1,0.1), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 0)
#Inner select shape is on top of select shape and updates it's color to the color of the part of the color wheel it is on
innerSelectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,1,1], pos=(0,0), size=(0.1,0.1), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 0)
win.mouseVisible = True #Show mouse at start
mouse3.setPos(newPos=(0, 0.001)) #resets position of mouse, has to be offset slightly or else it will select a color for some reason

#These two vars give the person help with knowing how to drag/color live
helpDrag = False
helpColor = False

opacOfArrows = 0.0 #Opacity of the arrows
opacUp = True #If Opacity is rising or falling

colorDeg = 0 #Degrees of slider for colorHelp
colorDegUp = True #Degrees of the slider going up or down
colorOpac = 0 #Opacity of the slider
# keep track of which components have finished
practiceExampleComponents = [Image3, mouse3, key_resp_9, screenRect3]
for thisComponent in practiceExampleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "practiceExample"-------
while continueRoutine:
    # get current time
    t = practiceExampleClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Image3* updates
    if t >= 0.0 and Image3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Image3.tStart = t  # not accounting for scr refresh
        Image3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Image3, 'tStartRefresh')  # time at next scr refresh
        Image3.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t  # not accounting for scr refresh
        key_resp_9.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        key_resp_9.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
    #This whole complicated thing makes sure that the stimuli always stays on the mouse if they click on the stimuli first
    if mouse3.isPressedIn(screenRect3) and didFinishDrag == False:#ScreenRect is used to detect if mouse is pressed anywhere on screen
        if mouse3.isPressedIn(noClickShape): #Checks when mouse is pressed down, see Begin Experiment for more about noClickShape
            if isOnColor == False: #Makes sure it didn't start on the color wheel
                #This calculates offset of mouse from center of object (Not needed but looks better in experiment)
                mousePlace = mouse3.getPos()
                if firstDrag == True: #Only updates offset once when starting the drag
                    mousex = mousePlace[0] - place[0] #Gets the difference between the Image place and the mouse place for x
                    mousey = mousePlace[1] - place[1] #Gets the difference between the Image place and the mouse place for y
                    firstDrag = False #Disables first drag
                place = mousePlace[0] - mousex, mousePlace[1] - mousey #Adds this onto the place of the image for more intuitive dragging
                Image3.setPos(place) #Sets position of the image equal to the position of the mouse
                noClickShape.setPos(place) #Set position
                isDragging = True #Sets is dragging to true when the mouse starts on the object (noClickShape in this case)
                hasDragged = True #For preventing the user from going on until dragged
                win.mouseVisible = False #Hide mouse when dragging
        elif isDragging == True: #If the mouse started on noClickShape but isnt there right now (and still pressed down) it will update position anyway
            #This calculates offset of mouse from center of object (Not needed but looks better in experiment)
            mousePlace = mouse3.getPos()
            if firstDrag == True: #Only updates offset once when starting the drag
                    mousex = mousePlace[0] - place[0] #Gets the difference between the Image place and the mouse place for x
                    mousey = mousePlace[1] - place[1] #Gets the difference between the Image place and the mouse place for y
                    firstDrag = False #Disables first drag
            place = mousePlace[0] - mousex, mousePlace[1] - mousey #Adds this onto the place of the image for more intuitive dragging
            Image3.setPos(place) #Sets position of the image equal to the position of the mouse
            noClickShape.setPos(place) #Set position
    elif didFinishDrag == True and isDragging == True: #Disables didFinishDrag for good
        didFinishDrag = False
    elif isDragging == True: #This is an elif statement so will only play if others above are false
        didFinishDrag = True #Makes var true so it only is true for one frame
        isDragging = False #It is no longer dragging
        win.mouseVisible = True #Show mouse once your done dragging
        firstDrag = True #re-enables first drag again so when the first if statement plays it will update position of offset
    else:
        didFinishDrag = False #Disables didFinishDrag for good
    
    noClickShape.draw() #Draws no click shape
    if didFinishDrag == True: #Only updates position once after you finish dragging, otherwise experiment will lag a lot
        stim.setPos(place)
        stim.draw()
    elif isDragging == False: #If your not dragging it won't redifine the position
        stim.draw()
    
    if mouse3.isPressedIn(screenRect3):#ScreenRect is used to detect if mouse is pressed anywhere on screen
        if mouse3.isPressedIn(stim) and not mouse3.isPressedIn(noClickShape):#Has to be initially pressed on wheel to set to true
            if isDragging == False: #Also cannot be dragging
                hasColored = True #For hiding the selectShape until you start coloring
                isOnColor = True #Then will set is on color to true
    else:
        isOnColor = False #If mouse is not pressed down it is not on color
    #MARK: Detect Mouse Press On Segment
    #Takes the multiplier (How many segments) and multiplies it by rad number
    #Then adds half of the multiplier (to make color average)
    if isDragging == False and isOnColor == True: #If its on a segment it will update the color of the Image3
        if mouse3.isPressedIn(rad0): #Will not set color if dragging Image3
            degrees = (orimult*0)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad1):
            degrees = (orimult*1)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad2):
            degrees = (orimult*2)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad3):
            degrees = (orimult*3)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad4):
            degrees = (orimult*4)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad5):
            degrees = (orimult*5)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad6):
            degrees = (orimult*6)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad7):
            degrees = (orimult*7)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad8):
            degrees = (orimult*8)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad9):
            degrees = (orimult*9)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad10):
            degrees = (orimult*10)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad11):
            degrees = (orimult*11)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad12):
            degrees = (orimult*12)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad13):
            degrees = (orimult*13)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad14):
            degrees = (orimult*14)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad15):
            degrees = (orimult*15)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad16):
            degrees = (orimult*16)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad17):
            degrees = (orimult*17)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad18):
            degrees = (orimult*18)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad19):
            degrees = (orimult*19)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad20):
            degrees = (orimult*20)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad21):
            degrees = (orimult*21)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad22):
            degrees = (orimult*22)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad23):
            degrees = (orimult*23)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad24):
            degrees = (orimult*24)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad25):
            degrees = (orimult*25)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad26):
            degrees = (orimult*26)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad27):
            degrees = (orimult*27)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad28):
            degrees = (orimult*28)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad29):
            degrees = (orimult*29)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad30):
            degrees = (orimult*30)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad31):
            degrees = (orimult*31)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad32):
            degrees = (orimult*32)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad33):
            degrees = (orimult*33)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad34):
            degrees = (orimult*34)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad35):
            degrees = (orimult*35)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad36):
            degrees = (orimult*36)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad37):
            degrees = (orimult*37)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad38):
            degrees = (orimult*38)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad39):
            degrees = (orimult*39)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad40):
            degrees = (orimult*40)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad41):
            degrees = (orimult*41)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad42):
            degrees = (orimult*42)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad43):
            degrees = (orimult*43)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad44):
            degrees = (orimult*44)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad45):
            degrees = (orimult*45)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad46):
            degrees = (orimult*46)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad47):
            degrees = (orimult*47)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad48):
            degrees = (orimult*48)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad49):
            degrees = (orimult*49)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad50):
            degrees = (orimult*50)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad51):
            degrees = (orimult*51)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad52):
            degrees = (orimult*52)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad53):
            degrees = (orimult*53)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad54):
            degrees = (orimult*54)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad55):
            degrees = (orimult*55)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad56):
            degrees = (orimult*56)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad57):
            degrees = (orimult*57)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad58):
            degrees = (orimult*58)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad59):
            degrees = (orimult*59)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad60):
            degrees = (orimult*60)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad61):
            degrees = (orimult*61)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad62):
            degrees = (orimult*62)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad63):
            degrees = (orimult*63)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad64):
            degrees = (orimult*64)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad65):
            degrees = (orimult*65)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad66):
            degrees = (orimult*66)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad67):
            degrees = (orimult*67)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad68):
            degrees = (orimult*68)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad69):
            degrees = (orimult*69)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad70):
            degrees = (orimult*70)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad71):
            degrees = (orimult*71)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad72):
            degrees = (orimult*72)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad73):
            degrees = (orimult*73)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad74):
            degrees = (orimult*74)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad75):
            degrees = (orimult*75)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad76):
            degrees = (orimult*76)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad77):
            degrees = (orimult*77)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad78):
            degrees = (orimult*78)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad79):
            degrees = (orimult*79)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad80):
            degrees = (orimult*80)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad81):
            degrees = (orimult*81)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad82):
            degrees = (orimult*82)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad83):
            degrees = (orimult*83)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad84):
            degrees = (orimult*84)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad85):
            degrees = (orimult*85)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad86):
            degrees = (orimult*86)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad87):
            degrees = (orimult*87)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad88):
            degrees = (orimult*88)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad89):
            degrees = (orimult*89)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad90):
            degrees = (orimult*90)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad91):
            degrees = (orimult*91)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad92):
            degrees = (orimult*92)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad93):
            degrees = (orimult*93)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad94):
            degrees = (orimult*94)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad95):
            degrees = (orimult*95)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad96):
            degrees = (orimult*96)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad97):
            degrees = (orimult*97)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad98):
            degrees = (orimult*98)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
        elif mouse3.isPressedIn(rad99):
            degrees = (orimult*99)+(orimult/2)
            Image3.setColor([degrees,1,1])#sets Image3 hsv color
    
    #MARK: Update Segment Positions And Draw Them
    if didFinishDrag == True: #This is to prevent slowness when picking up ubject to drag
        segpos = (place)#When it appears sets the pos equal to the current place of the object
        #Sets each segment position
        rad0.setPos(segpos)
        rad1.setPos(segpos)
        rad2.setPos(segpos)
        rad3.setPos(segpos)
        rad4.setPos(segpos)
        rad5.setPos(segpos)
        rad6.setPos(segpos)
        rad7.setPos(segpos)
        rad8.setPos(segpos)
        rad9.setPos(segpos)
        rad10.setPos(segpos)
        rad11.setPos(segpos)
        rad12.setPos(segpos)
        rad13.setPos(segpos)
        rad14.setPos(segpos)
        rad15.setPos(segpos)
        rad16.setPos(segpos)
        rad17.setPos(segpos)
        rad18.setPos(segpos)
        rad19.setPos(segpos)
        rad20.setPos(segpos)
        rad21.setPos(segpos)
        rad22.setPos(segpos)
        rad23.setPos(segpos)
        rad24.setPos(segpos)
        rad25.setPos(segpos)
        rad26.setPos(segpos)
        rad27.setPos(segpos)
        rad28.setPos(segpos)
        rad29.setPos(segpos)
        rad30.setPos(segpos)
        rad31.setPos(segpos)
        rad32.setPos(segpos)
        rad33.setPos(segpos)
        rad34.setPos(segpos)
        rad35.setPos(segpos)
        rad36.setPos(segpos)
        rad37.setPos(segpos)
        rad38.setPos(segpos)
        rad39.setPos(segpos)
        rad40.setPos(segpos)
        rad41.setPos(segpos)
        rad42.setPos(segpos)
        rad43.setPos(segpos)
        rad44.setPos(segpos)
        rad45.setPos(segpos)
        rad46.setPos(segpos)
        rad47.setPos(segpos)
        rad48.setPos(segpos)
        rad49.setPos(segpos)
        rad50.setPos(segpos)
        rad51.setPos(segpos)
        rad52.setPos(segpos)
        rad53.setPos(segpos)
        rad54.setPos(segpos)
        rad55.setPos(segpos)
        rad56.setPos(segpos)
        rad57.setPos(segpos)
        rad58.setPos(segpos)
        rad59.setPos(segpos)
        rad60.setPos(segpos)
        rad61.setPos(segpos)
        rad62.setPos(segpos)
        rad63.setPos(segpos)
        rad64.setPos(segpos)
        rad65.setPos(segpos)
        rad66.setPos(segpos)
        rad67.setPos(segpos)
        rad68.setPos(segpos)
        rad69.setPos(segpos)
        rad70.setPos(segpos)
        rad71.setPos(segpos)
        rad72.setPos(segpos)
        rad73.setPos(segpos)
        rad74.setPos(segpos)
        rad75.setPos(segpos)
        rad76.setPos(segpos)
        rad77.setPos(segpos)
        rad78.setPos(segpos)
        rad79.setPos(segpos)
        rad80.setPos(segpos)
        rad81.setPos(segpos)
        rad82.setPos(segpos)
        rad83.setPos(segpos)
        rad84.setPos(segpos)
        rad85.setPos(segpos)
        rad86.setPos(segpos)
        rad87.setPos(segpos)
        rad88.setPos(segpos)
        rad89.setPos(segpos)
        rad90.setPos(segpos)
        rad91.setPos(segpos)
        rad92.setPos(segpos)
        rad93.setPos(segpos)
        rad94.setPos(segpos)
        rad95.setPos(segpos)
        rad96.setPos(segpos)
        rad97.setPos(segpos)
        rad98.setPos(segpos)
        rad99.setPos(segpos)
    elif isDragging == False and isOnColor == True: #When dragging it will dispear
        #Draws each segment
        rad0.draw()
        rad1.draw()
        rad2.draw()
        rad3.draw()
        rad4.draw()
        rad5.draw()
        rad6.draw()
        rad7.draw()
        rad8.draw()
        rad9.draw()
        rad10.draw()
        rad11.draw()
        rad12.draw()
        rad13.draw()
        rad14.draw()
        rad15.draw()
        rad16.draw()
        rad17.draw()
        rad18.draw()
        rad19.draw()
        rad20.draw()
        rad21.draw()
        rad22.draw()
        rad23.draw()
        rad24.draw()
        rad25.draw()
        rad26.draw()
        rad27.draw()
        rad28.draw()
        rad29.draw()
        rad30.draw()
        rad31.draw()
        rad32.draw()
        rad33.draw()
        rad34.draw()
        rad35.draw()
        rad36.draw()
        rad37.draw()
        rad38.draw()
        rad39.draw()
        rad40.draw()
        rad41.draw()
        rad42.draw()
        rad43.draw()
        rad44.draw()
        rad45.draw()
        rad46.draw()
        rad47.draw()
        rad48.draw()
        rad49.draw()
        rad50.draw()
        rad51.draw()
        rad52.draw()
        rad53.draw()
        rad54.draw()
        rad55.draw()
        rad56.draw()
        rad57.draw()
        rad58.draw()
        rad59.draw()
        rad60.draw()
        rad61.draw()
        rad62.draw()
        rad63.draw()
        rad64.draw()
        rad65.draw()
        rad66.draw()
        rad67.draw()
        rad68.draw()
        rad69.draw()
        rad70.draw()
        rad71.draw()
        rad72.draw()
        rad73.draw()
        rad74.draw()
        rad75.draw()
        rad76.draw()
        rad77.draw()
        rad78.draw()
        rad79.draw()
        rad80.draw()
        rad81.draw()
        rad82.draw()
        rad83.draw()
        rad84.draw()
        rad85.draw()
        rad86.draw()
        rad87.draw()
        rad88.draw()
        rad89.draw()
        rad90.draw()
        rad91.draw()
        rad92.draw()
        rad93.draw()
        rad94.draw()
        rad95.draw()
        rad96.draw()
        rad97.draw()
        rad98.draw()
        rad99.draw()
    
    # *screenRect3* updates
    if t >= 0.0 and screenRect3.status == NOT_STARTED:
        # keep track of start time/frame for later
        screenRect3.tStart = t  # not accounting for scr refresh
        screenRect3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(screenRect3, 'tStartRefresh')  # time at next scr refresh
        screenRect3.setAutoDraw(True)
    if isDragging == False and hasColored == True: #Hides until you actually start selecting a color, this is separate from colorHelp in ExitCode so no interference ever occors
        #Explanation: Color is just hsv set to white, position on circle is calculated by, X:= origin of stimuli x position + cos of the angle in radians (cos funtion only takes radians) * the radius (circumference/2) and then subtracting a fourth of the radius of the color picker circle to make it in the middle of the color wheel
        selectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,1,0], pos=(place[0]+(math.cos(math.radians(-degrees+90))*(.15-(0.03/4))), place[1]+(math.sin(math.radians(-degrees+90))*(.15-(0.03/4)))), size=(0.03,0.03), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)
        #Explanation: Same as above except the color is set to the color wheel segment, and to get it centered I devided by 3.4 because for some reason 4 didn't center it correctly, but 3.4 centers it fine so just leaving it like that is ok
        innerSelectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[degrees,1,1], pos=(place[0]+(math.cos(math.radians(-degrees+90))*(.15-(0.025/3.4))), place[1]+(math.sin(math.radians(-degrees+90))*(.15-(0.025/3.4)))), size=(0.025,0.025), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)
        #Draws both shapes
        selectShape.draw()
        innerSelectShape.draw()
    if theseKeys == 'space':  # if space is pressed
        #a response ends the routine
        if hasColored and hasDragged: #Stops routine if they have colored and moved the stimuli
            continueRoutine = False
        elif not hasColored:
            helpColor = True
        elif not hasDragged:
            helpDrag = True
    
    #Help animations
    if helpColor == True and hasColored == False and isDragging == False: #If they need help coloring and they are not currently dragging the image
        helpDrag = False #Disables other option
        if colorOpac < 1.0:
            colorOpac += 0.01 #How fast opacity of slider increases
        if colorDeg < 1 and colorDegUp == True and colorOpac >= 0.75: #The last var is at what opacity to start sliding
            colorDeg += 0.1
        elif colorDeg < colorSpeed and colorDegUp == True and colorOpac >= 0.75:
            colorDeg += 0.1*colorDeg
        elif colorDeg < colorMaxDeg-colorSpeed and colorDegUp == True and colorOpac >= 0.75:
            colorDeg += colorSpeed/10 #Speed devided by 0.1 which is how much it increases by
        elif colorDeg < colorMaxDeg-1 and colorDegUp == True and colorOpac >= 0.75:
            colorDeg += 0.1*((-colorDeg)+colorMaxDeg)
        elif colorDeg < colorMaxDeg and colorDegUp == True and colorOpac >= 0.75:
            colorDegUp = False #Changes direction
        elif colorDeg > colorMaxDeg-colorSpeed and colorDegUp == False: #Starts going back down degrees here
            colorDeg -= 0.1*((-colorDeg)+colorMaxDeg)
        elif colorDeg > colorSpeed and colorDegUp == False:
            colorDeg -= colorSpeed/10
        elif colorDeg > 1 and colorDegUp == False:
            colorDeg -= 0.1*colorDeg
        elif colorDeg > 0 and colorDegUp == False:
            colorDeg -= 0.05
        elif colorOpac >= 0.75:
            colorDegUp = True #Resets the direction so degrees are going back up again
            colorDeg += 0.05
        #Sets postion of select shapes
        selectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,1,0], pos=(place[0]+(math.cos(math.radians(-colorDeg+90))*(.15-(0.03/4))), place[1]+(math.sin(math.radians(-colorDeg+90))*(.15-(0.03/4)))), size=(0.03,0.03), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = colorOpac)
        innerSelectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[colorDeg,1,1], pos=(place[0]+(math.cos(math.radians(-colorDeg+90))*(.15-(0.025/3.4))), place[1]+(math.sin(math.radians(-colorDeg+90))*(.15-(0.025/3.4)))), size=(0.025,0.025), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = colorOpac)
        #Draws each object
        selectShape.draw()
        innerSelectShape.draw()
        #ColorText.draw()
    elif helpDrag == True and hasDragged == False:
        helpColor = False #Disables other option
        #Makes a nice animation
        if opacOfArrows >= 1.0: #changes direction of opacity
            opacUp = False
        elif opacOfArrows <= 0.0:
            opacUp = True
        if opacUp == True:
            opacOfArrows += 0.01 #Changes opacity, change this var to make animation faster or slower
        else:
            opacOfArrows -= 0.01
        #Draws aroows and text
        arrowUp.opacity = opacOfArrows
        arrowDown.opacity = opacOfArrows
        arrowRight.opacity = opacOfArrows
        arrowLeft.opacity = opacOfArrows
        arrowUp.draw()
        arrowDown.draw()
        arrowRight.draw()
        arrowLeft.draw()
        #DragText.draw() #Tells user what to do
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceExampleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceExample"-------
for thisComponent in practiceExampleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Image3.started', Image3.tStartRefresh)
thisExp.addData('Image3.stopped', Image3.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse3.started', mouse3.tStart)
thisExp.addData('mouse3.stopped', mouse3.tStop)
thisExp.nextEntry()
thisExp.addData('screenRect3.started', screenRect3.tStartRefresh)
thisExp.addData('screenRect3.stopped', screenRect3.tStopRefresh)
win.mouseVisible = False #Hide mouse at end
# the Routine "practiceExample" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
