from datetime import datetime
from trans.tools import gen_trans_id
from work.tools import get_file_type


def test_trans_tool():
    """测试trans包中的tools模块"""

    id1 = gen_trans_id()
    print('流水号1：'+id1)
    date = datetime(2021, 10, 12, 12, 30, 25)
    id2 = gen_trans_id(date)
    print('流水号2：'+id2)

def test_work_tool():
    """测试work包中的tools模块 """
    file_name = 'C:\\Users\\Administrator\\Desktop\\SQL语句学习资料.docx'
    rest = get_file_type(file_name)
    print(rest)

if __name__ == '__main__':
    test_trans_tool()
    test_work_tool()
