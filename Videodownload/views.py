from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
import subprocess
from .contactform import contactdata
from django.http import HttpResponse
import re 
from django.contrib.auth import authenticate, login
import json
from .models import ads
import requests as rq;
 

def home(request):
	adsdata=ads.objects.all();
	if request.method=='POST':
		try:
			url=request.POST['url'];
			proc = subprocess.Popen([f"you-get -u --itag=18 {url}"], stdout=subprocess.PIPE, shell=True)
			(out, err) = proc.communicate()
			out=out.decode("utf-8")
			out={'urls':re.search(r"(?P<url>https?://[^\s]+)", out).group("url"),'adsdata':adsdata};
			return render(request,'Play/videodisplay.html',out)
		except :
			return HttpResponse("Url is not valid")
	return render(request,'home.html',{'adsdata':adsdata})
 
def contact(request):
	adsdata=ads.objects.all();
	if request.method=='POST':
		form=contactdata(request.POST);
		if form.is_valid():
			form.save(commit=True);
			messages.success(request, 'Message is sent')
			return redirect('/contact')
		else:
			return messages.error(request, 'Somting wrong');
		return render(request,'contact.html')
	else:
		form=contactdata();
		return render(request,'contact.html',{'form':form,'adsdata':adsdata})

def pinterestlink(request):
	adsdata=ads.objects.all();
	if request.method=='POST':
		try:
			url=request.POST['pinterestlink'];
			api=f'http://keepsaveit.com/api/?api_key=7jpp3bb3CbFaYpvlwY1TEdzJrIs6Z3qions9lfsO6VADh&url={url}'
			data=rq.get(api);
			links=data.json();
			link=links['response']['links'][0]['url']
			out={'urls':link,'adsdata':adsdata}
			return render(request,'Play/pinvideodisplay.html',out)
		except :
			return HttpResponse("Url is not valid")
	return render(request,'pinterestvideo.html',{'adsdata':adsdata});



def Instagram(request):
	adsdata=ads.objects.all();
	if request.method=='POST':
		try:
			url=request.POST['Instagramurl'];
			api=f'http://keepsaveit.com/api/?api_key=7jpp3bb3CbFaYpvlwY1TEdzJrIs6Z3qions9lfsO6VADh&url={url}'
			data=rq.get(api);
			links=data.json();
			link=links['response']['links'][0]['url']
			out={'urls':link,'adsdata':adsdata}
			return render(request,'Play/Instagramplay.html',out)
		except :
			return HttpResponse("Url is not valid")
	return render(request,'Instagram.html',{'adsdata':adsdata});
 
 

def videodisplay(request):
	return render(request,'Play/pinvideodisplay.html')


def Instagramplay(request):
	return render(request,'Play/Instagramplay.html')


def videodisplayPin(request):
	return render(request,'Play/videodisplay.html')

