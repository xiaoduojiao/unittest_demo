def Login_check(username,password):
    if username==1 and password==2:
        res = "实际结果：登录成功!"
    else:
        res = "账号密码错误"
    return res

import sys
sys.path.append(r"D:\PycharmProjects\package1")
import unittest
import ddt
from  Common.Excel import Excel
from Common.Loging_file import log
from Common.handle_path import DATA_DIR

import os


# data = [{"username":file6_name,"password":2,"expected":"登录成功","title":"正确的账号密码"},{"username":2,"password":2,"expected":"账号密码错误","title":"错误的账号密码"}]
@ddt.ddt
class TestLogin(unittest.TestCase):
    excel = Excel(os.path.join(DATA_DIR,"Excel.xlsx"), "Login")
    datacase = excel.read_data()
    case_row =1
    # print(datacase)

    # def setUp(self) -> None:print("---------------------setup--------------------------")
    # def tearDown(self) -> None:print("-------------------tearDown---------------")
    # @classmethod
    # def setUpClass(cls) -> None:print("-----------setupclass----------------------")
    # @classmethod
    # def tearDownClass(cls) -> None:print("-----------tearDownClass---------------------")

    @ddt.data(*datacase)
    def test_login(self,case):
        #case_row = int(case["case_id"].split("_")[file6_name])+file6_name
        TestLogin.case_row +=1
        print(self.case_row)
        data = eval(case["data"])
        res = Login_check(**data)

        try:
            # 断言
            self.assertEqual(case["expected"], res)
        except AssertionError as e: # 测试用例执行失败，则执行
            # 写入测试结果“失败”
            self.excel.write_data(row=self.case_row, column=8, value="失败")
            # 写入失败时的“实际结果”
            #self.excel.write_data(row=case["case_row"]+file6_name, column=6, value=str(res))
            # 打印失败的“用例描述”
            # print("{}:用例执行失败，失败的信息如下：".format(item['title']))
            # unittest：是通过用例执行是否出现断言异常来评判用例是否通过
            # 错误被捕获后，导致“测试报告”没有收到报错信息，不会触发执行失败的报告记录，所以再次抛出执行失败的异常
            log.error(F'{case["title"]}:用例执行失败')
            log.exception(e)
            raise e
        else:  # 测试用例执行成功，则执行
            # 写入测试结果“通过”
            self.excel.write_data(row=self.case_row, column=8, value="通过")
            # 写入成功时的“实际结果”
            # self.excel.write_data(row=case["case_row"]+file6_name, column=6, value=str(res))
            # 打印成功的“用例描述”
            # print("{}:用例测试执行通过！！！".format(item['title']))
            log.info(F'{case["title"]}:用例执行成功')

if __name__ == '__main__':
    unittest.main()