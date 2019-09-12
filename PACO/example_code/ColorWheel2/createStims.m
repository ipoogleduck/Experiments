function [discMat,recallLoc,probeLoc] = createStims(p,xPos,yPos,setSize,ss)

discMat = [];
for arc = 1:max(setSize)
    x1 = xPos(arc)-p.stimSize/2; y1 = yPos(arc)-p.stimSize/2; x2 = xPos(arc)+p.stimSize/2; y2 = yPos(arc)+p.stimSize/2;
    discPos = [x1 y1 x2 y2]';
    discMat = [discMat, discPos];
end;

% defining location and shape of probe circle
probeLoc = randsample(ss,1);
probeX1 = xPos(probeLoc)-p.stimSize/2;
probeX2 = xPos(probeLoc)+p.stimSize/2;
probeY1 = yPos(probeLoc)-p.stimSize/2;
probeY2 = yPos(probeLoc)+p.stimSize/2;

recallLoc = [probeX1 probeY1 probeX2 probeY2];