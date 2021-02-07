from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls', namespace='hello')),
    path('accounts/', include('django.contrib.auth.urls')),  # Add
    path('autos/', include('autos.urls')),                   # Add
    path('cats/', include('cats.urls')),
    #('account/', include('account.urls', namespace='account')),
    #path('home/', include('home.urls')),
]
