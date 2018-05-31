# myapp/api.py
from tastypie.resources import ModelResource
from app.models import Book, Tag, Category, Article
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.constants import ALL_WITH_RELATIONS, ALL
from tastypie.paginator import Paginator


"""

Resource ---> ModelBaseResource -->  ModelResource(空的对象)
--> get method
all cycl  start --> url 
    1. wrap_view() provides basic error handling & allows for returning serialized errors ==== django-tastypie/tastypie/api.py //处理url
    2. dispatch() ensure `allowed_methods` `the class has a method that can handle the request` `the user is authenticated`     // 处理meta中的验证

    3. hydrate(post)
    4  hydrate_field(post)
    5. obj_get_list (get)       //Resource(null) - ModelBaseResource(override)
    6. build_filters(get)      //对 meta 中 客户端 filtering  的一些情况进行后台filters
    7. get_object_list(get post)    // 必须在

    8. apply_sorting(get)       // 获取qs 进行sort

    9. dehydrate_field(get)
    10. dehydrate(get)           // 返回脱水返回数据，　每一个 obj 都会被脱水
"""


class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'

        authorization = Authorization()  # 认证
        paginator_class = Paginator


    def obj_get_list(self, bundle, **kwargs):
        print('I am obj_get_list')
        return super(BookResource, self).obj_get_list(bundle, **kwargs)

    def alter_deserialized_list_data(self, request, data):
        """
        A hook to alter list data just after it has been received from the user &
        gets deserialized.

        Useful for altering the user data before any hydration is applied.
        """
        print('I am alter_deserialized_list_data', data)
        return data

    def build_filters(self, filters=None, ignore_bad_filters=False): # 此方法是可以在后台对 filtering 中的字段进行一些补充
        filters = super(BookResource, self).build_filters(filters)
        print('I am build filters')
        return filters

    def get_object_list(self, request):
        print('I am get_object_list')
        res = super(BookResource, self).get_object_list(request)
        print('get_object_list res', res)
        return res

    def apply_sorting(self, obj_list, options=None):
        print('I am apply_sorting', obj_list)
        return super(BookResource, self).apply_sorting(obj_list)

    def apply_filters(self, request, applicable_filters):
        print('I am apply_filters', applicable_filters)
        return super(BookResource, self).apply_filters(request, applicable_filters)

    def hydrate(self, bundle, **kwargs):
        print('I am hydrate', bundle)
        return bundle

    def hydrate_book_name(self, bundle):
        print('I am hydrate_book_name', bundle)
        bundle.data['book_name'] = bundle.data['book_name'].lower()
        return bundle
    
    def dehydrate_book_name(self, bundle):  # 对某model中某一个字段进行处理
        print('dehydrate_book_name')
        return bundle.data['book_name'].upper()

    def dehydrate(self, bundle, **kwargs):
        print('I am dehydrate', bundle)
        return super(BookResource, self).dehydrate(bundle)

class TagResource(ModelResource):
    
    class Meta:

        queryset = Tag.objects.all()
        resource_name = 'tag'
        authorization = Authorization()  # 认证

        paginator_class = Paginator

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        authorization = Authorization()  # 认证

        paginator_class = Paginator

class ArticleResource(ModelResource):
    category = fields.ForeignKey(
        CategoryResource, 'category')

    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        authorization = Authorization()  # 认证
        paginator_class = Paginator

        # fields = ['author', 'category', 'is_publish']  # 从数据库中取出的字段

        filtering = { # 接收从客户端过滤的字段
            'is_publish': ALL,
        }



    def obj_get_list(self, bundle, **kwargs):
        print('I am obj_get_list')
        return super(ArticleResource, self).obj_get_list(bundle, **kwargs)

    def alter_deserialized_list_data(self, request, data):
        """
        A hook to alter list data just after it has been received from the user &
        gets deserialized.

        Useful for altering the user data before any hydration is applied.
        """
        print('I am alter_deserialized_list_data', data)
        return data


    def build_filters(self, filters=None, ignore_bad_filters=False): # 此方法是可以在后台对 filtering 中的字段进行一些补充
        filters = super(ArticleResource, self).build_filters(filters)
        print('I am build filters')
        return filters

    def get_object_list(self, request):
        print('I am get_object_list')
        res = super(ArticleResource, self).get_object_list(request)
        print('get_object_list res', res)
        return res

    def apply_sorting(self, obj_list, options=None):
        print('I am apply_sorting', obj_list)
        return super(ArticleResource, self).apply_sorting(obj_list)

    def apply_filters(self, request, applicable_filters):
        print('I am apply_filters', applicable_filters)
        return super(ArticleResource, self).apply_filters(request, applicable_filters)

    def hydrate(self, bundle, **kwargs):
        print('I am hydrate', bundle)
        return bundle

    def hydrate_author(self, bundle):
        print('I am hydrate_author', bundle)
        bundle.data['author'] = bundle.data['author'].lower()
        return bundle
    
    def dehydrate_author(self, bundle):  # 对某model中某一个字段进行处理
        print('嘤嘤怪')
        return bundle.data['author'].upper()

    def dehydrate(self, bundle, **kwargs):
        print('I am dehydrate', bundle)
        return super(ArticleResource, self).dehydrate(bundle)

    