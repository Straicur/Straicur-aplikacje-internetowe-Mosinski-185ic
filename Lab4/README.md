
# Laboratorium 4 REST API z DRF
<p><a href = "https://github.com/wsvincent/restapiswithdjango">Repozytorium poglądowe </a></p>
<br>
DRF jest naprawdę przyjemny po lekkim zgłębieniu . W miare przejrzysta dokumentacja , Redoc-Dokumentacja Moich API , bardzo mało kodu w porównaniu do czystego diango 

<h1>DRF api\v1</h1>

Post list dla nie zalogowanych . W kórym nie wyświetlają się żadne posty ponieważ zostasły ustawione opcje dostępu DEFAULT_PERMISSION_CLASSES ('rest_framework.permissions.IsAuthenticated') 

![list](DRF/static/Scr/1.PNG "Start")

Logowanie 

![list](DRF/static/Scr/2.PNG "Start")

Post list po zalogowaniu 

![list](DRF/static/Scr/3.PNG "Start")

Post detail 

![list](DRF/static/Scr/4.PNG "Start")

Jakie kolwiek akcje na poście może tylko wykonywać autor .

<h1>DRF api\v2</h1>
Model Ksiazka z danymi (author  title created_at updated_at) i serializer z fields = ('id', 'author', 'title',)
<br>
Filty : (filter_backends = [filters.SearchFilter ,filters.OrderingFilter])
<br>
Lista Ksiazek 

![list](DRF/static/Scr/5.PNG "Start")

Lista Ksiazek bez zalogowania 

![list](DRF/static/Scr/6.PNG "Start")

Wyszukiwanie i filtry 

![list](DRF/static/Scr/7.PNG "Start")

Filtr Id ASC

![list](DRF/static/Scr/8.PNG "Start")

Filtr Id DESC

![list](DRF/static/Scr/9.PNG "Start")

Przed wyszukiwaniem 

![list](DRF/static/Scr/10.PNG "Start")

Wyszukane posty 

![list](DRF/static/Scr/11.PNG "Start")

<h1>Swagger</h1>
Jak widać są tu dwie aplikacje v1 i v2 .

![list](DRF/static/Scr/12.PNG "Start")

<h1>Redoc (Dokumentacja Moich API)</h1>

![list](DRF/static/Scr/13.PNG "Start")






