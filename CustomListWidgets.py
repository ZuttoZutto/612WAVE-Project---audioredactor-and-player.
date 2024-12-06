from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QListWidget, QMenu
from PyQt6.QtCore import Qt


class PlaylistsCustomListWidget(QListWidget):
    def __init__(self, main_window_link, **kwargs):
        self.Parent = main_window_link
        super().__init__(**kwargs)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.RightButton:
            # Получаем индекс элемента под курсором
            index = self.indexAt(event.pos())

            if not index.isValid():  # Если клик был вне элемента
                return

            # Получаем соответствующий элемент списка
            item = self.itemFromIndex(index)

            # Создаем контекстное меню
            context_menu = QMenu()

            # Добавляем действия в меню
            action_delete = context_menu.addAction("Удалить")

            # Показываем контекстное меню
            action = context_menu.exec(QCursor.pos())

            # Обрабатываем выбранные действия
            if action == action_delete:
                self.takeItem(self.row(item))
                self.Parent.db_cursor.execute("""DELETE FROM Playlists WHERE Name == ?""", (item.text(),))
                self.Parent.db_cursor.execute(f"""DROP TABLE IF EXISTS {item.text()}""")
                self.Parent.db_connect.commit()
        else:
            super().mousePressEvent(event)


class SongsCustomListWidget(QListWidget):
    def __init__(self, main_window_link, **kwargs):
        self.Parent = main_window_link
        super().__init__(**kwargs)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.RightButton:
            # Получаем индекс элемента под курсором
            index = self.indexAt(event.pos())

            if not index.isValid():  # Если клик был вне элемента
                return

            # Получаем соответствующий элемент списка
            item = self.itemFromIndex(index)

            # Создаем контекстное меню
            context_menu = QMenu()

            # Добавляем действия в меню
            action_delete = context_menu.addAction("Удалить")

            # Показываем контекстное меню
            action = context_menu.exec(QCursor.pos())

            # Обрабатываем выбранные действия
            if action == action_delete:
                self.takeItem(self.row(item))
                self.Parent.db_cursor.execute(f"""DELETE FROM {self.Parent.SongsLabel.text()} WHERE Song_id == (SELECT Id FROM Songs WHERE Path LIKE '%{item.text()}')""")
                self.Parent.db_connect.commit()
        else:
            super().mousePressEvent(event)