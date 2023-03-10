from django.conf import settings
from django.db import models
class LanguagePhrase(models.Model):
    'Generated Model'
    language = models.TextField()
    phrase = models.TextField()
