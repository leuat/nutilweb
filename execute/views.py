from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from subprocess import Popen
from sys import stdout, stdin, stderr
from .forms import UploadFileForm
import subprocess
from django.views.static import serve

import time, os, signal

def executeNutil(name):
	command = "/Users/leuat/code/nutilweb/executeNutil.sh "+name
	proc = subprocess.Popen(command, shell=True, stdin=stdin, stdout=stdout, stderr=stderr)


def handle_uploaded_file(f):
	#with open('/home/leuat/django/nutilweb/name.txt', 'wb+') as destination:
	with open('uploads/temp.zip', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

def run(request):
	form = UploadFileForm(request.POST, request.FILES)
	ok = "false"
	if len(request.FILES)==0:
		return HttpResponse("NO FILES UPLOADED");
	file = request.FILES['file'] #returns a dict-like object
	if form.is_valid():
		#instance = file#ModelWithFileField(file_field=file)
		#instance.save()
		handle_uploaded_file(file) 		
		ok = "true"


	executeNutil(form.data['title'])
#	return HttpResponse(ok + "<br>EXECUTING "+form.data['title']+" DONE")

	return render(request, 'execute.html',{'name': form.data['title']})


#	return HttpResponse(ok + "<br>EXECUTING "+file.name + ".")

def index(request):
#	template = loader.get_template('submitform.html')
	context = {
#		'latest_question_list': latest_question_list,
	}
	#return HttpResponse(template.render(context, request))'
	form = UploadFileForm()
	return render(request, 'submitform.html', {'form': form})
#    return HttpResponse("Select file to execute")
# Create your views here.
import os 

def results(request):
    path="results/"  # insert the path to your directory   
    img_list =os.listdir(path)   
    return render(request, 'results.html', {'images': img_list})

def download(request, filename):
	filepath = "results/"+filename

#	fl = open(fl_path+filename, "rb")

	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
#	return HttpResponse(fl,content_type='application/force-download')
#	return HttpResponse(fl,content_type='application/force-download')
#	mime_type, _ = mimetypes.guess_type(fl_path)
#	response = HttpResponse(fl, content_type=mime_type)
#	response["Content-Disposition"] = "attachment; filename=%s" % filename
#	return response