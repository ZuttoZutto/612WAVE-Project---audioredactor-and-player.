# the code is assembled from different parts from different .ui files
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class MainWindowDesign(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ButtonLobbyPlayerLayout = QtWidgets.QHBoxLayout()
        self.ButtonLobbyPlayerLayout.setObjectName("ButtonLobbyPlayerLayout")
        self.SwitchToRedactorButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.SwitchToRedactorButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.SwitchToRedactorButton.setFont(font)
        self.SwitchToRedactorButton.setObjectName("SwitchToRedactorButton")
        self.ButtonLobbyPlayerLayout.addWidget(self.SwitchToRedactorButton)
        self.HelpPlayerButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.HelpPlayerButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.HelpPlayerButton.setFont(font)
        self.HelpPlayerButton.setObjectName("HelpPlayerButton")
        self.ButtonLobbyPlayerLayout.addWidget(self.HelpPlayerButton)
        self.SettingsPlayerButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.SettingsPlayerButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SettingsPlayerButton.setFont(font)
        self.SettingsPlayerButton.setObjectName("SettingsPlayerButton")
        self.ButtonLobbyPlayerLayout.addWidget(self.SettingsPlayerButton)
        self.verticalLayout.addLayout(self.ButtonLobbyPlayerLayout)
        self.LabelLayout = QtWidgets.QHBoxLayout()
        self.LabelLayout.setObjectName("LabelLayout")
        self.PlaylistsLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.PlaylistsLabel.setObjectName("PlaylistsLabel")
        self.LabelLayout.addWidget(self.PlaylistsLabel)
        self.SongsLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.SongsLabel.setObjectName("SongsLabel")
        self.LabelLayout.addWidget(self.SongsLabel)
        self.verticalLayout.addLayout(self.LabelLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddPlaylistButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.AddPlaylistButton.setObjectName("AddPlaylistButton")
        self.horizontalLayout.addWidget(self.AddPlaylistButton)
        self.AddSongButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.AddSongButton.setObjectName("AddSongButton")
        self.horizontalLayout.addWidget(self.AddSongButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollAreasLayout = QtWidgets.QHBoxLayout()
        self.scrollAreasLayout.setObjectName("scrollAreasLayout")
        self.verticalLayout.addLayout(self.scrollAreasLayout)
        self.WarningNoPlaylistChoosedLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.WarningNoPlaylistChoosedLabel.setGeometry(QtCore.QRect(410, 130, 371, 20))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        self.WarningNoPlaylistChoosedLabel.setFont(font)
        self.WarningNoPlaylistChoosedLabel.setObjectName("WarningNoPlaylistChoosedLabel")
        self.WarningSongExistLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.WarningSongExistLabel.setGeometry(QtCore.QRect(435, 85, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        self.WarningSongExistLabel.setFont(font)
        self.WarningSongExistLabel.setObjectName("WarningSongExistLabel")
        self.MainPlayerSongNameLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.MainPlayerSongNameLabel.setGeometry(QtCore.QRect(100, 470, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MainPlayerSongNameLabel.setFont(font)
        self.MainPlayerSongNameLabel.setObjectName("MainPlayerSongNameLabel")
        self.c5BackwardMainPlayerButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.c5BackwardMainPlayerButton.setGeometry(QtCore.QRect(630, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.c5BackwardMainPlayerButton.setFont(font)
        self.c5BackwardMainPlayerButton.setObjectName("c5BackwardMainPlayerButton")
        self.StandbyMainPlayerButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.StandbyMainPlayerButton.setGeometry(QtCore.QRect(670, 480, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.StandbyMainPlayerButton.setFont(font)
        self.StandbyMainPlayerButton.setObjectName("StandbyMainPlayerButton")
        self.MainPlayerSongSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.MainPlayerSongSlider.setGeometry(QtCore.QRect(100, 520, 431, 22))
        self.MainPlayerSongSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.MainPlayerSongSlider.setObjectName("MainPlayerSongSlider")
        self.c5ForwardMainPlayerButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.c5ForwardMainPlayerButton.setGeometry(QtCore.QRect(740, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.c5ForwardMainPlayerButton.setFont(font)
        self.c5ForwardMainPlayerButton.setObjectName("c5ForwardMainPlayerButton")
        self.NextSongMainPlayerButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.NextSongMainPlayerButton.setGeometry(QtCore.QRect(740, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.NextSongMainPlayerButton.setFont(font)
        self.NextSongMainPlayerButton.setObjectName("NextSongMainPlayerButton")
        self.PrecediousSongMainPlayerButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PrecediousSongMainPlayerButton.setGeometry(QtCore.QRect(630, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PrecediousSongMainPlayerButton.setFont(font)
        self.PrecediousSongMainPlayerButton.setObjectName("PrecediousSongMainPlayerButton")
        self.MainPlayerSongMaxTimeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.MainPlayerSongMaxTimeLabel.setGeometry(QtCore.QRect(535, 530, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MainPlayerSongMaxTimeLabel.setFont(font)
        self.MainPlayerSongMaxTimeLabel.setObjectName("MainPlayerSongMaxTimeLabel")
        self.MainPlayerSongTimeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.MainPlayerSongTimeLabel.setGeometry(QtCore.QRect(535, 510, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MainPlayerSongTimeLabel.setFont(font)
        self.MainPlayerSongTimeLabel.setObjectName("MainPlayerSongTimeLabel")
        self.PlayingSongIconLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.PlayingSongIconLabel.setGeometry(QtCore.QRect(10, 480,  81, 81))
        self.PlayingSongIconLabel.setObjectName("PlayingSongIconLabel")

        self.ConnectionButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ConnectionButton.setEnabled(True)
        self.ConnectionButton.setGeometry(QtCore.QRect(20, 280, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.ConnectionButton.setFont(font)
        self.ConnectionButton.setObjectName("ConnectionButton")
        self.CutPartButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.CutPartButton.setEnabled(True)
        self.CutPartButton.setGeometry(QtCore.QRect(410, 100, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.CutPartButton.setFont(font)
        self.CutPartButton.setObjectName("CutPartButton")
        self.ChangeSpeedStepButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ChangeSpeedStepButton.setEnabled(True)
        self.ChangeSpeedStepButton.setGeometry(QtCore.QRect(20, 370, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.ChangeSpeedStepButton.setFont(font)
        self.ChangeSpeedStepButton.setObjectName("ChangeSpeedStepButton")
        self.LayOwerButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.LayOwerButton.setEnabled(True)
        self.LayOwerButton.setGeometry(QtCore.QRect(410, 190, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.LayOwerButton.setFont(font)
        self.LayOwerButton.setObjectName("LayOwerButton")
        self.ChangeFormatButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ChangeFormatButton.setEnabled(True)
        self.ChangeFormatButton.setGeometry(QtCore.QRect(20, 100, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.ChangeFormatButton.setFont(font)
        self.ChangeFormatButton.setObjectName("ChangeFormatButton")
        self.CutSilenceButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.CutSilenceButton.setEnabled(True)
        self.CutSilenceButton.setGeometry(QtCore.QRect(410, 280, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.CutSilenceButton.setFont(font)
        self.CutSilenceButton.setObjectName("CutSilenceButton")
        self.RecorderButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.RecorderButton.setEnabled(True)
        self.RecorderButton.setGeometry(QtCore.QRect(410, 370, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.RecorderButton.setFont(font)
        self.RecorderButton.setObjectName("RecorderButton")
        self.ChangeMetadataButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ChangeMetadataButton.setEnabled(True)
        self.ChangeMetadataButton.setGeometry(QtCore.QRect(20, 190, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.ChangeMetadataButton.setFont(font)
        self.ChangeMetadataButton.setObjectName("ChangeMetadataButton")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SwitchToRedactorButton.setText(_translate("MainWindow", "РЕДАКТОР"))
        self.HelpPlayerButton.setText(_translate("MainWindow", "ПОМОЩЬ"))
        self.SettingsPlayerButton.setText(_translate("MainWindow", "НАСТРОЙКИ"))
        self.PlaylistsLabel.setText(_translate("MainWindow", "ВАШИ ПЛЕЙЛИСТЫ"))
        self.SongsLabel.setText(_translate("MainWindow", "Сдесь появится название вашего плейлиста"))
        self.AddPlaylistButton.setText(_translate("MainWindow", "Добавить плейлист"))
        self.AddSongButton.setText(_translate("MainWindow", "Добавить песню в плейлист"))
        self.WarningNoPlaylistChoosedLabel.setText(_translate("MainWindow", "ВЫБЕРИТЕ ПЛЕЙЛИСТ, В КОТОРЫЙ ХОТИТЕ ДОБАВИТЬ ПЕСНЮ"))
        self.WarningSongExistLabel.setText(_translate("Form", "ПЕСНЯ С ТАКИМ НАЗВАНИЕМ УЖЕ СУЩЕСТВУЕТ В ЭТОМ ПЛЕЙЛИСТЕ"))
        self.MainPlayerSongNameLabel.setText(
            _translate("MainWindow", "Mariya Takeuchi - Mainichiga Special(Golden ITSUMADEMO)"))
        self.c5BackwardMainPlayerButton.setText(_translate("MainWindow", "<<5c"))
        self.StandbyMainPlayerButton.setText(_translate("MainWindow", "▶"))
        self.c5ForwardMainPlayerButton.setText(_translate("MainWindow", "5c>>"))
        self.NextSongMainPlayerButton.setText(_translate("MainWindow", "▶|"))
        self.PrecediousSongMainPlayerButton.setText(_translate("MainWindow", "|◀"))
        self.MainPlayerSongMaxTimeLabel.setText(_translate("MainWindow", "00:00"))
        self.MainPlayerSongTimeLabel.setText(_translate("MainWindow", "00:00"))
        self.PlayingSongIconLabel.setText(_translate("MainWindow", "TextLabel"))

        self.ConnectionButton.setText(_translate("MainWindow", "СЛИЯНИЕ"))
        self.CutPartButton.setText(_translate("MainWindow", "ВЫРЕЗАТЬ ЧАСТЬ"))
        self.ChangeSpeedStepButton.setText(_translate("MainWindow", "ИЗМЕНЕНИЕ СКОРОСТИ\n"
                                                                    " И ЧАСТОТЫ(ШАГА)"))
        self.LayOwerButton.setText(_translate("MainWindow", "НАЛОЖЕНИЕ"))
        self.ChangeFormatButton.setText(_translate("MainWindow", "ИЗМЕНЕНИЕ ФОРМАТА"))
        self.CutSilenceButton.setText(_translate("MainWindow", "УБРАТЬ ТИШИНУ"))
        self.RecorderButton.setText(_translate("MainWindow", "ЗАПИСЬ"))
        self.ChangeMetadataButton.setText(_translate("MainWindow", "ИЗМЕНЕНИЕ МЕТАДАТЫ"))