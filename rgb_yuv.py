import numpy as np


def rgb_yuv(col_1, col_2, col_3):
    height = 1
    width = 1
    yuv = np.zeros([height, width, 3], dtype=np.uint8)
    y_val = 0.257 * col_1 + 0.504 * col_2 + 0.098 * col_3 + 16
    u_val = -0.148 * col_1 - 0.291 * col_2 + 0.439 * col_3 + 128
    v_val = 0.439 * col_1 - 0.368 * col_2 - 0.071 * col_3 + 128
    yuv[:, :] = [y_val, u_val, v_val]
    return yuv


def yuv_rgb(col_1, col_2, col_3):
    height = 1
    width = 1
    rgb = np.zeros([height, width, 3], dtype=np.uint8)
    b_val = 1.164 * (col_1 - 16) + 2.018 * (col_3 - 128)
    g_val = 1.164 * (col_1 - 16) - 0.813 * (col_2 - 128) - 0.391 * (col_3 - 128)
    r_val = 1.164 * (col_1 - 16) + 1.596 * (col_2 - 128)
    rgb[:, :] = [r_val, g_val, b_val]
    return rgb


#asking for values
VAL1, VAL2, VAL3 = input("Enter a three values rgb: ").split()
VAL4, VAL5, VAL6 = input("Enter a three values yuv: ").split()

RES1 = rgb_yuv(VAL1, VAL2, VAL3)
print(RES1)
RES2 = yuv_rgb(VAL4, VAL5, VAL6)
print(RES2)
