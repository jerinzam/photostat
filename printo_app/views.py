from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Document, Organization, UserProfile, Shop
#from .forms import DocUploadForm, ShopEditForm
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django import forms
from models import *

class DocUploadForm(ModelForm):
    class Meta:
	model = Document
	fields =("name","doc_type","pageNoRange",)

@login_required
def indexEmp(request):
    context = {'shop':shopid}
    return render(request,'index.html',context)
@login_required
def docUpload(request):
    if(request.method=='POST'):
	user = UserProfile.objects.get(user=request.user)
	if(user.userType == 1 ):
	    org = Organization.objects.get(owner = request.user)
	elif(user.userType == 2):
	    org = Organization.objects.get(employee = request.user)
	    
	    data = DocUploadForm(request.POST,request.FILES)

	    new_doc = data.save(commit=False)
	    new_doc.organization = org
	    new_doc.is_public = True
	    new_doc.save()
	    data.save_m2m() 
	    return HttpResponseRedirect(reverse('documentList'))
	else:
	    form = DocUploadForm()
	    context = { "docUploadForm" : form }
	    return render(request,'printo_app/docUpload.html',context)
@login_required
def docList(request):
    user = UserProfile.objects.get(user=request.user)
    if(user.userType == 1  ):
	org = Organization.objects.get(owner = request.user)
    elif(user.userType == 2):
	org = Organization.objects.get(employee = request.user)
    docList = Document.objects.filter(is_public=True).filter(organization=org)
    context = {"docs":docList}
    return render(request,'printo_app/docList.html',context)
@login_required
def docDetail(request,docid):
    docDetail = Document.objects.get(id=docid)
    form = DocUploadForm(instance = docDetail)
    context = {"docEditForm":form,"doc":docDetail}
    return render(request,'printo_app/docDetail.html',context)
@login_required
def docEditSave(request,docid):
    currentDoc = Document.objects.get(id=docid)
    docDetail = DocUploadForm(request.POST,request.FILES,instance=currentDoc)
    docDetail.save()	
    context = { "msg":docDetail }
    return HttpResponseRedirect(reverse('documentList'))
@login_required
def shopProfile(request,shopid=None):
    context = {}
    user = UserProfile.objects.get(user=request.user)
    if(user.userType == 1):
	pass
    elif(user.userType == 2):
	shop = Shop.objects.get(employee=request.user)
	shopForm = ShopEditForm(instance=shop)
	context = {'shopForm':shopForm}
	return render(request,'printo_app/shopProfile.html',context)
@login_required
def shopEditSave(request):
    shop = Shop.objects.get(employee=request.user)
    shopForm = ShopEditForm(request.POST,instance=shop)
    shopForm.save()
    return HttpResponseRedirect(reverse('shopProfile'))

@login_required
def indexEmp(request,shopid=None):
    user = UserProfile.objects.get(user=request.user)
    is_owner = False
    if(user.userType == 1):
	is_owner = True
    elif(user.userType == 2):
	is_owner = False
	context = {'is_owner':is_owner}
    return HttpResponseRedirect(reverse('ordersList'))
@login_required
def ordersList(request,shopid=None):
    context = {}
    return render(request,'printo_app/ordersList.html',context)
@login_required
def shopList(request):
    org = Organization.objects.get(owner = request.user)
    shops = Shop.objects.filter(owner = org )
    context={'shops' : shops}
    return render(request,'printo_app/shopList.html',context)


class ShopForm(forms.Form):
    shopName = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'mandatory', 'placeholder': 'Email'}),
                             label=_(u'email address'), required=False)
    

    
    address = forms.CharField(widget= forms.Textarea())
    pincode = forms.CharField(max_length=6, widget=forms.PasswordInput(attrs={'class': 'mandatory', 'placeholder': 'pincode'}),
    required=False)
    
	
    nearest_college = forms.CharField(max_length=200, required=False)
    
    nearest_town = forms.CharField(max_length=200, required=False)
		       
    mobile = forms.CharField(max_length=14)
    
    longitude = forms.DecimalField(max_digits=11, decimal_places=7)
    latitude = forms.DecimalField(max_digits=11, decimal_places=7)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'mandatory', 'placeholder': 'User Name'}),
                                label=_(u'Username'))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'mandatory', 'placeholder': 'Password'}, render_value=False),
                                label=_(u'Password'))
 			
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'mandatory', 'placeholder': ' Password Again'}, render_value=False),
                                label=_(u'Password Again'))
    services = forms.ModelMultipleChoiceField(queryset=Service.objects.all())
    
    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
       
        """
        if 'password1' in self.cleaned_data and 'password' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password']:
                raise forms.ValidationError(_(u'You must type the same password each time'))
        return self.cleaned_data    


    def clean_username(self):
	if 'email' in self.cleaned_data:
	    
	    try:
		user = User.objects.get(username= self.cleaned_data["username"])
		raise forms.ValidationError(_(u'Already this Username is Registered'))
	
	    except User.DoesNotExist:
		
		pass
	return self.cleaned_data["email"]
@login_required
def shopCreate(request):
    
    

    
    uprofile =get_object_or_404(UserProfile, user=request.user)
    if uprofile.userType==1:
	pass
    else:
	return HttpResponse("You don't have permission")
	
    if(request.method=='POST'):
	form = ShopCreateForm(request.POST)
		
	if(userform.is_valid):
	    username = form.cleaned_data.get("username", None)
	    password = form.cleaned_data.get("password", None)
	    mobile = form.cleaned_data.get("mobile", None)
	    email = form.cleaned_data.get("email", None)
	    if email == None:
		email = request.user.email
	    if username != None:
		user = User.objects.create_user(username,email, password)
		
		userprofile = UserProfile()
		userprofile.user = user
		userprofile.userType = 2
		if mobile !=None:
		    userprofile.mobile = mobile 
		userprofile.save()
		
	    shop = Shop()
	    shop.organization
	    shopprofile = shopform.save(commit=False)
	    shopprofile.employee = user
	    shopprofile.owner = Organization.objects.get(owner = request.user)
	    shopprofile.save()
	    shopform.save_m2m()

	    return HttpResponseRedirect(reverse('shopList'))
	else:
	    userform = UserForm(prefix='user')
	    shopform = ShopCreateForm(initial={'owner': Organization.objects.get(owner = request.user)},prefix='shopProfile')
	    context = { 'shopCreateForm' : shopform, 'userForm' : userform }
	return render(request,'printo_app/shopCreate.html',context)

@login_required
def index(request):
    user = UserProfile.objects.get(user=request.user)
    if(user.userType == 1):
	return HttpResponseRedirect(reverse('OwnerMain'))
    elif(user.userType == 2):
	return HttpResponseRedirect(reverse('EmployeeMain'))
    return None



class RegistrationForm(forms.Form):
    
    
    
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'mandatory', 'placeholder': 'Email'}),
                             label=_(u'email address'))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'mandatory', 'placeholder': 'Password'}, render_value=False),
                                label=_(u'Password'))
				
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'mandatory', 'placeholder': ' Password Again'}, render_value=False),
                                label=_(u'Password Again'))
		       
    mobile = forms.CharField(max_length=14)
    
    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
       
        """
        if 'password1' in self.cleaned_data and 'password' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password']:
                raise forms.ValidationError(_(u'You must type the same password each time'))
        return self.cleaned_data    


    def clean_email(self):
	if 'email' in self.cleaned_data:
	    
	    try:
		user = User.objects.get(username= self.cleaned_data["email"])
		raise forms.ValidationError(_(u'Already Email Address is registered'))
	
	    except User.DoesNotExist:
		
		pass
	return self.cleaned_data["email"]

def index_main(request):
    if request.user.is_authenticated()==True:
	return HttpResponseRedirect(reverse("main"))
    else:
	if request.method=="POST":
	    form= RegistrationForm(request.POST)
	    if form.is_valid():
		u = User.objects.create_user(form.cleaned_data["email"],  form.cleaned_data["email"], form.cleaned_data["password"],)
		# Send a mail with verification code
		profile = UserProfile()
		profile.user =u
		profile.userType =1
		profile.mobile = form.cleaned_data["mobile"]
		profile.save()
		
		org= Organization()
		org.owner = u
		org.save()
		return HttpResponse("Thanks") 
	else:
	    form =RegistrationForm()
	return render( request,  'index_main.html', context={"form":form},)

    
def docListOwner(request):
    pass
def docUploadOwner(request):
    pass
@login_required
def indexOwner(request):
    context = {}
    return render(request,'ownerMain.html',context)

import json

def get_colleges(request):
    p={}
    for c in College.objects.all():
	p[c.name] =(str(c.latitude), str(c.longitude))
    return HttpResponse(json.dumps(p), content_type="application/json")
def get_cities(request):
    p={}
    for c in City.objects.all():
	p[c.name] =(str(c.latitude), str(c.longitude))
    return HttpResponse(json.dumps(p), content_type="application/json")
