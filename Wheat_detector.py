from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import webbrowser
import PIL
import warnings
PIL.PILLOW_VERSION = '7.0.0'

warnings.filterwarnings("ignore")

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(718, 440)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_images/Icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(-130, -110, 971, 621))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("ui_images/logo.png"))
        self.logo.setObjectName("logo")
        self.BackGround = QtWidgets.QLabel(self.centralwidget)
        self.BackGround.setGeometry(QtCore.QRect(360, 0, 371, 441))
        self.BackGround.setStyleSheet("background-color: rgb(255, 230, 38);")
        self.BackGround.setText("")
        self.BackGround.setPixmap(QtGui.QPixmap("ui_images/background.jpg"))
        self.BackGround.setObjectName("BackGround")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(410, 250, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.StartButton.setFont(font)
        self.StartButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartButton.setStyleSheet("QPushButton {\n"
                                       "    color: #333;\n"
                                       "   font: 30pt \"Agency FB\";\n"
                                       "background-color: rgb(255, 252, 205);\n"
                                       "    border: 6px solid;\n"
                                       "border-color: rgb(5, 99, 80);\n"
                                       "    border-radius: 0px;\n"
                                       "    border-style: outset;\n"
                                       "\n"
                                       "    }\n"
                                       "\n"
                                       "QPushButton:hover {    \n"
                                       "    background-color: rgb(221, 222, 169);\n"
                                       "    }\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    border-style: inset;\n"
                                       "    background: qradialgradient(\n"
                                       "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                       "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                       "        );\n"
                                       "    }")
        self.StartButton.setObjectName("StartButton")
        self.ChooseButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChooseButton.setGeometry(QtCore.QRect(410, 20, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ChooseButton.setFont(font)
        self.ChooseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ChooseButton.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "   \n"
                                        "    font: 16pt \"Agency FB\";\n"
                                        "background-color: rgb(255, 252, 205);\n"
                                        "    border: 6px solid;\n"
                                        "border-color: rgb(5, 99, 80);\n"
                                        "    border-radius: 0px;\n"
                                        "    border-style: outset;\n"
                                        "\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {    \n"
                                        "    background-color: rgb(221, 222, 169);\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                        "        );\n"
                                        "    }")
        self.ChooseButton.setObjectName("ChooseButton")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(410, 100, 261, 61))
        self.SaveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveButton.setStyleSheet("QPushButton {\n"
                                      "    color: #333;\n"
                                      "      font: 16pt \"Agency FB\";\n"
                                      "background-color: rgb(255, 252, 205);\n"
                                      "    border: 6px solid;\n"
                                      "border-color: rgb(5, 99, 80);\n"
                                      "    border-radius: 0px;\n"
                                      "    border-style: outset;\n"
                                      "\n"
                                      "    }\n"
                                      "\n"
                                      "QPushButton:hover {    \n"
                                      "    background-color: rgb(221, 222, 169);\n"
                                      "    }\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    border-style: inset;\n"
                                      "    background: qradialgradient(\n"
                                      "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                      "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                      "        );\n"
                                      "    }")
        self.SaveButton.setObjectName("SaveButton")
        self.ChooseFormat = QtWidgets.QComboBox(self.centralwidget)
        self.ChooseFormat.setGeometry(QtCore.QRect(590, 250, 81, 31))
        self.ChooseFormat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ChooseFormat.setStyleSheet("color: #333;\n"
                                        "   font: 16pt \"Agency FB\";\n"
                                        "background-color: rgb(255, 252, 205);\n"
                                        "    border: 6px solid;\n"
                                        "border-color: rgb(5, 99, 80);\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "")
        self.ChooseFormat.setObjectName("ChooseFormat")
        self.ChooseFormat.addItem("")
        self.ChooseFormat.addItem("")
        self.PhotosCoords = QtWidgets.QPushButton(self.centralwidget)
        self.PhotosCoords.setGeometry(QtCore.QRect(540, 180, 131, 51))
        self.PhotosCoords.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PhotosCoords.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "   font: 16pt \"Agency FB\";\n"
                                        "background-color: rgb(255, 252, 205);\n"
                                        "    border: 6px solid;\n"
                                        "border-color: rgb(5, 99, 80);\n"
                                        "    border-radius: 0px;\n"
                                        "    border-style: outset;\n"
                                        "\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {    \n"
                                        "    background-color: rgb(221, 222, 169);\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                        "        );\n"
                                        "    }")
        self.PhotosCoords.setObjectName("PhotosCoords")
        self.FieldCoords = QtWidgets.QPushButton(self.centralwidget)
        self.FieldCoords.setGeometry(QtCore.QRect(410, 180, 111, 51))
        self.FieldCoords.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FieldCoords.setStyleSheet("QPushButton {\n"
                                       "    color: #333;\n"
                                       "   font: 16pt \"Agency FB\";\n"
                                       "background-color: rgb(255, 252, 205);\n"
                                       "    border: 6px solid;\n"
                                       "border-color: rgb(5, 99, 80);\n"
                                       "    border-radius: 0px;\n"
                                       "    border-style: outset;\n"
                                       "\n"
                                       "    }\n"
                                       "\n"
                                       "QPushButton:hover {    \n"
                                       "    background-color: rgb(221, 222, 169);\n"
                                       "    }\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    border-style: inset;\n"
                                       "    background: qradialgradient(\n"
                                       "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                       "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                       "        );\n"
                                       "    }")
        self.FieldCoords.setObjectName("FieldCoords")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setGeometry(QtCore.QRect(410, 325, 261, 111))
        self.label.setStyleSheet(" color: #333;\n"
                                 "   font: 30pt \"Agency FB\";\n"
                                 "background-color: rgb(255, 252, 205);\n"
                                 "    border: 6px solid;\n"
                                 "border-color: rgb(5, 99, 80);\n"
                                 "    border-radius: 0px;\n"
                                 "    border-style: outset;\n"
                                 "")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wheat Detector"))
        self.StartButton.setText(_translate("MainWindow", "START"))
        self.ChooseButton.setText(_translate("MainWindow", "CHOOSE FOLDER WITH PHOTOS"))
        self.SaveButton.setText(_translate("MainWindow", "CHOOSE FOLDER TO SAVE PHOTOS"))
        self.ChooseFormat.setItemText(0, _translate("MainWindow", "  PNG"))
        self.ChooseFormat.setItemText(1, _translate("MainWindow", "  JPG"))
        self.PhotosCoords.setText(_translate("MainWindow", "PHOTOS COORDS"))
        self.FieldCoords.setText(_translate("MainWindow", "FIELD COORDS"))
        self.label.setText(_translate("MainWindow", "RESULTS"))


class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)

        self.setupUi(self)
        self.dir_from = 'images'
        self.dir_to = 'detected_images'

        self.ChooseButton.clicked.connect(self.get_dir_from)
        self.SaveButton.clicked.connect(self.get_dir_to)

        self.FieldCoords.clicked.connect(self.get_field_coords)
        self.PhotosCoords.clicked.connect(self.get_photos_coords)

        self.StartButton.clicked.connect(self.make_predictions)

    def get_dir_from(self):
        self.dir_from = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

    def get_dir_to(self):
        self.dir_to = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

    def get_field_coords(self):
        webbrowser.open(r"txt_files\field_coords.txt")

    def get_photos_coords(self):
        webbrowser.open(r"txt_files\photos_coords.txt")

    def make_predictions(self):
        self.label.setStyleSheet(" color: #333;\n"
                                 "   font: 23pt \"Agency FB\";\n"
                                 "background-color: rgb(255, 252, 205);\n"
                                 "    border: 6px solid;\n"
                                 "border-color: rgb(5, 99, 80);\n"
                                 "    border-radius: 0px;\n"
                                 "    border-style: outset;\n"
                                 "")
        self.label.setText('Predicting...\n(this may take some time)')
        QtGui.QGuiApplication.processEvents()

        img_format = str(self.ChooseFormat.currentText()).strip().lower()

        try:
            corners = get_coords(r'txt_files\field_coords.txt')
            photos = get_coords(r'txt_files\photos_coords.txt')

            area = calculate_field_area(corners)

            field_lst = make_predictions(img_format, self.dir_from, self.dir_to)

            total_wheat, total_density = make_calculations(field_lst, area)

            self.label.setText(f'field area = {area}\n'
                               f'wheat on field = {int(total_wheat)}\n'
                               f'wheat per meter = {round(total_density, 2)}')
            self.label.setStyleSheet(" color: #333;\n"
                                     "   font: 19pt \"Agency FB\";\n"
                                     "background-color: rgb(255, 252, 205);\n"
                                     "    border: 6px solid;\n"
                                     "border-color: rgb(5, 99, 80);\n"
                                     "    border-radius: 0px;\n"
                                     "    border-style: outset;\n"
                                     "")

            create_points_plot(corners, photos, field_lst)
        except:
            self.label.setText('ERROR\n'
                               'please check the input data\n'
                               'or instruction')
            self.label.setStyleSheet(" color: #333;\n"
                                     "   font: 19pt \"Agency FB\";\n"
                                     "background-color: rgb(255, 252, 205);\n"
                                     "    border: 6px solid;\n"
                                     "border-color: rgb(5, 99, 80);\n"
                                     "    border-radius: 0px;\n"
                                     "    border-style: outset;\n"
                                     "")



if __name__ == "__main__":
    webbrowser.open(r"txt_files\INSTRUCTION_ИНСТРУКЦИЯ.txt")

    import sys
    from scripts_and_functions.model import *
    from scripts_and_functions.field import *

    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = '2'
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_DisableHighDpiScaling)
    app.setAttribute(QtCore.Qt.AA_Use96Dpi)
    nextGui = mainProgram()
    nextGui.show()
    sys.exit(app.exec_())

