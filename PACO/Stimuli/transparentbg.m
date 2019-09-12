%% Makes background of black and white images transparent
% Author: Stefania Ashby
% Date: 6.28.19

%%%% What does it do? %%%%
% Will take a black image with white background, invert the image so that
% the foreground is white, and then make the background transparent.
% See function file ('removebg.m') in general lab stimulus directory
% for more functionality.


% List all file names in your working directory (run script from directory
% with all your images).
% fdir = sprintf('%s/resized/', pwd);
% images = dir([fdir '*.png']);
% outdir = 'inverted2';

images = dir('*.png');
outdir = 'inverted2';

for i = 1:length(images)
    im_src = images(i).name; % input image
    im_out = sprintf('%s/%s/%s', pwd, outdir, images(i).name); % output image in new directory
    
    % Next we load the image in and invert black and white
    RGB_in = imcomplement( imread(im_src ));
    
    % We need to make a new matrix of the same size as the image to use for
    % writing out with transparent background. 
    [m, n] = size( RGB_in(:,:,1) );
    idx1 = ones(m, n)*255; % Use 255 here becaue we want the foreground to be white
    
    % Changes index -- takes everything in the original image that is not labeled as white
    % and makes it transparent in index
    idx1( RGB_in(:,:,1) < 255) = 0;
    
    % Use index as "alpha" when writing out the image. Will give you a white foreground and transparent background
    imwrite( RGB_in, im_out, 'png', 'Alpha', idx1 );
end

clear all
   
