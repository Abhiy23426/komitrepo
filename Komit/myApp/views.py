from django.shortcuts import render
from django.core.paginator import Paginator
from myApp.models import Roka,Prewedding,Shadi
# Create your views here.
def komit_view(request):
	return render(request,'myApp/komit.html')

def roka_view(request):
	post_list=Roka.objects.all()
	paginator=Paginator(post_list,7)
	page_number=request.GET.get('page')
	try:
		post_list=paginator.page(page_number)
	except:
		post_list=paginator.page(1)
	d={'post_list':post_list}
	return render(request,'myApp/roka_list.html',d)

def prewedding_view(request):
	return render(request,'myApp/prewedding_list.html')

def shadi_view(request):
	return render(request,'myApp/shadi_list.html')