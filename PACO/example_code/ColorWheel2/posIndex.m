function [xPos, yPos] = posIndex(xLocInd,yLocInd,minDist,numItems)

while 1
    critCnt = 0;
    xCoords = shuffle(xLocInd);
    yCoords = shuffle(yLocInd);
    coords = [xCoords; yCoords];

    locInd = randperm(length(xCoords));
    xPos = coords(1,locInd(1:numItems));
    yPos = coords(2,locInd(1:numItems));
    cnt1=0;
    for a = 1:length(xPos)
        for b = 1:length(yPos)
                cnt1=cnt1+1;
            if a~=b
                if sqrt((xPos(a)-xPos(b))^2+(yPos(a)-yPos(b))^2)>minDist
                    critCnt=critCnt+1;
                end
            end
        end
    end
    if critCnt==(length(xPos)*length(yPos))-length(xPos)
        break
    end
end
                    