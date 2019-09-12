#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on Fri Aug 30 13:54:46 2019
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
expName = 'PACOCO'  # from the Builder filename that created this script
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
    originPath='/Volumes/bamlab/Experiments/PACO/CO/PACOCO.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
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

# Initialize components for Routine "checkForOverwrite"
checkForOverwriteClock = core.Clock()
import shutil #To delete folders
#To check if files exist already
isData = False
isLive = False
text_6 = visual.TextStim(win=win, name='text_6',
    text='This participant already exists in both the live and data folder.\nWould you like too clear and OVERWRITE all data or CANCEL experiment?\nYou can also CONTINUE to create a new file (ex: data1) in the data folder.\nThis is not recommended as some live functionality may be lost.',
    font='Arial',
    pos=(0, 0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='Overwrite',
    font='Arial',
    pos=(0.15, 0), height=0.05, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='Cancel',
    font='Arial',
    pos=(-0.15, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='Continue Anyway (Not Recommended)',
    font='Arial',
    pos=(0.55, -0.46), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "header"
headerClock = core.Clock()
import random, xlrd #For randomization of stimuli
command = False #For exiting experiment

thisdir = os.path.abspath(os.path.join(os.path.dirname(_thisDir),'.'))

#randomize the seed
random.seed(int(expInfo['participant'])) #Put in subject number

#Version Number (Update this when you make changes to the experiment, it will go in the readme file in each participant's folder, see bottom of begin experiment tab)
versionNumber = '0.1.6'

#number of study items
num_study = 50 #50

#number of OLD OR NEW items they'll be tested on
num_test = 75 #75

#Skip the Old Or New Section
skipOldOrNew = False

#Skip Practice Section
skipPractice = False

#number of total items (stimuli)
num_items = 243



if skipOldOrNew:
    num_oldornew = 0
    num_practoldornew = 0
    numberofpractice = 0
else:
    num_oldornew = num_test
    num_practoldornew = 4
    numberofpractice = 5
if skipPractice:
    num_practstudy = 0
    num_practoldornew = 0
    numberofpractice = 0
else:
    num_practstudy = 2

finalxcords = [] #Blank array is so that later it is possible to put new values into the np stimuli array, like the oldornew status and rt
for i in range(num_test):
    finalxcords.append("N/A")

finalycords = [] #Blank array is so that later it is possible to put new values into the np stimuli array, like the oldornew status and rt
for i in range(num_test):
    finalycords.append("N/A")

place = (0,0)

#MARK: Generate And Randomize Stimulis Filenames
filenameNums = []
filenames = []
filenameNumbers = []
for i in range(num_items-1): #Randomizes cordNums to be used as pickers for the final cords, randomizing with numberofcords makes sure any coordinates the above function generates can be used
    filenameNums.append(i + 1)
random.shuffle(filenameNums) #Randomizes items in cordnums
for i in range(num_test): #Randomizes x and y cords together so they don't get all mixed up
    filenames.append(thisdir + "/Stimuli/" + str(filenameNums[i]) + ".png")
    filenameNumbers.append(str(filenameNums[i]))
#print(filenames)

#MARK: Randomize Rad#s For Color
amountofsegments = 100 #This number is only used for the header and save files but will help if you are trying to change the number of total segments
radNums = []
radColors = []
for i in range(amountofsegments): #There are 100 segments so that is the max randimizing amount
    radNums.append(i)
random.shuffle(radNums) #Randomizes items in radnums
if num_study > amountofsegments and num_study < amountofsegments*2:
    #WARNING: This has not been tested yet, please test when increasing num_study more than the number of segments but less than 2 times the number of segments, if more than 2 times make another if statement!!
    print("Warning: See code in header segment under MARK: Randomize Rad#s For Color")
    radNums2 = []
    for i in range(amountofsegments):
        radNums2.append(i)
    random.shuffle(radNums2) #Randomizes items in radnums
    radNums = radNums + radNums2
elif num_study > amountofsegments:
    print("Error: too many num_studys, see WARNING in above (header) code for more info")
for i in range(num_study):
    radColors.append(radNums[i])
#print(radNums) #For debugging
#print(radColors)

#MARK: Generate Old Or New Status
oldornewStatus = []
for i in range(num_study):
    oldornewStatus.append("Old")
for i in range(num_test-num_study):
    oldornewStatus.append("New")
#print(oldornewStatus)

blankArray = [] #Blank array is so that later it is possible to put new values into the np stimuli array, like the oldornew status and rt
for i in range(num_test):
    blankArray.append("N/A")

blankArray2 = [] #Blank array is so that later it is possible to put new values into the np stimuli array, like the oldornew status and rt
for i in range(num_test):
    blankArray2.append("N/A")

blankArray3 = [] #Blank array is so that later it is possible to put new values into the np stimuli array, like the oldornew status and rt
for i in range(num_test):
    blankArray3.append("N/A")

blankArray4 = [] #Blank array is so that later it is possible to put new values into the np stimuli array, like the oldornew status and rt
for i in range(num_test):
    blankArray4.append("N/A")

blankArray5 = [] #Blank array is so that later it is possible to put new values into the np stimuli array, like the oldornew status and rt
for i in range(num_test):
    blankArray5.append("N/A")

blankArray6 = [] #Blank array is so that later it is possible to put new values into the np stimuli array, like the oldornew status and rt
for i in range(num_test):
    blankArray6.append("N/A")

#MARK: Create Stimuli np.Array With All Other Factors
stimuli = np.array([filenames, finalxcords, finalycords, radColors, oldornewStatus, blankArray, blankArray2, filenameNumbers, blankArray3, blankArray4, blankArray5, blankArray6])
print(stimuli)

#MARK: Randomize Order For Each Task
study_order = []
for i in range(num_study):
    study_order.append(i)
random.shuffle(study_order)

oldornew_order = []
for i in range(num_test):
    oldornew_order.append(i)
random.shuffle(oldornew_order)

test_order = []
for i in range(num_study):
    test_order.append(i)
random.shuffle(test_order)

# Initialize components for Routine "practiceExampleInstr"
practiceExampleInstrClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='In this experiment, you will be presented with different images.\nYour task will be to remember each shape and its color.\n\nTo respond, you will need to use the mouse to choose a color.\n\nPress space to see an example and try it out',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "practiceExample"
practiceExampleClock = core.Clock()
Image3 = visual.ImageStim(
    win=win,
    name='Image3', 
    image=thisdir + '/Stimuli/test6.png', mask=None,
    ori=0, pos=(0, 0), size=(0.19, 0.19),
    color=[1,0,1], colorSpace='hsv', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
mouse3 = event.Mouse(win=win)
x, y = [None, None]
mouse3.mouseClock = core.Clock()
#Looking for code in Begin Experiment?
#All code and var definitions for begin experiment are in the test section
#Looking for code in Begin Experiment?
#All code and var definitions for begin experiment are in the test section
screenRect3 = visual.Rect(
    win=win, name='screenRect3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-6.0, interpolate=True)
#Looking for code in Begin Experiment?
#All code and var definitions for begin experiment are in the test section
#Color text 2 setup, tells user to select a color
ColorText2 = visual.TextStim(win=win, name='ColorText',
    text='                             Select a color from the color wheel\nYou can click or drag the mouse anywhere on the wheel to select a color',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practiceStudyInstr"
practiceStudyInstrClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Lets start with some practice.\n\nYou will now be shown two objects. Memorize their shape and color.\nEach object will stay on the screen for three seconds.\n\nPress Space To Continue',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "reset"
resetClock = core.Clock()
resettext = visual.TextStim(win=win, name='resettext',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "practiceStudy"
practiceStudyClock = core.Clock()
#This array defines the practice stimuli
practiceStim = np.array([[thisdir + "/Stimuli/test7.png", thisdir + "/Stimuli/test3.png", thisdir + "/Stimuli/test4.png", thisdir + "/Stimuli/test5.png"], 
    [-0.64514, .72917], 
    [.012639, .33681], 
    [13, 77]])

#Current trial used to select stimuli
practicestudytrail = 0
practicestudyimage = visual.ImageStim(
    win=win,
    name='practicestudyimage', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.19, 0.19),
    color='white', colorSpace='hsv', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "practiceOldornewInstr"
practiceOldornewInstrClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text="You'll now be shown multiple shapes.\nFor each shape, decide if you have seen the shape during the study, irrespective of its color.\nIf you have seen it during study, press 1 for OLD. If you have not seen it, press 2 for NEW.\n\nPress Space To Start",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "reset"
resetClock = core.Clock()
resettext = visual.TextStim(win=win, name='resettext',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "practiceOldornew"
practiceOldornewClock = core.Clock()
oldornewText2 = visual.TextStim(win=win, name='oldornewText2',
    text='default text',
    font='Arial',
    pos=(0, -.45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
import time
practiceoldornewtrail = 0 #Current trail user is on
practiceOldornewOrder = [3, 1, 2, 0] #order of the practice test, different then study order
oldornewImage2 = visual.ImageStim(
    win=win,
    name='oldornewImage2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.19, 0.19),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "practiceTestInstr"
practiceTestInstrClock = core.Clock()
testText = visual.TextStim(win=win, name='testText',
    text='You will now be tested on the color of the images you studied. \nUse the mouse to select the color of the image.\nDuring this practice, you will be given feedback on how close you are to the correct color\n\nPress Space To Start',
    font='Arial',
    pos=(0, 0), height=0.028, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "reset"
resetClock = core.Clock()
resettext = visual.TextStim(win=win, name='resettext',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "practiceTest"
practiceTestClock = core.Clock()
mouse2 = event.Mouse(win=win)
x, y = [None, None]
mouse2.mouseClock = core.Clock()
#Looking for code in Begin Experiment?
#All code and var definitions for begin experiment are in the test section
#Looking for code in Begin Experiment?
#All code and var definitions for begin experiment are in the test section
screenRect2 = visual.Rect(
    win=win, name='screenRect2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=0, depth=-4.0, interpolate=True)
#Looking for code in Begin Experiment?
#All code and var definitions for begin experiment are in the test section
#Feedback text setup, tells you how close you are
FeedbackText = visual.TextStim(win=win, name='FeedbackText',
    text='',
    font='Arial',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

#This text makes you select the correct color and location
ContinueText = visual.TextStim(win=win, name='ColorText',
    text='',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
practicetesttrail = 0 #Current trail user is on
practiceTestOrder = [0, 1] #order of the practice test, different then study order
practicetestPath = 'None'
Image2 = visual.ImageStim(
    win=win,
    name='Image2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.19, 0.19),
    color=[1,1,1], colorSpace='hsv', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)

# Initialize components for Routine "studyInstr"
studyInstrClock = core.Clock()
studyText = visual.TextStim(win=win, name='studyText',
    text='Now for the actual experiment\nYou will now study a larger number of images. For each image, try to remember the shape and color. \n\n\nPress Space To Start',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "reset"
resetClock = core.Clock()
resettext = visual.TextStim(win=win, name='resettext',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "study"
studyClock = core.Clock()
currentStudy = 0
studyrad = 0 #Requires it to be defined at the beginning for some reason
studyOnset = -1
studyImage = visual.ImageStim(
    win=win,
    name='studyImage', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.19, 0.19),
    color='white', colorSpace='hsv', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "oldornewInstr"
oldornewInstrClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='We will now test you on how well you remember the shapes you just saw.\nJust like in the practice, decide if you have seen each shape during the study, irrespective of its color.\nIf you have seen it during the study, press 1 for OLD. If you have not seen it, press 2 for NEW.\nYou will not be given feedback.\n\nPress Space To Start',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "reset"
resetClock = core.Clock()
resettext = visual.TextStim(win=win, name='resettext',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "oldornew"
oldornewClock = core.Clock()
oldornewText = visual.TextStim(win=win, name='oldornewText',
    text='1 - Old        2 - New',
    font='Arial',
    pos=(0, -.45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
currentOldornew = 0
oldornewrad = 0 #Requires it to be defined at the beginning for some reason

oldornewOnset = -1
oldornewImage = visual.ImageStim(
    win=win,
    name='oldornewImage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.19, 0.19),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
#Each variable for the live is separate from the actual data saving variables and they are all in string form

liveoldornewoldornew = 'N/A'
liveoldornewx = 'N/A'
liveoldornewy = 'N/A'
liveoldornewrad = 'N/A'

liveoldornewrt = 'N/A'
liveuseroldornew = 'N/A'

# Initialize components for Routine "testInstr"
testInstrClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text="You will now be tested on the color of the images you studied. \nUse the mouse to select the color of the image.\nOnce you're done press the spacebar to continue.\n\nYou will NOT be given feedback on how close you are.\n\nPress Space To Start",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "reset"
resetClock = core.Clock()
resettext = visual.TextStim(win=win, name='resettext',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "test"
testClock = core.Clock()
mouse1 = event.Mouse(win=win)
x, y = [None, None]
mouse1.mouseClock = core.Clock()
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
screenRect = visual.Rect(
    win=win, name='screenRect',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.851,1.000,-1.000], fillColorSpace='rgb',
    opacity=0, depth=-4.0, interpolate=True)
import math #Needed for cos and sin
import datetime #For saving raction times

currentTest = 0
testrad = 0 #Requires it to be defined at the beginning for some reason

testOnset = -1

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
#Max degrees and speed for color help
colorMaxDeg = 270 #1 to any real number, must be at least twice as much as speed for smooth animation
colorSpeed = 50 #1 to any real number, do not recomend setting this above 50

#To prevent user from clicking inside the color wheel and selecting a color, noClickShape surrounds entire image, set opacity to one to see for yourself ;)
noClickShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,0,1], pos=(0,0), size=(0.25,0.25), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 0)

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
Image = visual.ImageStim(
    win=win,
    name='Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.19, 0.19),
    color=[1,-1.000,1.000], colorSpace='hsv', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
#Each variable for the live is separate from the actual data saving variables and they are all in string form

livetestPath = 'N/A'
livetestoldornew = 'N/A'
livetestx = 'N/A'
livetesty = 'N/A'
livetestrad = 'N/A'

liveuseroldornew = 'N/A'
liveuserx = 'N/A'
liveusery = 'N/A'
liveuserrad = 'N/A'

liveoldornewrt = 'N/A'
livetestrt = 'N/A'

# Initialize components for Routine "End"
EndClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='            You have finished\nThank you for your participation\n    Please get the experimenter',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "checkForOverwrite"-------
t = 0
checkForOverwriteClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
if os.path.exists(_thisDir + os.sep + u'data/%s/sub_%s_%s_test.csv' % (expInfo['participant'], expInfo['participant'], expName)):
    isData = True #If the data folder exists
    print('isData')
    #Sets text to only say data folder
    text_6.setText('Participant ' + expInfo['participant'] + ' already exists in the data folder.\nWould you like too clear and OVERWRITE all data or CANCEL experiment?\nYou can also CONTINUE to create a new file (ex: data1) in the data folder.\nThis is not recommended as some live functionality may be lost.')
if os.path.exists(_thisDir + os.sep + u'live/'+ expInfo['participant'] + '/live1' + '.csv'):
    isLive = True #If the live folder exists
    print('isLive')
    #Sets text to only say live folder
    text_6.setText('Participant ' + expInfo['participant'] +' already exists in the live folder.\nWould you like too clear and OVERWRITE all data or CANCEL experiment?\nYou can also CONTINUE to create a new file (ex: data1) in the data folder.\nThis is not recommended as some live functionality may be lost.')

if isLive and isData:
    #Sets text to say both data and live folder
    text_6.setText('Participant ' + expInfo['participant'] +' already exists in both the live and data folder.\nWould you like too clear and OVERWRITE all data or CANCEL experiment?\nYou can also CONTINUE to create a new file (ex: data1) in the data folder.\nThis is not recommended as some live functionality may be lost.')
elif not isLive and not isData:
    #If the participant # is new, move on without giving a prompt
    continueRoutine = False
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
checkForOverwriteComponents = [text_6, text_7, text_8, text_9, mouse]
for thisComponent in checkForOverwriteComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "checkForOverwrite"-------
while continueRoutine:
    # get current time
    t = checkForOverwriteClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if mouse.isPressedIn(text_7):
        #Delete all data from folders
        shutil.rmtree(_thisDir + os.sep + u'data/%s' % (expInfo['participant']), ignore_errors=True)
        shutil.rmtree(_thisDir + os.sep + u'live/%s' % (expInfo['participant']), ignore_errors=True)
        continueRoutine = False #Move on to the next routine
    elif mouse.isPressedIn(text_8):
        core.quit() #If the user clicks cancel, quit the experiment
    elif mouse.isPressedIn(text_9):
        continueRoutine = False #If the user clicks continue anyway, go onto the next routine without doing anything else
    
    keys = event.getKeys()
    for key in keys:
        if 'command' in key:
            command = True
        if 'esc' in key and command:
            core.quit()
    
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
    
    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t  # not accounting for scr refresh
        text_8.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *text_9* updates
    if t >= 0.0 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t  # not accounting for scr refresh
        text_9.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in checkForOverwriteComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "checkForOverwrite"-------
for thisComponent in checkForOverwriteComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
# the Routine "checkForOverwrite" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "header"-------
t = 0
headerClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
win.mouseVisible = False #Hide mouse

#Save data files in begin routine so that if the participant already exists and the user clicks cancel, it won't save any data
if not skipOldOrNew:
    #Save Old or New data file
    filename4 = _thisDir + os.sep + u'data/%s/sub_%s_%s_OldOrNew' % (expInfo['participant'], expInfo['participant'], expName)
    thisExp4 = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath= thisdir + '/LOCO/PACOLOCO.py',
        savePickle=False, saveWideText=True,
        dataFileName=filename4)

#Save Normal Data File
filename2 = _thisDir + os.sep + u'data/%s/sub_%s_%s_test' % (expInfo['participant'], expInfo['participant'], expName)
thisExp2 = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath= thisdir + '/LOCO/PACOLOCO.py',
    savePickle=False, saveWideText=True,
    dataFileName=filename2)

#Save Live Update File
liveFileName = _thisDir + os.sep + u'live/%s/live' % (expInfo['participant'])
liveNum = 1

#Save Abort Data File, these kind of saves with 'thisExp' in them save no matter what when you quit the program
thisExp3 = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath= thisdir + '/LOCO/PACOLOCO.py',
    savePickle=False, saveWideText=True,
    dataFileName=liveFileName + 'live')

#Create readme
rmFile = open(_thisDir + os.sep + u'data/%s/README.txt' % (expInfo['participant']), 'w')
rmFile.write('VERSION ' + versionNumber + '\n\nIf this experiment was fully and successfully completed by the participant, you only need you use the test data file, it contains all the data you need.\nIf something went wrong during the experiment, or it was aborted before it was finished, you can use the oldornew data file to recover the user\'s responses for each old or new trail.' + 
    '\nThe columns for the test data file are ordered by the order that they are presented at test (Only the old stimuli), and then are ordered by the order they were presented at Old Or New (Only new stimuli).' + 
    '\n\nHow to use data in the test file:\nThe stimuli name corresponds to each stimuli in the stimuli folder (located in the main LOCO folder).\nUse the test order, oldorneworder, and study order to sort each data row. To do this, create an empty array and use a for loop to append the lowest to highest number of the order column, starting at 0.' + 
    '\nUser vs Correct is self explanatory, with old or new being added as N/A if it was skipped in the header file.\nColor is out of 360, and rad# is out of 100 (most usefull because there are only 100 possible color options).' + 
    '\nAproxColor is usefull for seeing if the participant was in the correct range, use it only for if one of the users color is in the correct colors, they are in range, and if not, they are out of range. Don\'t use this for any more accuracy than what was previously described. It is calculated by the maximum possible color that could possibly be in each category, and is subject to some human error.' + 
    '\nradColorDist is calculated by the distance off they are from the correct color out of the 100 possible options (50 is the max number this can be).\nOldOrNew rt and Test rt are reaction times of the user.' + 
    '\nStart times are the start times of each trail, with hour, minute, second.\nOnset time counts the amount of seconds when each stimuli was shown since the first reset (Fixation Cross) of that section (for example, the beginning of study) came on the screen\nDate is the date and time that the experiment started, and is not updated every trail.\nPsychopy running version should be at least 3.1.5.\n\nThanks for reading! Have any more questions? Contact me at ipoogleduck@gmail.com')
rmFile.close()
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

# ------Prepare to start Routine "practiceExampleInstr"-------
t = 0
practiceExampleInstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
if skipPractice:
    continueRoutine = False
key_resp = keyboard.Keyboard()
if not skipPractice:
    currentTime = datetime.datetime.now()
    liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
    liveFile.write('Practice,Instruction,1,1,1,' + str(numberofpractice+8) + ',' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second) + ',' + str(num_study) + ',' + str(num_test) + ',' + str(skipOldOrNew))
    liveFile.close()
    liveNum += 1
# keep track of which components have finished
practiceExampleInstrComponents = [text_2, key_resp]
for thisComponent in practiceExampleInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "practiceExampleInstr"-------
while continueRoutine:
    # get current time
    t = practiceExampleInstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # not accounting for scr refresh
        text_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp* updates
    if t >= 0.0 and key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp.tStart = t  # not accounting for scr refresh
        key_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        key_resp.clearEvents(eventType='keyboard')
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    for key in keys:
        if 'command' in key:
            command = True
        if 'esc' in key and command:
            liveliveFile = open(liveFileName+'live.csv', 'w')
            liveliveFile.write('Abort,Abort,1,1,1,1,')
            liveliveFile.close()
            core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceExampleInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceExampleInstr"-------
for thisComponent in practiceExampleInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "practiceExampleInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceExample"-------
t = 0
practiceExampleClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
if skipPractice:
    continueRoutine = False
# setup some python lists for storing info about the mouse3
gotValidClick = False  # until a click is received
key_resp_9 = keyboard.Keyboard()
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
mouse2.setPos(newPos=(0, 0.001)) #resets position of mouse, has to be offset slightly or else it will select a color for some reason

#These two vars give the person help with knowing how to drag/color live
helpColor = False

colorDeg = 0 #Degrees of slider for colorHelp
colorDegUp = True #Degrees of the slider going up or down
colorOpac = 0 #Opacity of the slider
if not skipPractice:
    currentTime = datetime.datetime.now()
    liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
    liveFile.write('Practice,Example,1,1,2,' + str(numberofpractice + 8) + ',' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second))
    liveFile.close()
    liveNum += 1
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
    stim.draw()
    
    if mouse3.isPressedIn(screenRect3):#ScreenRect is used to detect if mouse is pressed anywhere on screen
        if mouse3.isPressedIn(stim) and not mouse3.isPressedIn(noClickShape):#Has to be initially pressed on wheel to set to true
            hasColored = True #For hiding the selectShape until you start coloring
            isOnColor = True #Then will set is on color to true
    else:
        isOnColor = False #If mouse is not pressed down it is not on color
    #MARK: Detect Mouse Press On Segment
    #Takes the multiplier (How many segments) and multiplies it by rad number
    #Then adds half of the multiplier (to make color average)
    if isOnColor: #If its on a segment it will update the color of the Image3
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
    if hasColored == True: #Hides until you actually start selecting a color, this is separate from colorHelp in ExitCode so no interference ever occors
        #Explanation: Color is just hsv set to white, position on circle is calculated by, X:= origin of stimuli x position + cos of the angle in radians (cos funtion only takes radians) * the radius (circumference/2) and then subtracting a fourth of the radius of the color picker circle to make it in the middle of the color wheel
        selectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,0,1], pos=(place[0]+(math.cos(math.radians(-degrees+90))*(.15-(0.03/4))), place[1]+(math.sin(math.radians(-degrees+90))*(.15-(0.03/4)))), size=(0.03,0.03), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)
        #Explanation: Same as above except the color is set to the color wheel segment, and to get it centered I devided by 3.4 because for some reason 4 didn't center it correctly, but 3.4 centers it fine so just leaving it like that is ok
        innerSelectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[degrees,1,1], pos=(place[0]+(math.cos(math.radians(-degrees+90))*(.15-(0.025/3.4))), place[1]+(math.sin(math.radians(-degrees+90))*(.15-(0.025/3.4)))), size=(0.025,0.025), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)
        #Draws both shapes
        selectShape.draw()
        innerSelectShape.draw()
    if not hasColored:
        helpColor = True #This shows the popup to tell user to color right when they start the routine
    elif not isOnColor: #Tells user they can continue once they've colored and placed, re-uses colortext2 text
        ColorText2.setText('Great! Whenever you\'re ready to continue, click the spacebar')
        ColorText2.draw()
    
    if theseKeys == 'space':  # if space is pressed
        #a response ends the routine
        if hasColored: #Stops routine if they have colored and moved the stimuli
            continueRoutine = False
    
    #Help animations
    if helpColor == True and hasColored == False : #If they need help coloring and they are not currently dragging the image
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
        selectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,0,1], pos=(place[0]+(math.cos(math.radians(-colorDeg+90))*(.15-(0.03/4))), place[1]+(math.sin(math.radians(-colorDeg+90))*(.15-(0.03/4)))), size=(0.03,0.03), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = colorOpac)
        innerSelectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[colorDeg,1,1], pos=(place[0]+(math.cos(math.radians(-colorDeg+90))*(.15-(0.025/3.4))), place[1]+(math.sin(math.radians(-colorDeg+90))*(.15-(0.025/3.4)))), size=(0.025,0.025), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = colorOpac)
        #Draws each object
        selectShape.draw()
        innerSelectShape.draw()
        ColorText2.draw()
    keys = event.getKeys()
    for key in keys:
        if 'command' in key:
            command = True
        if 'esc' in key and command:
            liveliveFile = open(liveFileName+'live.csv', 'w')
            liveliveFile.write('Abort,Abort,1,1,1,1,')
            liveliveFile.close()
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

# ------Prepare to start Routine "practiceStudyInstr"-------
t = 0
practiceStudyInstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
if skipPractice:
    continueRoutine = False
key_resp_7 = keyboard.Keyboard()
if not skipPractice:
    currentTime = datetime.datetime.now()
    liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
    liveFile.write('Practice,Instruction,1,1,3,' + str(numberofpractice + 8) + ',' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second))
    liveFile.close()
    liveNum += 1
# keep track of which components have finished
practiceStudyInstrComponents = [text_5, key_resp_7]
for thisComponent in practiceStudyInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "practiceStudyInstr"-------
while continueRoutine:
    # get current time
    t = practiceStudyInstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # not accounting for scr refresh
        text_5.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # not accounting for scr refresh
        key_resp_7.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        key_resp_7.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    for key in keys:
        if 'command' in key:
            command = True
        if 'esc' in key and command:
            liveliveFile = open(liveFileName+'live.csv', 'w')
            liveliveFile.write('Abort,Abort,1,1,1,1,')
            liveliveFile.close()
            core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceStudyInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceStudyInstr"-------
for thisComponent in practiceStudyInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# the Routine "practiceStudyInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practicestudys = data.TrialHandler(nReps=num_practstudy, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practicestudys')
thisExp.addLoop(practicestudys)  # add the loop to the experiment
thisPracticestudy = practicestudys.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticestudy.rgb)
if thisPracticestudy != None:
    for paramName in thisPracticestudy:
        exec('{} = thisPracticestudy[paramName]'.format(paramName))

for thisPracticestudy in practicestudys:
    currentLoop = practicestudys
    # abbreviate parameter names if possible (e.g. rgb = thisPracticestudy.rgb)
    if thisPracticestudy != None:
        for paramName in thisPracticestudy:
            exec('{} = thisPracticestudy[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "reset"-------
    t = 0
    resetClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if studyOnset == 0:
        studyOnset = datetime.datetime.now()
    
    if oldornewOnset == 0:
        oldornewOnset = datetime.datetime.now()
    
    if testOnset == 0:
        testOnset = datetime.datetime.now()
    # keep track of which components have finished
    resetComponents = [resettext]
    for thisComponent in resetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "reset"-------
    while continueRoutine and routineTimer.getTime() > 0:
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
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resettext.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            resettext.tStop = t  # not accounting for scr refresh
            resettext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(resettext, 'tStopRefresh')  # time at next scr refresh
            resettext.setAutoDraw(False)
        keys = event.getKeys()
        for key in keys:
            if 'command' in key:
                command = True
            if 'esc' in key and command:
                liveliveFile = open(liveFileName+'live.csv', 'w')
                liveliveFile.write('Abort,Abort,1,1,1,1,')
                liveliveFile.close()
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
    practicestudys.addData('resettext.started', resettext.tStartRefresh)
    practicestudys.addData('resettext.stopped', resettext.tStopRefresh)
    
    # ------Prepare to start Routine "practiceStudy"-------
    t = 0
    practiceStudyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    practicestudyPath = practiceStim[0][practicestudytrail] #Gets path of the study image
    practicestudyx = practiceStim[1][practicestudytrail] #Gets x cord of the study image
    practicestudyy = practiceStim[2][practicestudytrail] #Gets y cord of the study image
    practicestudyrad = practiceStim[3][practicestudytrail] #Gets color of the study image
    practicestudyimage.setColor([(float(practicestudyrad)*orimult)+(orimult/2),1,1], colorSpace='hsv')
    practicestudyimage.setPos((0,0))
    practicestudyimage.setImage(practicestudyPath)
    currentTime = datetime.datetime.now()
    liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
    liveFile.write('Practice,Study,' + str(practicestudytrail+1) + ',2,' + str(practicestudytrail+4) + ',' + str(numberofpractice + 8) + ',' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second))
    liveFile.close()
    liveNum += 1
    # keep track of which components have finished
    practiceStudyComponents = [practicestudyimage]
    for thisComponent in practiceStudyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practiceStudy"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceStudyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practicestudyimage* updates
        if t >= 0.0 and practicestudyimage.status == NOT_STARTED:
            # keep track of start time/frame for later
            practicestudyimage.tStart = t  # not accounting for scr refresh
            practicestudyimage.frameNStart = frameN  # exact frame index
            win.timeOnFlip(practicestudyimage, 'tStartRefresh')  # time at next scr refresh
            practicestudyimage.setAutoDraw(True)
        frameRemains = 0.0 + 3.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if practicestudyimage.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            practicestudyimage.tStop = t  # not accounting for scr refresh
            practicestudyimage.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practicestudyimage, 'tStopRefresh')  # time at next scr refresh
            practicestudyimage.setAutoDraw(False)
        keys = event.getKeys()
        for key in keys:
            if 'command' in key:
                command = True
            if 'esc' in key and command:
                liveliveFile = open(liveFileName+'live.csv', 'w')
                liveliveFile.write('Abort,Abort,1,1,1,1,')
                liveliveFile.close()
                core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceStudyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceStudy"-------
    for thisComponent in practiceStudyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practicestudytrail += 1 #Next trail
    practicestudys.addData('practicestudyimage.started', practicestudyimage.tStartRefresh)
    practicestudys.addData('practicestudyimage.stopped', practicestudyimage.tStopRefresh)
    thisExp.nextEntry()
    
# completed num_practstudy repeats of 'practicestudys'


# ------Prepare to start Routine "practiceOldornewInstr"-------
t = 0
practiceOldornewInstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
if skipOldOrNew or skipPractice:
    continueRoutine = False
key_resp_10 = keyboard.Keyboard()
if not skipPractice and not skipOldOrNew:
    currentTime = datetime.datetime.now()
    liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
    liveFile.write('Practice,Instruction,1,1,6,' + str(numberofpractice + 8) + ',' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second))
    liveFile.close()
    liveNum += 1
# keep track of which components have finished
practiceOldornewInstrComponents = [key_resp_10, text_10]
for thisComponent in practiceOldornewInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "practiceOldornewInstr"-------
while continueRoutine:
    # get current time
    t = practiceOldornewInstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t  # not accounting for scr refresh
        key_resp_10.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        key_resp_10.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    for key in keys:
        if 'command' in key:
            command = True
        if 'esc' in key and command:
            liveliveFile = open(liveFileName+'live.csv', 'w')
            liveliveFile.write('Abort,Abort,1,1,1,1,')
            liveliveFile.close()
            core.quit()
    
    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t  # not accounting for scr refresh
        text_10.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceOldornewInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceOldornewInstr"-------
for thisComponent in practiceOldornewInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# the Routine "practiceOldornewInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceoldornews = data.TrialHandler(nReps=num_practoldornew, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practiceoldornews')
thisExp.addLoop(practiceoldornews)  # add the loop to the experiment
thisPracticeoldornew = practiceoldornews.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeoldornew.rgb)
if thisPracticeoldornew != None:
    for paramName in thisPracticeoldornew:
        exec('{} = thisPracticeoldornew[paramName]'.format(paramName))

for thisPracticeoldornew in practiceoldornews:
    currentLoop = practiceoldornews
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeoldornew.rgb)
    if thisPracticeoldornew != None:
        for paramName in thisPracticeoldornew:
            exec('{} = thisPracticeoldornew[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "reset"-------
    t = 0
    resetClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if studyOnset == 0:
        studyOnset = datetime.datetime.now()
    
    if oldornewOnset == 0:
        oldornewOnset = datetime.datetime.now()
    
    if testOnset == 0:
        testOnset = datetime.datetime.now()
    # keep track of which components have finished
    resetComponents = [resettext]
    for thisComponent in resetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "reset"-------
    while continueRoutine and routineTimer.getTime() > 0:
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
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resettext.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            resettext.tStop = t  # not accounting for scr refresh
            resettext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(resettext, 'tStopRefresh')  # time at next scr refresh
            resettext.setAutoDraw(False)
        keys = event.getKeys()
        for key in keys:
            if 'command' in key:
                command = True
            if 'esc' in key and command:
                liveliveFile = open(liveFileName+'live.csv', 'w')
                liveliveFile.write('Abort,Abort,1,1,1,1,')
                liveliveFile.close()
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
    practiceoldornews.addData('resettext.started', resettext.tStartRefresh)
    practiceoldornews.addData('resettext.stopped', resettext.tStopRefresh)
    
    # ------Prepare to start Routine "practiceOldornew"-------
    t = 0
    practiceOldornewClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    oldornewText2.setText('1 - Old        2 - New')
    theseKeys = '' #Gets key press
    win.mouseVisible = False #Hide mouse
    ttime = 1 #Lets user respond immediatly
    
    practiceoldornewPath = ''
    
    practiceoldornewPath = practiceStim[0][practiceOldornewOrder[practiceoldornewtrail]] #Gets path of the study image
    
    ttime = 1
    oldornewImage2.setImage(practiceoldornewPath)
    currentTime = datetime.datetime.now()
    liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
    liveFile.write('Practice,Old/New,' + str(practiceoldornewtrail+1) + ',4,' + str(practiceoldornewtrail+7) +',' + str(numberofpractice + 8) +',' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second))
    liveFile.close()
    liveNum += 1
    # keep track of which components have finished
    practiceOldornewComponents = [oldornewText2, oldornewImage2]
    for thisComponent in practiceOldornewComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practiceOldornew"-------
    while continueRoutine:
        # get current time
        t = practiceOldornewClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *oldornewText2* updates
        if t >= 0 and oldornewText2.status == NOT_STARTED:
            # keep track of start time/frame for later
            oldornewText2.tStart = t  # not accounting for scr refresh
            oldornewText2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(oldornewText2, 'tStartRefresh')  # time at next scr refresh
            oldornewText2.setAutoDraw(True)
        keys = event.getKeys()
        for key in keys:
            if key == '1' and ttime >= 1: #if user selected old
                if practiceOldornewOrder[practiceoldornewtrail] == 0 or practiceOldornewOrder[practiceoldornewtrail] == 1:
                    continueRoutine = False #If they are correct, go on to next routine
                else:
                    oldornewText2.setText('Wrong, the image is new') #If they are not correct, tell them they are wrong
                    #win.flip() #Updates screen
                    #time.sleep(1) #Waits for one second
                    ttime = 0
            elif key == '2' and ttime >= 1: #If user selected new
                if practiceOldornewOrder[practiceoldornewtrail] == 2 or practiceOldornewOrder[practiceoldornewtrail] == 3:
                    continueRoutine = False #If they are correct, go on to next routine
                else:
                    oldornewText2.setText('Wrong, the image is old') #If they are not correct, tell them they are wrong
                    #win.flip() #Updates screen
                    #time.sleep(1) #Waits for one second
                    ttime = 0
        
        if ttime >= 1:
            oldornewText2.setText('1 - Old        2 - New') #Re-displays old text
        else:
            ttime += 0.01
        
        # *oldornewImage2* updates
        if t >= 0.0 and oldornewImage2.status == NOT_STARTED:
            # keep track of start time/frame for later
            oldornewImage2.tStart = t  # not accounting for scr refresh
            oldornewImage2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(oldornewImage2, 'tStartRefresh')  # time at next scr refresh
            oldornewImage2.setAutoDraw(True)
        for key in keys:
            if 'command' in key:
                command = True
            if 'esc' in key and command:
                liveliveFile = open(liveFileName+'live.csv', 'w')
                liveliveFile.write('Abort,Abort,1,1,1,1,')
                liveliveFile.close()
                core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceOldornewComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceOldornew"-------
    for thisComponent in practiceOldornewComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceoldornews.addData('oldornewText2.started', oldornewText2.tStartRefresh)
    practiceoldornews.addData('oldornewText2.stopped', oldornewText2.tStopRefresh)
    practiceoldornewtrail += 1
    practiceoldornews.addData('oldornewImage2.started', oldornewImage2.tStartRefresh)
    practiceoldornews.addData('oldornewImage2.stopped', oldornewImage2.tStopRefresh)
    # the Routine "practiceOldornew" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed num_practoldornew repeats of 'practiceoldornews'


# ------Prepare to start Routine "practiceTestInstr"-------
t = 0
practiceTestInstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
if skipPractice:
    continueRoutine = False
key_resp_4 = keyboard.Keyboard()
if not skipPractice:
    currentTime = datetime.datetime.now()
    liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
    liveFile.write('Practice,Instruction,1,1,' + str(numberofpractice + 6) + ',' + str(numberofpractice + 8) + ',' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second))
    liveFile.close()
    liveNum += 1
# keep track of which components have finished
practiceTestInstrComponents = [key_resp_4, testText]
for thisComponent in practiceTestInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "practiceTestInstr"-------
while continueRoutine:
    # get current time
    t = practiceTestInstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_4* updates
    if t >= 0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # not accounting for scr refresh
        key_resp_4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *testText* updates
    if t >= 0 and testText.status == NOT_STARTED:
        # keep track of start time/frame for later
        testText.tStart = t  # not accounting for scr refresh
        testText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(testText, 'tStartRefresh')  # time at next scr refresh
        testText.setAutoDraw(True)
    keys = event.getKeys()
    for key in keys:
        if 'command' in key:
            command = True
        if 'esc' in key and command:
            liveliveFile = open(liveFileName+'live.csv', 'w')
            liveliveFile.write('Abort,Abort,1,1,1,1,')
            liveliveFile.close()
            core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceTestInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceTestInstr"-------
for thisComponent in practiceTestInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('testText.started', testText.tStartRefresh)
thisExp.addData('testText.stopped', testText.tStopRefresh)
# the Routine "practiceTestInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceTests = data.TrialHandler(nReps=num_practstudy, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practiceTests')
thisExp.addLoop(practiceTests)  # add the loop to the experiment
thisPracticeTest = practiceTests.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeTest.rgb)
if thisPracticeTest != None:
    for paramName in thisPracticeTest:
        exec('{} = thisPracticeTest[paramName]'.format(paramName))

for thisPracticeTest in practiceTests:
    currentLoop = practiceTests
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTest.rgb)
    if thisPracticeTest != None:
        for paramName in thisPracticeTest:
            exec('{} = thisPracticeTest[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "reset"-------
    t = 0
    resetClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if studyOnset == 0:
        studyOnset = datetime.datetime.now()
    
    if oldornewOnset == 0:
        oldornewOnset = datetime.datetime.now()
    
    if testOnset == 0:
        testOnset = datetime.datetime.now()
    # keep track of which components have finished
    resetComponents = [resettext]
    for thisComponent in resetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "reset"-------
    while continueRoutine and routineTimer.getTime() > 0:
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
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resettext.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            resettext.tStop = t  # not accounting for scr refresh
            resettext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(resettext, 'tStopRefresh')  # time at next scr refresh
            resettext.setAutoDraw(False)
        keys = event.getKeys()
        for key in keys:
            if 'command' in key:
                command = True
            if 'esc' in key and command:
                liveliveFile = open(liveFileName+'live.csv', 'w')
                liveliveFile.write('Abort,Abort,1,1,1,1,')
                liveliveFile.close()
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
    practiceTests.addData('resettext.started', resettext.tStartRefresh)
    practiceTests.addData('resettext.stopped', resettext.tStopRefresh)
    
    # ------Prepare to start Routine "practiceTest"-------
    t = 0
    practiceTestClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse2
    gotValidClick = False  # until a click is received
    key_resp_8 = keyboard.Keyboard()
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
    then = datetime.datetime.now() #Saves time they begun the section
    colorText = ''
    posText = ''
    degrees = 0 #Resests degrees so that if it saves with an exit the degrees will be 0 and not some random number
    Image2.setColor([0,0,1])#sets Image hsv color
    FeedbackText.setText('')
    ContinueText.setText('')
    colorIsCorrect = False #If they are on the correct color
    mouse2.setPos(newPos=(0, 0.001)) #resets position of mouse, has to be offset slightly or else it will select a color for some reason
    win.mouseVisible = True #Show mouse only if it is supposed to continue routine
    
    #These two vars give the person help with knowing how to drag/color live
    helpColor = False
    
    opacOfArrows = 0.0 #Opacity of the arrows
    opacUp = True #If Opacity is rising or falling
    
    colorDeg = 0 #Degrees of slider for colorHelp
    colorDegUp = True #Degrees of the slider going up or down
    colorOpac = 0 #Opacity of the slider
    
    practicetestPath = practiceStim[0][practiceTestOrder[practicetesttrail]] #Gets path of the study image
    practicetestx = practiceStim[1][practiceTestOrder[practicetesttrail]] #Gets x cord of the study image
    practicetesty = practiceStim[2][practiceTestOrder[practicetesttrail]] #Gets y cord of the study image
    practicetestrad = practiceStim[3][practiceTestOrder[practicetesttrail]] #Gets color of the study image
    Image2.setImage(practicetestPath)
    currentTime = datetime.datetime.now()
    liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
    liveFile.write('Practice,Test,' + str(practicetesttrail+1) + ',2,' + str(numberofpractice + practicetesttrail + 7) +',' + str(numberofpractice + 8) +',' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second))
    liveFile.close()
    liveNum += 1
    # keep track of which components have finished
    practiceTestComponents = [mouse2, key_resp_8, screenRect2, Image2]
    for thisComponent in practiceTestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practiceTest"-------
    while continueRoutine:
        # get current time
        t = practiceTestClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_8* updates
        if t >= 0.0 and key_resp_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_8.tStart = t  # not accounting for scr refresh
            key_resp_8.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            key_resp_8.clearEvents(eventType='keyboard')
        if key_resp_8.status == STARTED:
            theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
        stim.draw()
        
        if mouse2.isPressedIn(screenRect2):#ScreenRect is used to detect if mouse is pressed anywhere on screen
            if mouse2.isPressedIn(stim) and not mouse2.isPressedIn(noClickShape):#Has to be initially pressed on wheel to set to true
                    hasColored = True #For hiding the selectShape until you start coloring
                    isOnColor = True #Then will set is on color to true
        else:
            isOnColor = False #If mouse is not pressed down it is not on color
        #MARK: Detect Mouse Press On Segment
        #Takes the multiplier (How many segments) and multiplies it by rad number
        #Then adds half of the multiplier (to make color average)
        if isOnColor == True: #If its on a segment it will update the color of the Image2
            if mouse2.isPressedIn(rad0): #Will not set color if dragging Image2
                degrees = (orimult*0)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad1):
                degrees = (orimult*1)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad2):
                degrees = (orimult*2)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad3):
                degrees = (orimult*3)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad4):
                degrees = (orimult*4)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad5):
                degrees = (orimult*5)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad6):
                degrees = (orimult*6)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad7):
                degrees = (orimult*7)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad8):
                degrees = (orimult*8)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad9):
                degrees = (orimult*9)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad10):
                degrees = (orimult*10)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad11):
                degrees = (orimult*11)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad12):
                degrees = (orimult*12)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad13):
                degrees = (orimult*13)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad14):
                degrees = (orimult*14)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad15):
                degrees = (orimult*15)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad16):
                degrees = (orimult*16)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad17):
                degrees = (orimult*17)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad18):
                degrees = (orimult*18)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad19):
                degrees = (orimult*19)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad20):
                degrees = (orimult*20)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad21):
                degrees = (orimult*21)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad22):
                degrees = (orimult*22)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad23):
                degrees = (orimult*23)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad24):
                degrees = (orimult*24)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad25):
                degrees = (orimult*25)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad26):
                degrees = (orimult*26)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad27):
                degrees = (orimult*27)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad28):
                degrees = (orimult*28)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad29):
                degrees = (orimult*29)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad30):
                degrees = (orimult*30)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad31):
                degrees = (orimult*31)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad32):
                degrees = (orimult*32)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad33):
                degrees = (orimult*33)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad34):
                degrees = (orimult*34)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad35):
                degrees = (orimult*35)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad36):
                degrees = (orimult*36)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad37):
                degrees = (orimult*37)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad38):
                degrees = (orimult*38)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad39):
                degrees = (orimult*39)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad40):
                degrees = (orimult*40)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad41):
                degrees = (orimult*41)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad42):
                degrees = (orimult*42)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad43):
                degrees = (orimult*43)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad44):
                degrees = (orimult*44)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad45):
                degrees = (orimult*45)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad46):
                degrees = (orimult*46)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad47):
                degrees = (orimult*47)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad48):
                degrees = (orimult*48)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad49):
                degrees = (orimult*49)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad50):
                degrees = (orimult*50)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad51):
                degrees = (orimult*51)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad52):
                degrees = (orimult*52)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad53):
                degrees = (orimult*53)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad54):
                degrees = (orimult*54)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad55):
                degrees = (orimult*55)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad56):
                degrees = (orimult*56)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad57):
                degrees = (orimult*57)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad58):
                degrees = (orimult*58)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad59):
                degrees = (orimult*59)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad60):
                degrees = (orimult*60)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad61):
                degrees = (orimult*61)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad62):
                degrees = (orimult*62)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad63):
                degrees = (orimult*63)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad64):
                degrees = (orimult*64)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad65):
                degrees = (orimult*65)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad66):
                degrees = (orimult*66)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad67):
                degrees = (orimult*67)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad68):
                degrees = (orimult*68)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad69):
                degrees = (orimult*69)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad70):
                degrees = (orimult*70)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad71):
                degrees = (orimult*71)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad72):
                degrees = (orimult*72)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad73):
                degrees = (orimult*73)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad74):
                degrees = (orimult*74)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad75):
                degrees = (orimult*75)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad76):
                degrees = (orimult*76)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad77):
                degrees = (orimult*77)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad78):
                degrees = (orimult*78)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad79):
                degrees = (orimult*79)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad80):
                degrees = (orimult*80)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad81):
                degrees = (orimult*81)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad82):
                degrees = (orimult*82)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad83):
                degrees = (orimult*83)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad84):
                degrees = (orimult*84)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad85):
                degrees = (orimult*85)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad86):
                degrees = (orimult*86)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad87):
                degrees = (orimult*87)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad88):
                degrees = (orimult*88)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad89):
                degrees = (orimult*89)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad90):
                degrees = (orimult*90)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad91):
                degrees = (orimult*91)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad92):
                degrees = (orimult*92)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad93):
                degrees = (orimult*93)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad94):
                degrees = (orimult*94)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad95):
                degrees = (orimult*95)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad96):
                degrees = (orimult*96)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad97):
                degrees = (orimult*97)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad98):
                degrees = (orimult*98)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
            elif mouse2.isPressedIn(rad99):
                degrees = (orimult*99)+(orimult/2)
                Image2.setColor([degrees,1,1])#sets Image2 hsv color
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
        
        # *screenRect2* updates
        if t >= 0.0 and screenRect2.status == NOT_STARTED:
            # keep track of start time/frame for later
            screenRect2.tStart = t  # not accounting for scr refresh
            screenRect2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(screenRect2, 'tStartRefresh')  # time at next scr refresh
            screenRect2.setAutoDraw(True)
        if hasColored == True: #Hides until you actually start selecting a color, this is separate from colorHelp in ExitCode so no interference ever occors
            #Explanation: Color is just hsv set to white, position on circle is calculated by, X:= origin of stimuli x position + cos of the angle in radians (cos funtion only takes radians) * the radius (circumference/2) and then subtracting a fourth of the radius of the color picker circle to make it in the middle of the color wheel
            selectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,0,1], pos=(place[0]+(math.cos(math.radians(-degrees+90))*(.15-(0.03/4))), place[1]+(math.sin(math.radians(-degrees+90))*(.15-(0.03/4)))), size=(0.03,0.03), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)
            #Explanation: Same as above except the color is set to the color wheel segment, and to get it centered I devided by 3.4 because for some reason 4 didn't center it correctly, but 3.4 centers it fine so just leaving it like that is ok
            innerSelectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[degrees,1,1], pos=(place[0]+(math.cos(math.radians(-degrees+90))*(.15-(0.025/3.4))), place[1]+(math.sin(math.radians(-degrees+90))*(.15-(0.025/3.4)))), size=(0.025,0.025), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)
            #Draws both shapes
            selectShape.draw()
            innerSelectShape.draw()
        if isOnColor: #When you are in the prosses of selecting a color
            #Updates text with how close you are to the correct color
            colorIsCorrect = False #resets color is correct bool
            segNum = (degrees-(orimult/2))/orimult #Changes degrees back into rad #s
            segNum = round(segNum) #Round to prevent errors
            if abs(practicetestrad-segNum) > amountofsegments/2:
                if practicetestrad>segNum:
                    colorDist = amountofsegments-practicetestrad+segNum
                else:
                    colorDist = amountofsegments-segNum+practicetestrad
            else:
                colorDist = abs(practicetestrad-segNum)
            round(colorDist)
            if colorDist < 2:
                colorText = '        The color is perfect        '
                colorIsCorrect = True
            elif colorDist < 4:
                colorText = '     The color is very close     '
            elif colorDist < 8:
                colorText = '         The color is close         '
            else:
                colorText = '       The color is incorrect       '
            FeedbackText.setText(colorText)
            if not colorIsCorrect: #Same as above but for color
                ContinueText.setText('Please select a valid color')
        FeedbackText.draw()
        if not mouse2.isPressedIn(screenRect2) and colorIsCorrect:
            ContinueText.setText('Press Space To Continue') #When they finally are correct tell them you can press the space bar to continue
            ContinueText.autoDraw = True #Draw the text
        elif colorIsCorrect: #This will only call if they are dragging
            ContinueText.setText('') #Sets the text to nothing
        if theseKeys == 'space':  # if space is pressed
            #a response ends the routine
            helpColor = True #If they have not colored yet and try to end routine
            if hasColored: #Stops routine if they have colored and moved the stimuli
                if colorIsCorrect:
                    continueRoutine = False
                else:
                    ContinueText.autoDraw = True
        
        #Help animations
        if helpColor == True and hasColored == False: #If they need help coloring and they are not currently dragging the image
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
            selectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,0,1], pos=(place[0]+(math.cos(math.radians(-colorDeg+90))*(.15-(0.03/4))), place[1]+(math.sin(math.radians(-colorDeg+90))*(.15-(0.03/4)))), size=(0.03,0.03), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = colorOpac)
            innerSelectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[colorDeg,1,1], pos=(place[0]+(math.cos(math.radians(-colorDeg+90))*(.15-(0.025/3.4))), place[1]+(math.sin(math.radians(-colorDeg+90))*(.15-(0.025/3.4)))), size=(0.025,0.025), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = colorOpac)
            #Draws each object
            selectShape.draw()
            innerSelectShape.draw()
            ColorText.draw()
        
        # *Image2* updates
        if t >= 0.0 and Image2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Image2.tStart = t  # not accounting for scr refresh
            Image2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Image2, 'tStartRefresh')  # time at next scr refresh
            Image2.setAutoDraw(True)
        keys = event.getKeys()
        for key in keys:
            if 'command' in key:
                command = True
            if 'esc' in key and command:
                liveliveFile = open(liveFileName+'live.csv', 'w')
                liveliveFile.write('Abort,Abort,1,1,1,1,')
                liveliveFile.close()
                core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceTestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceTest"-------
    for thisComponent in practiceTestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practiceTests (TrialHandler)
    practiceTests.addData('mouse2.started', mouse2.tStart)
    practiceTests.addData('mouse2.stopped', mouse2.tStop)
    practiceTests.addData('screenRect2.started', screenRect2.tStartRefresh)
    practiceTests.addData('screenRect2.stopped', screenRect2.tStopRefresh)
    ContinueText.autoDraw = False #Stop drawing the text
    win.mouseVisible = False #Hide mouse
    practicetesttrail += 1
    practiceTests.addData('Image2.started', Image2.tStartRefresh)
    practiceTests.addData('Image2.stopped', Image2.tStopRefresh)
    # the Routine "practiceTest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed num_practstudy repeats of 'practiceTests'


# ------Prepare to start Routine "studyInstr"-------
t = 0
studyInstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = keyboard.Keyboard()
currentTime = datetime.datetime.now()
liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
skipPractStr = ''
if skipPractice:
    skipPractStr = ',' + str(num_study) + ',' + str(num_test) + ',' + str(skipOldOrNew)
liveFile.write('Study,Instruction,1,1,1,' + str(num_study+1) + ',' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second) + skipPractStr)
liveFile.close()
liveNum += 1
# keep track of which components have finished
studyInstrComponents = [studyText, key_resp_3]
for thisComponent in studyInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "studyInstr"-------
while continueRoutine:
    # get current time
    t = studyInstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *studyText* updates
    if t >= 0.0 and studyText.status == NOT_STARTED:
        # keep track of start time/frame for later
        studyText.tStart = t  # not accounting for scr refresh
        studyText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(studyText, 'tStartRefresh')  # time at next scr refresh
        studyText.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # not accounting for scr refresh
        key_resp_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    for key in keys:
        if 'command' in key:
            command = True
        if 'esc' in key and command:
            liveliveFile = open(liveFileName+'live.csv', 'w')
            liveliveFile.write('Abort,Abort,1,1,1,1,')
            liveliveFile.close()
            core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in studyInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "studyInstr"-------
for thisComponent in studyInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
studyOnset = 0
thisExp.addData('studyText.started', studyText.tStartRefresh)
thisExp.addData('studyText.stopped', studyText.tStopRefresh)
# the Routine "studyInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
studys = data.TrialHandler(nReps=num_study, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='studys')
thisExp.addLoop(studys)  # add the loop to the experiment
thisStudy = studys.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStudy.rgb)
if thisStudy != None:
    for paramName in thisStudy:
        exec('{} = thisStudy[paramName]'.format(paramName))

for thisStudy in studys:
    currentLoop = studys
    # abbreviate parameter names if possible (e.g. rgb = thisStudy.rgb)
    if thisStudy != None:
        for paramName in thisStudy:
            exec('{} = thisStudy[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "reset"-------
    t = 0
    resetClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if studyOnset == 0:
        studyOnset = datetime.datetime.now()
    
    if oldornewOnset == 0:
        oldornewOnset = datetime.datetime.now()
    
    if testOnset == 0:
        testOnset = datetime.datetime.now()
    # keep track of which components have finished
    resetComponents = [resettext]
    for thisComponent in resetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "reset"-------
    while continueRoutine and routineTimer.getTime() > 0:
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
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resettext.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            resettext.tStop = t  # not accounting for scr refresh
            resettext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(resettext, 'tStopRefresh')  # time at next scr refresh
            resettext.setAutoDraw(False)
        keys = event.getKeys()
        for key in keys:
            if 'command' in key:
                command = True
            if 'esc' in key and command:
                liveliveFile = open(liveFileName+'live.csv', 'w')
                liveliveFile.write('Abort,Abort,1,1,1,1,')
                liveliveFile.close()
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
    studys.addData('resettext.started', resettext.tStartRefresh)
    studys.addData('resettext.stopped', resettext.tStopRefresh)
    
    # ------Prepare to start Routine "study"-------
    t = 0
    studyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    studyPath = stimuli[0][study_order[currentStudy]] #Gets path of the study image
    studyx = stimuli[1][study_order[currentStudy]] #Gets x cord of the study image
    studyy = stimuli[2][study_order[currentStudy]] #Gets y cord of the study image
    studyrad = stimuli[3][study_order[currentStudy]] #Gets color of the study image
    
    nowtime = datetime.datetime.now().time() #Saves time they begun the section
    stimuli[8][study_order[currentStudy]] = nowtime
    
    stimuli[10][study_order[currentStudy]] = round((datetime.datetime.now()-studyOnset).total_seconds(),2)
    studyImage.setColor([(studyrad*orimult)+(orimult/2),1,1], colorSpace='hsv')
    studyImage.setPos((0,0))
    studyImage.setImage(studyPath)
    currentTime = datetime.datetime.now()
    liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
    liveFile.write('Study,Stimuli,' + str(currentStudy+1) + ',' + str(num_study) + ',' + str(currentStudy+2) + ',' + str(num_study+1) + ',' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second) + ',' + stimuli[7][study_order[currentStudy]] + ',' + str(studyx) + ',' + str(studyy) + ',' + str(studyrad))
    liveFile.close()
    liveNum += 1
    # keep track of which components have finished
    studyComponents = [studyImage]
    for thisComponent in studyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "study"-------
    while continueRoutine and routineTimer.getTime() > 0:
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
        frameRemains = 0.0 + 3.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if studyImage.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            studyImage.tStop = t  # not accounting for scr refresh
            studyImage.frameNStop = frameN  # exact frame index
            win.timeOnFlip(studyImage, 'tStopRefresh')  # time at next scr refresh
            studyImage.setAutoDraw(False)
        keys = event.getKeys()
        for key in keys:
            if 'command' in key:
                command = True
            if 'esc' in key and command:
                liveliveFile = open(liveFileName+'live.csv', 'w')
                liveliveFile.write('Abort,Abort,1,1,1,1,')
                liveliveFile.close()
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
    currentStudy += 1
    studys.addData('studyImage.started', studyImage.tStartRefresh)
    studys.addData('studyImage.stopped', studyImage.tStopRefresh)
    thisExp.nextEntry()
    
# completed num_study repeats of 'studys'


# ------Prepare to start Routine "oldornewInstr"-------
t = 0
oldornewInstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
if skipOldOrNew:
    continueRoutine = False
key_resp_11 = keyboard.Keyboard()
if not skipOldOrNew:
    currentTime = datetime.datetime.now()
    liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
    liveFile.write('Old/New,Instruction,1,1,1,' + str(num_test + 1) + ',' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second))
    liveFile.close()
    liveNum += 1
# keep track of which components have finished
oldornewInstrComponents = [key_resp_11, text_11]
for thisComponent in oldornewInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "oldornewInstr"-------
while continueRoutine:
    # get current time
    t = oldornewInstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_11* updates
    if t >= 0.0 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t  # not accounting for scr refresh
        key_resp_11.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        key_resp_11.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    for key in keys:
        if 'command' in key:
            command = True
        if 'esc' in key and command:
            liveliveFile = open(liveFileName+'live.csv', 'w')
            liveliveFile.write('Abort,Abort,1,1,1,1,')
            liveliveFile.close()
            core.quit()
    
    # *text_11* updates
    if t >= 0.0 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t  # not accounting for scr refresh
        text_11.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in oldornewInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "oldornewInstr"-------
for thisComponent in oldornewInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
oldornewOnset = 0
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
# the Routine "oldornewInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
oldornews = data.TrialHandler(nReps=num_oldornew, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='oldornews')
thisExp.addLoop(oldornews)  # add the loop to the experiment
thisOldornew = oldornews.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOldornew.rgb)
if thisOldornew != None:
    for paramName in thisOldornew:
        exec('{} = thisOldornew[paramName]'.format(paramName))

for thisOldornew in oldornews:
    currentLoop = oldornews
    # abbreviate parameter names if possible (e.g. rgb = thisOldornew.rgb)
    if thisOldornew != None:
        for paramName in thisOldornew:
            exec('{} = thisOldornew[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "reset"-------
    t = 0
    resetClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if studyOnset == 0:
        studyOnset = datetime.datetime.now()
    
    if oldornewOnset == 0:
        oldornewOnset = datetime.datetime.now()
    
    if testOnset == 0:
        testOnset = datetime.datetime.now()
    # keep track of which components have finished
    resetComponents = [resettext]
    for thisComponent in resetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "reset"-------
    while continueRoutine and routineTimer.getTime() > 0:
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
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resettext.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            resettext.tStop = t  # not accounting for scr refresh
            resettext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(resettext, 'tStopRefresh')  # time at next scr refresh
            resettext.setAutoDraw(False)
        keys = event.getKeys()
        for key in keys:
            if 'command' in key:
                command = True
            if 'esc' in key and command:
                liveliveFile = open(liveFileName+'live.csv', 'w')
                liveliveFile.write('Abort,Abort,1,1,1,1,')
                liveliveFile.close()
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
    oldornews.addData('resettext.started', resettext.tStartRefresh)
    oldornews.addData('resettext.stopped', resettext.tStopRefresh)
    
    # ------Prepare to start Routine "oldornew"-------
    t = 0
    oldornewClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    win.mouseVisible = False #Hide mouse
    then = datetime.datetime.now() #Gets time
    nowtime = datetime.datetime.now().time() #Saves time they begun the section
    stimuli[9][oldornew_order[currentOldornew]] = nowtime
    
    #Live stuff reset to N/A in case there is no correct location/color
    liveoldornewx = 'N/A'
    liveoldornewy = 'N/A'
    liveoldornewrad = 'N/A'
    
    oldornewx = "N/A"
    oldornewy = "N/A"
    oldornewrad = 0
    oldornewPath = stimuli[0][oldornew_order[currentOldornew]] #Gets path of the study image
    oldornewoldornew = stimuli[4][oldornew_order[currentOldornew]] #Gets color of the study image
    liveoldornewoldornew = oldornewoldornew #For live file
    if oldornewoldornew == "Old":
        oldornewx = stimuli[1][oldornew_order[currentOldornew]] #Gets x cord of the study image
        oldornewy = stimuli[2][oldornew_order[currentOldornew]] #Gets y cord of the study image
        oldornewrad = stimuli[3][oldornew_order[currentOldornew]] #Gets color of the study image
        liveoldornewx = str(oldornewx) #For live file
        liveoldornewy = str(oldornewy) #For live file
        liveoldornewrad = str(oldornewrad) #For live file
    
    stimuli[11][oldornew_order[currentOldornew]] = round((datetime.datetime.now()-oldornewOnset).total_seconds(),2)
    oldornewImage.setImage(oldornewPath)
    currentTime = datetime.datetime.now()
    liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
    liveFile.write('Old/New,Stimuli,' + str(currentOldornew+1) + ',' + str(num_test) + ',' + str(currentOldornew+2) + ',' + str(num_test+1) + ',' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second) + ',' + stimuli[7][oldornew_order[currentOldornew]] + ',' + liveoldornewoldornew + ',' + liveoldornewx + ',' + liveoldornewy + ',' + liveoldornewrad + ',' + liveoldornewrt + ',' + liveuseroldornew)
    liveFile.close()
    liveNum += 1
    # keep track of which components have finished
    oldornewComponents = [oldornewText, oldornewImage]
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
        keys = event.getKeys()
        for key in keys:
            if '1' in key or '2' in key: #t is a var for time psychopy automatically creates
                if key == '1':
                    stimuli[5][oldornew_order[currentOldornew]] = 'Old'
                    liveuseroldornew = 'Old'
                elif key == '2':
                    stimuli[5][oldornew_order[currentOldornew]] = 'New'
                    liveuseroldornew = 'New'
                now = datetime.datetime.now()
                diff = now-then
                oldornewrt = round(diff.total_seconds(),2)
                liveoldornewrt = str(oldornewrt)
                stimuli[6][oldornew_order[currentOldornew]] = oldornewrt
                continueRoutine = False
        
        # *oldornewImage* updates
        if t >= 0.0 and oldornewImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            oldornewImage.tStart = t  # not accounting for scr refresh
            oldornewImage.frameNStart = frameN  # exact frame index
            win.timeOnFlip(oldornewImage, 'tStartRefresh')  # time at next scr refresh
            oldornewImage.setAutoDraw(True)
        for key in keys:
            if 'command' in key:
                command = True
            if 'esc' in key and command:
                liveliveFile = open(liveFileName+'live.csv', 'w')
                liveliveFile.write('Abort,Abort,1,1,1,1,')
                liveliveFile.close()
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
    oldornews.addData('oldornewText.started', oldornewText.tStartRefresh)
    oldornews.addData('oldornewText.stopped', oldornewText.tStopRefresh)
    #Saves Stimuli name
    thisExp4.addData('StimuliName', stimuli[7][oldornew_order[currentOldornew]])
    
    #Saves user old or new
    thisExp4.addData('User_OldOrNew', stimuli[5][oldornew_order[currentOldornew]])
    
    #Save Correct oldornew
    thisExp4.addData('Correct_OldOrNew', oldornewoldornew)
    if oldornewoldornew == 'Old':
        #Save color and rad #
        degrees = (orimult*oldornewrad)+(orimult/2)
        degrees = round(degrees, 1) #Round because it should only go to one place w/ mult of 3.6
        thisExp4.addData('Correct_Color', degrees)
        thisExp4.addData('Correct_Rad#', oldornewrad)
        #Save approx color name
        thisExp4.addData('Correct_AproxColor', aproxColor(oldornewrad)) #AproxColor func is in Begin Experiment of test
    else:
        thisExp4.addData('Correct_Color', 'N/A')
        thisExp4.addData('Correct_Rad#', 'N/A')
        thisExp4.addData('Correct_AproxColor', 'N/A')
    
    thisExp4.addData('OldOrNew_RT', oldornewrt) #saves time from oldornew section
    
    thisExp4.addData('StudyStartTime', stimuli[8][oldornew_order[currentOldornew]]) #adds data
    thisExp4.addData('OldOrNewStartTime', stimuli[9][oldornew_order[currentOldornew]]) #adds data
    
    #Next Entry of experiment
    thisExp4.nextEntry()
    
    currentOldornew += 1
    oldornews.addData('oldornewImage.started', oldornewImage.tStartRefresh)
    oldornews.addData('oldornewImage.stopped', oldornewImage.tStopRefresh)
    # the Routine "oldornew" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed num_oldornew repeats of 'oldornews'


# ------Prepare to start Routine "testInstr"-------
t = 0
testInstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = keyboard.Keyboard()
currentTime = datetime.datetime.now()
liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
liveFile.write('Test,Instruction,1,1,1,' + str(num_study+1) + ',' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second) + ',' + liveoldornewrt + ',' + liveuseroldornew) #Gets stuff from last trail
liveFile.close()
liveNum += 1
# keep track of which components have finished
testInstrComponents = [text_3, key_resp_5]
for thisComponent in testInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "testInstr"-------
while continueRoutine:
    # get current time
    t = testInstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # not accounting for scr refresh
        text_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # not accounting for scr refresh
        key_resp_5.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        key_resp_5.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    for key in keys:
        if 'command' in key:
            command = True
        if 'esc' in key and command:
            liveliveFile = open(liveFileName+'live.csv', 'w')
            liveliveFile.write('Abort,Abort,1,1,1,1,')
            liveliveFile.close()
            core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstr"-------
for thisComponent in testInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
testOnset = 0
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "testInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
tests = data.TrialHandler(nReps=num_study, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='tests')
thisExp.addLoop(tests)  # add the loop to the experiment
thisTest = tests.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
if thisTest != None:
    for paramName in thisTest:
        exec('{} = thisTest[paramName]'.format(paramName))

for thisTest in tests:
    currentLoop = tests
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest != None:
        for paramName in thisTest:
            exec('{} = thisTest[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "reset"-------
    t = 0
    resetClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if studyOnset == 0:
        studyOnset = datetime.datetime.now()
    
    if oldornewOnset == 0:
        oldornewOnset = datetime.datetime.now()
    
    if testOnset == 0:
        testOnset = datetime.datetime.now()
    # keep track of which components have finished
    resetComponents = [resettext]
    for thisComponent in resetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "reset"-------
    while continueRoutine and routineTimer.getTime() > 0:
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
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resettext.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            resettext.tStop = t  # not accounting for scr refresh
            resettext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(resettext, 'tStopRefresh')  # time at next scr refresh
            resettext.setAutoDraw(False)
        keys = event.getKeys()
        for key in keys:
            if 'command' in key:
                command = True
            if 'esc' in key and command:
                liveliveFile = open(liveFileName+'live.csv', 'w')
                liveliveFile.write('Abort,Abort,1,1,1,1,')
                liveliveFile.close()
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
    tests.addData('resettext.started', resettext.tStartRefresh)
    tests.addData('resettext.stopped', resettext.tStopRefresh)
    
    # ------Prepare to start Routine "test"-------
    t = 0
    testClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse1
    gotValidClick = False  # until a click is received
    key_resp_2 = keyboard.Keyboard()
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
    then = datetime.datetime.now() #Saves time they begun the section
    nowtime = datetime.datetime.now().time() #Saves time they begun the section
    
    degrees = 0 #Resests degrees so that if it saves with an exit the degrees will be 0 and not some random number
    Image.setColor([0,0,1])#sets Image hsv color
    
    
    
    #Live stuff reset to N/A in case there is no correct location/color
    livetestx = 'N/A'
    livetesty = 'N/A'
    livetestrad = 'N/A'
    
    testPath = 'N/A'
    testx = "N/A"
    testy = "N/A"
    testrad = 0
    testPath = stimuli[0][test_order[currentTest]] #Gets path of the study image
    testoldornew = stimuli[4][test_order[currentTest]] #Gets color of the study image
    livetestPath = testPath #For live file
    livetestoldornew = testoldornew #For live file
    if testoldornew == "Old":
        testx = stimuli[1][test_order[currentTest]] #Gets x cord of the study image
        testy = stimuli[2][test_order[currentTest]] #Gets y cord of the study image
        testrad = stimuli[3][test_order[currentTest]] #Gets color of the study image
        livetestx = str(testx) #For live file
        livetesty = str(testy) #For live file
        livetestrad = str(testrad) #For live file
    mouse1.setPos(newPos=(0, 0.005)) #resets position of mouse, has to be offset slightly or else it will select a color for some reason
    win.mouseVisible = True #Show mouse only if it is supposed to continue routine
    
    #These two vars give the person help with knowing how to drag/color live
    helpColor = False
    
    opacOfArrows = 0.0 #Opacity of the arrows
    opacUp = True #If Opacity is rising or falling
    
    colorDeg = 0 #Degrees of slider for colorHelp
    colorDegUp = True #Degrees of the slider going up or down
    colorOpac = 0 #Opacity of the slider
    Image.setImage(testPath)
    currentTime = datetime.datetime.now()
    liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
    liveFile.write('Test,Stimuli,' + str(currentTest+1) + ',' + str(num_study) + ',' + str(currentTest+2) + ',' + str(num_study+1) + ',' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second) + ',' + stimuli[7][test_order[currentTest]] + ',' + livetestx + ',' + livetesty + ',' + livetestrad + ',' + stimuli[5][test_order[currentTest]] + ',' + liveuserx + ',' + liveusery + ',' + liveuserrad + ',' + str(stimuli[6][test_order[currentTest]]) + ',' + livetestrt)
    liveFile.close()
    liveNum += 1
    # keep track of which components have finished
    testComponents = [mouse1, key_resp_2, screenRect, Image]
    for thisComponent in testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "test"-------
    while continueRoutine:
        # get current time
        t = testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # not accounting for scr refresh
            key_resp_2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
        stim.draw()
        
        if mouse1.isPressedIn(screenRect):#ScreenRect is used to detect if mouse is pressed anywhere on screen
            if mouse1.isPressedIn(stim) and not mouse1.isPressedIn(noClickShape):#Has to be initially pressed on wheel to set to true
                hasColored = True #For hiding the selectShape until you start coloring
                isOnColor = True #Then will set is on color to true
        else:
            isOnColor = False #If mouse is not pressed down it is not on color
        #MARK: Detect Mouse Press On Segment
        #Takes the multiplier (How many segments) and multiplies it by rad number
        #Then adds half of the multiplier (to make color average)
        if isOnColor == True: #If its on a segment it will update the color of the image
            if mouse1.isPressedIn(rad0): #Will not set color if dragging image
                degrees = (orimult*0)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad1):
                degrees = (orimult*1)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad2):
                degrees = (orimult*2)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad3):
                degrees = (orimult*3)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad4):
                degrees = (orimult*4)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad5):
                degrees = (orimult*5)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad6):
                degrees = (orimult*6)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad7):
                degrees = (orimult*7)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad8):
                degrees = (orimult*8)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad9):
                degrees = (orimult*9)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad10):
                degrees = (orimult*10)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad11):
                degrees = (orimult*11)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad12):
                degrees = (orimult*12)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad13):
                degrees = (orimult*13)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad14):
                degrees = (orimult*14)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad15):
                degrees = (orimult*15)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad16):
                degrees = (orimult*16)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad17):
                degrees = (orimult*17)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad18):
                degrees = (orimult*18)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad19):
                degrees = (orimult*19)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad20):
                degrees = (orimult*20)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad21):
                degrees = (orimult*21)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad22):
                degrees = (orimult*22)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad23):
                degrees = (orimult*23)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad24):
                degrees = (orimult*24)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad25):
                degrees = (orimult*25)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad26):
                degrees = (orimult*26)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad27):
                degrees = (orimult*27)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad28):
                degrees = (orimult*28)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad29):
                degrees = (orimult*29)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad30):
                degrees = (orimult*30)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad31):
                degrees = (orimult*31)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad32):
                degrees = (orimult*32)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad33):
                degrees = (orimult*33)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad34):
                degrees = (orimult*34)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad35):
                degrees = (orimult*35)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad36):
                degrees = (orimult*36)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad37):
                degrees = (orimult*37)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad38):
                degrees = (orimult*38)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad39):
                degrees = (orimult*39)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad40):
                degrees = (orimult*40)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad41):
                degrees = (orimult*41)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad42):
                degrees = (orimult*42)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad43):
                degrees = (orimult*43)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad44):
                degrees = (orimult*44)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad45):
                degrees = (orimult*45)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad46):
                degrees = (orimult*46)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad47):
                degrees = (orimult*47)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad48):
                degrees = (orimult*48)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad49):
                degrees = (orimult*49)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad50):
                degrees = (orimult*50)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad51):
                degrees = (orimult*51)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad52):
                degrees = (orimult*52)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad53):
                degrees = (orimult*53)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad54):
                degrees = (orimult*54)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad55):
                degrees = (orimult*55)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad56):
                degrees = (orimult*56)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad57):
                degrees = (orimult*57)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad58):
                degrees = (orimult*58)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad59):
                degrees = (orimult*59)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad60):
                degrees = (orimult*60)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad61):
                degrees = (orimult*61)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad62):
                degrees = (orimult*62)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad63):
                degrees = (orimult*63)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad64):
                degrees = (orimult*64)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad65):
                degrees = (orimult*65)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad66):
                degrees = (orimult*66)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad67):
                degrees = (orimult*67)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad68):
                degrees = (orimult*68)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad69):
                degrees = (orimult*69)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad70):
                degrees = (orimult*70)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad71):
                degrees = (orimult*71)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad72):
                degrees = (orimult*72)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad73):
                degrees = (orimult*73)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad74):
                degrees = (orimult*74)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad75):
                degrees = (orimult*75)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad76):
                degrees = (orimult*76)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad77):
                degrees = (orimult*77)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad78):
                degrees = (orimult*78)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad79):
                degrees = (orimult*79)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad80):
                degrees = (orimult*80)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad81):
                degrees = (orimult*81)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad82):
                degrees = (orimult*82)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad83):
                degrees = (orimult*83)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad84):
                degrees = (orimult*84)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad85):
                degrees = (orimult*85)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad86):
                degrees = (orimult*86)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad87):
                degrees = (orimult*87)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad88):
                degrees = (orimult*88)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad89):
                degrees = (orimult*89)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad90):
                degrees = (orimult*90)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad91):
                degrees = (orimult*91)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad92):
                degrees = (orimult*92)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad93):
                degrees = (orimult*93)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad94):
                degrees = (orimult*94)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad95):
                degrees = (orimult*95)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad96):
                degrees = (orimult*96)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad97):
                degrees = (orimult*97)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad98):
                degrees = (orimult*98)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
            elif mouse1.isPressedIn(rad99):
                degrees = (orimult*99)+(orimult/2)
                Image.setColor([degrees,1,1])#sets Image hsv color
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
        
        # *screenRect* updates
        if t >= 0.0 and screenRect.status == NOT_STARTED:
            # keep track of start time/frame for later
            screenRect.tStart = t  # not accounting for scr refresh
            screenRect.frameNStart = frameN  # exact frame index
            win.timeOnFlip(screenRect, 'tStartRefresh')  # time at next scr refresh
            screenRect.setAutoDraw(True)
        if hasColored == True: #Hides until you actually start selecting a color, this is separate from colorHelp in ExitCode so no interference ever occors
            #Explanation: Color is just hsv set to white, position on circle is calculated by, X:= origin of stimuli x position + cos of the angle in radians (cos funtion only takes radians) * the radius (circumference/2) and then subtracting a fourth of the radius of the color picker circle to make it in the middle of the color wheel
            selectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,0,1], pos=(place[0]+(math.cos(math.radians(-degrees+90))*(.15-(0.03/4))), place[1]+(math.sin(math.radians(-degrees+90))*(.15-(0.03/4)))), size=(0.03,0.03), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)
            #Explanation: Same as above except the color is set to the color wheel segment, and to get it centered I devided by 3.4 because for some reason 4 didn't center it correctly, but 3.4 centers it fine so just leaving it like that is ok
            innerSelectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[degrees,1,1], pos=(place[0]+(math.cos(math.radians(-degrees+90))*(.15-(0.025/3.4))), place[1]+(math.sin(math.radians(-degrees+90))*(.15-(0.025/3.4)))), size=(0.025,0.025), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 1)
            #Draws both shapes
            selectShape.draw()
            innerSelectShape.draw()
        if theseKeys == 'space':  #if space is pressed
            #a response ends the routine
            helpColor = True #If they have not colored yet and try to end routine
            if hasColored == True: #Stops routine if they have colored and moved the stimuli
                continueRoutine = False
        
        #Help animations
        if helpColor == True and hasColored == False: #If they need help coloring and they are not currently dragging the image
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
            #Sets postion of selct shapes
            selectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,0,1], pos=(place[0]+(math.cos(math.radians(-colorDeg+90))*(.15-(0.03/4))), place[1]+(math.sin(math.radians(-colorDeg+90))*(.15-(0.03/4)))), size=(0.03,0.03), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = colorOpac)
            innerSelectShape = visual.RadialStim(win, colorSpace = 'hsv', color=[colorDeg,1,1], pos=(place[0]+(math.cos(math.radians(-colorDeg+90))*(.15-(0.025/3.4))), place[1]+(math.sin(math.radians(-colorDeg+90))*(.15-(0.025/3.4)))), size=(0.025,0.025), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = colorOpac)
            #Draws each object
            selectShape.draw()
            innerSelectShape.draw()
            ColorText.draw()
        
        noClickShape.draw()
        
        # *Image* updates
        if t >= 0.0 and Image.status == NOT_STARTED:
            # keep track of start time/frame for later
            Image.tStart = t  # not accounting for scr refresh
            Image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Image, 'tStartRefresh')  # time at next scr refresh
            Image.setAutoDraw(True)
        keys = event.getKeys()
        for key in keys:
            if 'command' in key:
                command = True
            if 'esc' in key and command:
                liveliveFile = open(liveFileName+'live.csv', 'w')
                liveliveFile.write('Abort,Abort,1,1,1,1,')
                liveliveFile.close()
                core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test"-------
    for thisComponent in testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for tests (TrialHandler)
    tests.addData('mouse1.started', mouse1.tStart)
    tests.addData('mouse1.stopped', mouse1.tStop)
    tests.addData('screenRect.started', screenRect.tStartRefresh)
    tests.addData('screenRect.stopped', screenRect.tStopRefresh)
    #NOTE: Some save code is in oldornew section of the experiment
    
    #Saves Stimuli name
    thisExp2.addData('StimuliName', stimuli[7][test_order[currentTest]])
    
    #Saves order of test, oldornew, and study, starting with 0
    thisExp2.addData('TestOrder', currentTest)
    #Very complicated function to find order
    testingNum = 0
    while oldornew_order[testingNum] != test_order[currentTest]:
        testingNum += 1
    thisExp2.addData('OldOrNewOrder', testingNum)
    testingNum = 0
    while study_order[testingNum] != test_order[currentTest]:
        testingNum += 1
    thisExp2.addData('StudyOrder', testingNum)
    
    #Saves user old or new
    thisExp2.addData('User_OldOrNew', stimuli[5][test_order[currentTest]])
    
    #MARK: User Save
    liveuserx = str('N/A') #For live data
    liveusery = str('N/A') #For live data
    #Save color and rad #
    degrees = round(degrees, 1) #Round because it should only go to one place w/ mult of 3.6
    thisExp2.addData('User_Color', degrees)
    #degrees = (orimult*0)+(orimult/2) original eq
    radNum = (degrees-(orimult/2))/orimult #Changes degrees back into rad #s
    radNum = round(radNum) #Round to prevent errors
    thisExp2.addData('User_Rad#', radNum)
    liveuserrad = str(radNum) #For live data
    #Save approx color name
    thisExp2.addData('User_AproxColor', aproxColor(radNum)) #AproxColor func is in Begin Experiment
    
    #MARK: Correct Save
    #Save Correct oldornew
    if not skipOldOrNew:
        thisExp2.addData('Correct_OldOrNew', testoldornew)
    else:
        thisExp2.addData('Correct_OldOrNew', 'N/A')
    
    #Save color and rad #
    degrees = (orimult*testrad)+(orimult/2)
    degrees = round(degrees, 1) #Round because it should only go to one place w/ mult of 3.6
    thisExp2.addData('Correct_Color', degrees)
    thisExp2.addData('Correct_Rad#', testrad)
    #Save approx color name
    thisExp2.addData('Correct_AproxColor', aproxColor(testrad)) #AproxColor func is in Begin Experiment
    
    #MARK: Get distance from correct location/color
    #Color
    if abs(testrad-radNum) > amountofsegments/2:
        if testrad>radNum:
            colorDist = amountofsegments-testrad+radNum
        else:
            colorDist = amountofsegments-radNum+testrad
    else:
        colorDist = abs(testrad-radNum)
    round(colorDist)
    thisExp2.addData('radColorDist', colorDist) #saves color distance
    
    #MARK: Gets reaction time 
    thisExp2.addData('OldOrNew_RT', stimuli[6][test_order[currentTest]]) #saves time from oldornew section
    now = datetime.datetime.now() #Gets time now
    diff = now-then #Gets the difference
    testrt = round(diff.total_seconds(),2) #Puts it in testrt and rounds to 2 decimal places
    thisExp2.addData('Test_RT', testrt) #adds data
    livetestrt = str(testrt) #Live file data
    
    thisExp2.addData('StudyStartTime', stimuli[8][test_order[currentTest]]) #adds data
    thisExp2.addData('OldOrNewStartTime', stimuli[9][test_order[currentTest]]) #adds data
    thisExp2.addData('TestStartTime', nowtime) #adds start time of stimulis on screen
    
    thisExp2.addData('StudyOnset', stimuli[10][test_order[currentTest]]) #adds data
    thisExp2.addData('OldOrNewOnset', stimuli[11][test_order[currentTest]]) #adds data
    thisExp2.addData('TestOnset', round((then-testOnset).total_seconds(),2)) #adds start time of stimulis on screen
    
    currentTest += 1 #Goes to next test stimuli
    
    #Next Entry of experiment
    thisExp2.nextEntry()
    win.mouseVisible = False #Hide mouse
    tests.addData('Image.started', Image.tStartRefresh)
    tests.addData('Image.stopped', Image.tStopRefresh)
    # the Routine "test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed num_study repeats of 'tests'


# ------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
StartEnd = False #Lets the screen update normally before quiting

if not skipOldOrNew:
    currentStimuliTest = num_study
    testingNums = []
    for i in range(num_test-num_study):
        testingNum = 0
        while oldornew_order[testingNum] != currentStimuliTest:
            testingNum += 1
        testingNums.append(testingNum)
        currentStimuliTest += 1

    print(testingNums)

    currentStimuli = 0
    for i in range(num_test-num_study):
        while not currentStimuli in testingNums:
            currentStimuli += 1
        print(currentStimuli)
        thisExp2.addData('StimuliName', stimuli[7][oldornew_order[currentStimuli]])
        thisExp2.addData('TestOrder', 'N/A')
        
        thisExp2.addData('OldOrNewOrder', currentStimuli)
        thisExp2.addData('StudyOrder', 'N/A')
        
        thisExp2.addData('User_OldOrNew', stimuli[5][oldornew_order[currentStimuli]])
        
        thisExp2.addData('User_Color', 'N/A')
        thisExp2.addData('User_Rad#', 'N/A')
        thisExp2.addData('User_AproxColor', 'N/A')
        
        thisExp2.addData('Correct_OldOrNew', 'New')
        
        thisExp2.addData('Correct_Color', 'N/A')
        thisExp2.addData('Correct_Rad#', 'N/A')
        thisExp2.addData('Correct_AproxColor', 'N/A')
        
        thisExp2.addData('radColorDist', 'N/A')
        
        thisExp2.addData('OldOrNew_RT', stimuli[6][oldornew_order[currentStimuli]])
        thisExp2.addData('Test_RT', 'N/A') 
        
        thisExp2.addData('StudyStartTime', 'N/A') #adds data
        thisExp2.addData('OldOrNewStartTime', stimuli[9][oldornew_order[currentStimuli]]) #adds data
        thisExp2.addData('TestStartTime', 'N/A') #adds start time of stimulis on screen
        
        thisExp2.addData('StudyOnset', 'N/A') #adds data
        thisExp2.addData('OldOrNewOnset', stimuli[11][oldornew_order[currentStimuli]]) #adds data
        thisExp2.addData('TestOnset', 'N/A') #adds start time of stimulis on screen
        
        thisExp2.nextEntry()
        currentStimuli += 1
currentTime = datetime.datetime.now()
liveFile = open(liveFileName+str(liveNum)+'.csv', 'w')
liveFile.write('Done,Done,1,1,1,1,' + str(currentTime.hour) + ',' + str(currentTime.minute) + ',' + str(currentTime.second) + ',N/A,N/A,N/A,N/A,N/A,' + liveuseroldornew + ',' + liveuserx + ',' + liveusery + ',' + liveuserrad + ',N/A,' + livetestrt) #To get the last one the user did
liveFile.close()
liveNum += 1
# keep track of which components have finished
EndComponents = [text]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # not accounting for scr refresh
        text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if StartEnd:
        win.flip()
        time.sleep(4) #Waits three seconds
        text.setText('Saving Data\n\nPlease Wait') #Changes text
        win.flip()
        core.quit()
    StartEnd += 0.1 #For some reason it takes 11 frames/flips to update?
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
thisExp2.saveAsWideText(filename2+'.csv')
thisExp2.abort()  # or data files will save again on exit

thisExp3.saveAsWideText(liveFileName+'live.csv')
thisExp3.abort()  # or data files will save again on exi

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
