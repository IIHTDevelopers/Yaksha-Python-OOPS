#import sys, os
import unittest
import collections
import part_a, part_b, part_c, part_d
#file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_revised.txt'
from tests.TestUtils import TestUtils
def return_magic_methods(c):
    magic = list()
    for m in dir(c):
        if m.startswith('__'):
            magic.append(m)
    return magic

class FuctionalTests(unittest.TestCase):
    def test_parta_return_magic_methods(self):
        test_obj = TestUtils()
        try:
            user_magic = part_a.return_magic_methods(int)
            test_magic = return_magic_methods(int)
            if collections.Counter(user_magic) == collections.Counter(test_magic):
                passed = True
                test_obj.yakshaAssert("TestPartaReturnMagicMethods", True, "functional")
                print("TestPartaReturnMagicMethods = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestPartaReturnMagicMethods", False, "functional")
                print("TestPartaReturnMagicMethods = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestPartaReturnMagicMethods", False, "functional")
            print("TestPartaReturnMagicMethods = Failed")
        assert passed

    def test_parta_return_no_of_magic_methods(self):
        test_obj = TestUtils()
        try:
            user_magic = part_a.return_no_of_magic_methods(int)
            test_magic = return_magic_methods(int)
            if user_magic==len(test_magic):
                passed = True
                test_obj.yakshaAssert("TestPartaReturnNoOfMagicMethods", True, "functional")
                print("TestPartaReturnNoOfMagicMethods = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestPartaReturnNoOfMagicMethods", False, "functional")
                print("TestPartaReturnNoOfMagicMethods = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestPartaReturnNoOfMagicMethods", False, "functional")
            print("TestPartaReturnNoOfMagicMethods = Failed")
        assert passed

    def test_parta_return_no_of_common_magic_methods(self):
        test_obj = TestUtils()
        try:
            user_magic_common = part_a.return_no_of_common_magic_methods(int, float)
            test_magic_int = set(return_magic_methods(int))
            test_magic_float = set(return_magic_methods(float))
            test_magic_common = len(test_magic_int.intersection(test_magic_float))

            if test_magic_common == user_magic_common:
                passed = True
                test_obj.yakshaAssert("TestPartaReturnNoOfCommonMagicMethods", True, "functional")
                print("TestPartaReturnNoOfCommonMagicMethods = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestPartaReturnNoOfCommonMagicMethods", False, "functional")
                print("TestPartaReturnNoOfCommonMagicMethods = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestPartaReturnNoOfCommonMagicMethods", False, "functional")
            print("TestPartaReturnNoOfCommonMagicMethods = Failed")
        assert passed

    def test_partc_MainClass_int(self):
        test_obj = TestUtils()
        try:
            x, y = 8, 4
            ob1 = part_c.MainClass(x)
            ob2 = part_c.MainClass(y)
            success = True

            if ob1 + ob2 != x + y: success = False
            if ob1 - ob2 != x - y: success = False
            if ob1 * ob2 != x * y: success = False
            if ob1 / ob2 != x / y: success = False

            if success:
                passed  = True
                test_obj.yakshaAssert("TestPartcMainClassInt", True, "functional")
                print("TestPartcMainClassInt = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestPartcMainClassInt", False, "functional")
                print("TestPartcMainClassInt = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestPartcMainClassInt", False, "functional")
            print("TestPartcMainClassInt = Failed")
            assert success
        assert passed

    def test_partc_faultyCalc_int(self):
        test_obj = TestUtils()
        try:
            x, y = 8, 4
            ob1 = part_c.FaultyCalc(x)
            ob2 = part_c.FaultyCalc(y)
            success = False

            if ob1 + ob2 != x - y: success = False
            if ob1 - ob2 != x + y: success = False
            if ob1 * ob2 != x * y: success = False
            if ob1 / ob2 != x / y: success = False
            success = True
            if success:
                passed = True
                test_obj.yakshaAssert("TestPartcFaultyCalcInt", True, "functional")
                print("TestPartcFaultyCalcInt = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestPartcFaultyCalcInt", False, "functional")
                print("TestPartcFaultyCalcInt = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestPartcFaultyCalcInt", False, "functional")
            print("TestPartcFaultyCalcInt = Failed")
            assert success
        assert passed

    def test_partc_correctCalc_int(self):
        test_obj = TestUtils()
        try:
            x, y = 8, 4
            ob1 = part_c.CorrectCalc(x)
            ob2 = part_c.CorrectCalc(y)
            success = False

            if ob1 + ob2 != x + y: success = False
            if ob1 - ob2 != x - y: success = False

            success = True
            if success:
                passed = True
                test_obj.yakshaAssert("TestPartcCorrectCalcInt", True, "functional")
                print("TestPartcCorrectCalcInt = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestPartcCorrectCalcInt", False, "functional")
                print("TestPartcCorrectCalcInt = Failed")

        except:
            passed = False
            test_obj.yakshaAssert("TestPartcCorrectCalcInt", False, "functional")
            print("TestPartcCorrectCalcInt = Failed")
            assert success
        assert passed

    def test_partc_correctCalc_inherited(self):
        test_obj = TestUtils()
        try:
            x, y = 8, 4
            ob1 = part_c.CorrectCalc(x)
            ob2 = part_c.CorrectCalc(y)
            passed = True
            if ob1 * ob2 != x * y: passed = False
            if ob1 / ob2 != x / y: passed = False
            passed = False
            if passed:
                test_obj.yakshaAssert("TestPartcCorrectCalcInherited", False, "functional")
                print("TestPartcCorrectCalcInherited = Failed")
            else:
                test_obj.yakshaAssert("TestPartcCorrectCalcInherited", False, "functional")
                print("TestPartcCorrectCalcInherited = Failed")

        except:
            test_obj.yakshaAssert("TestPartcCorrectCalcInherited", True, "functional")
            print("TestPartcCorrectCalcInherited = Passed")
        assert passed

    def test_partc_correctCalc_float(self):
        test_obj = TestUtils()
        try:
            x, y = 8, 4.5
            ob1 = part_c.MainClass(x)
            ob2 = part_c.MainClass(y)
            success = False

            if ob1 + ob2 != x + y: success = False
            if ob1 - ob2 != x - y: success = False
            if ob1 * ob2 != x * y: success = False
            if ob1 / ob2 != x / y: success = False
            success = True
            if success:
                passed = True
                test_obj.yakshaAssert("TestPartcCorrectCalcFloat", True, "functional")
                print("TestPartcCorrectCalcFloat = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestPartcCorrectCalcFloat", False, "functional")
                print("TestPartcCorrectCalcFloat = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestPartcCorrectCalcFloat", False, "functional")
            print("TestPartcCorrectCalcFloat = Failed")
            assert success
        assert passed

    def test_partb_abstraction_methods_defined(self):
        test_obj = TestUtils()
        try:
            ppf = part_b.PPF()
            ppf_l= ppf.lockin_period()
            ppf_i = ppf.interest_rate()
            pf = part_b.PF()
            pf_l= pf.lockin_period()
            pf_i = pf.interest_rate()
            test_obj.yakshaAssert("TestPartbAbstractionMethodsDefined", True, "functional")
            print("TestPartbAbstractionMethodsDefined = Passed")
        except:
            test_obj.yakshaAssert("TestPartbAbstractionMethodsDefined", False, "functional")
            print("TestPartbAbstractionMethodsDefined = Failed")
            assert False

    def test_partd_SOLID_implementation(self):
        test_obj = TestUtils()
        try:
            x, y = 8.4, 4
            m_obj = part_d.Main()
            ops = m_obj.get_operations(x, y)
            if set(ops) == set([x+y, x-y, x*y, x/y, x%y]):
                passed = True
                test_obj.yakshaAssert("TestPartdSOLIDImplementation", True, "functional")
                print("TestPartdSOLIDImplementation = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestPartdSOLIDImplementation", False, "functional")
                print("TestPartdSOLIDImplementation = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestPartdSOLIDImplementation", False, "functional")
            print("TestPartdSOLIDImplementation = Failed")
        assert passed
