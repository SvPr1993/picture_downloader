from django.forms import ModelForm
from app_downloader.models import ImageHistory


class UrlsForm(ModelForm):
    class Meta:
        model = ImageHistory
        fields = ('sourse_link', 'image')
