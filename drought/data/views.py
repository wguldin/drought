from drought.data.models import Drought
from django.shortcuts import render_to_response# Create your views here.

def index(request):
	droughts = Drought.objects.all()

	return render_to_response('index.html', {'drought': droughts})