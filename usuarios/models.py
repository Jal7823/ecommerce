from django.db import models
from django.contrib.auth.models  import AbstractUser,BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombre,password=None):
        if not email:
            raise  ValueError('El usuario debe tener un correo electronico')
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            nombre = nombre,

        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username,email,nombre,password):
        user = self.create_user(
            email,
            username = username,
            nombre = nombre,
            password=password,
        )

        user.usuario_administrador = True
        user.staff = True
        user.save()
        return user

class Usuario(AbstractUser):
    username = models.CharField('Nombre de usuario',unique=True, max_length=100)
    email = models.EmailField('Correo electronico',unique=True, max_length=254)
    nombre = models.CharField('Nombre', max_length=200,blank=True,null=True)
    apellido = models.CharField('Apellido', max_length=200,blank=True,null=True)
    imagen = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=None,null=True,blank=True)
    usuario_activo  = models.BooleanField(default=True)
    usuario_administrador  = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    dni = models.IntegerField(verbose_name='DNI',blank=True,null=True)
    direc = models.CharField(max_length=300,verbose_name='Direccion',blank=True,null=True)
    loc = models.CharField(max_length=300,verbose_name='Localidad',blank=True,null=True)
    provincias= (
        ('C.A.B.A.','C.A.B.A.'),
        ('Buenos Aires','Buenos Aires',),
        ('Catamarca','Catamarca'),
        ('Chaco','Chaco'),
        ('Chubut','Chubut'),
        ('Córdoba','Córdoba'),
        ('Corrientes','Corrientes'),
        ('Entre Ríos','Entre Ríos'),
        ('Formosa','Formosa'),
        ('Jujuy','Jujuy'),
        ('La Pampa','La Pampa'),
        ('La Rioja','La Rioja'),
        ('Mendoza','Mendoza'),
        ('Misiones','Misiones'),
        ('Neuquén','Neuquén'),
        ('Río Negro','Río Negro'),
        ('Salta','Salta'),
        ('San Juan','San Juan'),
        ('Santa Cruz','Santa Cruz'),
        ('Santa Fe','Santa Fe'),
        ('Santiago del Estero','Santiago del Estero'),
        ('Tierra del Fuego','Tierra del Fuego'),
        ('Tucumán','Tucumán'),
    )
    pcia = models.CharField(max_length=300,choices=provincias, verbose_name='Provincia',blank=True,null=True)
    tlf = models.IntegerField(verbose_name='Telefono',blank=True,null=True)
    transp = models.CharField(max_length=300,verbose_name='Trasporte',default='N/A',blank=True,null=True)
    objects = UsuarioManager()


    USER_NAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombre']

    

    def __str__(self):
        return f'{self.nombre}  {self.apellido}'.upper()
    
    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,usuarios_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
