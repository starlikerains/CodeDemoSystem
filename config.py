import os

# 图像参数
# 图像高度，像素值
IMAGE_HEIGHT = 40
# 图像宽度，像素值
IMAGE_WIDTH = 120
# 验证码的最长字符数
MAX_CAPTCHA = 4

use_label_file = True

model_name="\\model_2"

work_path = os.getcwd()

data_path = work_path + "\\train"  # 数据集
test_path = work_path + "\\test"  # 测试集

image1_path=work_path + "\\image1"

# 标签

train_label_path = work_path + "\\train_label.csv"  # 训练集标签
test_label_path = work_path +  "\\test_label.csv" # 测试集标签
enhanced_label_path = work_path + "\\enhanced_label_path.csv"  # 增强训练集标签

# 模型保存路径
model_path_name = work_path + '\\model\\crack_captcha_model'  # 模型名字及路径
model_path = work_path + "\\model"  # 中间模型保存路径

# 训练用路径

# train_data_path = work_path + '\\train_data'  # 训练集
# # train_data_path = work_path + '\\train_one'
# test_data_path = work_path + '\\test_new'  # 测试集

train_data_path = work_path + '\\train_data'  # 训练集
# train_data_path = work_path + '\\show'  # 训练集
# train_data_path = work_path + '\\train_one'
test_data_path = work_path +   '\\test' # 测试集
validation_data_path = work_path + '\\validation_data'  # 验证集

# 调试用路径
small_train_path = work_path + "\\small_train"
small_test_path = work_path + "\\small_test"
small_validation_path = work_path + "\\small_validation"

# 日志路径
logs_path = work_path + "\\logs"

# 字符集
# 数字字符集
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# 小写字母字符集
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# 大写字母字符集
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# 字符集
CHAR_SET = number + alphabet + ALPHABET  # 如果验证码长度小于MAX_CAPTCHA, '_'用来补齐
# 字符集长度
CHAR_SET_LEN = len(CHAR_SET)



# 训练用参数
# 每批次训练的数量
batch_size = 512

test_size = 64
# 学习率
learning_rate = 0.01
# 遗忘率
keep_prob = 0.5
# 训练次数
stop_step = 100000
# 目标正确率
stop_acc = 0.99
# 批次保存
cycle_save = 10


