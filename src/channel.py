import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')

    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        items = channel.get('items', [])

        snippet = items[0].get('snippet', {})
        statistics = items[0].get('statistics')

        self.title = snippet.get('title')
        self.description = snippet.get('description')
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscribe_count = statistics.get('subscriberCount')
        self.video_count = statistics.get('videoCount')
        self.view_count = statistics.get('viewCount')


    @property
    def channel_id(self):
        return self.__channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        channel_json = json.dumps(channel, indent=2, ensure_ascii=False)
        print(channel_json)

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=cls.api_key)


    def to_json(self, filename):
        """Сохраняет значения атрибутов экземпляра Channel в файл в формате JSON"""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.__dict__, file, ensure_ascii=False)
