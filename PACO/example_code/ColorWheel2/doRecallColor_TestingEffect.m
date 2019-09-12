function [p,stim,prefs] = doRecallColor_TestingEffect(p,w,stim,stimRoot,b,prefs,portcode)

rtStart = GetSecs;
SetMouse(p.xCenter,p.yCenter);
ShowCursor('Arrow');
sCol = [];
%prefs.colorwheeltemp = prefs.colorwheel;
prefs.colorWheelSizes = 25;
prefs.colorWheelRadius = 350;
prefs.colorWheelLocations = [cosd([1:360]).*prefs.colorWheelRadius; ...
    sind([1:360]).*prefs.colorWheelRadius];
prefs.ind(b,1) = ceil(randsample(360,1));  % setting prefs.ind == 0 would be NO change in color wheel position.
ind = wshift('1d',1:360,prefs.ind(b,1));
prefs.colorwheel = prefs.originalcolorwheel(ind,:);

LcueLoc = [p.xCenter, p.yCenter-p.fixSize; p.xCenter-p.fixSize, p.yCenter; p.xCenter, p.yCenter+p.fixSize];
RcueLoc = [p.xCenter, p.yCenter-p.fixSize; p.xCenter+p.fixSize, p.yCenter; p.xCenter, p.yCenter+p.fixSize];

% % compute eccentricity of color wheel


[x,y,buttons] = GetMouse(w);
while any(buttons)
    [x,y,buttons] = GetMouse(w);
end

everMovedFromCenter = false;

while ~any(buttons)
    %if block type is memory (1)
    
    %Original: 20
    %Screen('DrawDots', w, prefs.colorWheelLocations, prefs.colorWheelSizes, prefs.colorwheel', [], 1);
    for i = 1:360
        color = prefs.colorwheel;
        Screen('FrameArc',w,color(i,:),p.colorWheelRect,(i-1)*1+90,p.penArc,p.colPen,p.colPen);
        
    end
    [x,y,buttons] = GetMouse(w);
    [minDistance, minDistanceIndex] = min(sqrt((prefs.colorWheelLocations(1, :)+p.xCenter - x).^2 + (prefs.colorWheelLocations(2, :)+p.yCenter - y).^2));
    
    if(minDistance < 299)
        everMovedFromCenter = true;
    end
    
    if stim.blocktype(stim.cnt) == 1
        if(everMovedFromCenter)
            sCol = prefs.colorwheel(minDistanceIndex,:);
        else
            sCol = [255 255 255];
            while any(buttons)
                [x,y,buttons] = GetMouse(w);
            end
            if p.debug
                sCol = stim.alltestColRGB(:,b);
                %stim.reportedColor(t) = NaN;
            end
        end
    else
        if(everMovedFromCenter)
            sCol = stim.alltestColRGB(:,b);
        else
            sCol = stim.alltestColRGB(:,b);
            while any(buttons)
                [x,y,buttons] = GetMouse(w);
            end
        end
    end
    %%%%%worked before adding this%%%%%%
    ltmImg = getStim_retrieval_brady_encoding(stim,p,b,stimRoot,w,sCol);
    
    Screen('DrawTexture',w,ltmImg,[],p.stimRect);
    Screen('FillPoly',w,p.fixCol,LcueLoc);
    Screen('FillPoly',w,p.fixCol,RcueLoc);
    Screen('DrawingFinished',w);
    Screen('Flip',w);
    clear ltmImg
    Screen('Close')
    stim.blocktrial(b) = stim.blocktype(stim.cnt);
end


if(everMovedFromCenter)
    display(minDistanceIndex);
    if minDistanceIndex+prefs.ind(b)>360
        stim.reportedColor(b) = minDistanceIndex+prefs.ind(b)-360;
    else
        stim.reportedColor(b) = minDistanceIndex+prefs.ind(b);
    end
    %Gives actual reported color as number of degrees (already been
    %corrected for color wheel shift).
    stim.reportedColorDeg(b) = stim.reportedColor(b);
    stim.reportedColorRad(b) = deg2rad(stim.reportedColor(b));
    stim.trialblock(b) = stim.blocktype(stim.cnt);
    rtEnd = GetSecs;
    stim.rt(b) = rtEnd-rtStart;
    stim.notguess(b) = buttons(1);
    stim.guess(b) = buttons(3);
    stim.notfollowingintructions(b) = buttons(2);
    HideCursor;
end

clear ltmImg


