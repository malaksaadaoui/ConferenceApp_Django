from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView
from django.urls import reverse_lazy
from .models import Conference
def list_conference(request):
    conferenceList=Conference.objects.all()
    #retour :liste+pagehtml
    return render(request,"conferences/liste.html" , {"liste":conferenceList})
# Create your views here.
class ConferenceList(ListView):
    model=Conference
    context_object_name="liste"
    template_name="conferences/liste.html"
class ConferenceDetails(DetailView):
    model=Conference
    context_object_name="conference"
    template_name="conferences/details.html"

class ConferenceCreate(CreateView):
    model= Conference
    template_name ="conferences/form.html"
    fields = "__all__"
    success_url = reverse_lazy("liste_conferences")