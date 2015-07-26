from django.shortcuts import render

# Create your views here.

def home(request):
	title = 'TITRE - TEST'
	content = """

	<pre>

	TEST DE CONTENU

	<a href="/gdoc/gnr_doc"> Page de Generation </a>

	</pre>
	"""
	return render(request, 'tst1/tmpl1.html', {'content':content, 'title':title})

