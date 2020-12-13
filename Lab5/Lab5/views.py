from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from bs4 import BeautifulSoup
from lxml import html
import requests
import re


def home(request):
    page = requests.get("https://starwars.fandom.com/wiki/Star_Wars")
    soup = BeautifulSoup(page.content, "html.parser")
    # Przykład 1
    # Create all_p_tags as empty list
    all_p_tags = []

    # Set all_p_tags to all h1 tags of the soup
    for element in soup.select("p"):
        all_p_tags.append(element.text)

    # Create seventh_p_text and set it to 7th p element text of the page
    all_p_tagslen=len(all_p_tags)
    seventh_p_text = soup.select("p")[6].text


    # Przykład 2
    # Create top_items as empty list
    page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, "html.parser")
    top_items = []

    # Extract and store in top_items according to instructions on the left
    products = soup.select("div.thumbnail")
    for elem in products:
        title = elem.select("h4 > a.title")[0].text
        review_label = elem.select("div.ratings")[0].text
        info = {"title": title.strip(), "review": review_label.strip()}
        top_items.append(info)
    

    #Przykład 3
    # Create top_items as empty list


    image_data = []

    # Extract and store in top_items according to instructions on the left
    images = soup.select("img")
    print("Liczba obrazków =", len(images))
    for image in images:
        src = image.get("src")
        alt = image.get("alt")
        image_data.append({"src": src, "alt": alt})


    # Przykład 4
    all_products = []

    # Extract and store in top_items according to instructions on the left
    products = soup.select('div.thumbnail')
    for product in products:
        name = product.select('h4 > a')[0].text.strip()
        description = product.select('p.description')[0].text.strip()
        price = product.select('h4.price')[0].text.strip()
        reviews = product.select('div.ratings')[0].text.strip()
        image = product.select('img')[0].get('src')

        all_products.append({
            "name": name,
            "description": description,
            "price": price,
            "reviews": reviews,
            "image": image
        })  
    return render(request,'home.html',{'top_items':top_items,'all_p_tagslen':all_p_tagslen, 
        'seventh_p_text':seventh_p_text, 'image_data':image_data,'all_products':all_products})



def scraping (request):
    if request.method == "POST":
        allElements = []
        web_link = request.POST.get('web_link', None)
        element = request.POST.get('element', None)
        url = web_link
        source=requests.get(url).text
        soup = BeautifulSoup(source, "html.parser")
        items = soup.find_all(element)
        amount = len(items)    

        for i in items:
            # Szukanie klasy
            findClass = i.get('class')
            if findClass is None:
                findClass = "Brak" 
            
            # Szukanie id
            findId = i.get('id')
            findId = findId.strip() if findId is not None else "Brak"

            # Szukanie article
            findArticle = i.get('article')
            findArticle = findArticle.strip() if findArticle is not None else "Brak"

            # Szukanie atrybutu
            find_alt = i.get('alt')
            find_alt = find_alt.strip() if find_alt is not None else "Brak"

            # Szukanie tekstu
            getText = i.text
            getText = getText.strip() if getText is not None else "Brak"

            # Szukanie spanów
            findSpan = i.get('span')
            findSpan = findSpan.strip() if findSpan is not None else "Brak"

            # Szukanie linków
            findHref = i.get('href')
            findHref = findHref.strip() if findHref is not None else "Brak"

            allElements.append({"findId": findId, "findClass": findClass,"find_alt": find_alt, "findArticle": findArticle, "getText": getText, 'findHref':findHref, 'findSpan': findSpan})
        return render(request, 'lab5.html', {'allElements':allElements, 'amount': amount, 'web_link': web_link, 'element':element})
    return render(request, 'lab5.html')


def xml(request):
    # xPath
    url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'    
    path = '/html/body/div[2]/div[1]/div[1]/div[1]/div[1]/p'
    response = requests.get(url)
    source = html.fromstring(response.content)    
    tree = source.xpath(path)
    lxmlPrzyklad2 = tree[0].text_content()
    
    # klasy   
    url = 'http://zacniewski.gitlab.io/'  
    path = '//*[@class="well"]'
    response = requests.get(url)    
    source = html.fromstring(response.content)    
    tree = source.xpath(path)
    lxmlPrzyklad1 = tree[0].text_content()

    return render(request, 'xpath.html', {'lxml1': lxmlPrzyklad1,'lxml2': lxmlPrzyklad2 })
