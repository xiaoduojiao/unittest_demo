import os
# 项目的根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

# 测试用例的目录路径
CASE_DIR = os.path.join(BASE_DIR,'Testcase')
print(CASE_DIR)

# 测试报告的目录路径
REPORT_DIR = os.path.join(BASE_DIR,'report')
print(REPORT_DIR)

# 日志目录的绝对路径
LOG_DIR = os.path.join(BASE_DIR,'logs')
print(LOG_DIR)

# 用例数据的项目路径
DATA_DIR = os.path.join(BASE_DIR,'Data')
print(DATA_DIR)


CONF_DIR = os.path.join(BASE_DIR,"conf")
print(CONF_DIR)