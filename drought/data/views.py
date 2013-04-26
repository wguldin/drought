from drought.data.models import Drought
from django.shortcuts import render_to_response# Create your views here.

def index(request):
	all_dates = Drought.objects.all()

	return render_to_response('index.html', {'drought': all_dates})