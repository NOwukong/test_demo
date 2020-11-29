from datetime import datetime
from hogwarts_study import random


def gen_trans_id(date=None):
    """
    根据传入的时间生成一个唯一ID的交易流水号
    :param date: 日期
    :return:交易流水ID字符串
    """
    # 如果没有传入时间 就按当前系统时间传入
    if date is None:
        date = datetime.now()
        # 怎样保证流水号的唯一性
        # 日期+时间+毫秒+随机数（六位随机数）
    return date.strftime('%Y%m%d%H%M%S%f') + str(random.randint(100000, 999999))
    #return '{0}{1}'.format(date.strftime('%Y%m%d%H%M%S%f'), random.randint(100000, 999999))


if __name__ == '__main__':
    id = gen_trans_id()
    print(id)
