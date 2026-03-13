import cv2
import numpuy as np
import time

class Algorithm:
   def __init__(self,name):
      self.opsperpix={}
      self.name=name
      self.kernel=None
   def process(self,image):
       raise NotImplementedError("Subclasses should implement this method")
   def profile(self,image):
      h,w=image.shape[:2]
      k=self.kernel
      output_pixel=(h-(k-1))*(w-(k-1))
      total_ops=output_pixel*sum(self.opsperpix.values())
      return{
         "algorithm":self.name,
         "total_ops":total_ops,
         "output_pixels":output_pixel
      }
   



class Soble_Edge_Detection(Algorithm):
   def __init__(self):
      super ().__init__("Soble_Edge_Detection")
      self.opsperpix={
        "multiply":20,#18 direct for x and y then 2 for the magnitude
        "add":17,# 16 for direct and 1 for the magnitude
        "sqrt":1,
        "load":9,
        "store":1
      }
      self.kernel=3
   def process(self,image):

        t1=time.time()
        sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
        magnitude = np.hypot(sobel_x, sobel_y)
        magnitude = np.uint8(255 * magnitude / magnitude.max())#normalize to aviod trunketing
        
        elapsed = time.time() - t1
        
        return magnitude, elapsed
class GaussianBlur(Algorithm):
    def __init__(self):
        super().__init__("Gaussian Blur")
        
        self.ops_per_pixel = {
            'multiply': 25,  
            'add': 24,
            'load': 25,#at a time one kernal will be loaded that is 5*5 of the pixel 
            'store': 1,
        }
        self.kernel=5#even kernal will not work
    def process(self, image):
        start = time.time()
        result = cv2.GaussianBlur(image, (5, 5), 0)#0 here is sigma value 0 means that the value will be calculated automatic
        elapsed = time.time() - start
        return result, elapsed
class MedianFilter(Algorithm):
    def __init__(self):
        super().__init__("Median Filter")
        self.ops_per_pixel = {
            'compare': 36,   # using the formula n(n-1)/2, bubble short 
            'load': 9,
            'store': 1,
        }
        self.kernel=3
    def process(self, image):
        start = time.time()
        result = cv2.medianBlur(image, 3)
        elapsed = time.time() - start
        return result, elapsed
ALGORITHMS = {
    'sobel': Soble_Edge_Detection(),
    'blur': GaussianBlur(),
    'median': MedianFilter(),
}

  
