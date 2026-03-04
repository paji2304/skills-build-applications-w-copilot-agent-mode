from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Marvel", description="Marvel Team")
        user = User.objects.create(name="Spider-Man", email="spiderman@marvel.com", team=team, is_superhero=True)
        self.assertEqual(user.name, "Spider-Man")
        self.assertEqual(user.team.name, "Marvel")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name="DC", description="DC Team")
        user = User.objects.create(name="Batman", email="batman@dc.com", team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, activity_type="Running", duration_minutes=30, date=timezone.now().date())
        self.assertEqual(activity.user.name, "Batman")
        self.assertEqual(activity.activity_type, "Running")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Upper body strength")
        self.assertEqual(workout.name, "Pushups")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Avengers", description="Earth's Mightiest Heroes")
        leaderboard = Leaderboard.objects.create(team=team, total_points=100)
        self.assertEqual(leaderboard.team.name, "Avengers")
        self.assertEqual(leaderboard.total_points, 100)
