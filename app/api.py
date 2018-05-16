# myapp/api.py
from tastypie.resources import ModelResource
from app.models import Book
from tastypie.authorization import Authorization

class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'
        authorization = Authorization()