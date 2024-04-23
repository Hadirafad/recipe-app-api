from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError

class Command(BaseCommand):
    """" Django command to wait for db"""
    
    def handle(self, *args, **options):
        """" command entry """
        self.stdout.write('Waiting for db...')
        db_up   =   False
        while  not db_up:
            try:
                self.check(databases=['default']) # check default database
                db_up = True
            except(Psycopg2OpError, OperationalError):
                self.stdout.write('DB unavailable, waiting 1sec...')
                time.sleep(1)
            self.stdout.write(self.style.SUCCESS('DB available!'))