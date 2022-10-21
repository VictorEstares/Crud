from django.urls import path
from .views import AlumnoView
 
urlpatterns=[
    path('Alumnos/', AlumnoView.as_view(), name='companies_list'),
    path('Alumnos/<int:id>', AlumnoView.as_view(), name='Alumnos_process')
]
