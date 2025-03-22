from django.urls import path
from .views import Home


app_name='core'

urlpatterns = [
    path('', Home.as_view())  #since it is class-based

]