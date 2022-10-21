from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Alumno
import json
# Create your views here.
 
class AlumnoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args , **kwargs):
        return super().dispatch(request, *args, **kwargs)
 
    def get(self, request, id=0):
        if (id>0):
            alumnos=list(Alumno.objects.filter(id=id).values())
            if len(alumnos)>0:
                alumno=alumnos[0]
                datos = {'message': "Success", 'Alumno': alumno}
            else:
                datos = {'message': "Alumno no existe..."}
            return JsonResponse(datos)
        else:
            alumnos=list(Alumno.objects.values())
            if len(alumnos)>0:
                datos={'message':"Success",'Alumnos':alumnos}
            else:
                datos={'message':"Alumno no existe..."}
            return JsonResponse(datos)
 
    def post(self, request):
        jd = json.loads(request.body)
        Alumno.objects.create(nombre=jd['nombre'], apellido=jd['apellido']
        , cI=jd['cI'], fecha_nacimiento=jd['fecha_nacimiento'], edad=jd['edad'])
        datos ={'message':"Success"}
        return JsonResponse(datos)
 
    def put(self, request, id):
        jd = json.loads(request.body)
        alumnos=list(Alumno.objects.filter(id=id).values())
        if len(alumnos)>0:
            alumno=Alumno.objects.get(id=id)
            alumno.nombre=jd['nombre']
            alumno.apellido=jd['apellido']
            alumno.cI=jd['cI']
            alumno.fecha_nacimiento=jd['fecha_nacimiento']
            alumno.edad=jd['edad']
            alumno.save()
            datos ={'message':"Success"}
        else:
            datos = {'message': "Alumno no existe..."}
        return JsonResponse(datos)
 
    def delete(self, request, id):
        alumnos=list(Alumno.objects.filter(id=id).values())
        if len(alumnos) > 0:
            Alumno.objects.filter(id=id).delete()
            datos ={'message':"Success"}
        else:
            datos = {'message': "Alumno no existe..."}
        return JsonResponse(datos)