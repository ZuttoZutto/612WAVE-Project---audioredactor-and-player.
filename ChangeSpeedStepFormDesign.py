# Form implementation generated from reading ui file 'ChangeSpeedStepFormDesignUi.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class ChangeSpeedStepFormDesign(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 336)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(40, 0, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.SpeedChangeSpeedSlider = QtWidgets.QSlider(parent=Form)
        self.SpeedChangeSpeedSlider.setGeometry(QtCore.QRect(110, 90, 201, 22))
        self.SpeedChangeSpeedSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SpeedChangeSpeedSlider.setObjectName("SpeedChangeSpeedSlider")
        self.StepChangeSpeedSlider = QtWidgets.QSlider(parent=Form)
        self.StepChangeSpeedSlider.setGeometry(QtCore.QRect(110, 190, 201, 22))
        self.StepChangeSpeedSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.StepChangeSpeedSlider.setObjectName("StepChangeSpeedSlider")
        self.FileChoseChangeSpeedButton = QtWidgets.QPushButton(parent=Form)
        self.FileChoseChangeSpeedButton.setGeometry(QtCore.QRect(10, 60, 88, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.FileChoseChangeSpeedButton.setFont(font)
        self.FileChoseChangeSpeedButton.setObjectName("FileChoseChangeSpeedButton")
        self.PixmapChangeSpeedLabel = QtWidgets.QLabel(parent=Form)
        self.PixmapChangeSpeedLabel.setGeometry(QtCore.QRect(17, 150, 71, 71))
        self.PixmapChangeSpeedLabel.setText("")
        self.PixmapChangeSpeedLabel.setObjectName("PixmapChangeSpeedLabel")
        self.SpeedChangeSpeedLineEdit = QtWidgets.QLineEdit(parent=Form)
        self.SpeedChangeSpeedLineEdit.setGeometry(QtCore.QRect(330, 90, 61, 25))
        self.SpeedChangeSpeedLineEdit.setObjectName("SpeedChangeSpeedLineEdit")
        self.StepChangeSpeedLineEdit = QtWidgets.QLineEdit(parent=Form)
        self.StepChangeSpeedLineEdit.setGeometry(QtCore.QRect(330, 190, 61, 25))
        self.StepChangeSpeedLineEdit.setObjectName("StepChangeSpeedLineEdit")
        self.label_11 = QtWidgets.QLabel(parent=Form)
        self.label_11.setGeometry(QtCore.QRect(320, 130, 68, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.ChangeSpeedChangeSpeedButton = QtWidgets.QPushButton(parent=Form)
        self.ChangeSpeedChangeSpeedButton.setGeometry(QtCore.QRect(10, 270, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ChangeSpeedChangeSpeedButton.setFont(font)
        self.ChangeSpeedChangeSpeedButton.setObjectName("ChangeSpeedChangeSpeedButton")
        self.label_12 = QtWidgets.QLabel(parent=Form)
        self.label_12.setGeometry(QtCore.QRect(90, 230, 71, 16))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.FormatChangeSpeedComboBox = QtWidgets.QComboBox(parent=Form)
        self.FormatChangeSpeedComboBox.setGeometry(QtCore.QRect(150, 260, 71, 25))
        self.FormatChangeSpeedComboBox.setObjectName("FormatChangeSpeedComboBox")
        self.WarningChangeSpeedLabel = QtWidgets.QLabel(parent=Form)
        self.WarningChangeSpeedLabel.setGeometry(QtCore.QRect(240, 260, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        self.WarningChangeSpeedLabel.setFont(font)
        self.WarningChangeSpeedLabel.setObjectName("WarningChangeSpeedLabel")
        self.label_14 = QtWidgets.QLabel(parent=Form)
        self.label_14.setGeometry(QtCore.QRect(110, 60, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=Form)
        self.label_15.setGeometry(QtCore.QRect(110, 160, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=Form)
        self.label_16.setGeometry(QtCore.QRect(110, 110, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=Form)
        self.label_17.setGeometry(QtCore.QRect(110, 210, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=Form)
        self.label_18.setGeometry(QtCore.QRect(200, 210, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=Form)
        self.label_19.setGeometry(QtCore.QRect(200, 110, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=Form)
        self.label_20.setGeometry(QtCore.QRect(290, 110, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=Form)
        self.label_21.setGeometry(QtCore.QRect(290, 210, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(parent=Form)
        self.label_22.setGeometry(QtCore.QRect(90, 260, 68, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.PathChangeSpeedButton = QtWidgets.QPushButton(parent=Form)
        self.PathChangeSpeedButton.setGeometry(QtCore.QRect(90, 300, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        self.PathChangeSpeedButton.setFont(font)
        self.PathChangeSpeedButton.setObjectName("PathChangeSpeedButton")
        self.SpeedWarningChangeSpeedLabel = QtWidgets.QLabel(parent=Form)
        self.SpeedWarningChangeSpeedLabel.setGeometry(QtCore.QRect(290, 70, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(6)
        self.SpeedWarningChangeSpeedLabel.setFont(font)
        self.SpeedWarningChangeSpeedLabel.setObjectName("SpeedWarningChangeSpeedLabel")
        self.StepWarningChangeSpeedLabel = QtWidgets.QLabel(parent=Form)
        self.StepWarningChangeSpeedLabel.setGeometry(QtCore.QRect(290, 170, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(6)
        self.StepWarningChangeSpeedLabel.setFont(font)
        self.StepWarningChangeSpeedLabel.setObjectName("StepWarningChangeSpeedLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ИЗМЕНЕНИЕ СКОРОСТИ И ЧАСТОТЫ(ШАГА)"))
        self.FileChoseChangeSpeedButton.setText(_translate("Form", "Выберите\n"
" файл"))
        self.label_11.setText(_translate("Form", "  Ввести\n"
"вручную"))
        self.ChangeSpeedChangeSpeedButton.setText(_translate("Form", "СКАЧАТЬ"))
        self.WarningChangeSpeedLabel.setText(_translate("Form", "ОШИБКА КОДИРОВАНИЯ"))
        self.label_14.setText(_translate("Form", "СКОРОСТЬ"))
        self.label_15.setText(_translate("Form", "ЧАСТОТА(ШАГ)"))
        self.label_16.setText(_translate("Form", "0.1"))
        self.label_17.setText(_translate("Form", "-15"))
        self.label_18.setText(_translate("Form", "+0"))
        self.label_19.setText(_translate("Form", "1.0"))
        self.label_20.setText(_translate("Form", "2.0"))
        self.label_21.setText(_translate("Form", "+15"))
        self.label_22.setText(_translate("Form", "Формат"))
        self.PathChangeSpeedButton.setText(_translate("Form", "Выберите расположение выходного файла"))
        self.SpeedWarningChangeSpeedLabel.setText(_translate("Form", "НЕКОРРЕКТНЫЙ ФОРМАТ"))
        self.StepWarningChangeSpeedLabel.setText(_translate("Form", "НЕКОРРЕКТНЫЙ ФОРМАТ"))
