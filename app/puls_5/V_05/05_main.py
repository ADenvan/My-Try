import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_05_pulsi import Ui_MainWindow

class Puls_5(QMainWindow):
    def __init__(self):
        super(Puls_5, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Puls_5()
    window.show()

    sys.exit(app.exec_())