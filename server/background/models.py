from django.db import models


class Notice(models.Model):
    notice_title = models.TextField(default='', unique=True)
    notice_author = models.IntegerField(default='')
    notice_date = models.DateTimeField(default='')
    notice_receiver = models.IntegerField()
    notice_content = models.TextField(default='')

    def to_dict(self):
        return {
            "notice_title": self.notice_title,
            "notice_author": self.notice_author,
            "notice_date": self.notice_date,
            "notice_receiver": self.notice_receiver,
            "notice_content": self.notice_content
        }