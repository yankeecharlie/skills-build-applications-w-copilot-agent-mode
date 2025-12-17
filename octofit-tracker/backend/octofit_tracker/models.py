from djongo import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField()
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        db_table = 'activities'
    def __str__(self):
        return f"{self.user} - {self.activity}"

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
    def __str__(self):
        return f"{self.user}: {self.points}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    suggested_for = models.JSONField()
    class Meta:
        db_table = 'workouts'
    def __str__(self):
        return self.name
