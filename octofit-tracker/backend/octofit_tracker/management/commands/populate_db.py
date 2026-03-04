from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name="Marvel", description="Marvel superheroes team")
        dc = Team.objects.create(name="DC", description="DC superheroes team")

        # Create Users
        users = [
            User(name="Spider-Man", email="spiderman@marvel.com", team=marvel, is_superhero=True),
            User(name="Iron Man", email="ironman@marvel.com", team=marvel, is_superhero=True),
            User(name="Captain America", email="cap@marvel.com", team=marvel, is_superhero=True),
            User(name="Batman", email="batman@dc.com", team=dc, is_superhero=True),
            User(name="Superman", email="superman@dc.com", team=dc, is_superhero=True),
            User(name="Wonder Woman", email="wonderwoman@dc.com", team=dc, is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Refresh users from DB to get IDs
        marvel_users = list(User.objects.filter(team=marvel))
        dc_users = list(User.objects.filter(team=dc))

        # Create Activities
        for user in marvel_users + dc_users:
            Activity.objects.create(user=user, activity_type="Running", duration_minutes=30, date=timezone.now().date())
            Activity.objects.create(user=user, activity_type="Cycling", duration_minutes=45, date=timezone.now().date())

        # Create Workouts
        workout1 = Workout.objects.create(name="Pushups", description="Upper body strength")
        workout2 = Workout.objects.create(name="Squats", description="Lower body strength")
        workout1.suggested_for.set(marvel_users)
        workout2.suggested_for.set(dc_users)

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=150)
        Leaderboard.objects.create(team=dc, total_points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
