import os.path
import constants

def get_file_type(file_name):
    """
    根据文件的名称获取文件的类型
    :param file_name: str 文件名
    :return: int 文件类型
    -1:未知文件类型
    0：图片类型
    1：word 文档
    2：EXCEL 表格
    3：PPT 文件
    """
    print('-1:未知文件类型\n0：图片类型\n1：word 文档\n2：EXCEL 表格\n3：PPT 文件')
    # 设定一个默认返回值
    result = constants.FILE_TYPE_UNKNOWN
    # 判断传进来的文件名是一个存在的且合法的文件；如果不是就返回未知文件类型-1
    if not os.path.isfile(file_name):
        return result

    path_name, ext = os.path.splitext(file_name)

    # 将文件的后缀转换成小写格式
    ext = ext.lower()

    if ext in ('.jpg', '.png', '.img', '.gif', '.bmp'):
        result = constants.FILE_TYPE_IMG
    elif ext in ('.doc', '.docx'):
        result = constants.FILE_TYPE_DOC
    elif ext in ('.xls', '.xlsx'):
        result = constants.FILE_TYPE_EXCEL
    elif ext in ('.ppt', '.pptx'):
        result = constants.FILE_TYPE_PPT
    return result
