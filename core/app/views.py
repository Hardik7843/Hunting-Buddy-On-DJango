from django.shortcuts import render , HttpResponse
import spacy
import re
from collections import defaultdict
import pandas as pd
from .process import examine
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def show(request):
    if request.method == 'POST':
        data = request.POST
        job = data.get('job_desc')
        output = examine(job)  
        keywords = dict(output)
        
        return render(request , 'show.html', {'keywords':keywords}) 
    
    return render(request , 'show.html')



def index(request):
    return render(request, 'index.html', context = {'age': "500" , 'age': "40" , 'age': "81"})