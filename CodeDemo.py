import os
import config
import tensorflow as tf
import tools
import numpy as np 
import cv2
from PIL import Image

class CodeDemo:
    def __init__(self,model_name):
        self.model_path=config.model_path+model_name
        self.IMAGE_WIDTH=config.IMAGE_WIDTH
        self.IMAGE_HEIGHT=config.IMAGE_HEIGHT
        self.MAX_CAPTCHA=config.MAX_CAPTCHA
        self.CHAR_SET_LEN=config.CHAR_SET_LEN
        self.model=tf.keras.models.load_model(self.model_path)

    def predict(self,image):
        model = self.model
        image = tools.to_dry(image,3)
        data_x = np.zeros([1, self.IMAGE_HEIGHT, self.IMAGE_WIDTH, 1])
        data_x[0,:]=image.reshape(self.IMAGE_HEIGHT, self.IMAGE_WIDTH, 1)
        prediction_value=model.predict(data_x)
        prediction_value=tools.vec2text(
            np.argmax(prediction_value,axis=2)[0]
        )
        return prediction_value


        
        


