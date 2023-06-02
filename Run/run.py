import sys
sys.path.append(r"D:\PycharmProjects\package1")
import unittest
import os
from Common.handle_path import CASE_DIR,REPORT_DIR
from Common.config import cfg


# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestLogin))

suite = unittest.defaultTestLoader.discover(CASE_DIR)
print(111)
# runner = unittest.TextTestRunner()
# runner.run(suite)
from unittestreport import TestRunner
runner = TestRunner(suite,
                    filename=cfg.get("report","filename"),
                    report_dir=REPORT_DIR,
                    title=cfg.get("report","title"),
                    tester=cfg.get("report","tester"),
                    desc=cfg.get("report","desc"),
                    templates=1)
runner.run()
