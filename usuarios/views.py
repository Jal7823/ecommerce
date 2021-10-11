from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.


class LoginFromView(LoginView):
    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')

            
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio de sesion'
        return context

def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }

    if request.method =='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            user = authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login(request,user)
            return redirect(to='login')


        data ['form'] = formulario 
        messages.error(request,'algo fallo en la suscripcion')
    return render(request,'usuarios/registro.html',data)

class logout(LoginView):
    pass

def formulario(request):
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('tienda')
    else:
        form = CustomUserCreationForm()

    return render(request,'registro.html',{'form':form})


