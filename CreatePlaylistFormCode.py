import sqlite3
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QWidget, QFileDialog, QListWidgetItem
from PyQt6.QtCore import Qt

from CreatePlaylistFormDesign import CreatePlaylistDesign

class CreatePlaylistForm(QWidget, CreatePlaylistDesign):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.Parent = parent

    def initUI(self):
        self.setFixedSize(326, 357)

        self.create_playlist_file_name = 'default_playlist_image.jpg'
        self.CreatePlaylistCreateButton.pressed.connect(self.create_new_playlist)
        self.CreatePlaylistChooseFileButton.pressed.connect(self.create_new_playlist_choose_file)

        self.WarningPlaylistNameLabel.hide()

    def create_new_playlist(self):
        if self.CreatePlaylistNameLineEdit.text() != "":
            if len(set(""" !"№;%:?*()-=+/\,.@#$^&""") & set(self.CreatePlaylistNameLineEdit.text())) == 0:
                if not self.CreatePlaylistNameLineEdit.text() == "Songs" and not self.CreatePlaylistNameLineEdit.text() == "Playlists":
                    try:
                        self.Parent.db_cursor.execute("""INSERT INTO Playlists(ImagePath, Name) VALUES (?, ?)""", (self.create_playlist_file_name, self.CreatePlaylistNameLineEdit.text()))
                        self.Parent.db_connect.commit()
                        self.hide()
                        playlist_item = QListWidgetItem()
                        playlist_item.setText(self.CreatePlaylistNameLineEdit.text())
                        playlist_item.setIcon(QIcon(self.create_playlist_file_name))
                        self.Parent.PlaylistsListWidget.insertItem(0, playlist_item)
                        self.Parent.db_cursor.execute(f"""CREATE TABLE {self.CreatePlaylistNameLineEdit.text()} (Song_id REFERENCES Songs (Id) NOT NULL);""")
                    except sqlite3.IntegrityError:
                        self.WarningPlaylistNameLabel.setText("ПЛЕЙЛИСТ С ТАКИМ НАЗВАНИЕМ УЖЕ СУЩЕСТВУЕТ")
                        self.WarningPlaylistNameLabel.show()
                else:
                    self.WarningPlaylistNameLabel.setText("НАЗВАНИЯ 'Songs' И 'Playlists' - НЕДОПУСТИМЫ")
                    self.WarningPlaylistNameLabel.show()
            else:
                self.WarningPlaylistNameLabel.setText("""ВЫ МОЖЕТЕ ИСПОЬЗОВАТЬ В НАЗВАНИИ ТОЛЬКО БУКВЫ И "_" """)
                self.WarningPlaylistNameLabel.show()

    def create_new_playlist_choose_file(self):
        self.create_playlist_file_name = QFileDialog.getOpenFileName(self, 'Выберите изображение для обложки плейлиста', '', 'Все файлы (*);;Картинка (*.jpg);;Картинка (*.png);;Картинка (*.jpeg)')[0]
        self.CreatePlaylistImagePixmap = QPixmap(self.create_playlist_file_name)
        self.CreatePlaylistImagePixmap = self.CreatePlaylistImagePixmap.scaled(131, 131,
                                                                               aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                                                                               transformMode=Qt.TransformationMode.SmoothTransformation)
        self.CreatePlaylistImageLabel.setPixmap(self.CreatePlaylistImagePixmap)
        if self.create_playlist_file_name == "":
            self.CreatePlaylistImageLabel.setText("Сдесь появится\n изображение\n для обложки")
            self.create_playlist_file_name = "default_playlist_image"
            self.CreatePlaylistPathLabel.setText("Сдесь появится путь к файлу с изображением")
        else:
            self.CreatePlaylistPathLabel.setText(self.create_playlist_file_name)