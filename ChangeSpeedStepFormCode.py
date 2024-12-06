from ChangeSpeedStepFormDesign import ChangeSpeedStepFormDesign

from PyQt6.QtWidgets import QWidget, QFileDialog
from pydub import AudioSegment
import pygame
import mutagen
from mutagen.id3 import ID3
import pydub
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.uic.Compiler.qtproxies import QtGui
from PyQt6 import QtCore, QtGui, QtWidgets
import librosa
import soundfile


class ChangeSpeedStepForm(QWidget, ChangeSpeedStepFormDesign):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 336)

        self.SpeedChangeSpeedSlider.setRange(1, 20)
        self.StepChangeSpeedSlider.setRange(-15, 15)
        self.SpeedChangeSpeedSlider.setValue(10)
        self.StepChangeSpeedSlider.setValue(0)
        self.SpeedChangeSpeedLineEdit.setText("1.0")
        self.StepChangeSpeedLineEdit.setText("0")
        self.speed_is_valid = True
        self.step_is_valid = True

        self.SpeedChangeSpeedSlider.valueChanged.connect(self.speed_slider_changed)
        self.StepChangeSpeedSlider.valueChanged.connect(self.step_slider_changed)
        self.SpeedChangeSpeedLineEdit.textChanged.connect(self.speed_line_changed)
        self.StepChangeSpeedLineEdit.textChanged.connect(self.step_line_changed)
        self.PathChangeSpeedButton.pressed.connect(self.chose_path)
        self.FileChoseChangeSpeedButton.pressed.connect(self.chose_file)
        self.ChangeSpeedChangeSpeedButton.pressed.connect(self.change_speed_step)

        self.SpeedWarningChangeSpeedLabel.hide()
        self.StepWarningChangeSpeedLabel.hide()
        self.WarningChangeSpeedLabel.hide()

        self.FormatChangeSpeedComboBox.addItem("mp3")
        self.FormatChangeSpeedComboBox.addItem("ogg")
        self.FormatChangeSpeedComboBox.addItem("flac")
        self.FormatChangeSpeedComboBox.addItem("aac")
        self.FormatChangeSpeedComboBox.addItem("oga")
        self.FormatChangeSpeedComboBox.addItem("wav")

    def speed_slider_changed(self):
        self.SpeedChangeSpeedLineEdit.setText(str(self.SpeedChangeSpeedSlider.value() / 10))

    def step_slider_changed(self):
        self.StepChangeSpeedLineEdit.setText(str(self.StepChangeSpeedSlider.value()))

    def speed_line_changed(self):
        try:
            float(self.SpeedChangeSpeedLineEdit.text())
            self.SpeedWarningChangeSpeedLabel.hide()
            self.speed_is_valid = True
        except ValueError:
            self.SpeedWarningChangeSpeedLabel.show()
            self.speed_is_valid = False

    def step_line_changed(self):
        try:
            int(self.StepChangeSpeedLineEdit.text())
            self.StepWarningChangeSpeedLabel.hide()
            self.step_is_valid = True
        except ValueError:
            self.StepWarningChangeSpeedLabel.show()
            self.step_is_valid = False

    def chose_path(self):
        product_file_name = QFileDialog.getSaveFileName(self, "Сохранить файл", "")[0]
        if product_file_name != '':
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(6)
            self.PathChangeSpeedButton.setFont(font)
            self.PathChangeSpeedButton.setText(product_file_name)

    def chose_file(self):
        self.file_name = QFileDialog.getOpenFileName(self,
                                                          'Выберите файл для изменения скорости и частоты(шага). Поддерживаются форматы: wav, mp3, ogg(oga), aac, flac.',
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
                        self.PixmapChangeSpeedLabel.setPixmap(pixmap)
                except mutagen.id3._util.ID3NoHeaderError:
                    pass
                if len(self.file_name) > 31:
                    mod_str = self.file_name[:15] + "\n" + self.file_name[15:30] + "\n" + self.file_name[30:]
                    self.FileChoseChangeSpeedButton.setText(mod_str)
                elif len(self.file_name) > 16:
                    mod_str = self.file_name[:15] + "\n" + self.file_name[15:]
                    self.FileChoseChangeSpeedButton.setText(mod_str)
                else:
                    self.FileChoseChangeSpeedButton.setText(self.file_name)
                font.setPointSize(6)
                self.FileChoseChangeSpeedButton.setFont(font)
            except pydub.exceptions.CouldntDecodeError:
                font.setPointSize(8)
                self.FileChoseChangeSpeedButton.setFont(font)
                self.FileChoseChangeSpeedButton.setText("ОШИБКА ЧТЕ-\nНИЯ ФАЙЛА")
        else:
            self.file_name = self.FileChoseChangeSpeedButton.text()

    def change_speed_step(self):
        self.WarningChangeSpeedLabel.hide()
        if self.FileChoseChangeSpeedButton.text() != "Выберите\nфайл" and self.FileChoseChangeSpeedButton.text() != "ОШИБКА ЧТЕ-\nНИЯ ФАЙЛА" and self.PathChangeSpeedButton.text() != "Выберите расположение выходного файла" and self.speed_is_valid and self.step_is_valid:
            try:
                y, sr = librosa.load(self.file_name, sr=None)
                y = librosa.effects.time_stretch(y, rate=round(float(self.SpeedChangeSpeedLineEdit.text()), 2))
                y = librosa.effects.pitch_shift(y, sr=sr, n_steps=int(self.StepChangeSpeedLineEdit.text()))
                soundfile.write(self.PathChangeSpeedButton.text() + '.' + self.FormatChangeSpeedComboBox.currentText(), y, sr)
                self.WarningChangeSpeedLabel.setText("УСПЕШНО СОХРАНЕНО")
                self.WarningChangeSpeedLabel.show()
            except pydub.exceptions.CouldntEncodeError:
                self.WarningChangeSpeedLabel.setText("ОШИБКА КОДИРОВАНИЯ")
                self.WarningChangeSpeedLabel.show()
        else:
            self.WarningChangeSpeedLabel.setText("УКАЖИТЕ ВСЕ ДАННЫЕ")
            self.WarningChangeSpeedLabel.show()