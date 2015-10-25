from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load new songs from available sources'

    def handle(self, *args, **options):
        print("Gettings playlists")
