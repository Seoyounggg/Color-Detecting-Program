# Color Detecting Program
Masking.py generates a binary image file separating a drone's route (white) and the part that is not(black) from a given color image by detecting the color of the drone's path.  
<p align="center"><img width="300" alt="show" src="https://user-images.githubusercontent.com/42035101/144532804-4702c015-f7ee-4606-83fe-ea2294a840e4.PNG"></p>
  
## Table of contents
* [Description](#description)
* [Instructions](#instructions)
* [Future goals](#future-goals)

## Description
For a self-driving drone, it is vital to recognize the color of the path received from its camera. However, there are some issues when using the camera’s image file.
1. Representing a color
- While RGB represents a color by combining red, green, and blue, HSV represents using the color's hue, saturation, and value. In other words, HSV gives us the information of the color itself, not the combination with different colors. Therefore, HSV is a more appropriate method of representation when detecting an object. So, this program converts the RGB image file into an HSV image file.
2. Inconsistency of the path's color
- The image files received from the drone’s camera are sometimes of low quality. The external environment, such as the reflection of light, distorts the actual color of the path. To resolve this issue, the user clicks three different points in the image of the route where the colors seem different in this program. The program calculates the mean and standard deviation of colors and sets a range for the path’s color with this information.


## Instructions
1. Place the image file under the folder named test_data. <br/>
2. Run the mask_generator.py, then a window will pop up as below. <br/><p align="center"><img width="300" alt="show" src="https://user-images.githubusercontent.com/42035101/144532804-4702c015-f7ee-4606-83fe-ea2294a840e4.PNG"></p>  
3. Click OPEN in the menu named FILE, and select the image file you want to convert. <br/><p align="center"><img width="300" alt="select" src="https://user-images.githubusercontent.com/42035101/144532757-e6d6ce43-d791-4a1c-9112-d8053b9af062.PNG"></p>  
4. After selecting the image file you want to convert, the follwoing window will appear. <br/><p align="center"><img width="300" alt="after_select" src="https://user-images.githubusercontent.com/42035101/144532774-08aedc84-c747-4793-a8ce-16790a3bf600.PNG"></p>  
    *   Left-click three different points where the color of the path seems different.  
    *   You can check how many times you have clicked on the window. <br/><p align="center"><img width="300" alt="click" src="https://user-images.githubusercontent.com/42035101/144532785-b8d0cadf-02ee-4664-b02c-e3868ed96a48.PNG"></p>
    *   If you clicked more than three times, the program will tell you that you have exceeded the number of allowed clicks. <br/><p align="center"><img width="300" alt="exceeded" src="https://user-images.githubusercontent.com/42035101/144532795-5cbf04bb-6dba-4669-a425-46fd95dfc2fb.PNG"></p> 
5. After finishing clicking three times, press the SHOW button to see the converted image. <br/><p align="center"><img width="300" alt="show" src="https://user-images.githubusercontent.com/42035101/144532804-4702c015-f7ee-4606-83fe-ea2294a840e4.PNG"></p>
6. You can exit the program by either clicking the X button on the window or pressing EXIT in the menu name FILE.
You can find the converted file at the same path with the mask_generator.py file.


## Future goals
Currently, there are two improvements that can be made with the developed program. </br>
- Converting new image without executing the program
    - To convert a new image, the program has to be re-started for now. 
    - This can be improved by adding a new menu named “NEW FILE” which initializes the current values.
- Un-do misclick
    - With the developed program so far, there is no way to undo the misclicked event. 
    - This can be improved by adding right-click event which can un-do the unintentionally clicked event.

