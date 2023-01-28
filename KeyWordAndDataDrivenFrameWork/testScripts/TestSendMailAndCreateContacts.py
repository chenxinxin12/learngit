import traceback

# from . import *
# from . import CreateContacts
# from .WriteTestResult import writeTestResult
from action.PageAction import capture_screen
from config.VarConfig import *
from testScripts import excelObj, CreateContacts
from testScripts.WriteTestResult import writeTestResult
from action.PageAction import *

def TestSendMailAndCreateContacts():
    try:
        # 根据Excel文件的sheet名字获取sheet对象
        caseSheet = excelObj.getSheetByName("测试用例")
        # 获取测试用例sheet中是否执行列对象
        isExecuteColumn = excelObj.getColumn(caseSheet, testCase_isExecute)
        # 记录执行成功的测试用例个数
        successfulCase = 0
        # 记录需要执行的用例个数
        requiredCase = 0
        for idx, i in enumerate(isExecuteColumn[1:]):
            # 因为用例第一行为标题，无需执行
            caseName = excelObj.getCellOfValue(caseSheet, rowNo=idx + 2, colsNo=testCase_testCaseName)
            # 循环遍历测试用例表中的测试用例，执行被设置为执行的用例
            if i.value == "y":
                requiredCase += 1
                # 获取测试用例表中第idx+1行
                # 用例执行过程中使用的框架类型
                useFrameWorkName = excelObj.getCellOfValue(caseSheet, rowNo=idx + 2, colsNo=testCase_frameWorkName)
                # 获取获取测试用例表中，第idx+1行执行用例的步骤sheet名字
                stepSheetName = excelObj.getCellOfValue(caseSheet, rowNo=idx + 2, colsNo=testCase_testStepSheetName)
                print("---" + stepSheetName)
                if useFrameWorkName == "数据":
                    print("***调用数据驱动***")
                    # 获取数据驱动对应的数据sheet
                    dataSheetName = excelObj.getCellOfValue(caseSheet, rowNo=idx + 2,
                                                            colsNo=testCase_dataSourceSheetName)
                    # 获取第idx+1行测试用例的步骤sheet对象
                    stepSheetObj = excelObj.getSheetByName(stepSheetName)
                    # 获取数据对应的sheet对象
                    dataSheetObj = excelObj.getSheetByName(dataSheetName)
                    # 通过数据驱动执行添加联系人
                    result = CreateContacts.dataDriverFun(dataSheetObj, stepSheetObj)
                    if result:
                        print("用例%s执行成功" % caseName)
                        successfulCase += 1
                        writeTestResult(caseSheet, rowNo=idx + 2, colsNo="testCase", testResult="pass")
                    else:
                        print("用例%s执行失败" % caseName)
                        writeTestResult(caseSheet, rowNo=idx + 2, colsNo="testCase", testResult="fail")
                elif useFrameWorkName == "关键字":
                    print("***调用关键字驱动***")
                    caseStepObj = excelObj.getSheetByName(stepSheetName)
                    stepNums = excelObj.getRowsNumber(caseStepObj)
                    successfulSteps = 0
                    print("测试共%s步" % stepNums)
                    for index in range(2, stepNums + 1):
                        # 获取步骤sheet中第index行对象
                        stepRow = excelObj.getRow(caseStepObj, index)
                        # 获取关键字作为调用的函数名
                        keyWord = stepRow[testStep_keyWords - 1].value
                        # 获取操作元素定位方法作为调用函数的参数
                        locationType = stepRow[testStep_locationType - 1].value
                        # 获取操作元素的定位表达式作为调用函数的参数
                        locatorExpression = stepRow[testStep_locatorExpression - 1].value
                        # 获取操作值作为调用函数的参数
                        operateValue = stepRow[testStep_operatValue - 1].value
                        if isinstance(operateValue, int):
                            operateValue = str(operateValue)
                        tmpStr = "'%s','%s'" % (locationType.lower(), locatorExpression.replace(
                            "'", '"')) if locationType and locatorExpression else ""
                        if tmpStr:
                            tmpStr += \
                                ",'" + operateValue + "'" if operateValue else ""
                        else:
                            tmpStr += \
                                "'" + operateValue + "'" if operateValue else ""
                        runStr = keyWord + "(" + tmpStr + ")"
                        print("runStr" + runStr)
                        try:
                            eval(runStr)
                        except Exception as e:
                            print('执行步骤%s发生异常' % stepRow[testStep_testStepDescribe - 1].value)
                            print(traceback.print_exc())
                            # # 截取异常屏幕图片
                            capturePic = capture_screen()
                            # # 获取详细的异常堆栈信息
                            errorInfo = traceback.format_exc()
                            writeTestResult(stepSheetObj, rowNo=index, colsNo="caseStep", testResult="faild",
                                            errorInfo=str(errorInfo), picPath=capturePic)
                        else:
                            successfulSteps += 1
                            print('执行步骤%s成功' % stepRow[testStep_testStepDescribe - 1].value)
                            writeTestResult(caseStepObj, rowNo=index, colsNo="caseStep", testResult="pass")
                    if successfulSteps == stepNums - 1:
                        successfulCase += 1
                        print("用例%s执行通过" % caseName)
                        writeTestResult(caseSheet, rowNo=index + 2, colsNo="testCase", testResult="pass")
                    else:
                        print("用例%执行失败" % caseName)
                        writeTestResult(caseSheet, rowNo=index + 2, colsNo="testCase", testResult="fail")
            else:
                # 清空不需要执行用例的执行时间和执行结果
                writeTestResult(caseSheet, rowNo=index + 2, colsNo="testCase", testResult="")
        print("共%d条用例，%d条需要被执行，成功执行%d条" % (len(isExecuteColumn) - 1, requiredCase, successfulCase))
    except Exception as err:
        print(traceback.print_exc())


if __name__ == "__main__":
    TestSendMailAndCreateContacts()
