import json

from app.comments.comment import Comment


class CommentDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """Загружаем данные из json файла
        и создаем список объектов класса Comment"""
        with open(self.path + '../../data/comments.json', encoding='utf-8') as file:
            comments_data = json.load(file)
            comments = []

            for comment in comments_data:
                comments.append(
                    Comment(comment['post_id'],
                            comment['commenter_name'],
                            comment['comment'],
                            comment['pk'])
                )

        return comments

    def get_all_by_post_id(self, post_id):
        """Получаем все комментарии
        для конкретного поста по его ID"""
        comments = self.load_data()

        post_comments = [comment for comment in comments if comment.post_id == post_id]

        return post_comments
