from django.contrib import admin
from .models import HeaderModel, MiddleModel,FooterModel

admin.site.register(HeaderModel)
admin.site.register(MiddleModel)
admin.site.register(FooterModel)