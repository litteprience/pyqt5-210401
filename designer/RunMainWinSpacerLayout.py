import sys
import MainWinSpacerLine
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = MainWinSpacerLine.Ui_MainWindow()
    # 向主窗口上添加控件
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())




