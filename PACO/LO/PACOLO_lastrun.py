#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on Fri Aug 30 13:44:56 2019
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
expName = 'PACOLO'  # from the Builder filename that created this script
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
    originPath='/Volumes/bamlab/Experiments/PACO/LO/PACOLO_lastrun.py',
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
import random, xlrd, math #For randomization of stimuli
command = False #For exiting experiment

thisdir = os.path.abspath(os.path.join(os.path.dirname(_thisDir),'.'))

#randomize the seed
random.seed(int(expInfo['participant'])) #Put in subject number

#Version Number (Update this when you make changes to the experiment, it will go in the readme file in each participant's folder, see bottom of begin experiment tab)
versionNumber = '0.1.6'

#number of study items
num_study = 5 #50

#number of OLD OR NEW items they'll be tested on
num_test = 7 #75

#Skip the Old Or New Section
skipOldOrNew = False

#Skip Practice Section
skipPractice = True

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

#MARK: Generate coordinates
#This will create the x and y coordiantes for use, change num_study variable and this will adapt by itself
#Maximum coordinates (Right Top of screen) (You probably don't want this to go all the way to the end of the screen)
screenx = 0.78 #Maximum x point on Psychopy screen you want the stimuli to go to
screeny = 0.39 #Maximum y point on Psychopy screen you want the stimuli to go to

#screen is approx 2 by 1, so below numbers should reflect that
divx = 4 #How many points there can be accross the x axis minimum
divy = 2 #How many points there can be accross the y axis minimum

numberofcords = 0 #Number of actual cords when excluding center ones

while numberofcords < num_study:
  if divy*2 == divx or divy*2 == divx+1:
    divx += 1
  else:
    divy += 1
  howmanyall = divx*divy #How many 
  numberofcords = 0
  xcords = [] #array of cords for x
  ycords = [] #array of cords for y
  ix = 0
  while ix <= divx:
    if ix == 0:
      xmult = 0
    else:
      xmult = ix/divx
    iy = 0
    while iy <= divy:
      if iy == 0:
        ymult = 0
      else:
        ymult = iy/divy
      #print(" ")
      #print(xmult, ymult) #For debugging
      xcord = ((screenx*2)*xmult)-screenx
      ycord = ((screeny*2)*ymult)-screeny
      if not xcord < 0.15 or not xcord > -0.15 or not ycord < 0.15 or not ycord > -0.15: #Exclusion points, change these to choose which points are excluded bc they are too close to the center
        #print("Cordinates:")
        numberofcords += 1
        #print(xcord) #Uncomment these to get the raw x and y coordinates on separate lines
        #print(ycord)
        #print("(" + str(xcord) + "," + str(ycord) + ")") #Uncomment to print coordinates as (x,y), you can use this for testing out points on desmos graph?
        xcords.append(round(xcord, 5))
        ycords.append(round(ycord, 5))
      iy += 1
    ix += 1
#You want this to equal as close to the number of possible coordinates you want as possible (In my case I want it to be close to 70)
print(" ")
#print(xcords)
#print(ycords)
print("Number of Coordinates: " + str(numberofcords)) 
print("There are " + str(divx + 1) + " x coordinates and " + str(divy + 1) + " y coordinates")

#MARK: Randomize coordinates
cordNums= [] #These numbers direct the final cords to the correct place in cords
#Final coordinates that are randomized
finalxcords = []
finalycords = []

for i in range(numberofcords): #Randomizes cordNums to be used as pickers for the final cords, randomizing with numberofcords makes sure any coordinates the above function generates can be used
    cordNums.append(i)
random.shuffle(cordNums) #Randomizes items in cordnums
for i in range(num_study): #Randomizes x and y cords together so they don't get all mixed up
    finalxcords.append(xcords[cordNums[i]])
    finalycords.append(ycords[cordNums[i]])
#print(cordNums)

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
radColors = [] #Blank array is so that later it is possible to put new values into the np stimuli array, like the oldornew status and rt
for i in range(num_test):
    radColors.append("N/A")

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
    text='In this experiment, you will be presented with different images.\nYour task will be to remember each shape and its location on the screen.\n\nTo respond, you will need to use the mouse to drag an image to a place on the screen.\n\nPress space to see an example and try it out',
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
screenRect3 = visual.Rect(
    win=win, name='screenRect3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-5.0, interpolate=True)
#Color text 2 setup, keep this so it's reused for telling the user to continue
ColorText2 = visual.TextStim(win=win, name='ColorText',
    text='',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

#Drag text 2 setup, tells user to select a place
DragText2 = visual.TextStim(win=win, name='DragText',
    text='Drag and Drop the object to a location on the screen',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practiceStudyInstr"
practiceStudyInstrClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Lets start with some practice.\n\nYou will now be shown two objects. Memorize their shape and location.\nEach object will stay on the screen for three seconds.\n\nPress Space To Continue',
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
    color='white', colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "practiceOldornewInstr"
practiceOldornewInstrClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text="You'll now be shown multiple shapes.\nFor each shape, decide if you have seen the shape during the study, irrespective of its location.\nIf you have seen it during study, press 1 for OLD. If you have not seen it, press 2 for NEW.\n\nPress Space To Start",
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
    text='You will now be tested on the location of the images you studied. \nUse the mouse to drag the image to its original location.\nDuring this practice, you will be given feedback on how close you are to the correct location\n\nPress Space To Start',
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
screenRect2 = visual.Rect(
    win=win, name='screenRect2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=0, depth=-3.0, interpolate=True)
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
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "studyInstr"
studyInstrClock = core.Clock()
studyText = visual.TextStim(win=win, name='studyText',
    text='Now for the actual experiment\nYou will now study a larger number of images. For each image, try to remember the shape and location. \n\n\nPress Space To Start',
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
    text='We will now test you on how well you remember the shapes you just saw.\nJust like in the practice, decide if you have seen each shape during the study, irrespective of its location.\nIf you have seen it during the study, press 1 for OLD. If you have not seen it, press 2 for NEW.\nYou will not be given feedback.\n\nPress Space To Start',
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
    text="You will now be tested on the location of the images you studied. \nUse the mouse to drag the image to its original location.\nOnce you're done press the spacebar to continue.\n\nYou will NOT be given feedback on how close you are.\n\nPress Space To Start",
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
#To prevent user from clicking inside the color wheel and selecting a color, noClickShape surrounds entire image, set opacity to one to see for yourself ;)
noClickShape = visual.RadialStim(win, colorSpace = 'hsv', color=[180,0,1], pos=(0,0), size=(0.25,0.25), angularCycles = 0, radialCycles = 0, radialPhase = 0.5, opacity = 0)
screenRect = visual.Rect(
    win=win, name='screenRect',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.851,1.000,-1.000], fillColorSpace='rgb',
    opacity=0, depth=-3.0, interpolate=True)
import datetime #For saving raction times

currentTest = 0
testrad = 0 #Requires it to be defined at the beginning for some reason

testOnset = -1
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
    ori=0, pos=(0, .15), size=(0.03, 0.03),
    color=[1,0,1], colorSpace='hsv', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

arrowDown = visual.ImageStim(
    win=win, name='arrowDown',
    image='sin', mask=None,
    ori=0, pos=(0, -.15), size=(0.03, 0.03),
    color=[1,0,1], colorSpace='hsv', opacity=1,
    flipHoriz=False, flipVert=True,
    texRes=128, interpolate=True, depth=0.0)

arrowRight = visual.ImageStim(
    win=win, name='arrowRight',
    image='sin', mask=None,
    ori=0, pos=(.15, 0), size=(0.03, 0.03),
    color=[1,0,1], colorSpace='hsv', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

arrowLeft = visual.ImageStim(
    win=win, name='arrowLeft',
    image='sin', mask=None,
    ori=0, pos=(-.15, 0), size=(0.03, 0.03),
    color=[1,0,1], colorSpace='hsv', opacity=1,
    flipHoriz=True, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

#Set images
arrowUp.setImage(thisdir + '/LO/arrowUp.png')
arrowDown.setImage(thisdir + '/LO/arrowUp.png')
arrowRight.setImage(thisdir + '/LO/arrowRight.png')
arrowLeft.setImage(thisdir + '/LO/arrowRight.png')

Image = visual.ImageStim(
    win=win,
    name='Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.19, 0.19),
    color=[1,-1.000,1.000], colorSpace='hsv', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
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
    '\nUser vs Correct is self explanatory, with old or new being added as N/A if it was skipped in the header file.\nThe X and Y are coordinates on the screen (0.5 is the highest y value, while 0.9? is the highest x value).' + 
    '\nLocation distance is calculated using the pythagorean theorem, where a and b are the x and y coordinates.\nOldOrNew rt and Test rt are reaction times of the user.' + 
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
win.mouseVisible = True #Show mouse at start
mouse2.setPos(newPos=(0, 0.001)) #resets position of mouse, has to be offset slightly or else it will select a color for some reason

#These two vars give the person help with knowing how to drag/color live
helpColor = False

opacOfArrows = 0.0 #Opacity of the arrows
opacUp = True #If Opacity is rising or falling

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
    #This whole complicated thing makes sure that the stimuli always stays on the mouse if they click on the stimuli first
    if mouse3.isPressedIn(screenRect3) and didFinishDrag == False:#ScreenRect is used to detect if mouse is pressed anywhere on screen
        if mouse3.isPressedIn(noClickShape): #Checks when mouse is pressed down, see Begin Experiment for more about noClickShape
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
    
    # *screenRect3* updates
    if t >= 0.0 and screenRect3.status == NOT_STARTED:
        # keep track of start time/frame for later
        screenRect3.tStart = t  # not accounting for scr refresh
        screenRect3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(screenRect3, 'tStartRefresh')  # time at next scr refresh
        screenRect3.setAutoDraw(True)
    if not hasDragged:
        helpDrag = True #Tells the user to drag if they have already colored
    elif not isDragging: #Tells user they can continue once they've colored and placed, re-uses colortext2 text
        ColorText2.setText('Great! Whenever you\'re ready to continue, click the spacebar')
        ColorText2.draw()
    
    if theseKeys == 'space':  # if space is pressed
        #a response ends the routine
        if hasDragged: #Stops routine if they have colored and moved the stimuli
            continueRoutine = False
    
    #Help animations
    if helpDrag == True and hasDragged == False:
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
        DragText2.draw() #Tells user what to do
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
    practicestudyimage.setColor([1,1,1], colorSpace='rgb')
    practicestudyimage.setPos((practicestudyx, practicestudyy))
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
    isDragging = False #Lets other parts of experiment know that the user is dragging the stimuli
    didFinishDrag = False #Lets some aspects of the experiment only do something once after a drag has finished
    hasDragged = False #For preventing the user from going on until dragged
    place = (0,0) #Place of object (Image)
    Image2.setPos(place) #Sets image to (0,0)
    noClickShape.setPos(place) #Sets noClickShape to (0,0), see Begin Experiment for more about noClickShape
    mousePlace = (0,0) #Place of mouse when clicked
    mousex = 0.0 #Offset of mouse x
    mousey = 0.0 #Offset of mouse y
    firstDrag = True #For updating positions of mousex and mousey
    then = datetime.datetime.now() #Saves time they begun the section
    colorText = ''
    posText = ''
    degrees = 0 #Resests degrees so that if it saves with an exit the degrees will be 0 and not some random number
    Image2.setColor([0,0,1])#sets Image hsv color
    FeedbackText.setText('')
    ContinueText.setText('')
    colorIsCorrect = False #If they are on the correct color
    locationIsCorrect = False #If they are on the correct location
    mouse2.setPos(newPos=(0, 0.001)) #resets position of mouse, has to be offset slightly or else it will select a color for some reason
    win.mouseVisible = True #Show mouse only if it is supposed to continue routine
    
    #These two vars give the person help with knowing how to drag/color live
    helpDrag = False
    
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
        #This whole complicated thing makes sure that the stimuli always stays on the mouse if they click on the stimuli first
        if mouse2.isPressedIn(screenRect2) and didFinishDrag == False:#ScreenRect is used to detect if mouse is pressed anywhere on screen
            if mouse2.isPressedIn(noClickShape): #Checks when mouse is pressed down, see Begin Experiment for more about noClickShape
                #This calculates offset of mouse from center of object (Not needed but looks better in experiment)
                mousePlace = mouse2.getPos()
                if firstDrag == True: #Only updates offset once when starting the drag
                    mousex = mousePlace[0] - place[0] #Gets the difference between the Image place and the mouse place for x
                    mousey = mousePlace[1] - place[1] #Gets the difference between the Image place and the mouse place for y
                    firstDrag = False #Disables first drag
                place = mousePlace[0] - mousex, mousePlace[1] - mousey #Adds this onto the place of the image for more intuitive dragging
                Image2.setPos(place) #Sets position of the image equal to the position of the mouse
                noClickShape.setPos(place) #Set position
                isDragging = True #Sets is dragging to true when the mouse starts on the object (noClickShape in this case)
                hasDragged = True #For preventing the user from going on until dragged
                win.mouseVisible = False #Hide mouse when dragging
            elif isDragging == True: #If the mouse started on noClickShape but isnt there right now (and still pressed down) it will update position anyway
                #This calculates offset of mouse from center of object (Not needed but looks better in experiment)
                mousePlace = mouse2.getPos()
                if firstDrag == True: #Only updates offset once when starting the drag
                        mousex = mousePlace[0] - place[0] #Gets the difference between the Image place and the mouse place for x
                        mousey = mousePlace[1] - place[1] #Gets the difference between the Image place and the mouse place for y
                        firstDrag = False #Disables first drag
                place = mousePlace[0] - mousex, mousePlace[1] - mousey #Adds this onto the place of the image for more intuitive dragging
                Image2.setPos(place) #Sets position of the image equal to the position of the mouse
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
        
        # *screenRect2* updates
        if t >= 0.0 and screenRect2.status == NOT_STARTED:
            # keep track of start time/frame for later
            screenRect2.tStart = t  # not accounting for scr refresh
            screenRect2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(screenRect2, 'tStartRefresh')  # time at next scr refresh
            screenRect2.setAutoDraw(True)
        if isDragging: #When you are dragging the image
            locationIsCorrect = False #resets location is correct bool
            xpos, ypos = place
            distx = abs(xpos-practicetestx) #find the distance in x between correct and user
            disty = abs(ypos-practicetesty) #find the distance in y between correct and user
            pythDist = math.sqrt((distx*distx)+(disty*disty)) #Uses pythagorean theorem to find distance
            pythDist = round(pythDist,5) #Round to prevent errors
            if pythDist > 0.15:
                posText = '    The location is incorrect    '
            elif pythDist > 0.05:
                posText = 'The location is nearly correct'
            elif pythDist < 0.05:
                posText = '     The location is spot on!     '
                locationIsCorrect = True
            FeedbackText.setText(posText)
        FeedbackText.draw()
        if isDragging and not locationIsCorrect: #If you try to continue it will wave a finger at you a say no oh, choose a correct location
                ContinueText.setText('Please select a valid loaction')
        if not mouse2.isPressedIn(screenRect2) and locationIsCorrect:
            ContinueText.setText('Press Space To Continue') #When they finally are correct tell them you can press the space bar to continue
            ContinueText.autoDraw = True #Draw the text
        elif locationIsCorrect: #This will only call if they are dragging
            ContinueText.setText('') #Sets the text to nothing
        if theseKeys == 'space':  # if space is pressed
            #a response ends the routine
            helpDrag = True #If they have not dragged yet and try to end routine
            if hasDragged: #Stops routine if they have colored and moved the stimuli
                if locationIsCorrect:
                    continueRoutine = False
                else:
                    ContinueText.autoDraw = True
        
        #Help animations
        if helpDrag == True and hasDragged == False:
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
            DragText.draw() #Tells user what to do
        
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
    studyImage.setColor([0,0,1], colorSpace='hsv')
    studyImage.setPos((studyx, studyy))
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
        #Save correct position of the image
        thisExp4.addData('Correct_Image_x', oldornewx)
        thisExp4.addData('Correct_Image_y', oldornewy)
    else:
        thisExp4.addData('Correct_Image_x', 'N/A')
        thisExp4.addData('Correct_Image_y', 'N/A')
    
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
    isDragging = False #Lets other parts of experiment know that the user is dragging the stimuli
    didFinishDrag = False #Lets some aspects of the experiment only do something once after a drag has finished
    hasDragged = False #For preventing the user from going on until dragged
    place = (0,0) #Place of object (Image)
    Image.setPos(place) #Sets image to (0,0)
    noClickShape.setPos(place) #Sets noClickShape to (0,0), see Begin Experiment for more about noClickShape
    mousePlace = (0,0) #Place of mouse when clicked
    mousex = 0.0 #Offset of mouse x
    mousey = 0.0 #Offset of mouse y
    firstDrag = True #For updating positions of mousex and mousey
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
    helpDrag = False
    
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
        #This whole complicated thing makes sure that the stimuli always stays on the mouse if they click on the stimuli first
        if mouse1.isPressedIn(screenRect) and didFinishDrag == False:#ScreenRect is used to detect if mouse is pressed anywhere on screen
            if mouse1.isPressedIn(noClickShape): #Checks when mouse is pressed down, see Begin Experiment for more about noClickShape
                #This calculates offset of mouse from center of object (Not needed but looks better in experiment)
                mousePlace = mouse1.getPos()
                if firstDrag == True: #Only updates offset once when starting the drag
                    mousex = mousePlace[0] - place[0] #Gets the difference between the Image place and the mouse place for x
                    mousey = mousePlace[1] - place[1] #Gets the difference between the Image place and the mouse place for y
                    firstDrag = False #Disables first drag
                place = mousePlace[0] - mousex, mousePlace[1] - mousey #Adds this onto the place of the image for more intuitive dragging
                Image.setPos(place) #Sets position of the image equal to the position of the mouse
                noClickShape.setPos(place) #Set position
                isDragging = True #Sets is dragging to true when the mouse starts on the object (noClickShape in this case)
                hasDragged = True #For preventing the user from going on until dragged
                win.mouseVisible = False #Hide mouse when dragging
            elif isDragging == True: #If the mouse started on noClickShape but isnt there right now (and still pressed down) it will update position anyway
                #This calculates offset of mouse from center of object (Not needed but looks better in experiment)
                mousePlace = mouse1.getPos()
                if firstDrag == True: #Only updates offset once when starting the drag
                        mousex = mousePlace[0] - place[0] #Gets the difference between the Image place and the mouse place for x
                        mousey = mousePlace[1] - place[1] #Gets the difference between the Image place and the mouse place for y
                        firstDrag = False #Disables first drag
                place = mousePlace[0] - mousex, mousePlace[1] - mousey #Adds this onto the place of the image for more intuitive dragging
                Image.setPos(place) #Sets position of the image equal to the position of the mouse
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
        
        # *screenRect* updates
        if t >= 0.0 and screenRect.status == NOT_STARTED:
            # keep track of start time/frame for later
            screenRect.tStart = t  # not accounting for scr refresh
            screenRect.frameNStart = frameN  # exact frame index
            win.timeOnFlip(screenRect, 'tStartRefresh')  # time at next scr refresh
            screenRect.setAutoDraw(True)
        if theseKeys == 'space':  #if space is pressed
            #a response ends the routine
            helpDrag = True #If they have not dragged yet and try to end routine
            if hasDragged: #Stops routine if they have colored and moved the stimuli
                continueRoutine = False
        
        #Help animations
        if helpDrag == True and hasDragged == False:
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
            DragText.draw() #Tells user what to do
        
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
    #save position (place var)
    x, y = place
    #Save user's position of the image
    thisExp2.addData('User_Image_x', round(x,5))
    thisExp2.addData('User_Image_y', round(y,5))
    liveuserx = str(round(x,5)) #For live data
    liveusery = str(round(y,5)) #For live data
    
    #MARK: Correct Save
    #Save Correct oldornew
    if not skipOldOrNew:
        thisExp2.addData('Correct_OldOrNew', testoldornew)
    else:
        thisExp2.addData('Correct_OldOrNew', 'N/A')
    
    #Save correct position of the image
    thisExp2.addData('Correct_Image_x', testx)
    thisExp2.addData('Correct_Image_y', testy)
    
    #MARK: Get distance from correct location/color
    #Location
    distx = abs(x-testx) #find the distance in x between correct and user
    disty = abs(y-testy) #find the distance in y between correct and user
    pythDist = math.sqrt((distx*distx)+(disty*disty)) #Uses pythagorean theorem to find distance
    pythDist = round(pythDist,5) #Round to prevent errors
    thisExp2.addData('locationDist', pythDist) #saves distance
    
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
        
        thisExp2.addData('User_Image_x', 'N/A')
        thisExp2.addData('User_Image_y', 'N/A')
        
        thisExp2.addData('Correct_OldOrNew', 'New')
        
        thisExp2.addData('Correct_Image_x', 'N/A')
        thisExp2.addData('Correct_Image_y', 'N/A')
        
        thisExp2.addData('locationDist', 'N/A')
        
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
