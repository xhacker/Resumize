from annoying.decorators import render_to
from django.views.decorators.csrf import csrf_exempt
import json


@render_to('home.html')
def home(request):
    return locals()

@render_to('resume.html')
def resume(request):
    return locals()

@csrf_exempt
@render_to('resume.html')
def submit_resume(request):
    data = json.loads(request.body)
    print data
    return locals()
