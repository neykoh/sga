from django.db import models

# Create your models here.
class Alumno(models.Model):
	TIPO_IDENTIFICACION = (('P', 'Pasaporte'),('C','Cedula de Identidad'))
	Tipo_Identificación = models.CharField(max_length=1, choices=TIPO_IDENTIFICACION, default='C')
	C_I = models.CharField(max_length=10, primary_key=True)
	Apellido_Paterno = models.CharField(max_length=35)
	Apellido_Materno = models.CharField(max_length=35)
	Primer_Nombre = models.CharField(max_length=35)
	Segundo_Nombre = models.CharField(max_length=35)
	Fecha_Nacimiento = models.DateField()
	Edad = models.CharField(max_length=10)
	SEXO = (('F', 'Femenino'),('M', 'Masculino'))
	Sexo = models.CharField(max_length=1, choices=SEXO, default='M')
	Tipo_Sangre = models.CharField(max_length=10)
	Lugar_Nacimiento = models.CharField(max_length=10)
	Lugar_Residencia = models.CharField(max_length=10)
	Instrucción = models.CharField(max_length=10)
	Dirección = models.TextField()
	Teléfono = models.CharField(max_length=10)
	Email = models.EmailField()
	Tipo_Licencia = models.CharField(max_length=10)
	Dirección = models.CharField(max_length=10)
	Direccion = models.CharField(max_length=10)
	Direccion = models.CharField(max_length=10)

	def NombreCompleto(self):
		cadena="{0} {1}, {2}"
		return cadena.format(self.Apellido_Paterno, self.Apellido_Materno, self.Primer_Nombre, self.Segundo_Nombre)

	def __str__(self):
		return self.NombreCompleto()

class Curso(models.Model):
	Nombre: models.CharField(max_length=35)
	Estado: models.BooleanField(default=True)

	def __str__(self):
		return "{1} ".format(self.Nombre)

class Matricula(models.Model):
	Alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
	Curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
	Fecha_Matricula = models.DateField(auto_now_add=True)

	def __str__(self):
		cadena = "{0} => {1}"
		return cadena.format(self.Alumno, self.Curso.Nombre)