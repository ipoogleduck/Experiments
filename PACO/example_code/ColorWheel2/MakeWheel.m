function [R,G,B]=MakeWheel(CIE_L,CenterCIE_A,CenterCIE_B)
% Convert CIE color values into RGB space for MATLAB. This allows you to 
% render a CIE color wheel. Calculations by KF, scripting by KF & EE, 6/08

% Initialize some starting parameters
CIE_a = zeros(1,180);
CIE_b = zeros(1,180);
XX = zeros(1,180);
YY = zeros(1,180);
ZZ = zeros(1,180);
R = zeros(1,180);
G = zeros(1,180);
B = zeros(1,180);
radius = 60;

% Convert CIE space to XYZ
for i = 1:180
    CurrentCIE_A = CenterCIE_A+radius*cos(2*i/360*2*pi);
    CurrentCIE_B = CenterCIE_B+radius*sin(2*i/360*2*pi);
    
    CIE_a(i)= CurrentCIE_A;
    CIE_b(i)= CurrentCIE_B;
    var_Y1 = ( CIE_L + 16 ) / 116;
    var_X1 = CurrentCIE_A / 500 + var_Y1;
    var_Z1 = var_Y1 - CurrentCIE_B / 200;

    if  var_Y1^3 > 0.008856
        var_Y1 = var_Y1^3;
    else
        var_Y1 = ( var_Y1 - 16 / 116 ) / 7.787;
    end
    if  var_X1^3 > 0.008856 
        var_X1 = var_X1^3;
    else
        var_X1 = ( var_X1 - 16 / 116 ) / 7.787;
    end
    if  var_Z1^3 > 0.008856 
        var_Z1 = var_Z1^3;
    else
        var_Z1 = ( var_Z1 - 16 / 116 ) / 7.787;
    end

    ref_X =  95.047; 
    ref_Y = 100.000;
    ref_Z = 108.883;

    X = ref_X * var_X1 ;   %ref_X =  95.047  
    Y = ref_Y * var_Y1 ;   %ref_Y = 100.000
    Z = ref_Z * var_Z1 ;    %ref_Z = 108.883

    XX(i) = X;
    YY(i) = Y;
    ZZ(i) = Z;

    %Converting XYG to RGB
    var_X = X / 100;        %X from 0 to  95.047      (Observer = 2¡, Illuminant = D65)
    var_Y = Y / 100;       %Y from 0 to 100.000
    var_Z = Z / 100;        %Z from 0 to 108.883

    var_R = var_X *  3.2406 + var_Y * -1.5372 + var_Z * -0.4986;
    var_G = var_X * -0.9689 + var_Y *  1.8758 + var_Z *  0.0415;
    var_B = var_X *  0.0557 + var_Y * -0.2040 + var_Z *  1.0570;

    if ( var_R > 0.0031308 ) 
        var_R = 1.055 * ( var_R ^ ( 1 / 2.4 ) ) - 0.055;
    else
        var_R = 12.92 * var_R;
    end
    if ( var_G > 0.0031308 ) 
        var_G = 1.055 * ( var_G ^ ( 1 / 2.4 ) ) - 0.055;
    else
        var_G = 12.92 * var_G;
    end
    if ( var_B > 0.0031308 ) 
        var_B = 1.055 * ( var_B ^ ( 1 / 2.4 ) ) - 0.055;
    else
        var_B = 12.92 * var_B;
    end

    current_R = var_R * 255; 
    current_G = var_G * 255;
    current_B = var_B * 255;

    R(i) = current_R;
    G(i) = current_G;
    B(i) = current_B;
end

R(R<0) = 0; R(R>255)=255;
G(G<0) = 0; G(G>255)=255;
B(B<0) = 0; B(B>255)=255;