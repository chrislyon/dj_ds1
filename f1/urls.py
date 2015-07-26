from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'dj_doctest.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	#url(r'^$', 'f1.views.home', name='home'),
	url(r'^name$', 'f1.views.get_name', name='get_name'),
	url(r'^thanks$', 'f1.views.thanks', name='thanks'),
)

