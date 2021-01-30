import tensorflow as tf
import config
import Get_Batch
import cnn_network
import os
import numpy as np
from tensorflow.keras.callbacks import TensorBoard


class train_cnn_model:
    def __init__(self):
        self.train_data_path = config.train_data_path
        self.test_data_path = config.test_data_path
        
        self.use_label_file = config.use_label_file
        if self.use_label_file:
            self.train_label=self.load_label(config.train_label_path)
            self.test_label=self.load_label(config.test_label_path)
        else:
            self.train_label=None
            self.test_label=None
        
        self.model_path = config.model_path+config.model_name
        self.logs_path = config.logs_path
        self.cycle_save = config.cycle_save
        self.stop_step = config.stop_step
        self.batch_size =config.batch_size
        self.test_size = config.test_size

    def load_label(self,file_path):
        data = np.loadtxt(file_path, str, delimiter=",", skiprows=1)
        label = dict(data)
        return label

    def train(self):
        try:
            # if not os.path.exists(self.moder_path):
            #     os.mkdir(self.moder_path)
            model = tf.keras.models.load_model(self.model_path)
        except Exception as e:
            print('#######Exception', e)
            model = cnn_network.crack_captcha_cnn()
            if os.path.exists(self.logs_path):
                for f in os.listdir(self.logs_path):
                    path_file=os.path.join(self.logs_path,f)
                    if os.path.isfile(path_file):
                        os.remove(path_file)
            else:
                os.mkdir(self.logs_path,755)
        finally:
            tensorboard = TensorBoard(log_dir=self.logs_path)

        model.compile(optimizer='Adam',
                    metrics=['accuracy'],
                    loss='categorical_crossentropy')

        get_batch=Get_Batch.get_batch()
        
        for times in range(self.stop_step):
            batch_x, batch_y = get_batch.get_batch(self.train_data_path, self.train_label, self.batch_size)
            test_x, test_y = get_batch.get_batch(self.test_data_path, self.test_label, self.test_size)
            print('times=', times, ' batch_x.shape=',
                batch_x.shape, ' batch_y.shape=', batch_y.shape)
            model.fit(batch_x, batch_y, epochs=4, validation_data=(
                test_x, test_y), callbacks=[tensorboard])
            print("y预测=\n", np.argmax(model.predict(test_x), axis=2))
            print("y实际=\n", np.argmax(test_y, axis=2))

            if 0 == times % self.cycle_save:
                print("save model at times=", times)
                model.save(self.model_path)

if __name__ == "__main__":
    model=train_cnn_model()
    model.train()