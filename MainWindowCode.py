import sqlite3
import pygame
import mutagen
from mutagen.id3 import ID3
from PyQt6.QtGui import QPixmap, QIcon
import pydub
from pydub import AudioSegment
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QListWidgetItem
from PyQt6.QtCore import Qt, QSize, QTimer

from MainWindowDesign import MainWindowDesign
from CustomListWidgets import PlaylistsCustomListWidget
from CustomListWidgets import SongsCustomListWidget
from CreatePlaylistFormCode import CreatePlaylistForm
from ConnectionFormCode import ConnectionForm
from ChangeSpeedStepFormCode import ChangeSpeedStepForm
from CutPartFormCode import CutPartForm
from ChangeMetadataFormCode import ChangeMetadataForm


class MainWindow(QMainWindow, MainWindowDesign):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        pygame.mixer.init()
        self.main_mode = "PLAYER"
        self.channel = False
        self.standby = False

        self.PlaylistsListWidget = PlaylistsCustomListWidget(main_window_link=self, parent=self.verticalLayoutWidget)
        self.PlaylistsListWidget.setObjectName("PlaylistsListWidget")
        self.scrollAreasLayout.addWidget(self.PlaylistsListWidget)

        self.SongsListWidget = SongsCustomListWidget(main_window_link=self, parent=self.verticalLayoutWidget)
        self.SongsListWidget.setObjectName("SongsListWidget")
        self.scrollAreasLayout.addWidget(self.SongsListWidget)

        self.db_connect = sqlite3.connect("612WAVE_db.db")
        self.db_cursor = self.db_connect.cursor()
        self.setFixedSize(800, 600)
        self.button_count = 0

        self.AddPlaylistButton.clicked.connect(self.add_playlist)
        self.AddSongButton.clicked.connect(self.add_song)
        self.PlaylistsListWidget.itemClicked.connect(self.playlist_item_clicked)
        self.SongsListWidget.itemClicked.connect(self.song_item_clicked)
        self.StandbyMainPlayerButton.pressed.connect(self.standby_play)
        self.MainPlayerSongSlider.valueChanged.connect(self.main_slider_time)
        self.c5ForwardMainPlayerButton.clicked.connect(self.c5_forward)
        self.c5BackwardMainPlayerButton.clicked.connect(self.c5_backward)
        self.PrecediousSongMainPlayerButton.clicked.connect(self.precedious_song)
        self.NextSongMainPlayerButton.clicked.connect(self.next_song)
        self.SwitchToRedactorButton.clicked.connect(self.SWITCH)
        self.HelpPlayerButton.clicked.connect(self.help)

        self.ConnectionButton.pressed.connect(self.open_connection_form)
        self.ChangeSpeedStepButton.pressed.connect(self.open_change_speed_form)
        self.CutPartButton.pressed.connect(self.open_cut_part_form)
        self.ChangeMetadataButton.pressed.connect(self.open_change_metadata_form)


        self.PlaylistsListWidget.setStyleSheet(""" QListView::item { height: 70px; } """)
        self.PlaylistsListWidget.setIconSize(QSize(60, 60))
        self.SongsListWidget.setStyleSheet(""" QListView::item { height: 70px; } """)
        self.SongsListWidget.setIconSize(QSize(60, 60))

        self.playlist_choosed = False
        self.readme_showed = False
        self.WarningNoPlaylistChoosedLabel.hide()
        self.WarningSongExistLabel.hide()

        self.c5ForwardMainPlayerButton.hide()
        self.c5BackwardMainPlayerButton.hide()
        self.NextSongMainPlayerButton.hide()
        self.PrecediousSongMainPlayerButton.hide()
        self.StandbyMainPlayerButton.hide()
        self.MainPlayerSongSlider.hide()
        self.MainPlayerSongTimeLabel.hide()
        self.MainPlayerSongMaxTimeLabel.hide()
        self.MainPlayerSongNameLabel.hide()
        self.PlayingSongIconLabel.hide()

        self.ConnectionButton.hide()
        self.CutPartButton.hide()
        self.RecorderButton.hide()
        self.ChangeMetadataButton.hide()
        self.ChangeFormatButton.hide()
        self.ChangeSpeedStepButton.hide()
        self.LayOwerButton.hide()
        self.CutSilenceButton.hide()

        #Отображение всех плейлистов при запуске приложения
        for start_show_playlist_item in self.db_cursor.execute("""SELECT * FROM Playlists""").fetchall()[::-1]:
            start_playlist_item = QListWidgetItem()
            start_playlist_item.setText(start_show_playlist_item[2])
            start_playlist_item.setIcon(QIcon(start_show_playlist_item[1]))
            self.PlaylistsListWidget.addItem(start_playlist_item)

    def playlist_item_clicked(self, item):
        self.SongsLabel.setText(item.text())
        self.playlist_choosed = True
        self.WarningNoPlaylistChoosedLabel.hide()
        self.SongsListWidget.clear()
        self.WarningSongExistLabel.hide()
        for start_show_song_item in self.db_cursor.execute(f"""SELECT Path FROM Songs WHERE Id IN (SELECT Song_id FROM {self.SongsLabel.text()})""").fetchall()[::-1]:
            start_song_item = QListWidgetItem()
            start_song_item.setText(start_show_song_item[0].split("/")[-1])
            try:
                test_exist_file = open(start_show_song_item[0], "rb")
                test_exist_file.close()
                try:
                    search_metadata_icon = ID3(start_show_song_item[0])
                    # Получаем обложку альбома (если есть)
                    temp_flag = False
                    for key in search_metadata_icon.keys():
                        if key.startswith("APIC:"):
                            cover_data = search_metadata_icon[key].data
                            temp_flag = True
                            break

                    temp_pixmap = QPixmap()
                    if temp_flag:
                        temp_pixmap.loadFromData(cover_data)
                        temp_icon = QIcon(temp_pixmap)
                        start_song_item.setIcon(temp_icon)
                except mutagen.id3._util.ID3NoHeaderError:
                    pass
                self.SongsListWidget.addItem(start_song_item)
            except FileNotFoundError:
                self.db_cursor.execute(
                    f"""DELETE FROM {self.SongsLabel.text()} WHERE Song_id == (SELECT Id FROM Songs WHERE Path LIKE '%{item.text()}')""")
                self.db_cursor.execute(f"""DELETE FROM Songs WHERE Path LIKE '%{item.text()}'""")

    def song_item_clicked(self, item, next=False):
        if self.standby:
            self.channel.stop()
        self.standby = False
        self.SongsListWidget.setCurrentItem(item)
        self.playing_song_index = self.SongsListWidget.currentRow()
        self.playing_file_name = self.db_cursor.execute(f"""SELECT Path FROM Songs WHERE Path LIKE '%{item.text()}'""").fetchone()[0]
        try:
            self.playing_song_pydub_obj = AudioSegment.from_file(self.playing_file_name)
            self.playing_song_duration_ms = len(self.playing_song_pydub_obj)
            self.playing_song_duration_s = self.playing_song_duration_ms // 1000 + 1
            self.c5ForwardMainPlayerButton.show()
            self.c5BackwardMainPlayerButton.show()
            self.NextSongMainPlayerButton.show()
            self.PrecediousSongMainPlayerButton.show()
            self.StandbyMainPlayerButton.show()
            self.MainPlayerSongSlider.show()
            self.MainPlayerSongTimeLabel.show()
            self.MainPlayerSongMaxTimeLabel.show()
            self.MainPlayerSongNameLabel.show()
            self.PlayingSongIconLabel.show()
            pixmap = item.icon().pixmap(81, 81)
            pixmap = pixmap.scaled(81, 81, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                                   transformMode=Qt.TransformationMode.SmoothTransformation)
            self.PlayingSongIconLabel.setPixmap(pixmap)
            self.MainPlayerSongNameLabel.setText(item.text())
            self.MainPlayerSongMaxTimeLabel.setText(str("0" * (self.playing_song_duration_s // 60 // 60 < 10)) + str(self.playing_song_duration_s // 60 // 60) + ":" + str("0" * (self.playing_song_duration_s // 60 < 10)) + str(self.playing_song_duration_s // 60) + ":" + str("0" * (self.playing_song_duration_s % 60 < 10) + str(self.playing_song_duration_s % 60)))
            self.MainPlayerSongTimeLabel.setText("00:00:00")
            self.MainPlayerSongSlider.setMinimum(0)
            self.MainPlayerSongSlider.setMaximum(self.playing_song_duration_ms)
            self.MainPlayerSongSlider.setValue(0)

            self.last_slider_pos = 0

            self.playing_song_pydub_obj.export("special_audiofile_container.mp3", format="mp3", bitrate="192k")
            sound = pygame.mixer.Sound("special_audiofile_container.mp3")
            self.channel = sound.play()
            self.channel.stop()
            self.last_slider_pos = 0

            if next:
                self.standby_play()
        except FileNotFoundError:
            self.db_cursor.execute(f"""DELETE FROM {self.SongsLabel.text()} WHERE Song_id == (SELECT Id FROM Songs WHERE Path LIKE '%{item.text()}')""")
            self.db_cursor.execute(f"""DELETE FROM Songs WHERE Path LIKE '%{item.text()}'""")
            self.SongsListWidget.takeItem(self.SongsListWidget.currentRow())

    def standby_play(self):
        if self.standby:
            self.standby = not self.standby
            self.timer.stop()
            self.channel.stop()
            self.StandbyMainPlayerButton.setText("▶")
            self.last_slider_pos = self.MainPlayerSongSlider.value()
        else:
            self.last_slider_pos = self.MainPlayerSongSlider.value()
            self.timer = QTimer()
            self.timer.start(100)
            self.MainPlayerSongSlider.setValue(self.MainPlayerSongSlider.value() + 100)
            self.timer.timeout.connect(self.move_slider_for_timer)
            self.standby = not self.standby
            self.StandbyMainPlayerButton.setText("||")
            self.playing_song_pydub_obj[self.MainPlayerSongSlider.value():].export("special_audiofile_container.mp3",
                                                                                   format="mp3", bitrate="192k")
            sound = pygame.mixer.Sound("special_audiofile_container.mp3")
            self.channel = sound.play()

    def move_slider_for_timer(self):
        if self.MainPlayerSongSlider.value() == self.MainPlayerSongSlider.maximum():
            if self.playing_song_index + 1 != self.SongsListWidget.count():
                self.song_item_clicked(self.SongsListWidget.item(self.playing_song_index + 1), next=True)
        else:
            if self.last_slider_pos + 100 == self.MainPlayerSongSlider.value():
                self.MainPlayerSongSlider.setValue(self.MainPlayerSongSlider.value() + 100)
                self.last_slider_pos += 100
            else:
                self.timer.stop()
                self.channel.stop()
                self.standby = False
                self.StandbyMainPlayerButton.setText("▶")

    def main_slider_time(self):
        pos = self.MainPlayerSongSlider.value() // 1000
        self.MainPlayerSongTimeLabel.setText(
            str("0" * (pos // 60 // 60 < 10)) + str(pos // 60 // 60) + ":" + str("0" * (pos // 60 < 10)) + str(
                pos // 60) + ":" + str("0" * (pos % 60 < 10) + str(pos % 60)))

    def c5_forward(self):
        self.channel.stop()
        if self.standby:
            self.standby_play()
            self.MainPlayerSongSlider.setValue(self.MainPlayerSongSlider.value() + 5000)
            self.standby_play()
        else:
            self.MainPlayerSongSlider.setValue(self.MainPlayerSongSlider.value() + 5000)

    def c5_backward(self):
        self.channel.stop()
        if self.standby:
            self.standby_play()
            self.MainPlayerSongSlider.setValue(self.MainPlayerSongSlider.value() - 5000)
            self.standby_play()
        else:
            self.MainPlayerSongSlider.setValue(self.MainPlayerSongSlider.value() - 5000)

    def precedious_song(self):
        if self.playing_song_index != 0:
            self.channel.stop()
            if self.standby:
                self.song_item_clicked(self.SongsListWidget.item(self.playing_song_index - 1), next=True)
            else:
                self.song_item_clicked(self.SongsListWidget.item(self.playing_song_index - 1))

    def next_song(self):
        if self.playing_song_index + 1 != self.SongsListWidget.count():
            self.channel.stop()
            if self.standby:
                self.song_item_clicked(self.SongsListWidget.item(self.playing_song_index + 1), next=True)
            else:
                self.song_item_clicked(self.SongsListWidget.item(self.playing_song_index + 1))


    def add_playlist(self):
        self.CreatePlaylistFormObject = CreatePlaylistForm(self)
        self.CreatePlaylistFormObject.show()

    def add_song(self):
        self.WarningSongExistLabel.hide()
        if self.playlist_choosed:
            add_song_path = QFileDialog.getOpenFileName(self, f'Выберите песню, которую хотите добавить в плейлист {self.SongsLabel.text()}. Поддерживаемые форматы: mp3, wav, aac, ogg(oga), flac.', '', 'Все файлы (*);;(*.mp3);;(*.wav);;(*.aac);;(*.ogg);;(*.oga);;(*.flac)')[0]
            if add_song_path != '':
                try:
                    test_audiofile = AudioSegment.from_file(add_song_path)
                    if add_song_path.split("/")[-1] not in [i[0].split("/")[-1] for i in self.db_cursor.execute(f"""SELECT Path FROM Songs WHERE Id IN (SELECT Song_id FROM {self.SongsLabel.text()})""").fetchall()]:
                        try:
                            self.db_cursor.execute("""INSERT INTO Songs(Path) VALUES (?)""", (add_song_path,))
                        except sqlite3.IntegrityError:
                            pass
                        self.db_cursor.execute(f"""INSERT INTO {self.SongsLabel.text()}(Song_id) SELECT Id FROM Songs WHERE Path == ?""", (add_song_path,))
                        self.db_connect.commit()
                        song_item = QListWidgetItem()
                        song_item.setText(add_song_path.split("/")[-1])

                        try:
                            search_metadata_icon = ID3(add_song_path)
                            # Получаем обложку альбома (если есть)
                            temp_flag = False
                            for key in search_metadata_icon.keys():
                                if key.startswith("APIC:"):
                                    cover_data = search_metadata_icon[key].data
                                    temp_flag = True
                                    break
                            temp_pixmap = QPixmap()
                            if temp_flag:
                                temp_pixmap.loadFromData(cover_data)
                                temp_icon = QIcon(temp_pixmap)
                                song_item.setIcon(temp_icon)
                        except mutagen.id3._util.ID3NoHeaderError:
                            pass
                        self.SongsListWidget.insertItem(0, song_item)
                    else:
                        self.WarningSongExistLabel.setText("ПЕСНЯ С ТАКИМ НАЗВАНИЕМ УЖЕ СУЩЕСТВУЕТ В ЭТОМ ПЛЕЙЛИСТЕ")
                        self.WarningSongExistLabel.show()
                except pydub.exceptions.CouldntDecodeError:
                    self.WarningSongExistLabel.setText("НЕКОРРЕКТНЫЙ ФОРМАТ ФАЙЛА")
                    self.WarningSongExistLabel.show()
        else:
            self.WarningNoPlaylistChoosedLabel.show()

    def closeEvent(self, event):
        self.db_connect.close()
        try:
            self.CreatePlaylistFormObject.hide()
        except AttributeError:
            pass
        try:
            self.ConnectionFormObject.hide()
        except AttributeError:
            pass
        try:
            self.ChangeSpeedStepFormObject.hide()
        except AttributeError:
            pass
        try:
            self.CutPartFormObject.hide()
        except AttributeError:
            pass
        try:
            self.ChangeMetadataFormObject.hide()
        except AttributeError:
            pass

    def SWITCH(self):
        if self.main_mode == "PLAYER":
            self.SongsListWidget.hide()
            self.PlaylistsListWidget.hide()
            self.AddSongButton.hide()
            self.AddPlaylistButton.hide()
            self.SongsLabel.hide()
            #чтобы 3 верхние кнопки не съезжали
            self.PlaylistsLabel.setText("")

            self.ConnectionButton.show()
            self.CutPartButton.show()
            self.RecorderButton.show()
            self.ChangeMetadataButton.show()
            self.ChangeFormatButton.show()
            self.ChangeSpeedStepButton.show()
            self.LayOwerButton.show()
            self.CutSilenceButton.show()

            self.SwitchToRedactorButton.setText("ПЛЕЕР")
            self.main_mode = "REDACTOR"
        else:
            self.ConnectionButton.hide()
            self.CutPartButton.hide()
            self.RecorderButton.hide()
            self.ChangeMetadataButton.hide()
            self.ChangeFormatButton.hide()
            self.ChangeSpeedStepButton.hide()
            self.LayOwerButton.hide()
            self.CutSilenceButton.hide()

            self.SongsListWidget.show()
            self.PlaylistsListWidget.show()
            self.AddSongButton.show()
            self.AddPlaylistButton.show()
            self.SongsLabel.show()
            # чтобы 3 верхние кнопки не съезжали
            self.PlaylistsLabel.setText("ВАШИ ПЛЕЙЛИСТЫ")

            self.SwitchToRedactorButton.setText("РЕДАКТОР")
            self.main_mode = "PLAYER"

    def open_connection_form(self):
        self.ConnectionFormObject = ConnectionForm()
        self.ConnectionFormObject.show()

    def open_change_speed_form(self):
        self.ChangeSpeedStepFormObject = ChangeSpeedStepForm()
        self.ChangeSpeedStepFormObject.show()

    def open_cut_part_form(self):
        self.CutPartFormObject = CutPartForm()
        self.CutPartFormObject.show()

    def open_change_metadata_form(self):
        self.ChangeMetadataFormObject = ChangeMetadataForm()
        self.ChangeMetadataFormObject.show()

    def help(self):
        if self.readme_showed:
            self.HelpPlayerButton.setText("ПОМОЩЬ")
        else:
            self.HelpPlayerButton.setText("откройте файл README.md")
        self.readme_showed = not self.readme_showed