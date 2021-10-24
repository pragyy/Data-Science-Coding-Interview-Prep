"""
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
"""

import numpy as np
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        
        img = np.array(image)
        
        img1 = np.flip(img, axis = 1)
        
        for idx, x in np.ndenumerate(img1):
            if x == 0:
                img1[idx] = 1
            else:
                img1[idx] = 0
            
        return img1
