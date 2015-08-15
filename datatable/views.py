from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def home(request):
	title = 'TEST -DT1'
	content = """

	<pre>

	TEST DE CONTENU

	</pre>
	"""
	return render(request, 'datatable/dt1.html', {'content':content, 'title':title})

def data(request):
	my_data = {}
	my_data['draw'] = 1
	my_data['recordsTotal'] = 3
	my_data['recordsFiltered'] = 3
	data = []
	for x in range(1,200):
		data.append( [ x, "John Doe", "%s route de lagnieu" % (100+x) ] )
	my_data['data'] = data

	return JsonResponse(my_data)
