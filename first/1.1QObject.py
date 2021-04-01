'''
        obj = QObject()
        obj.setObjectName('name')  # 设置一个唯一名称
        print(obj.objectName())

        obj.setProperty('level1','第一')  # 给对象添加一个属性和值
        obj.setProperty('level2','第二')
        print(obj.property('level2'))

        print(obj.dynamicPropertyNames())   # 获取所有setProperty()设置属性的对象和属性名称
'''

################################
# PyQt5中文网 - PyQt5全套视频教程 #
#    https://www.PyQt5.cn/     #
#         主讲： 村长            #
################################

from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("object对象")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()
        self.func1()

    def func(self):
        obj = QObject()
        obj.setObjectName('第一个Object对象')
        print(obj.objectName())

    def func1(self):
        obj1 = QObject()
        obj1.setProperty('level1', '第一')
        obj1.setProperty('level2', '第二')
        print(obj1.property('level1'))
        print(obj1.dynamicPropertyNames())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    #print(window.windowTitle())

    window.show()
    sys.exit(app.exec_())