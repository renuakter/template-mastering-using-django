from django.urls import path
from  authentication_app.views import basepage
urlpatterns = [
    path('', basepage, name='basepage'),
    
]
