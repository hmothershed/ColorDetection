# Color Detection Using Computer Vision: A Camera Based Approach
*EE 4780 Computer Vision Final Project*

## Problem Statement
To develop an algorithm that can identify the colors within an object accurately from a camera approach. The algorithm should be able to recognize a wide range of colors and distinguish between shades and hues of the same color.

## TESTING PHASE 1
The first test involved implementing the code without a region of interest (ROI) and was conducted under room lighting conditions. While most colors were accurately detected, we observed inaccuracies in detecting brown, and grey was detected as both gray and purple. Yellow was detected as both yellow and orange, and orange was detected as both brown and orange. Shadows on the paper were also detected as grey. These findings suggested that lighting conditions and environmental factors had a significant impact on the color detection.
![test1](https://github.com/hmothershed/HUiE/assets/112271331/21faf6ce-02cc-4c57-a884-ef8aa87a95ea)

## TESTING PHASE 2
The second test was conducted under sunlight conditions without ROI, and while it revealed better detection, we found that some colors had multiple bounding boxes around them. This was likely due to them falling in the same range and being closely related to each other. For example, brown was detected as both brown and orange, which is to be expected if the color isn’t a pure brown. In addition, black was inaccurately detected as grey, which is a limitation of our current implementation.
![test2](https://github.com/hmothershed/HUiE/assets/112271331/670121d1-d430-41a4-90e5-a3b0f552f27a)

## TESTING PHASE 3
The final test was conducted under room lighting conditions and involved the implementation of the ROI. This new implementation significantly improved the accuracy of color detection within a specified area. If the color detected is not defined in the color library, the camera assigns colors that are similar to it based on their RGB values. As shown in the image below, we have a lilac/lavender keyboard slip, which is not defined in our color library, the code looks for colors like lilac/lavender and assigns them as the detected colors. In this case, magenta, pink, and purple are assigned as they are the closest colors that fell within the defined upper and lower bounds. This process of color quantization helps to ensure that the detected colors are as accurate as possible, even if they are not defined in the color library.
![test3](https://github.com/hmothershed/HUiE/assets/112271331/54b72c48-f56a-432d-baa6-67515c3a0ab8)

## References
https://www.askpython.com/python/examples/color-detection
https://www.youtube.com/watch?v=aFNDh5k3SjU
https://www.geeksforgeeks.org/detect-the-rgb-color-from-a-webcam-using-python-opencv/
https://pyimagesearch.com/2014/08/04/opencv-python-color-detection/
https://www.youtube.com/watch?v=6Otgyyv--UU
