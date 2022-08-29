import unittest
#import sys, os
import part_c, part_d
#file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_exception_revised.txt'
from tests.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_partc_correctCalc_div_by_zero(self):
        test_obj = TestUtils()
        try:
            x, y = 8.4, 0
            ob1 = part_c.MainClass(x)
            ob2 = part_c.MainClass(y)

            if ob1/ob2 == -1:
                passed = True
                test_obj.yakshaAssert("TestPartcCorrectCalcDivByZero", True, "exception")
                print("TestPartcCorrectCalcDivByZero = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestPartcCorrectCalcDivByZero", False, "exception")
                print("TestPartcCorrectCalcDivByZero = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestPartcCorrectCalcDivByZero", False, "exception")
            print("TestPartcCorrectCalcDivByZero = Failed")
        #assert passed

    def test_partd_div_by_zero(self):
        test_obj = TestUtils()
        try:
            x, y = 8.4, 0
            m_obj = part_d.Main()
            ops = m_obj.get_operations(x, y)
            if y==0:
                assert set(ops) == set([x+y, x-y, x*y, -1, -1])
            else:
                assert set(ops) == set([x+y, x-y, x*y, x/y, x%y])
            test_obj.yakshaAssert("TestPartdDivByZero", True, "exception")
            print("TestPartdDivByZero = Passed")
        except:
            test_obj.yakshaAssert("TestPartdDivByZero", False, "exception")
            print("TestPartdDivByZero = Failed")
            #assert False
