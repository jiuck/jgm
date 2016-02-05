from django.db.models      import Q
from django.core.mail      import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http           import HttpResponse, HttpResponseRedirect
from django.shortcuts      import render, get_object_or_404
from web.forms             import HelloForm
from web.models            import Post


def index(request):
    context = {'title': 'Index',
               'description': 'Django and PHP web developer',
              }
    return render(request, 'index.html', context) 

def hello(request):
    form = HelloForm()
    if request.method == 'POST': 
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('email', '')
        if subject and message and from_email:
            #We should be able to send the email here.
            #try:
            #    send_mail(subject, message, from_email, ['jiuck.grecords@gmail.com'])
            #except BadHeaderError:
            #    return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/jgm/thank-you/')
        form = HelloForm({'subject':subject, 
                    'message':message, 
                    'email':from_email
                    }) 
    #First time and resend your data if wrong
    context = { 'title': 'Say Hello!',
                'description': 'Django and PHP contact page',
                'form': form,
              }
    return render(request, 'hello.html', context) 

def thankYou(request):
    context = {'title': 'Thank you',
               'description': 'Django and PHP web developer',
              }
    return render(request, 'thank-you.html', context) 

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

def post(request, title):
    queryset = get_object_or_404(Post, id=title)
    return HttpResponse("Buenas! Bienvenido al apartado post !") 

def projects(request):
    return HttpResponse("Buenas! Bienvenido al apartado projects !") 

def aboutme(request):
    return HttpResponse("Buenas! Bienvenido al apartado aboutme !") 
