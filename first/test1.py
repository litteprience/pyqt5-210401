from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()  #调用父类QWidget的属性和方法
        self.setWindowTitle("软件名称")
        self.resize(600,500)
        self.func_list()

    def func_list(self):
        self.func()
        self.func1()

    def func(self):
        btn = QPushButton(self)
        btn.setText("软件内容")
        btn.resize(120, 30)
        btn.move(100, 100)
        btn.setStyleSheet('background-color:green;font-size:16px;')

    def func1(self):
        label = QLabel(self)
        label.setText("标签")
        label.setStyleSheet('background-color:green;font-size:16px;')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    window.show()
    sys.exit(app.exec_())