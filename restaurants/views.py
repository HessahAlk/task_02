from django.shortcuts import render

# Create your views here.
def hello_function(request):
	context = { "msg": "Hello World!"}
	return render(request, 'Hello.html', context)