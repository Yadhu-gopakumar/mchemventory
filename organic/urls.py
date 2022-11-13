
from django.urls import path
from . import views
app_name = 'organic'

urlpatterns =[
    path('',views.home,name='home'),
    path('organic/',views.organic,name='organic'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('add/',views.add,name='add'),
    # path('search/',views.orgsearchView.as_view(),name='search'),
    path('search/',views.organicsearch,name='search'),
]