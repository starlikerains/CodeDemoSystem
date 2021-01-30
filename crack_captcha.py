
import CodeDemo
import cv2
import tools
from captcha.image import ImageCaptcha
from random import randint
import config
import numpy as np
import matplotlib.pyplot as plt

class crack_captcha:
    def __init__(self):
        pass
    def show(self,image,label,predict):
        image=np.array(image)
        plt.axis('off')
        plt.imshow(image)
        plt.text(config.IMAGE_WIDTH*0.1,config.IMAGE_HEIGHT*0.1,"真实值："+label,fontsize="large",alpha = 1.0,fontproperties="SimSun",fontweight='black')
        plt.text(config.IMAGE_WIDTH*0.4,config.IMAGE_HEIGHT*0.1,"预测值："+predict,fontsize="large",alpha = 1.0,fontproperties="SimSun",fontweight='black')
        if label.upper()==predict.upper():
            plt.text(config.IMAGE_WIDTH*0.7,config.IMAGE_HEIGHT*0.1,"预测正确",fontsize="large",alpha = 1.0,fontproperties="SimSun",fontweight='black')
        else:
            plt.text(config.IMAGE_WIDTH*0.7,config.IMAGE_HEIGHT*0.1,"预测错误",fontsize="large",alpha = 1.0,fontproperties="SimSun")
        plt.show()
    


# if __name__=="__main__":
#     model=CodeDemo.CodeDemo()
#     count=0
#     success=0
#     for i in range(5000):
#         count+=1
#         image_name = ''
#         for i in range(config.MAX_CAPTCHA):
#             image_name += config.CHAR_SET[randint(0, config.CHAR_SET_LEN-1)]
#         image = ImageCaptcha().generate_image(image_name)
#         real_image=image
#         image=cv2.cvtColor(np.asarray(image),cv2.COLOR_BGR2GRAY)
#         # image=tools.to_dry(image,3)
#         image = cv2.resize(image, (config.IMAGE_WIDTH, config.IMAGE_HEIGHT),) 
#         predict_name=model.predict(image)
#         if image_name.upper()==predict_name.upper():
#             success+=1
#             print("真实值："+image_name+",预测值："+predict_name+",预测正确,正确率："+str(success/count))
#         else:
#             print("真实值："+image_name+",预测值："+predict_name+",预测错误,正确率："+str(success/count))
