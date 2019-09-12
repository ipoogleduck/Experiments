
function MemoryvsStudy_Blocked1

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
    p.subNum = num2str(box{1}); p.rndSeed = str2num(box{2});
    rand('state',p.rndSeed);                                                % seed the generator
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

% Load Stimulus Texture Index
root = pwd;
stimRoot = [root,'/MemImages/'];
fName = [root,'/ImageNames1.mat'];
load(fName);
%nStims = length(imgNames);
stim.ImageNames = ImageNames1;


% Turn off keyboard echoing
ListenChar(2);

%--------------------------------------------------------------------------
% General Experimental Parameters
%--------------------------------------------------------------------------
portcode = 'cc98';
nStims = length(stim.ImageNames);
%x = 1:nStims;w
stim.nRepeat = 0;
p.nTrials = nStims+stim.nRepeat;
stim.repeat = randsample(stim.ImageNames,stim.nRepeat);
p.windowed = 0;
p.debug = 0;

% stim geometry (in pixels):
p.stimSize = 300;
p.colPen = 50;
p.penArc = 2;
p.fixSize = 5;

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
p.trialBreak = 1; % Trials between breaks
p.testBreak =10; % Number of Trials before break
p.feedback = .25;
p.recallDelay = 1; % 500 ms delay between probe and recall ring Change here for EEG
p.ITI = .5;

%--------------------------------------------------------------------------
% Build the stimulus display
%--------------------------------------------------------------------------
if AnalysisMachine == 1
    s = 1;
else
s = max(Screen('Screens'));    % Grab a handle for the display ID (should return 0 for single-monitor setups)
end                                              % grab and save the frame rate

s = 0;
[w,p.sRect] = Screen('OpenWindow',s,p.backCol,[120 120 1024,720]);

% if p.windowed                                                               % if we're debugging, open up a small window
%     [w,p.sRect] = Screen('OpenWindow',s,p.backCol,[120 120 1024,720]);
% else
%     [w,p.sRect] = Screen('OpenWindow',s,p.backCol);                         % otherwise, go full-screen
%     HideCursor;
%     Priority(MaxPriority(w));                                               % set priority to max to discourage interruptions
% end

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
%New Color Wheel Prefs

prefs.colorWheelRadius = 350;
prefs.originalcolorwheel = [];
prefs.originalcolorwheel = load('colorwheel360.mat', 'fullcolormatrix');
prefs.originalcolorwheel = prefs.originalcolorwheel.fullcolormatrix;

% %compute eccentricity of color wheel
% colWheelRect = [0 0 600 600];
% p.colWheelRect = CenterRect(colWheelRect,p.sRect);

% Center fixation textures on the main display
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

fName = [p.root, '\Subject Data\', num2str(p.subNum),'_Block_1_','LTM_Encoding.mat'];

if exist(fName)
    Screen('CloseAll');
    msgbox('File already exists!', 'modal')
    return;
end

%--------------------------------------------------------
% Preallocate some vectors to control experimental params
%--------------------------------------------------------
stim.alltestItems = []; stim.alltestColRGB = []; stim.alltestCol = [];
% Stimulus parameters:
stim.tStructure = nan(2,p.nTrials);
stim.config = nan(1,p.nTrials);
%stim.colors = [];
%stim.colorLTM = nan(3,p.nTrials);
stim.repeatColorLTM = nan(3,p.nTrials);



% Response params
stim.response = nan(1,p.nTrials);           % record ID of final response
stim.offset = nan(1,p.nTrials);             % record error
stim.rt = nan(1,p.nTrials);
% ITI = repmat(p.ITI,1,(p.nTrials+4)/length(p.ITI)); ITIshuf = Shuffle(ITI);
stim.ITI = p.ITI;
% randomly select 12 positions in the trial order to repeat to
% duplicate from image order
% stim.duplicate = randperm(p.nTrials);
% stim.duplicate = stim.duplicate(1:12);
% scramble trial order
stim.ltmStim = randperm(nStims);
blocktype1 = ones(1,((p.nTrials/p.testBreak)/2));
blocktype2 = ones(1,((p.nTrials/p.testBreak)/2))*2;
blocktype = horzcat(blocktype1,blocktype2);
stim.blocktype = Shuffle(blocktype);
stim.trialblock = nan(1,p.nTrials);
stim.alltestIndex = nan(1,p.nTrials);
%stim.blocktype = stim.blocktype(stim.ltmStim);
stim.imageOrder = stim.ImageNames(stim.ltmStim);
stim.blocktrial = nan(1,p.nTrials);
miniblockpresentationorder = [1:10];
stim.miniblockpresorder = repmat(miniblockpresentationorder,1,20);
miniblocktestorder = [1:10];
stim.miniblocktestorder = repmat(miniblocktestorder,1,20);
stim.imgOrderRep = [];
for i = 1:nStims
    stim.imgOrderRep = [stim.imgOrderRep, stim.imageOrder(i)];
    if sum(ismember(stim.repeat,stim.imageOrder(i)))
        stim.imgOrderRep = [stim.imgOrderRep, stim.imageOrder(i)];
    end
end


colors = [];
% Determine orientation & color
% Determine which colors to repeat
ind = 1:nStims;
%Creates a logical with a list of ones and zeros that list the locations of
%where the images repeat
imgInd = ismember(stim.imageOrder,stim.repeat);
%this then creates a matrix with the actual value of the index values
colRepeat = ind(imgInd);
%runs through and makes a vector of random numbers form 1 to 360 which we
%cn assign rgb values.
for c = 1:nStims
    col = ceil(rand(1,1)*360);
    colors=[colors,col];
    if sum(ismember(colRepeat,c))
        colors = [colors,col];
        
    end
    
end
stim.colors = colors;
for d = 1:length(stim.colors)
    stim.colorLTM(:,d) = prefs.originalcolorwheel(stim.colors(d), :)';
end

TF = [];
for g = 2:p.nTrials
    TF(g) = strcmp(stim.imgOrderRep(g),stim.imgOrderRep(g-1));
end
stim.duplicate = TF;
%--------------------------------------------------------
% Create and flip up the basic stimulus display
%--------------------------------------------------------

Screen('FillRect',w,p.foreCol,p.foreRect);            % Draw the foreground window
Screen('FillOval',w,p.fixCol,p.fixRect);              % Draw the fixation point
Screen('DrawingFinished',w);                        % Tell ptb we're done drawing for the moment (makes subsequent flip command execute faster)
Screen('Flip',w);                                   % Flip all the stuff we just drew onto the main display

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
    [keyIsDown,secs,keyCode]=KbCheck(-1);
    if keyIsDown
        kp = find(keyCode); kp=kp(1);
        if kp == 27
            Screen('CloseAll')
            return
        end
    end
    g=g+1;
end
clear g
% Display for Block loading
text2 = 'Press the spacebar to continue';
tCenter2 = [p.xCenter-RectWidth(Screen('TextBounds', w, text2))/2 p.yCenter-70];
Screen('FillRect',w,p.foreCol,p.foreRect);            % Draw the foreground window
% Screen('FillOval',w,p.fixCol,p.fixRect);           % Draw the fixation point
Screen('DrawText', w, text2, tCenter2(1), tCenter2(2), p.fixCol);
Screen('DrawingFinished', w);
Screen('Flip', w);
WaitSecs(.5);

% Wait for a spacebar press to continue
while 1
    [keyIsDown,secs,keyCode]=KbCheck(-1);
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
Screen('DrawingFinished',w);                          % Tell ptb we're done drawing for the moment (makes subsequent flip command execute faster)
Screen('Flip',w);                                     % Flip all the stuff we just drew onto the main display

%-------------------------------------------------------
% Begin Trial Loop
%-------------------------------------------------------
stim.cnt = 1;
for t = 1:p.nTrials
    HideCursor
    %%write_parallel(portcode,17);
    % Give subjects a break
    text1 = 'Press Spacebar to Continue';
    tCenter1 = [p.xCenter-RectWidth(Screen('TextBounds', w, text1))/2 p.yCenter-120];
    Screen('FillRect',w,p.foreCol,foreRect);            % Draw the foreground window
    Screen('FillOval',w,p.fixCol,p.fixRect);           % Draw the fixation point
    Screen('DrawText', w, text1, tCenter1(1), tCenter1(2), p.fixCol);
    Screen('DrawingFinished', w);
    Screen('Flip', w);
    WaitSecs(.5);
    
    % Wait for a spacebar press to continue
    while 1
        [keyIsDown,secs,keyCode]=KbCheck(-1);
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
    
    %write_parallel(eventPort,17)
    
    sCol = stim.colorLTM(:,t)
    xx = stim.imgOrderRep(t)
    % wait the fixaStion interval
    
    Screen('FillPoly',w,p.fixCol,LcueLoc);
    Screen('FillPoly',w,p.fixCol,RcueLoc);            % Draw the fixation point
    Screen('DrawingFinished',w);
    Screen('Flip',w);
    %     %write_parallel(portcode,1);
    WaitSecs(stim.ITI);
    ltmImg = getStim_repeat_brady(stim,p,t,stimRoot,w,sCol);
    
    % draw stimuli
    
    Screen('DrawTexture',w,ltmImg,[],p.stimRect);
    Screen('FillPoly',w,p.fixCol,LcueLoc);
    Screen('FillPoly',w,p.fixCol,RcueLoc);
    Screen('DrawingFinished',w);
    Screen('Flip',w);
    %write_parallel(eventPort,01)
    [keyIsDown,secs,keyCode]=KbCheck(-1);
    if keyIsDown
        kp = find(keyCode); kp=kp(1);
        if kp == 27
            Screen('CloseAll')
            return
        end
    end
    WaitSecs(p.encoding)
    %write_parallel(eventPort,02)
    
    
    clear ltmImg
    
    
    % stop every 10 items and conduct a retrieval period
    if rem(t,p.testBreak)==0 && t>0
        
        %pick out the trial numbers that need to be tested
        stim.testIndex = []; stim.testItems = []; testColRGB = [];
        stim.testIndex = Shuffle((t-p.testBreak+1):t);
        %snag items then Shuffle order before testing
        stim.testItems = stim.imgOrderRep(stim.testIndex);
        stim.alltestItems = [stim.alltestItems,stim.testItems];
        testColRGB = stim.colorLTM(:,stim.testIndex);
        stim.alltestColRGB = [stim.alltestColRGB,testColRGB];
        testcol = stim.colors(stim.testIndex);
        stim.alltestCol = [stim.alltestCol,testcol];
        stim.alltestIndex = [stim.alltestIndex,stim.testIndex];
       

        
        text1 = sprintf('Start Retrieval %d of %d!',stim.cnt, 20);
        tCenter1 = [p.xCenter-RectWidth(Screen('TextBounds', w, text1))/2 p.yCenter-120];
        Screen('FillRect',w,p.foreCol,foreRect);            % Draw the foreground window
        Screen('FillOval',w,p.fixCol,p.fixRect);           % Draw the fixation point
        Screen('DrawText', w, text1, tCenter1(1), tCenter1(2), p.fixCol);
        %Screen('DrawText', w, text2, tCenter2(1), tCenter2(2), p.fixCol);
        Screen('DrawingFinished', w);
        Screen('Flip', w);
        WaitSecs(1);
        
        for b = (t-p.testBreak+1):t
            
            % Allow Subj Time to Press Space Bar
            text1 = 'Press Spacebar to Continue';
            tCenter1 = [p.xCenter-RectWidth(Screen('TextBounds', w, text1))/2 p.yCenter-120];
            Screen('FillRect',w,p.foreCol,foreRect);            % Draw the foreground window
            Screen('FillOval',w,p.fixCol,p.fixRect);           % Draw the fixation point
            Screen('DrawText', w, text1, tCenter1(1), tCenter1(2), p.fixCol);
            Screen('DrawingFinished', w);
            Screen('Flip', w);
            WaitSecs(.5);
            
            % Wait for a spacebar press to continue
            while 1
                [keyIsDown,secs,keyCode]=KbCheck(-1);
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
            
            %Trial Code for MiniBlock Retrieval
             stim.trialblock(b) = stim.blocktype(stim.cnt);
             sCol = stim.alltestColRGB(:,b);
             if stim.blocktype(stim.cnt) == 1
                 ltmImg = getStim_retrieval_brady_encoding(stim,p,b,stimRoot,w,p.stimCol);
             else
                 ltmImg = getStim_retrieval_brady_encoding(stim,p,b,stimRoot,w,sCol);
             end
            Screen('FillPoly',w,p.fixCol,LcueLoc);
            Screen('FillPoly',w,p.fixCol,RcueLoc);            % Draw the fixation point
            Screen('DrawingFinished',w);
            Screen('Flip',w);
            %write_parallel(portcode,5);
            [keyIsDown,secs,keyCode]=KbCheck(-1);
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
            WaitSecs(p.recallDelay);
            clear ltmImg
           
            %do recall
            %Start Function to recall Item
            %write_parallel(eventPort,02)
            [p,stim,prefs] = doRecallColor_TestingEffect(p,w,stim,stimRoot,b,prefs,portcode);
            %write_parallel(eventPort,03)
            HideCursor;
            %Figure how how they did
            stim.presentedColor(b) = stim.alltestCol(b);
            %look at presented color and reported color in degrees (useful
            %for plots of absolute color responses
            stim.presentedColorDeg(b) = stim.presentedColor(b);
            stim.degreeoffset(b) = stim.reportedColorDeg(b) - stim.presentedColorDeg(b);
            %gg = stim.degreeoffset(b);
            %Compare Presented to Reported in Radians
            stim.presentedColorRad(b) = deg2rad(stim.presentedColor(b));
            stim.offset(b) = (180/pi) .* (angle(exp(1i*stim.reportedColorRad(b))./exp(1i*stim.presentedColorRad(b))));
            %Show Subject the correct color of the item as well as how far
            %off they were
            sCol = stim.alltestColRGB(:,b);
            
            
            %Uncomment this to add feedback during the learning period.
            %Useful for checking changes to the code. 
            
            %Create the item for display
%             ltmImg = getStim_retrieval_brady_encoding(stim,p,b,stimRoot,w,sCol);
%             Screen('DrawTexture',w,ltmImg,[],p.stimRect)
%             Screen('FillPoly',w,p.fixCol,LcueLoc);
%             Screen('FillPoly',w,p.fixCol,RcueLoc);
%             clear ltmImg
%             Screen('DrawText',w,num2str(stim.offset(b)),p.xCenter,p.yCenter-150,[0 0 0]);
%             Screen('DrawingFinished',w);
%             Screen('Flip',w);
%             WaitSecs(1);
        end
        
        stim.cnt = stim.cnt + 1;
        if stim.cnt < 21
            text2 = sprintf('Press Spacebar to Start Encoding Block %d of %d',stim.cnt, 20);
            tCenter1 = [p.xCenter-RectWidth(Screen('TextBounds', w, text2))/2 p.yCenter-120];
            Screen('FillRect',w,p.foreCol,foreRect);            % Draw the foreground window
            Screen('FillOval',w,p.fixCol,p.fixRect);           % Draw the fixation point
            Screen('DrawText', w, text2, tCenter1(1), tCenter1(2), p.fixCol);
            Screen('DrawingFinished', w);
            Screen('Flip', w);
            WaitSecs(.5);
        end
        % Wait for a spacebar press to continue
        while 1
            [keyIsDown,secs,keyCode]=KbCheck(-1);
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
    end
    save(fName,'p','stim');
end
% save data file at the end of each block
save(fName,'p','stim','prefs');                                             % end of block loop

text1 = 'Task Complete!';
tCenter1 = [p.xCenter-RectWidth(Screen('TextBounds', w, text1))/2 p.yCenter-120];
text2 = 'Thanks for playing Memory Blaster 3000 Part 1!';
tCenter2 = [p.xCenter-RectWidth(Screen('TextBounds', w, text2))/2 p.yCenter-70];
Screen('FillRect',w,p.foreCol,foreRect);            % Draw the foreground window
Screen('FillOval',w,p.fixCol,p.fixRect);           % Draw the fixation point
Screen('DrawText', w, text1, tCenter1(1), tCenter1(2), p.fixCol);
% Screen('DrawText', w, text2, tCenter2(1), tCenter2(2), p.fixCol);
Screen('DrawingFinished', w);
Screen('Flip', w);
WaitSecs(2);

ListenChar(0);
% pack up and go home
Screen('CloseAll');
ShowCursor('Arrow');