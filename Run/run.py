import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.path.append(r"D:\software\work\anaconda\envs\pytorch\Lib")
sys.path.append(r"D:\software\work\anaconda\envs\pytorch\Lib\site-packages")
sys.path.append(r"C:\Users\XDJ\AppData\Roaming\Python\Python36\site-packages")

import unittest

from Common.handle_path import CASE_DIR,REPORT_DIR
from Common.config import cfg


# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestLogin))

suite = unittest.defaultTestLoader.discover(CASE_DIR)

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
