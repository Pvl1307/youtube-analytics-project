from googleapiclient.discovery import build
import os


class Video:
    def __init__(self, video_id):
        api_key: str = os.getenv('YT_API_KEY')

        youtube = build('youtube', 'v3', developerKey=api_key)

        self.__video_id = video_id

        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id).execute()

        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        self.comment_count: int = video_response['items'][0]['statistics']['commentCount']
        self.video_url: str = f'https://youtu.be/{self.__video_id}'

    def __str__(self):
        return f'{self.video_title}'


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
