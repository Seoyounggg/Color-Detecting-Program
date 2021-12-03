# Color Detecting Program
Masking.py generates a binary image file separating a drone's route (white) and the part that is not(black) from a given color image by detecting the color of the drone's path. 
show 이미지
  
## Table of contents
* [Description](#description)
* [Instructions](#instructions)
* [Future goals](#future-goals)

## Description
For a self-driving drone, it is vital to recognize the color of the path received from its camera. However, there are some issues when using the camera’s image file.
1. Representing a color
- While RGB represents a color by combining red, green, and blue, HSV represents using the hue, saturation, and value of a color. In other words, HSV gives us the information of the color itself, not the combination with different colors. Therefore, HSV is a more appropriate method of representation when detecting an object. I converted the RGB image file into an HSV image file in this program.
2. Inconsistency of the path's color
- The image files received from the drone’s camera are sometimes of low quality. The external environment, such as the reflection of light, distorts the actual color of the path. To resolve this issue, the user clicks three different points in the image of the route where the colors seem different in this program. The program calculates the mean and standard deviation of colors and sets a range for the path’s color with this information.


## Instructions
1. Place the image file under the folder named test_data.
2. Run the mask_generator.py, then a window will pop up as below.
start 이미지
3. Click OPEN in the menu named FILE, and select the image file you want to convert.
select 이미지
4. After selecting the image file you want to convert, the follwoing window will appear.
after select 이미지
Left-click three different points where the color of the path seems different.
You can check how many times you have clicked on the window.
click 이미지
If you clicked more than three times, the program will tell you that you have exceeded the number of allowed clicks.
exceeded 이미지
5. After finishing clicking three times, press the SHOW button to see the converted image.
show 이미지
6. You can exit the program by either clicking the X button on the window or pressing EXIT in the menu name FILE.
You can find the converted file at the same path with the mask_generator.py file.


## Future goals
Right now,
