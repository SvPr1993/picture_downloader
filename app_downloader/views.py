import requests
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.shortcuts import render

from app_downloader.forms import UrlsForm
from app_downloader.models import ImageHistory


# Реализовать все тоже самое только без форм, прописать код сохранения без forms.py
# API endpoint, который возвращает имя и hello используя только django
def base_page(request):
    imagehistory = ImageHistory.objects.all()
    link = request.POST.get("img_url")
    if request.method == 'POST':
        response = requests.get(link)
        img_history = ImageHistory()
        img_history.sourse_link = request.POST.get("img_url")
        link_clear = link.split("/")
        img_history.image.save(link_clear[-1], ContentFile(response.content), save=True)
        form = UrlsForm(request.POST, request.FILES)
        if form.is_valid():
            img_history = ImageHistory(file_field=request.FILES["image"])
            img_history.save()
            return HttpResponseRedirect("/")
        else:
            print("Ошибка")
    print(link)
    return render(request, "index.html", {'imagehistory': imagehistory})

