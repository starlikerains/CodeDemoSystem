import config
import cv2
import numpy as np

def text2vec(text):
        """
        将图像的名称转化为一阶张量
        :param text:
        :return:
        """
        text_len = len(text)
        if text_len > config.MAX_CAPTCHA:
            print(text)
            raise ValueError('验证码最长4个字符')
        vector = np.zeros([config.MAX_CAPTCHA, config.CHAR_SET_LEN])

        def char2pos(c):
            if c == '_':
                k = 62
                return k
            k = ord(c) - 48
            if k > 9:
                k = ord(c) - 55
                if k > 35:
                    k = ord(c) - 61
                    if k > 61:
                        raise ValueError('No Map')
            return k

        for i, c in enumerate(text):
            idx = char2pos(c)
            vector[i][idx] = 1
        return vector

# def vec2text(vec):
#         """
#         将向量转化为对应的文本
#         :param vec:
#         :return:
#         """
#         char_pos = vec[0]
#         text = []
#         for i, c in enumerate(char_pos):
#             char_at_pos = i  # c/63
#             char_idx = c % config.CHAR_SET_LEN
#             if char_idx < 10:
#                 char_code = char_idx + ord('0')
#             elif char_idx < 36:
#                 char_code = char_idx - 10 + ord('A')
#             elif char_idx < 62:
#                 char_code = char_idx - 36 + ord('a')
#             elif char_idx == 62:
#                 char_code = ord('_')
#             else:
#                 raise ValueError('error')
#             text.append(chr(char_code))
#         return "".join(text)

def vec2text(vec):
    text = []
    for i, c in enumerate(vec):
        text.append(config.CHAR_SET[c])
    return "".join(text)

def to_dry(image, num):
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.medianBlur(image, num)
    _, image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
    # cv2.namedWindow("Image")   
    # cv2.imshow("Image", image)   
    # cv2.waitKey (0)  
    # cv2.destroyAllWindows()
    return image