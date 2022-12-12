import sys
import cv2
import threading
import logging
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt6.QtGui import QPalette, QColor, QIcon, QPixmap
from PyQt6.QtCore import Qt

from save_send_network_tables import *


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
 
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
 
 
class MainWindow(QMainWindow):
    bot_active = False
    auto_bot = None
    window_message = ""
    mode = 0
    tries = 0
 
    def __init__(self):
        super(MainWindow, self).__init__()#*args, **kwargs)
     #   self.setupUi(self)
        self.setWindowTitle("Smarter Dashboard")
        self.setWindowIcon(QIcon("GUI/4829logo.png"))
        self.field_image = QPixmap(cv2.imread("GUI/rapid-react-field-red.png"))

        layout = QGridLayout()

        playingfieldmap = QLabel()
        pixmap = self.convert_cv_qt(self.field_image)
        playingfieldmap.setPixmap(pixmap)
        


        #first row
        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('orange'), 0, 1)
        layout.addWidget(Color('yellow'), 0, 2)
        layout.addWidget(Color('red'), 0, 3)
        layout.addWidget(Color('orange'), 0, 4)
        layout.addWidget(Color('yellow'), 0, 5)
        #second row
        layout.addWidget(playingfieldmap, 1, 0, 4, 2)
        #layout.addWidget(Color('green'), 1, 0, 4, 1)
        #layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 1, 2)
        layout.addWidget(Color('green'), 1, 3)
        layout.addWidget(Color('blue'), 1, 4)
        layout.addWidget(Color('purple'), 1, 5)
        #third row
        #layout.addWidget(Color('pink'), 2, 0)
        #layout.addWidget(Color('grey'), 2, 1)
        layout.addWidget(Color('black'), 2, 2)  
        layout.addWidget(Color('pink'), 2, 3)
        layout.addWidget(Color('grey'), 2, 4)
        layout.addWidget(Color('black'), 2, 5)
        #fourth row
        #layout.addWidget(Color('red'), 3, 0)
        #layout.addWidget(Color('orange'), 3, 1)
        layout.addWidget(Color('yellow'), 3, 2)
        layout.addWidget(Color('red'), 3, 3)
        layout.addWidget(Color('orange'), 3, 4)
        layout.addWidget(Color('yellow'), 3, 5)
 
        #fifth row
        #layout.addWidget(Color('green'), 4, 0)
        #layout.addWidget(Color('blue'), 4, 1)
        layout.addWidget(Color('purple'), 4, 2)
        layout.addWidget(Color('green'), 4, 3)
        layout.addWidget(Color('blue'), 4, 4)
        layout.addWidget(Color('purple'), 4, 5)
 
        #sixth row
        #layout.addWidget(Color('pink'), 5, 0)
        layout.addWidget(Color('grey'), 5, 1)
        layout.addWidget(Color('black'), 5, 2)
        layout.addWidget(Color('pink'), 5, 3)
        layout.addWidget(Color('grey'), 5, 4)
        layout.addWidget(Color('black'), 5, 5)
 
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

"""
    def establish_network_table_connection(self):
        cond = threading.Condition()
        notified = [False]

        def connectionListener(connected, info):
            print(info, '; Connected=%s' % connected)
            with cond:
                notified[0] = True
                cond.notify()

        logging.basicConfig(level=logging.DEBUG)
        NetworkTables.startClientTeam(4829)
        NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

        with cond:
            print("Waiting")
            if not notified[0]:
                cond.wait()
                self.connected_to_network_table = False

        # This is reached once it is connected to the network table
        self.connected_to_network_table = True
        nt = NetworkTables.getTable("climbZerosTable")
        self.nt = nt
        print("Connected")


    def save_climb_zeroes(self):
        if self.nt is not None:
            self.label.setText("Connected")
            # This starts a thread that will run until climb values are saved
            t2 = threading.Thread(target=receive_climb_values, args=[self.nt])
            t2.start()
            self.button1.setStyleSheet("background-color: green")
        else:
            self.label.setText("Cannot establish connection")
    
    def send_button_clicked(self):
        if self.nt is not None:
            self.label.setText("Connected")
            self.sending_climb_zeroes = not self.sending_climb_zeroes
            if self.sending_climb_zeroes:
                self.button2.setText("Stop Sending")
                self.button1.setStyleSheet("")
                self.button1.setDisabled(True)
                t3 = threading.Thread(target=send_climb_values, args=[self.nt])
                t3.start()
            else:
                self.button2.setText("Send")
                self.button1.setEnabled(True)
        else:
            self.label.setText("Cannot establish connection")


"""
    def convert_cv_qt(self, cv_img) -> QPixmap:
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
        p = convert_to_Qt_format.scaled(int(self.width() / 2), int(self.height() / 2), Qt.AspectRatioMode.KeepAspectRatio)
        return QPixmap.fromImage(p)



        


    
app = QApplication(sys.argv)
 
window = MainWindow()
window.show()
 
app.exec()

