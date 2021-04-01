'''
        deleteLater()  # 在代码执行完之后删除对象
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
        self.setWindowTitle("父子关系")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        obj1 = QObject()
        self.obj1 = obj1    #全局变量存储在堆中
        obj2 = QObject()
        obj3 = QObject()

        obj2.setParent(obj1)
        obj3.setParent(obj2)

        print(obj1)
        print(obj2)
        print(obj3)

        obj1.destroyed.connect(lambda :print('obj1被释放'))
        obj2.destroyed.connect(lambda :print('obj2被释放'))
        obj3.destroyed.connect(lambda :print('obj3被释放'))

        #del obj2    #删除栈中的对象，该对象指向堆中的全局变量

        print(obj2.deleteLater())       #deleteLater：删除堆中的对象
        print(obj1.children())          #deleteLater在代码执行完成之后删除对象，所以可以打印出obj2

        #案例
        label1 = QLabel(self)
        label1.setText('label1')
        label1.move(50,50)
        label1.setStyleSheet('background-color:green')

        label2 = QLabel(self)
        label2.setText('label2')
        label2.move(100, 100)
        label2.setStyleSheet('background-color:green')

        label3 = QLabel(self)
        label3.setText('label3')
        label3.move(150, 150)
        label3.setStyleSheet('background-color:green')

        #label2.deleteLater()
        del label2

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())