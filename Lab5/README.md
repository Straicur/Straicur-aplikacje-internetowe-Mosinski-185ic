# Laboratorium 5 Web Scraping
<br>
<h1>Na potrzeby Laboratorium stworzyłem nową aplikację . </h1>
<h1>Oczywiście przed dodaniem elementów pobrałem  Beautifulsoup4 oraz lxml . </h1>
<h1>Dla każdej z podstrony dodałem widoki</h1>
# Przykłady z zajęć
Do wyświetlenia przykładów z laboratorium wystarczyło do funkcji return przekazać render z dobrze ustawionym słownikiem oraz requestem . 

![list](/Lab5/Scr/1.PNG "Start")

![list](/Lab5/Scr/8.PNG "Start")

![list](/Lab5/Scr/2.PNG "Start")

![list](/Lab5/Scr/3.PNG "Start")

![list](/Lab5/Scr/7.PNG "Start")

# Formularz do Web Scrapingu
<h1>Do stworzenia formularza wykorzystałem gotowy szablon bootstrapa</h1>
<h1>Jako przykład wykorzystałem moje reame z Lab 4 i wyszukałem element "h1"</h1>
Po wypełnieniu formularza działającym linkiem i elementen kórego szukamy funkcja z wie czego ma szukać.
Po pobraniu wskazanego elementu poszukiwane są w nim tagi :
<ul>
  <li>span</li>
  <li>id</li>
  <li>class</li>
  <li>alt</li>
  <li>href</li>
  <li>text(jest to tekst z danego tagu)</li>
</ul>
<h1>Przed wyszukaniem</h1>
![list](/Lab5/Scr/5.PNG "Start")

<h1>Po wyszukaniu.Zostało odnalezione 7 elementów.</h1>
![list](/Lab5/Scr/4.PNG "Start")

# Szuaknie elemntów ze strony przy pomocy xml i XPath
<h1>Na tej podstronie wykorzystałem obie metody :</h1>
<h1>- pobranie elementu za pomocą klasy </h1>
<h1>- pobranie elementu za pomocą ścieżki xpath</h1>

![list](/Lab5/Scr/6.PNG "Start")

<h1>Element pobrany przy pomocy XPath</h1>
Szukanie odbywa się za pomocą xPath czyli ścieżki w drzewie projektu .

![list](/Lab5/Scr/10.PNG "Start")

<h1>Element pobrany przy pomocy Klasy</h1>
Szukanie odbywa się za pomocą nazwy klasy w której znajduje się nasz szukany obiekt.

![list](/Lab5/Scr/9.PNG "Start")
