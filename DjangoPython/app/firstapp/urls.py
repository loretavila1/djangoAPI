from django.urls import path

from . import views

urlpatterns = [
    path('',views.vista,name='vista'),
    path('cotizador',views.vista2,name='vista2'),
    path('cellphones', views.cellphones, name='cellphones'),
    path('cellphones/add', views.cellphonesAdd, name='cellphonesAdd'),
    path('cellphones/delete', views.cellphoneDelete, name='cellphoneDelete'),
    path('cellphones/get', views.cellphonesGet, name='cellphonesGet'),
    path('cellphones/get/<int:phoneid>', views.cellphonesGetId, name='cellphonesGetId'),
    path('cellphones/update/<int:phoneid>', views.cellphonesUpdate, name='cellphonesUpdate'),
    path('companies', views.companies, name='companies')
]
