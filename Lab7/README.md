# Lab7 Python + Redis + Django

<h1>Przykłady ze strony <a href="https://mmazurek.dev/tag/redis-i-python/?order=asc" rel="nofollow">strona</a></h1>

# Check
![list](/Lab7/SCR/1.PNG "Start")

W poniższym kodzie nawiązujemy połączenie z redisem , następnie dodajemy wartość i klucz i na koniec zostaje ona wyświetlona.

![list](/Lab7/SCR/2.PNG "Start")

Opcja append(dodaje wartość do podanego klucza) i delete(natychmiast usuwa klucz). Dzięki decode_response = true zwracamy stringa,

![list](/Lab7/SCR/3.PNG "Start")

Opcja incr i decr odpowiadają za zwiększenie wartość podanego klucza lub ją zmniejsza o określoną wartość.

![list](/Lab7/SCR/4.PNG "Start") 

![list](/Lab7/SCR/5.PNG "Start")

![list](/Lab7/SCR/6.PNG "Start")
 
![list](/Lab7/SCR/7.PNG "Start")
 
![list](/Lab7/SCR/8.PNG "Start")

# Listy 
Przy pomocy rpush dodaje elementy do tablicy a przy pomocy lrange zwracam jej elementy z podanego przedziału (od 2 do 5), jeżeli podane zostały by argumenty 0 i -1 wtedy wyświetliły by się wszystkie elementy listy.

![list](/Lab7/SCR/9.PNG "Start")

Przy pomocy opcji setex ustawiony został TTL dla klucza . Po upływie tego czasu klucz zostanie automatycznie usunięty.

![list](/Lab7/SCR/11.PNG "Start")

# Zbiory
Tworzenie zbioru i następnie jego wyświetlenie.

![list](/Lab7/SCR/12.PNG "Start")

zrange wyświetla klucze posortowane według wartości.

![list](/Lab7/SCR/13-3.PNG "Start")

![list](/Lab7/SCR/14.PNG "Start")

Hashe to mapy, słowniki lub tablice asocjacyjne. Są to struktury do przechowywania kluczy i ich wartości.

![list](/Lab7/SCR/13.PNG "Start")
# Pubsub
Tworzenie urzytkownika z kluczem "testowa_kanal_tekstowy" , po uruchomieniu go przogram oczekuje na wiadomość.

![list](/Lab7/SCR/15.PNG "Start")

# Strumienie
Tworzenie strumienia . Duża liczba przed kluczem to ilość sekund od 1 stycznia 1970r.
![list](/Lab7/SCR/16.PNG "Start")

Dodawanie elementów do strumienia .

![list](/Lab7/SCR/17.PNG "Start")
 

![list](/Lab7/SCR/18.PNG "Start")


![list](/Lab7/SCR/19.PNG "Start")

# Pipelining 
Na screanie widać 2 podejścia 1 naiwne bez pipelingu i 2 z . Jak widać 2 podejście jest dużo szybsze .
![list](/Lab7/SCR/20.PNG "Start")
 
# Lua
Przekazanie skryptu redisowi przy pomocy komendy eval. I wyświetlenie stringa.

![list](/Lab7/SCR/21.PNG "Start")
 
Przekazywanie paremetrów do skryptu.

![list](/Lab7/SCR/22.PNG "Start")

Kod zwracający tablicę 10 elementową.

![list](/Lab7/SCR/23.PNG "Start")

Wykorzystanie JSONA do  dodania 2 liczb.

![list](/Lab7/SCR/24.PNG "Start")

Dodawanie 10 i 5.Pobranie z redisa danych , praca na nich i zapis. Pierwsze zostanie zwrucone none ponieważ eval zwraca nill a key2 przechowuje wynik.

![list](/Lab7/SCR/25.PNG "Start")

Utworzenie grupy i ich uprawnień.

![list](/Lab7/SCR/26.PNG "Start")

Nasłuchiwanie zmian klucza . Najpierw ustawiona do klucza zostaje wartość 15 a potem dodana jeszcze wartość 11 .

![list](/Lab7/SCR/28.PNG "Start")

![list](/Lab7/SCR/27.PNG "Start")

# Django-Redis-Celery
Aby wszystko zadziałało na windowsie potrzebne było potrzebne parę zmian m.in: pobranie odpowiednich pakietów , cofnięcie się z wersją celery i zainstalowanie visual c++ tools. 
Wygląd strony

![list](/Lab7/SCR/30.PNG "Start")

Projekt thumbnailer:
Zmiany w pliku settings :
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'thumbnailer.apps.ThumbnailerConfig',
    'widget_tweaks',
    'django_celery_beat',
]
```

```python

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media'))
IMAGES_DIR = os.path.join(MEDIA_ROOT, 'images')

if not os.path.exists(MEDIA_ROOT) or not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)


# celery
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
```
# Skrypt tasku 
Skrypt wymagał małych poprawek. Program pobiera i kopiuje oryginalny  po czym oblicza wymiary na miniature i ustawia je , po tym zapisuje oryginał i minioatukę do folderu media/images oraz pakuje je do pliku zip.
```python
@shared_task
def make_thumbnails(file_path, thumbnails=[]):
    os.chdir(settings.IMAGES_DIR)
    path, file = os.path.split(file_path)
    file_name, ext = os.path.splitext(file)

    zip_file = f"{file_name}.zip"
    results = {'archive_path': f"{settings.MEDIA_URL}images/{zip_file}"}
    try:
        img = Image.open(file_path)
        zipper = ZipFile(zip_file, 'w')
        zipper.write(file)
        for w, h in thumbnails:
            img_copy = img.copy()
            img_copy.thumbnail((w, h))
            thumbnail_file = f'{file_name}_{w}x{h}.{ext}'
            img_copy.save(thumbnail_file)
            zipper.write(thumbnail_file)

        img.close()
        zipper.close()
    except IOError as e:
        print(e)

    return results

```
![list](/Lab7/SCR/31.PNG "Start")

Wynikiem działania programu jest zmiana obrazu na mniejszy o wymiarach 128 x 102 .

![list](/Lab7/SCR/32.PNG "Start")
![list](/Lab7/SCR/33.PNG "Start")

Pobrane obrazki przed i po modyfikacji w zippie.

![list](/Lab7/SCR/35.PNG "Start")

# Taski
Kod z pliku task
```python
@shared_task(name='notifiction')
def send_notifiction():
     print('Hello World !!!')
     # Another trick


@shared_task(name='summary') 
def send_import_summary():
    print('Hello every 30 sec')

@shared_task
def adding_task(x, y, items=[]):
    result = x + y
    if items:
        for x, y in items:
            result += (x + y)
    return result

```
Ustawienia do tasków z pliku settings
```python
from celery.schedules import crontab
CELERY_BEAT_SCHEDULE = {
'30 SEKUND': {
       'task': 'summary',
       'schedule': 30.0
    },
'Witaj o 13:21': { 
         'task': 'notifiction', 
         'schedule': crontab(hour=13, minute=21),
    },
}
```
Uruchomienie Celery + Redis
![list](/Lab7/SCR/34.PNG "Start")
![list](/Lab7/SCR/29.PNG "Start")
