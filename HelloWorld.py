picture1 = pickAFile();
picture2 = pickAFile();
picture3 = pickAFile();
picture4 = pickAFile();
picture5 = pickAFile();
picture6 = pickAFile();
picture7 = pickAFile();
picture8 = pickAFile();
picture9 = pickAFile();
picture10 = pickAFile();

pic1 = makePicture(picture1);
pic2 = makePicture(picture2);
pic3 = makePicture(picture3);
pic4 = makePicture(picture4);
pic5 = makePicture(picture5);
pic6 = makePicture(picture6);
pic7 = makePicture(picture7);
pic8 = makePicture(picture8);
pic9 = makePicture(picture9);
Final = makePicture(picture10);

list pics = [pic1, pic2, pic3, pic4, pic5, pic6, pic7, pic8, pic9, Final];
list colors;

x=0;
y=0;

 for a in range(494): #loop through rows of pixels
   x++;
   for b in range(556): #loop through columns of pixels
     y++;
     for i in range(8): #loop through all 9 pictures
       curerentPixel = getPixel(pics[i],x,y);
       col = getColor(currentPixel);
       colors.append(col);
   
    #At this point you have all 9 pixel colors in the colors list
    #Now sort the colors (?)
    #Pick out the median one, set it to medianColor variable
    #erase the contents of the colors list for the next pixel
    #set the color of the pixel in the final picture to the median color
    finalPixel = getPixel(pics[9],x,y)
    setColor(finalPixel,medianColor);
    
  
   
  
show(Final); # At the end of the loops Final should have the completed image
 

