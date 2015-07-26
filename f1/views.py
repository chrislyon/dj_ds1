from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import f1_form

# Create your views here.

def home_contents(request):
	title = 'TEST FORMULAIRE'
	content = """

	<pre>

	TEST DE CONTENU

	<a href="/gdoc/gnr_doc"> Page de Generation </a>

	</pre>
	"""
	return render(request, 'tst1/tmpl1.html', {'content':content, 'title':title})

def thanks(request):
	title = 'REPONSE TEST FORMULAIRE'
	content = """

	<pre>

	Ton nom est %s 
	<a href="/gdoc/gnr_doc"> Page de Generation </a>

	</pre>
	"""
	return render(request, 'f1/tmpl1.html', {'content':content, 'title':title})

def get_name(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = f1_form(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/thanks/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = f1_form()

	return render(request, 'f1/tmpl1.html', {'form': form})
