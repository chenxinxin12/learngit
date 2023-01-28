import win32clipboard as w
import win32con


class Clipboard(object):
    '''模拟windo设置剪切板'''

    # 读取剪切板
    @staticmethod
    def getText():
        # 打开剪切板
        w.OpenClipboard()
        # 获取剪切板中的数据
        d = w.GetClipboardData(win32con.CF_TEXT)
        # 关闭剪切板
        w.CloseClipboard()
        # 返回剪切板数据给调用者
        return d

    # 设置剪切板内容
    @staticmethod
    def setText(aString):
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
        w.CloseClipboard()
