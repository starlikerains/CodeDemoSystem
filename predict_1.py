import CodeDemo
import crack_captcha
import cv2
import tools
import config
import numpy as np

from captcha.image import ImageCaptcha
from random import randint

if __name__ == "__main__":
    model=CodeDemo.CodeDemo(config.model_name)
    image_name = ''
    for i in range(config.MAX_CAPTCHA):
        image_name += config.CHAR_SET[randint(0, config.CHAR_SET_LEN-1)]
    
    image = ImageCaptcha().generate_image(image_name)
    real_image=image
    image=cv2.cvtColor(np.asarray(image),cv2.COLOR_BGR2GRAY)
    image=tools.to_dry(image,3)
    image = cv2.resize(image, (config.IMAGE_WIDTH, config.IMAGE_HEIGHT),) 
    predict_name=model.predict(image)
    crack_captcha.crack_captcha().show(real_image,image_name,predict_name)

# if __name__ == "__main__":
#     # model=CodeDemo.CodeDemo("\\model_1")
#     for j in range(5):

#         image_name = ''
#         for i in range(config.MAX_CAPTCHA):
#             image_name += config.CHAR_SET[randint(0, config.CHAR_SET_LEN-1)]
        
#         image = ImageCaptcha().generate_image(image_name)
#         # image.show()
#         image.save(config.image1_path+"\\"+image_name+".png")
    