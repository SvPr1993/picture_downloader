import requests
from django.shortcuts import render


def getImage():
    while True:
        url = input("Введите ссылку на картинку: ")
        dirName = input("Введите название картинки: ") + ".jpg"
        img = requests.get(url)
        with open(dirName, "wb") as imgFile:
            imgFile.write(img.content)
            imgFile.close()
        if input("Выход q") == "q" or "Q":
            break


#getImage()

#создать переменную link, которая выводит ссылку из формы index.html
#скачать ссылку и сохранить с картинки на компьютер
#создать код который будет сохранять ссылку и саму картинку в models, orm запрос
def base_page(request):
    return render(request, "index.html")
