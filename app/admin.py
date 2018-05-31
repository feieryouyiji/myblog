from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)