from PyPDF2 import PdfFileMerger
import os


def get_listdir(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.pdf':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


path = r''
pdf_list = get_listdir(path)

file_merger = PdfFileMerger()
for i in pdf_list:
    file_merger.append(i, import_outline=False)  # 合并pdf文件

file_merger.write(r"合并.pdf")
