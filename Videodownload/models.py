from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User;

# Create your models here.

class contact(models.Model):
	Email=models.CharField(max_length=30,null=False,blank=False);
	Name=models.CharField(max_length=25,null=False,blank=False);
	Message=models.TextField(max_length=500,null=False,blank=False)

	def __str__(self):
		return (self.Email);

class ads(models.Model):
	User=models.OneToOneField(User,on_delete=models.CASCADE)
	Ads1=models.TextField(max_length=500,null=True,blank=False);
	Ads2=models.TextField(max_length=500,null=True,blank=False);
	Ads3=models.TextField(max_length=500,null=True,blank=False);
	Ads4=models.TextField(max_length=500,null=True,blank=False);
	Ads5=models.TextField(max_length=500,null=True,blank=False);
	Ads6=models.TextField(max_length=500,null=True,blank=False);
	Ads7=models.TextField(max_length=500,null=True,blank=False);
	Ads8=models.TextField(max_length=500,null=True,blank=False);
	
	def __str__(self):
		return (self.User.username)




