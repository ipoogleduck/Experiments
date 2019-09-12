function Block1_Retrieval

close all;
clc;
warning('off','MATLAB:dispatcher:InexactMatch');                            % turn off case-mismatch manager (it's annoying)
KbName('UnifyKeyNames');
% Build a GUI for subject information
prompt = {'Subject Number', 'Random Seed'};                                 % What info do we want from the subject?
s = ClockRandSeed;                                                          % grab a seed
defAns = {'',num2str(s)};                                                   % fill in some default answers
box = inputdlg(prompt, 'Enter Subject Information', 1, defAns);             % actually make GUI
if length(box) == length(defAns)                                            % simple check for enough input, otherwise bail
    subNum = num2str(box{1}); rndSeed = str2num(box{2});
    rand('state',rndSeed);                                                % seed the generator
else
    return;
end

%Set this to 1 if you're on a computer with 2 monitors. Otherwise set it to
%zero. Psychophysics toolbox typically freaks out about timing with dual
%monitor setups (especially lcds). 
AnalysisMachine = 1;
if AnalysisMachine == 1
    %Skip Memtoolbox checks FOR use with Jarvis only MAKE SURE TO COMMENT OUT
    % FOR TASK COMPUTERS!!!!!!!
    Screen('Preference','VisualDebugLevel', 0)
    Screen('Preference','SkipSyncTests', 1)
else
end

% Load Encoding Parameters
root = pwd;
fName = [root, '\Subject Data\', num2str(subNum),'_Block_1_', 'LTM_Encoding.mat'];
load(fName)
encode_imgInd = stim.ltmStim;
%encode_imgInd = squeeze(encode_imgInd);
encode_imgCol = stim.colors;
encode_RGB = stim.colorLTM;
encode_images = stim.imgOrderRep;
nRepeat = stim.nRepeat;
encode_repeat = stim.repeat;


%test_imgInd = encode_imgInd(ismember(stim.imgOrderRep,stim.repeat)==0);
testItems = stim.imgOrderRep(ismember(stim.imgOrderRep,stim.repeat)==0);
testCol =  stim.colors(ismember(stim.imgOrderRep,stim.repeat)==0);
testColRGB = stim.colorLTM(:,ismember(stim.imgOrderRep,stim.repeat)==0);
testblocktrial = stim.blocktrial;
clear p stim
stim.testItems = testItems;
p.subNum = subNum; p.rndSeed = rndSeed;
stim.ImageNames = encode_images;
nStims = length(stim.ImageNames)-(2*nRepeat);

% Load Stimulus Texture Index
stimRoot = [root,'/MemImages/'];

% Turn off keyboard echoing
ListenChar(2);

%--------------------------------------------------------------------------
% General Experimental Parameters
%--------------------------------------------------------------------------
portcode = 'cc98';
p.nTrials = nStims;
p.windowed = 0;
p.debug = 0;

% stim geometry (in pixels):
p.stimSize = 300;
p.colPen = 50;
p.penArc = 2;
p.fixSize = 5;
p.testBreak = 10; % Number of Trials before break
% Color information
p.backCol = [150 150 150];
p.foreCol = p.backCol;
p.fixCol = [0 0 0];
p.fixWrong = [255 0 0];
p.fixCorrect = [0 255 0];
p.stimCol = [255 255 255];

eventPort = ['DCC8'];
% Timing stuff
p.encoding = 1; % Encoding Time
%p.encITI = .1; % Encoding ITI
p.trialBreak = 1; % Trials between breaks
p.recallDelay = 1; % 500 ms delay between probe and recall ring
p.ITI = .5;

%--------------------------------------------------------------------------
% Build the stimulus display
%--------------------------------------------------------------------------
if AnalysisMachine == 1
    s = 1
else
s = max(Screen('Screens'));    % Grab a handle for the display ID (should return 0 for single-monitor setups)
end                                              % grab and save the frame rate

if p.windowed                                                               % if we're debugging, open up a small window
    [w,p.sRect] = Screen('OpenWindow',s,p.backCol,[120 120 1024,720]);
else
    [w,p.sRect] = Screen('OpenWindow',s,p.backCol);                         % otherwise, go full-screen
    HideCursor;
    Priority(MaxPriority(w));                                               % set priority to max to discourage interruptions
end

% Turn on alpha blending. this makes drawing the stims much easier.
% Type Screen('BlendingFunction?') for more info.
Screen('BlendFunction',w,GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA);

% Compute and store the center of the screen
p.xCenter = (p.sRect(3)-p.sRect(1))/2;
p.yCenter = (p.sRect(4)-p.sRect(2))/2;

% Compute foreground and fixation rectangles
foreRect = p.sRect./1.5;
p.foreRect = CenterRect(foreRect,p.sRect);  % center the foreRect in p.sRect

% compute eccentricity of stimulus presentation
eccRect = [0 0 300 300];
p.eccRect = CenterRect(eccRect,p.sRect);
colorWheelRect = [0 0 600 600];
p.colorWheelRect = CenterRect(colorWheelRect,p.sRect);

% Stimulus Size
p.stimRect = [p.xCenter-p.stimSize/2,p.yCenter-p.stimSize/2,p.xCenter+p.stimSize/2,p.yCenter+p.stimSize/2];


%Brady Color Wheel prefs

prefs.colorWheelRadius = 350;
prefs.tempcolorwheel = [];
prefs.tempcolorwheel = load('colorwheel360.mat', 'fullcolormatrix');
prefs.originalcolorwheel = prefs.tempcolorwheel.fullcolormatrix;


p.fixRect = CenterRect([0 0 12 12],p.sRect);

% make a dummy call to GetSecs to load the .dll before we need it
dummy = GetSecs; clear dummy;

%--------------------------------------------------------------------------
% Scale RGB color values into CIE space - these will be used to render the
% clock rims
%--------------------------------------------------------------------------

CIE_L = 70;
CenterCIE_A = 20;
CenterCIE_B = 38;
[R,G,B] = MakeWheel(CIE_L,CenterCIE_A,CenterCIE_B);

%---------------------------------------------------
% Begin block loop
%---------------------------------------------------

% Build an output directory & check to make sure it doesn't already
% exist
p.root = pwd;
if ~exist([p.root, '\Subject Data\'], 'dir');
    mkdir([p.root, '\Subject Data\']);
end

% Build an output file and check to make sure that it doesn't exist yet
% either

fName = [p.root, '\Subject Data\', num2str(p.subNum),'_Block_1_','LTM_Retrieval_1.mat'];

if exist(fName)
    Screen('CloseAll');
    msgbox('File already exists!', 'modal')
    return;
end

%--------------------------------------------------------
% Preallocate some vectors to control experimental params
%--------------------------------------------------------

% Stimulus parameters:
stim.tStructure = nan(2,p.nTrials);
stim.config = nan(1,p.nTrials);

% Response params
stim.response = nan(1,p.nTrials);           % record ID of final response
stim.offset = nan(1,p.nTrials);             % record error
stim.rt = nan(1,p.nTrials);                 % record of rt
stim.ind = randi(180,1,p.nTrials);                % record of colorwheel index


% scramble trial order
stim.ltmStim = randperm(p.nTrials);
stim.imageOrder = stim.testItems(stim.ltmStim);     %order of items at test
stim.colors = testCol(stim.ltmStim);                %order of colors at test
stim.colorLTM = testColRGB(stim.ltmStim);           %order of RGB values at test
stim.retrievalblocktrial = testblocktrial(stim.ltmStim);
% ITI = repmat(p.ITI,1,(p.nTrials+4)/length(p.ITI)); ITIshuf = shuffle(ITI);
stim.ITI = p.ITI;
stim.blink = 1.5;
%--------------------------------------------------------
% Create and flip up the basic stimulus display
%--------------------------------------------------------

Screen('FillRect',w,p.foreCol,p.foreRect);            % Draw the foreground window
Screen('FillOval',w,p.fixCol,p.fixRect);              % Draw the fixation point
Screen('DrawingFinished',w);                        % Tell ptb we're done drawing for the moment (makes subsequent flip command execute faster)
Screen('Flip',w);                                         % Flip all the stuff we just drew onto the main display

%------------------------------------------------
% Define Stimulus Parameters Before starting block
%------------------------------------------------
% Cue Position
LcueLoc = [p.xCenter, p.yCenter-p.fixSize; p.xCenter-p.fixSize, p.yCenter; p.xCenter, p.yCenter+p.fixSize];
RcueLoc = [p.xCenter, p.yCenter-p.fixSize; p.xCenter+p.fixSize, p.yCenter; p.xCenter, p.yCenter+p.fixSize];

g = 1;
for t = 1:p.nTrials
    % Display for Block loading
    % This is totally useless but makes it look badass legit :)
    text1 = ['Experiment Loading'];
    tCenter1 = [p.xCenter-RectWidth(Screen('TextBounds', w, text1))/2 p.yCenter-120];
    text2 = [num2str(round2(g/p.nTrials,1e-2)*100), ' %'];
    tCenter2 = [p.xCenter-RectWidth(Screen('TextBounds', w, text2))/2 p.yCenter-70];
    Screen('FillRect',w,p.foreCol,p.foreRect);            % Draw the foreground window
    Screen('DrawText', w, text1, tCenter1(1), tCenter1(2), p.fixCol);
    Screen('DrawText', w, text2, tCenter2(1), tCenter2(2), p.fixCol);
    Screen('DrawingFinished', w);
    Screen('Flip', w);
    [keyIsDown,secs,keyCode]=KbCheck;
    if keyIsDown
        kp = find(keyCode); kp=kp(1);
        if kp == 27
            Screen('CloseAll')
            return
        end
    end
    g=g+1;
end
% Wait for a spacebar press to continue
while 1
    [keyIsDown,secs,keyCode]=KbCheck;
    if keyIsDown
        kp = find(keyCode);
        if kp == 32
            break;
        end
    end
end

%--------------------------------------------------------
% Create and flip up the basic stimulus display
%--------------------------------------------------------

Screen('FillRect',w,p.foreCol,p.foreRect);            % Draw the foreground window
Screen('FillOval',w,p.fixCol,p.fixRect);              % Draw the fixation point
Screen('DrawingFinished',w);                        % Tell ptb we're done drawing for the moment (makes subsequent flip command execute faster)
Screen('Flip',w);                                   % Flip all the stuff we just drew onto the main display

%-------------------------------------------------------
% Begin Trial Loop
%-------------------------------------------------------
cnt = 1;

for t = 1:p.nTrials
    
    HideCursor;
    
    if rem(t,p.testBreak)==0 && t>0
    text1 = sprintf('Start Retrieval %d of %d!',cnt/10, 20);
        tCenter1 = [p.xCenter-RectWidth(Screen('TextBounds', w, text1))/2 p.yCenter-120];
        Screen('FillRect',w,p.foreCol,foreRect);            % Draw the foreground window
        Screen('FillOval',w,p.fixCol,p.fixRect);           % Draw the fixation point
        Screen('DrawText', w, text1, tCenter1(1), tCenter1(2), p.fixCol);
        %Screen('DrawText', w, text2, tCenter2(1), tCenter2(2), p.fixCol);
        Screen('DrawingFinished', w);
        Screen('Flip', w);
        WaitSecs(1);
    end
    
    % Give subjects a break
    
    text1 = 'Press Spacebar to Continue';
    tCenter1 = [p.xCenter-RectWidth(Screen('TextBounds', w, text1))/2 p.yCenter-120];
    %         text2 = 'Press the spacebar to continue';
    %         tCenter2 = [p.xCenter-RectWidth(Screen('TextBounds', w, text2))/2 p.yCenter-70];
    Screen('FillRect',w,p.foreCol,foreRect);            % Draw the foreground window
    Screen('FillOval',w,p.fixCol,p.fixRect);           % Draw the fixation point
    Screen('DrawText', w, text1, tCenter1(1), tCenter1(2), p.fixCol);
    % Screen('DrawText', w, text2, tCenter2(1), tCenter2(2), p.fixCol);
    Screen('DrawingFinished', w);
    Screen('Flip', w);
    WaitSecs(.5);
    % Wait for a spacebar press to continue
    while 1
        [keyIsDown,secs,keyCode]=KbCheck;
        if keyIsDown
            kp = find(keyCode);
            if kp == 32
                break;
            end
            if kp == 27
                Screen('CloseAll')
                return
            end
        end
    end
    WaitSecs(.5);
    
    %write_parallel(eventPort,19)
    
    ltmImg = getStim_retrieval_brady(stim,p,t,stimRoot,w,p.stimCol);
   
    % wait the ITI
    Screen('FillPoly',w,p.fixCol,LcueLoc);
    Screen('FillPoly',w,p.fixCol,RcueLoc);            % Draw the fixation point
    Screen('DrawingFinished',w);
    Screen('Flip',w);
    
    [keyIsDown,secs,keyCode]=KbCheck;
    if keyIsDown
        kp = find(keyCode); kp=kp(1);
        if kp == 27
            Screen('CloseAll')
            return
        end
    end
    WaitSecs(stim.ITI);
    
    % draw stimuli
    Screen('DrawTexture',w,ltmImg,[],p.stimRect);
    Screen('FillPoly',w,p.fixCol,LcueLoc);
    Screen('FillPoly',w,p.fixCol,RcueLoc);
    Screen('DrawingFinished',w);
    Screen('Flip',w);
    %write_parallel(eventPort,01);
    WaitSecs(p.encoding);
    clear ltmImg
    %------------------------------------------------------------------
    % Figure out the change stuff
    %------------------------------------------------------------------
    %write_parallel(eventPort,02);
    [p,stim,prefs] = doRecallColor_Color(p,w,stim,stimRoot,t,testColRGB,prefs,portcode);
    %write_parallel(eventPort,03);
    stim.presentedColorDeg(t) = stim.colors(t);
    stim.presentedColorRad(t) = deg2rad(stim.presentedColorDeg(t));
    stim.offset(t) = (180/pi) .* (angle(exp(1i*stim.reportedColorRad(t))./exp(1i*stim.presentedColorRad(t))));
    
    sCol = testColRGB(:,stim.ltmStim(t));
    ltmImg = getStim_retrieval_brady(stim,p,t,stimRoot,w,sCol);
    % Screen('DrawTexture',w,ltmImg,[],p.stimRect)
    Screen('DrawTexture',w,ltmImg,[],p.stimRect)
    Screen('FillPoly',w,p.fixCol,LcueLoc);
    Screen('FillPoly',w,p.fixCol,RcueLoc);
    clear ltmImg
    Screen('DrawText',w,num2str(stim.offset(t)),p.xCenter,p.yCenter-150,[0 0 0]);
    Screen('DrawingFinished',w);
    Screen('Flip',w);
    WaitSecs(1);
    
%     if p.debug
%         Screen('DrawText',w,num2str(stim.offset(t)),p.xCenter,p.yCenter,[0 0 0]);
%         Screen('DrawingFinished',w);
%         Screen('Flip',w);
%         WaitSecs(.5);
%     end
    
    cnt = cnt +1;
    
    % save data file at the end of each block
    save(fName,'p','stim','prefs');
end  % end of trial loop

text1 = 'Task Complete!';
tCenter1 = [p.xCenter-RectWidth(Screen('TextBounds', w, text1))/2 p.yCenter-120];
text2 = 'Thanks for playing Memory Blaster 3000!';
tCenter2 = [p.xCenter-RectWidth(Screen('TextBounds', w, text2))/2 p.yCenter-70];
Screen('FillRect',w,p.foreCol,foreRect);            % Draw the foreground window
Screen('FillOval',w,p.fixCol,p.fixRect);           % Draw the fixation point
Screen('DrawText', w, text1, tCenter1(1), tCenter1(2), p.fixCol);
 Screen('DrawText', w, text2, tCenter2(1), tCenter2(2), p.fixCol);
Screen('DrawingFinished', w);
Screen('Flip', w);
WaitSecs(10);


% end of block loop

ListenChar(0);

% pack up and go home
Screen('CloseAll');
ShowCursor('Arrow');