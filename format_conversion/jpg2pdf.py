from PIL import Image


def convert_img_pdf(filepath, output_path):
    """
    转换图片为pdf格式
    Args:
        filepath (str): 文件路径
        output_path (str): 输出路径
    """
    output = Image.open(filepath)
    output.save(output_path, "pdf", save_all=True)


if __name__ == "__main__":
    convert_img_pdf(r"E:\增强非增强配准转换\专利\6.jpg", r"E:\增强非增强配准转换\专利\6.pdf")
