function MakeAbridgedImageNames120

load WBImageNames;
load BImageNames;
ImageNames = horzcat(WBImageNames,BImageNames);
ImageNames = randsample(ImageNames,120);

save('ImageNames')