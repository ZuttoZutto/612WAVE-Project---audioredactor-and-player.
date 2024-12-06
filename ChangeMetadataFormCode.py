from PyQt6.QtWidgets import QWidget, QFileDialog
from pydub import AudioSegment
import pygame
import mutagen
from mutagen.id3 import ID3
import pydub
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QByteArray
from PyQt6.uic.Compiler.qtproxies import QtGui
from PyQt6 import QtCore, QtGui, QtWidgets
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, TRCK, TYER, COMM
from PIL import Image
from mutagen.mp3 import MP3
import PIL

from ChangeMetadataFormDesign import ChangeMetadataFormDesign


class ChangeMetadataForm(QWidget, ChangeMetadataFormDesign):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 280)

        self.WarningChangeMetadataLabel.hide()
        self.WarningImageChangeMetadataLabel.hide()
        self.FieldChangeMetadataComboBox.hide()
        self.ValueChangeMetadataLineEdit.hide()

        self.file_loaded = False
        self.metadata_values = {}
        self.FieldChangeMetadataComboBox.addItems(["Название", "Исполнитель", "Альбом", "Трек", "Год", "Комментарий"])

        self.FileChoseChangeMetadataButton.pressed.connect(self.chose_file)
        self.ImagePathChangeMetadataButton.pressed.connect(self.image_path_change)
        self.ValueChangeMetadataLineEdit.textChanged.connect(self.text_changed)
        self.FieldChangeMetadataComboBox.currentIndexChanged.connect(self.index_changed)

    def chose_file(self):
        self.file_name = QFileDialog.getOpenFileName(self,
                                                     'Выберите файл для редакции метадаты. Поддерживается только формат mp3',
                                                     '',
                                                     'Все файлы (*);;(*.mp3)')[
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
                    temp_flag = False
                    for key in search_metadata_icon.keys():
                        if key.startswith("APIC:"):
                            cover_data = search_metadata_icon[key].data
                            temp_flag = True
                            break

                    pixmap = QPixmap()

                    if temp_flag:
                        pixmap.loadFromData(cover_data)
                        pixmap = pixmap.scaled(141, 141, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                                               transformMode=Qt.TransformationMode.SmoothTransformation)
                        self.PixmapChangeMetadataLabel.setPixmap(pixmap)
                except mutagen.id3._util.ID3NoHeaderError:
                    pass
                self.FileChoseChangeMetadataButton.setText(self.file_name)
                font.setPointSize(6)
                self.FileChoseChangeMetadataButton.setFont(font)
                self.file_loaded = True
                self.FieldChangeMetadataComboBox.show()
                self.ValueChangeMetadataLineEdit.show()
                self.WarningChangeMetadataLabel.hide()

                audio = MP3(self.FileChoseChangeMetadataButton.text())
                id3 = ID3(self.FileChoseChangeMetadataButton.text())

                # Загрузка метаданных
                self.metadata_values.clear()
                self.metadata_values["Название"] = id3.get("TIT2").text[0] if id3.get("TIT2") else ""
                self.metadata_values["Исполнитель"] = id3.get("TPE1").text[0] if id3.get("TPE1") else ""
                self.metadata_values["Альбом"] = id3.get("TALB").text[0] if id3.get("TALB") else ""
                self.metadata_values["Трек"] = id3.get("TRCK").text[0] if id3.get("TRCK") else ""
                self.metadata_values["Год"] = id3.get("TYER").text[0] if id3.get("TYER") else ""
                self.metadata_values["Комментарий"] = id3.get("COMM:").text[0] if id3.get("COMM:") else ""
                self.ValueChangeMetadataLineEdit.setText(
                self.metadata_values[self.FieldChangeMetadataComboBox.currentText()])
            except pydub.exceptions.CouldntDecodeError:
                font.setPointSize(8)
                self.FileChoseChangeMetadataButton.setFont(font)
                self.file_loaded = False
                self.FieldChangeMetadataComboBox.hide()
                self.ValueChangeMetadataLineEdit.hide()
                self.FileChoseChangeMetadataButton.setText("ОШИБКА ЧТЕНИЯ ФАЙЛА")
            except IndexError:
                font.setPointSize(8)
                self.FileChoseChangeMetadataButton.setFont(font)
                self.file_loaded = False
                self.FieldChangeMetadataComboBox.hide()
                self.ValueChangeMetadataLineEdit.hide()
                self.FileChoseChangeMetadataButton.setText("ОШИБКА ЧТЕНИЯ ФАЙЛА")
        else:
            self.file_name = self.FileChoseChangeMetadataButton.text()

    def image_path_change(self):
        if self.file_loaded:
            self.image_path = \
            QFileDialog.getOpenFileName(self, 'Выберите изображение', '',
                                        'Все файлы (*);;Картинка (*.jpg);;Картинка (*.png);;Картинка (*.jpeg)')[0]
            if self.image_path != '':
                self.WarningImageChangeMetadataLabel.hide()
                try:
                    img = Image.open(self.image_path)
                    format = img.format.lower()
                    audio = MP3(self.FileChoseChangeMetadataButton.text(), ID3=ID3)
                    with open(self.image_path, 'rb') as f:
                        self.image_data = f.read()
                    try:
                        audio.tags.delall("APIC")
                    except KeyError:
                        pass
                    audio.tags = ID3()
                    audio.tags.add(
                        APIC(
                            encoding=3,
                            mime='image/jpeg',
                            type=3,
                            desc=u'Cover',
                            data=self.image_data
                        )
                    )
                    audio.save()
                    byte_image_data = QByteArray(self.image_data)
                    pixmap = QPixmap()
                    pixmap.loadFromData(byte_image_data, format)
                    pixmap = pixmap.scaled(141, 141, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                                           transformMode=Qt.TransformationMode.SmoothTransformation)
                    self.PixmapChangeMetadataLabel.setPixmap(pixmap)
                except PIL.UnidentifiedImageError:
                    self.WarningImageChangeMetadataLabel.setText("НЕВЕРНЫЙ ФОРМАТ ФАЙЛА")
                    self.WarningImageChangeMetadataLabel.show()
        else:
            self.WarningChangeMetadataLabel.setText("ВЫБЕРИТЕ ФАЙЛ")
            self.WarningChangeMetadataLabel.show()

    def text_changed(self):
        self.WarningChangeMetadataLabel.hide()
        index = self.FieldChangeMetadataComboBox.currentIndex()
        field_key = self.FieldChangeMetadataComboBox.itemText(index)
        new_value = self.ValueChangeMetadataLineEdit.text()
        try:
            id3 = ID3(self.FileChoseChangeMetadataButton.text())

            if field_key == "Название":
                id3.add(TIT2(encoding=3, text=new_value))
            elif field_key == "Исполнитель":
                id3.add(TPE1(encoding=3, text=new_value))
            elif field_key == "Альбом":
                id3.add(TALB(encoding=3, text=new_value))
            elif field_key == "Трек":
                id3.add(TRCK(encoding=3, text=new_value))
            elif field_key == "Год":
                id3.add(TYER(encoding=3, text=new_value))
            elif field_key == "Комментарий":
                id3.add(COMM(encoding=3, lang='eng', desc='', text=new_value))

            id3.save()
            self.metadata_values.clear()
            self.metadata_values["Название"] = id3.get("TIT2").text[0] if id3.get("TIT2") else ""
            self.metadata_values["Исполнитель"] = id3.get("TPE1").text[0] if id3.get("TPE1") else ""
            self.metadata_values["Альбом"] = id3.get("TALB").text[0] if id3.get("TALB") else ""
            self.metadata_values["Трек"] = id3.get("TRCK").text[0] if id3.get("TRCK") else ""
            self.metadata_values["Год"] = id3.get("TYER").text[0] if id3.get("TYER") else ""
            self.metadata_values["Комментарий"] = id3.get("COMM:").text[0] if id3.get("COMM:") else ""
        except Exception:
            self.WarningChangeMetadataLabel.setText("ОШИБКА")
            self.WarningChangeMetadataLabel.show()

    def index_changed(self):
        print(self.metadata_values.values())
        self.ValueChangeMetadataLineEdit.setText(self.metadata_values[self.FieldChangeMetadataComboBox.currentText()])