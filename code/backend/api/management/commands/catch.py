from django.core.management.base import BaseCommand
from utils.decorators import log_decorator
import time

import logging
logger = logging.getLogger("catchup")

class Command(BaseCommand):
    help = 'Display the number of blog articles'

    @log_decorator()
    def handle(self, *args, **options):
        for i in range(1,100):
            # time.sleep(0.1)
            if i%2 == 1:
                print(f"catch {i}")

