import requests
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from app_downloader.forms import UrlsForm
from app_downloader.models import ImageHistory


# def getImage():
#    while True:
#        url = input("Введите ссылку на картинку: ")
#        dirName = input("Введите название картинки: ") + ".jpg"
#        img = requests.get(url)
#        with open(dirName, "wb") as imgFile:
#            imgFile.write(img.content)
#            imgFile.close()
#        if input("Выход q") == "q" or "Q":
#            break


# getImage()

#Докомпозировать задачу, а именно разбить ее на маленькие шаги
#1 этап, нам нужно скачать файл по ссылке
#2 этап, подготовить базу для сохранения в базу данный
#3 этап, сохранение файла в базу
#Вставлять вместо image.jpg реальное имя
#API endpoint, который возвращает имя и hello используя только django
def base_page(request):
    imagehistory = ImageHistory.objects.all()
    link = request.POST.get("img_url")
    if request.method == 'POST':
        response = requests.get(link)
        img_history = ImageHistory()
        img_history.sourse_link = request.POST.get("img_url")
        img_history.image.save("image2.jpg", ContentFile(response.content), save=True)
        #img_history.save()
    print(link)
    return render(request, "index.html", {'imagehistory': imagehistory})

