
'''
        Qt.TimerType
        killTimer(timer_id)
'''


from PyQt5.Qt import *
import sys

class Obj(QObject):
    def timerEvent(self, QTimerEvent) :
        print(QTimerEvent,2)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    obj = Obj()
    timer_id = obj.startTimer(1000)

    obj.killTimer(timer_id)    


    window.show()
    sys.exit(app.exec_())
