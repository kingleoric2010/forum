from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Block(models.Model):
    name = models.CharField("名字", max_length=30)
    desc = models.CharField("描述", max_length=150)
    manager = models.CharField("板块管理员", max_length=100)
    status = models.IntegerField("状态",
        choices=(
            (0, "正常"),
            (-1, "删除")
        )
    )
    #manager = models.ForeignKey(User, verbose_name="管理员")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "类别"
        verbose_name_plural = "很多版块"
