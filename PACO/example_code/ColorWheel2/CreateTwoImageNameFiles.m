load allimagenames

allimagenames = shuffle(allimagenames);

ImageNames1 = allimagenames(1:200);
ImageNames2 = allimagenames(201:400);

save('ImageNames1')
save('ImageNames2')