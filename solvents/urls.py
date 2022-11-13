
from django.urls import path
from . import views
app_name = 'solvents'

urlpatterns =[
    path('',views.solvents,name='solvents'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('add/',views.add,name='add'),
    path('search/',views.solventssearch,name='search'),
]