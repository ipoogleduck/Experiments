function [p,stim,prefs] = doRecallColor_Color(p,w,stim,stimRoot,t,testColRGB,prefs,portcode)

rtStart = GetSecs;
SetMouse(p.xCenter,p.yCenter);
ShowCursor('Arrow');
sCol = [];
%prefs.colorwheeltemp = prefs.colorwheel;
prefs.colorWheelSizes = 25;
prefs.colorWheelRadius = 350;
prefs.colorWheelLocations = [cosd([1:360]).*prefs.colorWheelRadius; ...
    sind([1:360]).*prefs.colorWheelRadius];
prefs.ind(t,1) = ceil(randsample(360,1));  % setting prefs.ind == 0 would be NO change in color wheel position.
ind = wshift('1d',1:360,prefs.ind(t,1));
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
    
    if(everMovedFromCenter)
        sCol = prefs.colorwheel(minDistanceIndex,:);
    else
        sCol = [255 255 255];
        while any(buttons)
            [x,y,buttons] = GetMouse(w);
        end
        if p.debug
            sCol = testColRGB(:,stim.ltmStim(t));
            %stim.reportedColor(t) = NaN;
        end
    end
    %%%%%worked before adding this%%%%%%
    ltmImg = getStim_retrieval_brady(stim,p,t,stimRoot,w,sCol);
    
    Screen('DrawTexture',w,ltmImg,[],p.stimRect);
    Screen('FillPoly',w,p.fixCol,LcueLoc);
    Screen('FillPoly',w,p.fixCol,RcueLoc);  
    Screen('DrawingFinished',w);
    Screen('Flip',w);
    clear ltmImg
    Screen('Close')
end

if(everMovedFromCenter)
    display(minDistanceIndex);
    if minDistanceIndex+prefs.ind(t)>360
        stim.reportedColor(t) = minDistanceIndex+prefs.ind(t)-360;
    else
        stim.reportedColor(t) = minDistanceIndex+prefs.ind(t);
    end
    %Gives actual reported color as number of degrees (already been
    %corrected for color wheel shift).
    stim.reportedColorDeg(t) = stim.reportedColor(t);
    %Converts to Radians 
    stim.reportedColorRad(t) = deg2rad(stim.reportedColor(t));
    rtEnd = GetSecs;
    stim.rt(t) = rtEnd-rtStart;
    stim.notguess(t) = buttons(1);
    stim.guess(t) = buttons(3);
    stim.notfollowingintructions(t) = buttons(2);
    HideCursor;
end



%clear prefs.colorwheel
%
%
% calculating x&y coords in trig unit
% sin_mouse = (stim.tLoc(t,2) - p.yCenter)/sqrt((stim.tLoc(t,1) - p.xCenter)^2+(stim.tLoc(t,2) - p.yCenter)^2);   % based on the radius given here (tLoc-yCenter), this shows y in trigonometric functions
% cos_mouse = (stim.tLoc(t,1) - p.xCenter)/sqrt((stim.tLoc(t,1) - p.xCenter)^2+(stim.tLoc(t,2) - p.yCenter)^2);   % '' for x
%
% trig unit is now converted to degree (0deg starts off from the standard position and goes clockwise)
% if sin_mouse > 0 && cos_mouse > 0                           % 0-90degrees
%     mouse_angle = atan(sin_mouse/cos_mouse);
% elseif sin_mouse > 0 && cos_mouse < 0                       % 90-180degrees
%     mouse_angle = atan(sin_mouse/cos_mouse)+pi;
% elseif sin_mouse < 0 && cos_mouse < 0                       % 180-270degrees
%     mouse_angle = atan(sin_mouse/cos_mouse)+pi;
% elseif sin_mouse < 0 && cos_mouse > 0                       % 270-360degrees
%     mouse_angle = atan(sin_mouse/cos_mouse)+2*pi;
% elseif sin_mouse == 0 && cos_mouse == 1                     % 0degree
%     mouse_angle = 0;
% elseif sin_mouse == 1 && cos_mouse == 0                     % 90degrees
%     mouse_angle = pi/2;
% elseif sin_mouse == 0 && cos_mouse == -1                    % 180 degrees
%     mouse_angle = pi;
% elseif sin_mouse == -1 && cos_mouse == 0                    % 270 degrees
%     mouse_angle = 3/2*pi;
% end;
%
% compute test color
% probed_angle = (stim.ind(t)-1)*2+stim.colors(t)*2-1;   % computing the original angle of probed color
%
% Compute probed color angle
% if probed_angle > 360 && probed_angle < 720
%     probed_angle = probed_angle-360;
% elseif probed_angle > 720
%     probed_angle = probed_angle-720;
% end;
%
% calculate offset of subject response from actual color value
% tAngle = round(probed_angle);
% stim.tAngle(t) = tAngle;
%
% calculate offset of subject response and actual angle
% sAngle = round(mouse_angle/2/pi*360); stim.sAngle(t) = sAngle;
% stim.offset(t) = sAngle-tAngle;
%
% if stim.offset(t) > 180
%     stim.offset(t) = stim.offset(t)-360;
% elseif stim.offset(t) < -180
%     stim.offset(t) = stim.offset(t)+360;
% end

%     function drawColorWheel(window, prefs)
%     colorWheelLocations = [cosd([1:360]).*prefs.colorWheelRadius + window.centerX; ...
%         sind([1:360]).*prefs.colorWheelRadius + window.centerY];
%     colorWheelSizes = 25;  %Original: 20
%     Screen('DrawDots', window.onScreen, colorWheelLocations, colorWheelSizes, prefs.colorwheel', [], 1);
%     end
%
%     function L = colorwheelLocations(window,prefs)
%     L = [cosd([1:360]).*prefs.colorWheelRadius + window.centerX; ...
%         sind([1:360]).*prefs.colorWheelRadius + window.centerY];
%     end