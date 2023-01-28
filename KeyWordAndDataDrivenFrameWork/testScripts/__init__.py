from imp import reload

from action.PageAction import *
from util.ParseExcel import ParseExcel
from config.VarConfig import *
import time
import traceback

# 设置此次测试环境的环境编码为utf8
import sys

reload(sys)
#sys.setdefaultencoding("utf-8")
# 创建解析Excel对象
excelObj = ParseExcel()
# 将Excel数据加载到内存
excelObj.loadWorkBook(dataFilePath)
