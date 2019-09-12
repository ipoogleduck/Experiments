function NewimportImages

root = [pwd,'/'];
ftype = '.png';
fn = dir([root, 'images/*',ftype]);
nImages = size(fn,1);

outFolder = [root,'MemImages/'];
BG = [1 1 1]; % Default Background Color

imgNames = [];
bad = [];
for i = 1:nImages % 6
    i
    iname = fn(i).name
    img = [root, 'images/',iname];
    image = imread(img,'png','BackgroundColor',BG);
    imgOut = [outFolder,[iname(1:end-length(ftype)),'.mat']];
    save(imgOut,'image')
    imgNames = [imgNames, {fn(i).name}];
end

outName = [outFolder,'ImageNames.mat'];
%cd X:\Sutterer\LTM   didn't work
save(outName,'imgNames')