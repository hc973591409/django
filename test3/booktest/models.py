from django.db import models

# Create your models here. 如果已经由存在的数据库，可以不用迁移数据库
# +----------+-------------+------+-----+---------+----------------+
# | Field    | Type        | Null | Key | Default | Extra          |
# +----------+-------------+------+-----+---------+----------------+
# | id       | int(11)     | NO   | PRI | NULL    | auto_increment |
# | title    | varchar(20) | NO   |     | NULL    |                |
# | pub_date | datetime(6) | NO   |     | NULL    |                |
# | read     | int(11)     | NO   |     | NULL    |                |
# | comment  | int(11)     | NO   |     | NULL    |                |
# | isDelete | tinyint(1)  | NO   |     | NULL    |                |
# +----------+-------------+------+-----+---------+----------------+

class Book(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    read = models.IntegerField()
    comment = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    class Meta():
        """设置元类，用于设置表明"""
        db_table = 'book'


# mysql> desc hero;
# +----------+--------------+------+-----+---------+----------------+
# | Field    | Type         | Null | Key | Default | Extra          |
# +----------+--------------+------+-----+---------+----------------+
# | id       | int(11)      | NO   | PRI | NULL    | auto_increment |
# | name     | varchar(20)  | NO   |     | NULL    |                |
# | hgender  | tinyint(1)   | NO   |     | NULL    |                |
# | isDelete | tinyint(1)   | NO   |     | NULL    |                |
# | content  | varchar(100) | NO   |     | NULL    |                |
# | hbook_id | int(11)      | NO   | MUL | NULL    |                |
# +----------+--------------+------+-----+---------+----------------+

    
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
