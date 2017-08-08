from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


# Create your views here.
def Index(request):
	return render(request, 'account/account.html', context={ 'name': 'Felipe' });
