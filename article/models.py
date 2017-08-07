from django.db import models
from django.contrib.auth.models import User
from block.models import Block
from django.utils import timezone
# Create your models here.


class Article(models.Model):
    block = models.ForeignKey(Block, verbose_name=u"所属版块")
    owner = models.ForeignKey(User, verbose_name=u"作者")
    title = models.CharField("标题", max_length=100)
    content = models.CharField("内容", max_length=10000)
    status = models.IntegerField("状态", choices=((0, u"普通"), (-1, u"删除"), (10, u"精华")), default=0)
    create_timestamp = models.DateTimeField(default=timezone.now())
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"
