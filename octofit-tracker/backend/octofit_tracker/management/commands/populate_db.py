from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

# Sample data for superheroes, teams, activities, leaderboard, and workouts
data = {
    "users": [
        {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
        {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
        {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
        {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
        {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
        {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
    ],
    "teams": [
        {"name": "Marvel", "members": ["Iron Man", "Captain America", "Black Widow"]},
        {"name": "DC", "members": ["Superman", "Batman", "Wonder Woman"]},
    ],
    "activities": [
        {"user": "Superman", "activity": "Flight", "duration": 60},
        {"user": "Batman", "activity": "Martial Arts", "duration": 45},
        {"user": "Iron Man", "activity": "Engineering", "duration": 30},
    ],
    "leaderboard": [
        {"user": "Superman", "points": 100},
        {"user": "Iron Man", "points": 90},
        {"user": "Batman", "points": 80},
    ],
    "workouts": [
        {"name": "Strength Training", "suggested_for": ["Superman", "Wonder Woman"]},
        {"name": "Agility Drills", "suggested_for": ["Batman", "Black Widow"]},
    ],
}

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop collections if they exist
        for collection in data.keys():
            db[collection].delete_many({})

        # Insert data
        for collection, docs in data.items():
            db[collection].insert_many(docs)

        # Create unique index on email for users
        db['users'].create_index([('email', 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
