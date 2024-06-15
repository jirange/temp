#--------------------------------------------#
#   该部分代码用于看网络结构
#--------------------------------------------#
import torch
from torchsummary import summary

from nets.ssd import SSD300

if __name__ == "__main__":
    # 需要使用device来指定网络在GPU还是CPU运行
    device  = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    m       = SSD300(20, "vgg").to(device)
    summary(m, input_size=(3, 300, 300))
    # summary 提供模型对象和输入尺寸, 打印出模型的摘要信息。这个摘要包括了模型的层级结构、每个层的输出尺寸、参数数量、以及整个模型的总参数数量等信息
