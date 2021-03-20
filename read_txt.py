def place(zi, mu):
    """查询子字符串在大字符串中的所有位置"""
    len1 = len(zi)
    pl = []
    for each in range(len(mu) - len1):
        if mu[each:each + len1] == zi:  # 找出与子字符串首字符相同的字符位置
            pl.append(each)
    return pl


def text_save(filename, data):  # filename为写入txt文件的路径，data为要写入数据列表
    """将列表中数据写入txt"""
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")


def text_save_dice(filename, data):  # filename为写入txt文件的路径，data为要写入数据列表
    """将列表中数据写入txt"""
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s + '\n'  # 每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")


def read_info(fold, s, txt_save_name):
    count = 0  # 输出行数，正常应为1000
    out = []
    for i in fold:
        t = place(s, i)
        if t:
            begin = t[0] + len(s)
            out.append(i[begin:])
            count += 1
    text_save(txt_save_name, out)
    print(count)


def read_dice(fold, s, txt_save_name):
    count = 0  # 输出行数，正常应为1000
    out = []
    for i in fold:
        t = place(s, i)
        if t:
            begin = t[0] + len(s)
            out.append(i[begin:])
            count += 1
    text_save_dice(txt_save_name, out)
    print(count)


if __name__ == '__main__':
    txt_name = 'D:/术前术后肺叶分割课题/lobe512/fold4/training_log_2021_3_8_21_12_58.txt'
    txt_save_name = 'D:/术前术后肺叶分割课题/lobe512/fold4/'
    fold = []
    with open(txt_name, "r") as f:
        for line in f.readlines():
            fold.append(line.strip('\n'))  # 去掉列表中每一个元素的换行符
    read_info(fold, 'train loss : ', txt_save_name + 'train_loss.txt')
    read_info(fold, 'validation loss: ', txt_save_name + 'validation_loss.txt')
    read_info(fold, 'lr: ', txt_save_name + 'lr.txt')
    read_dice(fold, 'Average global foreground Dice: ', txt_save_name + 'Dice.txt')
