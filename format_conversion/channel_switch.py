from PIL import Image
import os


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if (os.path.splitext(file)[1] == '.png'):
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


if __name__ == '__main__':
    rootdir = r'F:\my_code\zhanghe\pytorch-CycleGAN-and-pix2pix-master\results\he-GAN\100\images'
    path = get_listdir(rootdir)
    for i in path:
        filename = i
        image = Image.open(filename)
        print(image.mode)
        gray = image.convert('L')
        print(gray.mode)
        gray.save(i, 'png')

'''
1    （1位像素，黑白，每字节一个像素存储）
L    （8位像素，黑白）
P    （8位像素，使用调色板映射到任何其他模式）
RGB  （3x8位像素，真彩色）
RGBA （4x8位像素，带透明度掩模的真彩色）
CMYK （4x8位像素，分色）
YCbCr（3x8位像素，彩色视频格式）
I    （32位有符号整数像素）
F    （32位浮点像素）
'''
