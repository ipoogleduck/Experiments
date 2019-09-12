

a = dir('*.png');

for i=1:length(a)
    
     img = imread(a(i).name);
     
     % If the image is not grayscale then read it in with appropriate
     % background setting, otherwise read
     if size(img,3) == 3
         img = imread(a(i).name,'BackgroundColor',[1 1 1]);
         img = rgb2gray(img);
     else
         img = imread(a(i).name, 'BackgroundColor', 1);
     end
     
    pix = size(img);
    ratio = pix(1)./pix(2);
    if ratio > .85 && ratio < 1.176
        img2 = imresize(img,[262 232]);
    else
        if pix(1) < pix(2)
            dd = pix(2) - pix(1);
            whitespace = 255*ones(ceil(dd/2),pix(2));
            img2 = [whitespace; img; whitespace];
            img2 = imresize(img2,[262 232]);
        else
            dd = pix(1) - pix(2);
            whitespace = 255*ones(pix(1),ceil(dd./2));
            img2 = [whitespace, img, whitespace];
            img2 = imresize(img2,[262 232]);
        end
    end
    % Make sure you tell it where you want the images to go
    imwrite(img2,['/Volumes/bamlab/Experiments/PACO/Stimuli/resized/' a(i).name],'PNG');
    
end