from django.shortcuts import redirect, render
from  django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import *
from rest_framework.views import APIView
from django.views.generic.edit import FormView ,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class CustomLoginView(LoginView):
    template_name='ticket/login.html'
    fields='__all__'
    redirect_authenticated=True

    def get_success_url(self):
        return reverse_lazy('index')

class RegisterPage(FormView):
    template_name='ticket/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('index')

    def form_valid(self,form):
        user=form.save()
        if user is not None :
            login(self.request.user)
        return super(RegisterPage,self).form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage,self).get(*args,**kwargs)

class IndexPage(TemplateView,LoginRequiredMixin):
    def get(self,request,**kwarges):
        ticket_data=[]
        user_info=UserProfile.objects.get(user=request.user)
        if user_info.role ==1 or user_info.role=='1':
            all_ticket=Ticket.objects.filter(user_id=user_info.id)
        else:
            all_ticket=Ticket.objects.filter(user_id=user_info.id)
            all_ticket_Op=Ticket.objects.filter(Department_name_id=user_info.department_name_id)
            for ticket in all_ticket :
                ticket_data.append({
                    'title':ticket.title,
                    'Department_name':ticket.Department_name,
                    'description':ticket.description,
                    'status':ticket.status
                })
            ticket_data_op=[]
            for ticket in all_ticket_Op :
                ticket_data_op.append({
                    'title':ticket.title,
                    'Department_name':ticket.Department_name,
                    'description':ticket.description,
                    'status':ticket.status
                })
        context={'tickets':ticket_data,'ticketsOp':ticket_data_op}
        return render(request,'ticket/index.html',context)

class CreateTicket(LoginRequiredMixin,CreateView):
    model=Ticket
    fields =['title','description','Department_name','user']
    success_url=reverse_lazy('index')

class UpdateTicket(LoginRequiredMixin,UpdateView):
    model=Ticket
    fields=['title','description','status']
    success_url=reverse_lazy('index')
    
    
