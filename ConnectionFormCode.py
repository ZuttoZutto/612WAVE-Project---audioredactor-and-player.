from PyQt6.QtWidgets import QWidget, QFileDialog
from pydub import AudioSegment
import pygame
import mutagen
from mutagen.id3 import ID3
import pydub
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from ConnectionFormDesign import ConnectionFormDesign
from PyQt6.uic.Compiler.qtproxies import QtGui
from PyQt6 import QtCore, QtGui, QtWidgets


class ConnectionForm(QWidget, ConnectionFormDesign):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 300)

        self.FileChooseUpConnectionButton.pressed.connect(self.chose_up_file)
        self.FileChooseDownConnectionButton.pressed.connect(self.chose_down_file)
        self.ConnectionConnectionButton.pressed.connect(self.connection)
        self.PathConnectionButton.pressed.connect(self.chose_path)

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        self.FileChooseUpConnectionButton.setFont(font)
        self.FileChooseDownConnectionButton.setFont(font)
        self.ConnectionConnectionButton.setFont(font)
        self.PixmapUpConnectionLabel.setText("")
        self.PixmapDownConnectionLabel.setText("")
        self.WarningConnectionLabel.hide()

        self.FromatConnectionComboBox.addItem("mp3")
        self.FromatConnectionComboBox.addItem("ogg")
        self.FromatConnectionComboBox.addItem("flac")
        self.FromatConnectionComboBox.addItem("aac")
        self.FromatConnectionComboBox.addItem("oga")
        self.FromatConnectionComboBox.addItem("wav")
        self.MetadataConnectionComboBox.addItem("От верхнего файла")
        self.MetadataConnectionComboBox.addItem("От нижнего файла")

    def chose_up_file(self):
        self.up_file_name = QFileDialog.getOpenFileName(self, 'Выберите первый файл для слияния. Поддерживаются форматы: wav, mp3, ogg(oga), aac, flac.', '','Все файлы (*);;(*.mp3);;(*.wav);;(*.ogg);;(*.aac);;(*.flac);;(*.oga)')[0]
        if self.up_file_name != '':
            font = QtGui.QFont("font")
            font.setFamily("Comic Sans MS")
            try:
                audio_test = AudioSegment.from_file(self.up_file_name)
                self.up_audio = audio_test
                audio_test.export("redactor_audiofile_container.mp3", format="mp3", bitrate="192k")
                audio_test = pygame.mixer.Sound("redactor_audiofile_container.mp3")
                test_channel = audio_test.play()
                test_channel.stop()
                try:
                    search_metadata_icon = ID3(self.up_file_name)
                    # Получаем обложку альбома (если есть)
                    temp_flag = False
                    for key in search_metadata_icon.keys():
                        if key.startswith("APIC:"):
                            cover_data = search_metadata_icon[key].data
                            temp_flag = True
                            break

                    pixmap = QPixmap()

                    if temp_flag:
                        pixmap.loadFromData(cover_data)
                        pixmap = pixmap.scaled(61, 61, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                                               transformMode=Qt.TransformationMode.SmoothTransformation)
                        self.PixmapUpConnectionLabel.setPixmap(pixmap)
                except mutagen.id3._util.ID3NoHeaderError:
                    pass
                self.FileChooseUpConnectionButton.setText(self.up_file_name)
                font.setPointSize(6)
                self.FileChooseUpConnectionButton.setFont(font)
            except pydub.exceptions.CouldntDecodeError:
                font.setPointSize(8)
                self.FileChooseUpConnectionButton.setFont(font)
                self.FileChooseUpConnectionButton.setText("ОШИБКА ЧТЕНИЯ ФАЙЛА")
        else:
            self.up_file_name = self.FileChooseUpConnectionButton.text()

    def chose_down_file(self):
        self.down_file_name = QFileDialog.getOpenFileName(self,'Выберите первый файл для слияния. Поддерживаются форматы: wav, mp3, ogg(oga), aac, flac.', '', 'Все файлы (*);;(*.mp3);;(*.wav);;(*.ogg);;(*.aac);;(*.flac);;(*.oga)')[0]
        if self.down_file_name != '':
            font = QtGui.QFont("font")
            font.setFamily("Comic Sans MS")
            try:
                audio_test = AudioSegment.from_file(self.down_file_name)
                self.down_audio = audio_test
                audio_test.export("redactor_audiofile_container.mp3", format="mp3", bitrate="192k")
                audio_test = pygame.mixer.Sound("redactor_audiofile_container.mp3")
                test_channel = audio_test.play()
                test_channel.stop()
                try:
                    search_metadata_icon = ID3(self.down_file_name)
                    # Получаем обложку альбома (если есть)
                    temp_flag = False
                    for key in search_metadata_icon.keys():
                        if key.startswith("APIC:"):
                            cover_data = search_metadata_icon[key].data
                            temp_flag = True
                            break

                    pixmap = QPixmap()

                    if temp_flag:
                        pixmap.loadFromData(cover_data)
                        pixmap = pixmap.scaled(61, 61, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                                               transformMode=Qt.TransformationMode.SmoothTransformation)
                        self.PixmapDownConnectionLabel.setPixmap(pixmap)
                except mutagen.id3._util.ID3NoHeaderError:
                    pass
                self.FileChooseDownConnectionButton.setText(self.down_file_name)
                font.setPointSize(6)
                self.FileChooseDownConnectionButton.setFont(font)
            except pydub.exceptions.CouldntDecodeError:
                font.setPointSize(8)
                self.FileChooseDownConnectionButton.setFont(font)
                self.FileChooseDownConnectionButton.setText("ОШИБКА ЧТЕНИЯ ФАЙЛА")
        else:
            self.down_file_name = self.FileChooseDownConnectionButton.text()

    def connection(self):
        self.WarningConnectionLabel.hide()
        if self.FileChooseUpConnectionButton.text() != "Выберите 1-ый файл" and self.FileChooseUpConnectionButton.text() != "ОШИБКА ЧТЕНИЯ ФАЙЛА" and self.FileChooseDownConnectionButton.text() != "Выберите 2-ой файл" and self.FileChooseDownConnectionButton.text() != "ОШИБКА ЧТЕНИЯ ФАЙЛА" and self.PathConnectionButton.text() != "Выберите расположение выходного файла":
            product_audio = self.up_audio + self.down_audio
            try:
                product_audio.export(self.PathConnectionButton.text() + "." + self.FromatConnectionComboBox.currentText(),
                                     format=self.FromatConnectionComboBox.currentText())
                try:
                    if self.MetadataConnectionComboBox.currentText() == "От верхнего файла":
                        source_tags = ID3(self.up_file_name)
                        target_tags = ID3(self.down_file_name)
                        for frame in source_tags.keys():
                            target_tags[frame] = source_tags[frame]
                        target_tags.save(self.PathConnectionButton.text() + "." + self.FromatConnectionComboBox.currentText())
                    else:
                        source_tags = ID3(self.down_file_name)
                        target_tags = ID3(self.up_file_name)
                        for frame in source_tags.keys():
                            target_tags[frame] = source_tags[frame]
                        target_tags.save(self.PathConnectionButton.text() + "." + self.FromatConnectionComboBox.currentText())
                except mutagen.id3._util.ID3NoHeaderError:
                    pass
                self.WarningConnectionLabel.setText("СЛИЯНИЕ ВЫПОЛНЕНО УСПЕШНО")
                self.WarningConnectionLabel.show()
            except pydub.exceptions.CouldntEncodeError:
                self.WarningConnectionLabel.setText("ОШИБКА КОДИРОВАНИЯ")
                self.WarningConnectionLabel.show()
        else:
            self.WarningConnectionLabel.setText("ВЫБЕРИТЕ 2 ФАЙЛА И ПУТЬ ДЛЯ ВЫХОДНОГО ФАЙЛА")
            self.WarningConnectionLabel.show()

    def chose_path(self):
        product_file_name = QFileDialog.getSaveFileName(self, "Сохранить файл", "")[0]
        if product_file_name != '':
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(6)
            self.PathConnectionButton.setFont(font)
            self.PathConnectionButton.setText(product_file_name)