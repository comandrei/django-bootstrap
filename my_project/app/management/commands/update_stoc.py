from django.core.management.base import BaseCommand, CommandError, CommandParser
from app.models import Produs

class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('stoc', type=int)
        parser.add_argument('--test', type=bool, default=False)
        return super().add_arguments(parser)
    
    def handle(self, *args, **options):
        from pprint import pprint
        pprint(options)
        print("In comanda")
        modified = Produs.objects.all().update(stoc=options['stoc'])
        print(f"Am actualizate {modified} produse")