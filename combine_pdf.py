from PyPDF2 import PdfFileMerger

path1 = r'E:\增强非增强配准转换\专利\1.pdf'
path2 = r'E:\增强非增强配准转换\专利\2.pdf'

file_merger = PdfFileMerger()

file_merger.append(path1, import_outline=False)  # 合并pdf文件
file_merger.append(path2, import_outline=False)


file_merger.write(r"E:\增强非增强配准转换\专利\2021版专利申请表-图像转换-2022-12-12（签字版本）.pdf")
