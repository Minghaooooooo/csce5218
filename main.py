# This is a sample Python script.
import math
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

def negative_log_sigmoid(x):
    return math.log2(1 + np.exp(-x))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import torch

    # 创建一个形状为 (3, 4) 的二维张量
    tensor_2d = torch.tensor([[1, 2, 3, 4],
                              [5, 6, 7, 8],
                              [9, 10, 11, 12]])

    # 创建一个相同形状的充满 0 和 1 的矩阵
    mask_matrix = torch.tensor([[0, 0, 0, 0],
                              [1, 1, 0, 1],
                              [1, 1, 0, 0]])

    # 将tensor_2d中每行中为1的元素选出来，并保存在一个list中
    negative_elements_list = []
    positive_elements_list = []
    for row, mask_row in zip(tensor_2d, mask_matrix):
        positive_elements = [float(element) for element, mask in zip(row, mask_row) if mask == 1]
        positive_elements_list.append(positive_elements)
        negative_elements = [float(element) for element, mask in zip(row, mask_row) if mask == 0]
        negative_elements_list.append(negative_elements)
    print(positive_elements_list,
          negative_elements_list)
    sum_auc = 0
    for pos_list, neg_list in zip(positive_elements_list, negative_elements_list):
        for pos in pos_list:
            if len(pos_list) != 0:
                sum_auc += negative_log_sigmoid(pos) / len(pos_list)
                print('positive', sum_auc)
        for neg in neg_list:
            if len(neg_list) != 0:
                sum_auc += negative_log_sigmoid(-neg) / len(neg_list)
                print('negative', sum_auc)

    print_hi('Minghao Li')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
