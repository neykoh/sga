from django.contrib import admin
from apps.inscripcion.models import Alumno, Curso, Matricula
# Register your models here.
admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Matricula)