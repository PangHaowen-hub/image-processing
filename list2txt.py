if __name__ == '__main__':
    test_txt = r'D:\my_code\Federated_Learning\FL-NC2CE\data\test.txt'
    tumor_txt = r'D:\my_code\Federated_Learning\FL-NC2CE\data\tumor_list.txt'
    name_list_test = []
    with open(test_txt, "r") as f:
        for line in f.readlines():
            name_list_test.append(line.strip('\n'))

    name_list_tumor = []
    with open(tumor_txt, "r") as f:
        for line in f.readlines():
            name_list_tumor.append(line.strip('\n'))

    metrics_list = []
    for i in name_list_tumor:
        if i in name_list_test:
            metrics_list.append(i)
    with open('example.txt', 'w') as f:
        for line in metrics_list:
            f.writelines(line + '\n')
