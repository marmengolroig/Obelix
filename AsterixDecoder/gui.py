from interface import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        self.ui = Ui_MainWindow()
        self.ui.setupUI(self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())