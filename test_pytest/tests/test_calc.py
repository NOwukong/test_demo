# -*- coding: utf-8 -*-
# @Time     :2021/1/20 19:43
# @Author   :xiangdong
# @File     :test_calc.py
import pytest
from test_pytest.core.calc import Calc


class TestCalc:

    def setup_class(self):
        self.calc = Calc()

    def set_up(self):
        pass

    # 乘法计算案例
    # 用参数化格式批量执行案例
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, -1]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

        # 原始参数需逐条写入断言语句中
        # assert calc.mul(1, 2) == 2
        # assert calc.mul(-1, -1) == 1
        # assert calc.mul(1, -1) == 1

    # 除法计算案例(正常值)
    @pytest.mark.parametrize('a, b, c', [
        [2, 2, 1],
        [0.2, 0.1, 2],
        [0, 2, 0]
    ])
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 除0异常测试案例数据
    @pytest.mark.parametrize('a,b', [
        [2, 0],
        [0.2, 0],
        [0, 0]
    ])
    def test_div(self, a, b):
        with pytest.raises(ZeroDivisionError):
            assert self.calc.div(a, b)

    # 流程示例
    def test_process(self):
        r1 = self.calc.div(2, 1)
        r2 = self.calc.mul(1, 2)
        assert r1 == 2
        assert r2 == 2
