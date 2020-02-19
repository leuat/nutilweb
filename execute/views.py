from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from subprocess import Popen
from sys import stdout, stdin, stderr
from .forms import UploadFileForm


import time, os, signal

def executeNutil():
	command = "/home/leuat/django/nutilweb/executeNutil.sh"
	proc = Popen(command, shell=True, stdin=stdin, stdout=stdout, stderr=stderr)


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

	executeNutil()
#	return HttpResponse(ok + "<br>EXECUTING "+form.data['title']+" DONE")
	return HttpResponse(ok + "<br>EXECUTING "+file.name+" DONE")

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
