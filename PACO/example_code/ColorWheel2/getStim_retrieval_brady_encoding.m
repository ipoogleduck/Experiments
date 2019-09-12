function imgTxt = getStim_retrieval_brady(stim,p,b,stimRoot,w,sCol)

tmpStim = stim.alltestItems(b);
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
tmp(:,:,1) = sCol(1);
tmp(:,:,2) = sCol(2);
tmp(:,:,3) = sCol(3);

tmp(backInd) = p.backCol(1);

image = tmp;
imgTxt = Screen('MakeTexture',w,image);

clear img tmp backInd image i sCol 
