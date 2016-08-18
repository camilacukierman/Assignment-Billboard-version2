from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone


class Message(models.Model):
    title_text = models.CharField(max_length=100)
    message_text = models.CharField(max_length=600)
    author_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)



    #
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


