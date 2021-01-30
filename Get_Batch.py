import numpy as np
import random
from imgaug import augmenters as iaa
from PIL import Image
import config
import os
import cv2
import tensorflow as tf

import tools

from captcha.image import ImageCaptcha
from random import randint


class get_batch:
    def __init__(self):
        self.MAX_CAPTCHA=config.MAX_CAPTCHA
        self.CHAR_SET=config.CHAR_SET
        self.CHAR_SET_LEN=config.CHAR_SET_LEN
        self.IMAGE_WIDTH=config.IMAGE_WIDTH
        self.IMAGE_HEIGHT=config.IMAGE_HEIGHT
        self.batch_size=config.batch_size

    def get_name(self,image_name,label):
        image_label=""
        if label == None:
            image_label=image_name[:self.MAX_CAPTCHA]
        else:
            image_label=label[image_name]
        return image_label

    def get_name_and_image_1(self,data_path):
        """
        随机获取路径下的图像名称和图像数据
        :param data_path:
        :return:
        """
        all_image = os.listdir(data_path)
        random_file = random.randint(0, len(all_image) - 1)
        image_name = str(all_image[random_file][:])
        image = cv2.imread(os.path.join(data_path, all_image[random_file]))
        
        image = cv2.resize(image, (self.IMAGE_WIDTH, self.IMAGE_HEIGHT),)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # ret2,image = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        # image = cv2.medianBlur(image, 3)
        # cv2.namedWindow("Image")
        # cv2.imshow("Image", image)   
        # cv2.waitKey (0)  
        # cv2.destroyAllWindows()

        # image_name = ''
        # for i in range(self.MAX_CAPTCHA):
        #     image_name += self.CHAR_SET[randint(0, self.CHAR_SET_LEN-1)]
        # image = ImageCaptcha().generate_image(image_name)
        # # image.show()
        # image=cv2.cvtColor(np.asarray(image),cv2.COLOR_BGR2GRAY)
        # image=tools.to_dry(image,3)

        # cv2.namedWindow("Image")   
        # cv2.imshow("Image", image)   
        # cv2.waitKey (0)  
        # cv2.destroyAllWindows()  

        image = cv2.resize(image, (self.IMAGE_WIDTH, self.IMAGE_HEIGHT),)  
        return image_name, image

    def get_name_and_image_2(self,data_path):
        image_name = ''
        for i in range(self.MAX_CAPTCHA):
            image_name += self.CHAR_SET[randint(0, self.CHAR_SET_LEN-1)]
        image = ImageCaptcha().generate_image(image_name)
        # image.show()
        image=cv2.cvtColor(np.asarray(image),cv2.COLOR_BGR2GRAY)
        image=tools.to_dry(image,3)

        # cv2.namedWindow("Image")   
        # cv2.imshow("Image", image)   
        # cv2.waitKey (0)  
        # cv2.destroyAllWindows()  

        image = cv2.resize(image, (self.IMAGE_WIDTH, self.IMAGE_HEIGHT),)  
        return image_name, image

    
    def get_batch(self, data_path, label=None, size=config.batch_size):
        """
        获取一批数据
        :param data_path: 获取数据的路径，通常为训练集、验证集目录
        :param size: 每个批次处理的样本数量
        :return:
        """
        batch_x = np.zeros([size, self.IMAGE_HEIGHT, self.IMAGE_WIDTH, 1])
        batch_y = np.zeros([size, self.MAX_CAPTCHA, self.CHAR_SET_LEN])

        for i in range(size):
            if label!=None:
                image_name, image = self.get_name_and_image_1(data_path)
            else:
                image_name, image = self.get_name_and_image_2(data_path)
            batch_x[i, :] =image.reshape(self.IMAGE_HEIGHT, self.IMAGE_WIDTH, 1)
            # tf.reshape(image, (self.IMAGE_HEIGHT, self.IMAGE_WIDTH, 1))
            batch_y[i, :] = tools.text2vec(self.get_name(image_name,label))

            # print(self.get_name(image_name,label))
        return batch_x, batch_y

    
if __name__=="__main__":
    data = np.loadtxt(config.train_label_path, str, delimiter=",", skiprows=1)
    label = None
    beatch=get_batch()
    beatch.get_batch(config.train_data_path,label,size=1)