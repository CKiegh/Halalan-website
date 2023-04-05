from pyexpat import model
from xml.etree.ElementTree import Comment
from django.db import models
# from datetime import date

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 300)
    password = models.CharField(max_length = 300)
    first_name = models.CharField(max_length = 300, default='First Name')
    last_name = models.CharField(max_length = 300, default='Last Name')
    birthday = models.DateTimeField(blank = True, null = True)
    sex = models.CharField(max_length = 300, default='')
    objects = models.Manager()

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getBirthday(self):
        return self.birthday

    def getSex(self):
        return self.sex
    
    def getPK(self):
        return self.pk 

    def __str__(self):
        return str(self.pk) + ":" + str(self.username) + ", " + str(self.first_name) + str(self.last_name) + ", " + str(self.birthday) + ", " + str(self.sex)
        
class Position(models.Model):
    # This name should be Unique
    name = models.CharField(max_length = 300)

    def getName(self):
        return self.name

    def __str__(self):
        return "Position Name: " + str(self.name)

class Candidates(models.Model):
    first_name = models.CharField(max_length = 300)
    last_name = models.CharField(max_length = 300)
    nickname = models.CharField(max_length = 300)
    slogan = models.CharField(max_length = 300)
    position_id = models.ForeignKey(Position, on_delete = models.CASCADE)

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getNickname(self):
        return self.nickname

    def getSlogan(self):
        return self.slogan

    def __str__(self):
        return str(self.pk) + ":" + str(self.position_id) + ", " + str(self.first_name) + " " + str(self.last_name) + ", " + str(self.nickname) + ", " + str(self.slogan)

class Vote(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    candidate_id = models.ForeignKey(Candidates, on_delete = models.CASCADE)
    comment = models.CharField(max_length = 1000)

    def getComment(self):
        return self.comment

    def __str__(self):
        return str(self.pk) + ": " + str(self.candidate_id) + ". " + str(self.comment)