from django.urls import path
from . import views
app_name = 'inorganic'
urlpatterns =[
    path('',views.inorganic,name='inorganic'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('add/',views.add,name='add'),
    path('search/',views.inorganicsearch,name='search'),

]