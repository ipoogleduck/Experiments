function HowToRotateTest()
  % Which image to use:
  %Original:
  %fName = '/Volumes/bamlab/Experiments/COLOR/colorwheelcode_kuhl/ColorRotationStimuli/TestObjects/obj417.jpg';
  %Stimuli
  %%fName = '/Volumes/bamlab/Stimuli/Objects/Objects_from_CVP/object_129_1.jpg';
  %Color test folder
  fName = '/Volumes/bamlab/RA/Oliver/Images/blueTest.jpg';
  %fnameMAT = '/Volumes/bamlab/Experiments/COLOR/ColorWheel2/MemImages/Africa.mat';
  
  % Setup figure and load image:
  figure(1); %Graph
  set(gcf, 'Color', [1 1 1]); %????
  img = imread(fName); %%reads image and puts it into img array
 
  % Show every 10 degrees:
    %anglesShow = 0:10:360;
    %Angles to show:
    anglesShow = [0 90 180 270];
  for r = 1:length(anglesShow)
    subplot(6,6,r); %r is place in array
    imgOut = RotateImage(img, anglesShow(r));
    %figure(r); %comment this to display all on one graph
    imshow(imgOut);
  end
end

function img = RotateImage(img, angle)

  % Convert to LAB and correct format:
  img = double(img)/255; %devide by 255 which is max rgb value so that it goes to 
  disp("IMG Value before LAB conversion:")
  disp(img(1,1))
  
  lab = colorspace('rgb->lab', img);
  disp("LAB Value before rotation:")
  disp(lab(1,1))
  
  x = lab(:,:,2);
  y = lab(:,:,3);
  v = [x(:)'; y(:)'];
  dispvars = "X value is " + x(1,1) +", Y value is " + y(1,1) + ", v value is " + v(1,1);
  disp(dispvars)
  
  % Rotate:
  percentRotation = angle/360;
  theta = 2*pi*percentRotation;
  vo = [cos(theta) -sin(theta); sin(theta) cos(theta)] * v;
  
  % Reshape into correct format:
  lab(:,:,2) = reshape(vo(1,:), size(img,1), size(img,2));
  lab(:,:,3) = reshape(vo(2,:), size(img,1), size(img,2));
  img = uint8(colorspace('lab->rgb', lab) .* 255);
end