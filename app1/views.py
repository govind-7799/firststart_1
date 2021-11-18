from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import FormCreateForm, FormChoiceMaker
from .models import TempModel


class Home(TemplateView):
    template_name = 'home.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = FormCreateForm
        return context

    def post(self, request):
        request.session['name'] = self.request.POST.get('title')
        return HttpResponseRedirect('/formmaker')


class FormMake(TemplateView):
    template_name = 'formcreate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['name'] = FormChoiceMaker
        context['data'] = TempModel.objects.all()
        return context

    def post(self,request):
        data = TempModel(question=self.request.POST.get('question'), type=self.request.POST.get('type'),
                         options=self.request.POST.get('options'))
        data.save()
        return HttpResponseRedirect("/formmaker")

def navbar(request):
    return render(request,'navbar.html')


def navbar1(request):
    return render(request,'nav12.html')

def navbar2(request):
    return render(request,'nav21.html')


