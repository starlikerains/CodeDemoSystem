import tensorflow as tf
import config

def crack_captcha_cnn():

    #构建一个Sequential序贯模型
    model = tf.keras.Sequential()

    # model.add(tf.keras.layers.Conv2D(32, (3, 3)))
    # model.add(tf.keras.layers.PReLU())
    # model.add(tf.keras.layers.MaxPool2D((2, 2), strides=2))
    # model.add(tf.keras.layers.Dropout(config.keep_prob))

    # model.add(tf.keras.layers.Conv2D(64, (3, 3)))
    # model.add(tf.keras.layers.PReLU())
    # model.add(tf.keras.layers.MaxPool2D((2, 2), strides=2))
    # model.add(tf.keras.layers.Dropout(config.keep_prob))

    # model.add(tf.keras.layers.Conv2D(128, (3, 3)))
    # model.add(tf.keras.layers.PReLU())
    # model.add(tf.keras.layers.MaxPool2D((2, 2), strides=2))
    # model.add(tf.keras.layers.Dropout(config.keep_prob))

    # model.add(tf.keras.layers.Flatten())

    # model.add(tf.keras.layers.Dense(1024))
    # model.add(tf.keras.layers.PReLU())
    # model.add(tf.keras.layers.Dropout(config.keep_prob))
    
    # model.add(tf.keras.layers.Dense(config.MAX_CAPTCHA * config.CHAR_SET_LEN))
    # model.add(tf.keras.layers.Reshape([config.MAX_CAPTCHA, config.CHAR_SET_LEN]))
    # model.add(tf.keras.layers.Softmax())

    #conv1
    #卷积
    model.add(tf.keras.layers.Conv2D(32, (5, 5)))
    #使用ReLU激活
    model.add(tf.keras.layers.PReLU())
    #池化
    model.add(tf.keras.layers.MaxPool2D((2, 2), strides=2))
    #Dropout
    model.add(tf.keras.layers.Dropout(0.5))

    #conv2
    model.add(tf.keras.layers.Conv2D(64, (3, 3)))
    model.add(tf.keras.layers.PReLU())
    model.add(tf.keras.layers.MaxPool2D((2, 2), strides=2))
    model.add(tf.keras.layers.Dropout(0.5))

    #conv3
    model.add(tf.keras.layers.Conv2D(128, (3, 3)))
    model.add(tf.keras.layers.PReLU())
    model.add(tf.keras.layers.MaxPool2D((2, 2), strides=2))
    model.add(tf.keras.layers.Dropout(0.5))

    #将矩阵拉为一维
    model.add(tf.keras.layers.Flatten())
    
    #Fully connected 

    # model.add(tf.keras.layers.Dense(1024))
    # model.add(tf.keras.layers.PReLU())
    # model.add(tf.keras.layers.Dropout(config.keep_prob))


    model.add(tf.keras.layers.Dense(config.MAX_CAPTCHA * config.CHAR_SET_LEN))
    model.add(tf.keras.layers.Reshape([config.MAX_CAPTCHA, config.CHAR_SET_LEN]))
    #使用softmax得到4个位置字符类别的概率似然值
    model.add(tf.keras.layers.Softmax())

    return model