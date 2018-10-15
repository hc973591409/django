from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    read = models.IntegerField()
    comment = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    class Meta():
        """设置元类，用于设置表明"""
        db_table = 'book'


class Hero(models.Model):
    name = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    content = models.CharField(max_length=100)
    hbook = models.ForeignKey('Book')

    def show_gender(self):
        if self.hgender:
            return '男'
        else:
            return '女'

    class Meta():
        db_table = 'hero'


class Areas(models.Model):
    atitle = models.CharField(max_length=20)
    p = models.ForeignKey('self', null=True, blank=True)