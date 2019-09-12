function imgTxt = getStim(stim,p,t,stimRoot,w,col)

tmpStim = stim.imgOrderRep(t);
ftype = 'png';
iName = [stimRoot,char(tmpStim)];
iName = [iName(1:end-length(ftype)),'mat'];
img = load(iName);
if max(img.image(:))==1
    img.image = img.image.*255;
end
i = img.image;
if length(size(i))==2
    i = repmat(i,[1,1,3]);
end

backInd = i==255;
tmp = zeros(size(i,1),size(i,2),3);
tmp(:,:,1) = col(1);
tmp(:,:,2) = col(2);
tmp(:,:,3) = col(3);

tmp(backInd) = p.backCol(1);

image = tmp;
imgTxt = Screen('MakeTexture',w,image);

clear img tmp backInd image i