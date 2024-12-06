from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QFileDialog
from PyQt6.QtCore import Qt
from PyQt6.uic.Compiler.qtproxies import QtGui
from pydub import AudioSegment
import pygame
import mutagen
from mutagen.id3 import ID3
import pydub

from CutPartFormDesign import CutPartFormDesign


class CutPartForm(QWidget, CutPartFormDesign):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 300)
        self.file_loaded = False

        self.PathCutPartButton.clicked.connect(self.chose_path)
        self.FileChoseCutPartButton.clicked.connect(self.chose_file)
        self.UpCutPartSlider.valueChanged.connect(self.up_value_changed)
        self.DownCutPartSlider.valueChanged.connect(self.down_value_changed)
        self.CutPartCutPartButton.pressed.connect(self.cut_part)

        self.FormatCutPartComboBox.addItem("mp3")
        self.FormatCutPartComboBox.addItem("ogg")
        self.FormatCutPartComboBox.addItem("flac")
        self.FormatCutPartComboBox.addItem("aac")
        self.FormatCutPartComboBox.addItem("oga")
        self.FormatCutPartComboBox.addItem("wav")

        self.WarningCutPartLabel.hide()

    def chose_path(self):
        product_file_name = QFileDialog.getSaveFileName(self, "Сохранить файл", "")[0]
        if product_file_name != '':
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(6)
            self.PathCutPartButton.setFont(font)
            self.PathCutPartButton.setText(product_file_name)

    def chose_file(self):
        self.file_name = QFileDialog.getOpenFileName(self,
                                                          'Выберите файл для извлечения части. Поддерживаются форматы: wav, mp3, ogg(oga), aac, flac.',
                                                          '',
                                                          'Все файлы (*);;(*.mp3);;(*.wav);;(*.ogg);;(*.aac);;(*.flac);;(*.oga)')[
            0]
        if self.file_name != '':
            font = QtGui.QFont("font")
            font.setFamily("Comic Sans MS")
            try:
                audio_test = AudioSegment.from_file(self.file_name)
                self.audio = audio_test
                audio_test.export("redactor_audiofile_container.mp3", format="mp3", bitrate="192k")
                audio_test = pygame.mixer.Sound("redactor_audiofile_container.mp3")
                test_channel = audio_test.play()
                test_channel.stop()
                try:
                    search_metadata_icon = ID3(self.file_name)
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
                        self.PixmapCutPartLabel.setPixmap(pixmap)
                except mutagen.id3._util.ID3NoHeaderError:
                    pass
                self.FileChoseCutPartButton.setText(self.file_name)
                font.setPointSize(6)
                self.FileChoseCutPartButton.setFont(font)
                self.file_loaded = True
                self.UpCutPartSlider.setMaximum(len(self.audio))
                self.DownCutPartSlider.setMaximum(len(self.audio))
                self.UpCutPartSlider.setValue(len(self.audio))
            except pydub.exceptions.CouldntDecodeError:
                font.setPointSize(8)
                self.FileChoseCutPartButton.setFont(font)
                self.file_loaded = False
                self.UpCutPartSlider.setValue(0)
                self.DownCutPartSlider.setValue(0)
                self.UpTimeCutPartLabel.setText("00:00:00")
                self.DownTimeCutPartLabel.setText("00:00:00")
                self.FileChoseCutPartButton.setText("ОШИБКА ЧТЕНИЯ ФАЙЛА")
        else:
            self.file_name = self.FileChoseCutPartButton.text()

    def up_value_changed(self):
        if self.file_loaded:
            if self.UpCutPartSlider.value() < self.DownCutPartSlider.value():
                self.UpCutPartSlider.setValue(self.DownCutPartSlider.value())
            pos = self.UpCutPartSlider.value()
            self.UpTimeCutPartLabel.setText(
                str("0" * (pos // 1000 // 60 // 60 < 10)) + str(pos // 1000 // 60 // 60) + ":" + str(
                    "0" * (pos // 1000 // 60 < 10)) + str(
                    pos // 1000 // 60) + ":" + str("0" * (pos // 1000 % 60 < 10) + str(pos // 1000 % 60)) + ":" + str(
                    "0" * (pos // 100 == 0)) + str("0" * (pos // 10 == 0)) + str(pos % 1000))
        else:
            self.UpCutPartSlider.setValue(0)
        self.segment_time_change()

    def down_value_changed(self):
        if self.file_loaded:
            if self.UpCutPartSlider.value() < self.DownCutPartSlider.value():
                self.DownCutPartSlider.setValue(self.UpCutPartSlider.value())
            pos = self.DownCutPartSlider.value()
            self.DownTimeCutPartLabel.setText(
                str("0" * (pos // 1000 // 60 // 60 < 10)) + str(pos // 1000 // 60 // 60) + ":" + str(
                    "0" * (pos // 1000 // 60 < 10)) + str(
                    pos // 1000 // 60) + ":" + str("0" * (pos // 1000 % 60 < 10) + str(pos // 1000 % 60)) + ":" + str(
                    "0" * (pos // 100 == 0)) + str("0" * (pos // 10 == 0)) + str(pos % 1000))
        else:
            self.DownCutPartSlider.setValue(0)
        self.segment_time_change()

    def segment_time_change(self):
        pos = self.UpCutPartSlider.value() - self.DownCutPartSlider.value()
        self.SegmentTimeCutPartLabel.setText(str("0" * (pos // 1000 // 60 // 60 < 10)) + str(pos // 1000 // 60 // 60) + ":" + str("0" * (pos // 1000 // 60 < 10)) + str(
                    pos // 1000 // 60) + ":" + str("0" * (pos // 1000 % 60 < 10) + str(pos // 1000 % 60)) + ":" + str("0" * (pos // 100 == 0)) + str("0" * (pos // 10 == 0)) + str(pos % 1000))

    def cut_part(self):
        self.WarningCutPartLabel.hide()
        if self.file_loaded and self.PathCutPartButton.text() != "Выберите расположение для выходного файла":
            product_audio = self.audio[self.DownCutPartSlider.value():self.UpCutPartSlider.value() + 1]
            try:
                product_audio.export(
                    self.PathCutPartButton.text() + "." + self.FormatCutPartComboBox.currentText(),
                    format=self.FormatCutPartComboBox.currentText())
                self.WarningCutPartLabel.setText("УСПЕШНО СОХРАНЕНО")
                self.WarningCutPartLabel.show()
            except pydub.exceptions.CouldntEncodeError:
                self.WarningCutPartLabel.setText("ОШИБКА КОДИРОВАНИЯ")
                self.WarningCutPartLabel.show()
        else:
            self.WarningCutPartLabel.setText("ВЫБЕРИТЕ ФАЙЛ И РАСПОЛОЖЕНИЕ")
            self.WarningCutPartLabel.show()