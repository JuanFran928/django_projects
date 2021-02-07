import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, States, Region, Iso, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python
    for row in reader:
        print(row)
        # Se ajusta antes de insertar los datos
        try:
            y = int(row[3])
        except:
            y = None

        try:
            lo = float(row[4])
        except:
            lo = None
        try:
            la = float(row[5])
        except:
            la = None
        try:
            he = float(row[6])
        except:
            he = None

        ca, created = Category.objects.get_or_create(name=row[7])
        st, created = States.objects.get_or_create(name=row[8])
        re, created = Region.objects.get_or_create(name=row[9])
        ix, created = Iso.objects.get_or_create(name=row[10])

        s = Site.objects.get_or_create(name=row[0], description=row[1], justification=row[2],
            year=y, longitude=lo, latitude=la, area_hectares=he, category=ca, states=st , region=re, iso=ix)

         #s.save()