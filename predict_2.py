import CodeDemo
import crack_captcha
import cv2
import tools
import config
import numpy as np
import os

from captcha.image import ImageCaptcha
import random

if __name__ == "__main__":
    model=CodeDemo.CodeDemo(config.model_name)
    all_image = os.listdir(config.train_data_path)
    random_file = random.randint(0, len(all_image) - 1)
    data = np.loadtxt(config.train_label_path, str, delimiter=",", skiprows=1)
    label = dict(data)
    image_name = label[str(all_image[random_file][:])]
    image = cv2.imread(os.path.join(config.train_data_path, all_image[random_file]))
    real_image=image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    predict_name=model.predict(image)
    crack_captcha.crack_captcha().show(real_image,image_name,predict_name)