from django.db.models      import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http           import HttpResponse
from django.shortcuts      import render
from web.models            import Post


def index(request):
    context = {     'title': 'Index',
                    'description': 'Django and PHP web developer',
              }
    return render(request, 'index.html', context) 

def hello(request):
    return HttpResponse("Buenas! Bienvenido al apartado hello!") 

def blog(request):
    queryset_list = Post.objects.order_by('-pub_date')

    #Search query
    search_query = request.GET.get("q")
    if search_query:
        queryset_list = queryset_list.filter(
                Q(headline__icontains = search_query) |
                Q(text__icontains     = search_query)
                ).distinct()

    #paginator
    paginator = Paginator(queryset_list, 10)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {     'title': 'Blog',
                    'description': 'Django and PHP blog',
                    'blog': queryset,
              }
    return render(request, 'blog.html', context) 

def post(request):
    return HttpResponse("Buenas! Bienvenido al apartado post !") 

def projects(request):
    return HttpResponse("Buenas! Bienvenido al apartado projects !") 

def aboutme(request):
    return HttpResponse("Buenas! Bienvenido al apartado aboutme !") 
