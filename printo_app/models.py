from __future__ import unicode_literals

from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import time, random,hashlib
from django.template.defaultfilters import slugify
 
class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(Course, self).save()
    def __str__(self):
        return self.name


class UserProfile(models.Model):
    USER_TYPE_CHOICES = ((1,'owner'),(2,'employee'),(3,'Private person'),)
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to='documents', null=True, blank=True)
    userType = models.IntegerField(choices=USER_TYPE_CHOICES)
    mobile = models.CharField(max_length=14, blank=True)
    def __str__(self):
        return self.user.username

class Organization(models.Model):
    owner = models.ForeignKey(User, related_name='org_owner')
    employee = models.ManyToManyField(User, related_name='org_employee' ,blank=True)
    docCount = models.IntegerField(default=0)
    is_email_verified = models.BooleanField(default=False)
    time_email_verified = models.DateTimeField(editable= False, null=True)
    is_sms_verified = models.BooleanField(default=False)
    time_email_verified = models.DateTimeField(editable= False, null=True)
    is_person_verified = models.BooleanField(default=False)
    time_person_verified = models.DateTimeField(editable= False, null=True)
    def __str__(self):
        return self.owner.username

class Service(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(Service, self).save()
    def __str__(self):
        return self.name

class Shop(models.Model):
    employee =  models.OneToOneField(User,related_name='shop_employee')
    owner = models.ForeignKey(Organization,related_name='shop_owner')
    address = models.TextField(blank=True, default="")
    pincode = models.IntegerField(null=True, blank=True)
    shopName = models.CharField(max_length=100)
    telephone = models.CharField(max_length=14, blank=True)
    email = models.EmailField(null=True,blank=True)
    createdOn = models.DateTimeField(auto_now_add=True,null=True)
    rate = models.DecimalField(max_digits=4,decimal_places=2,default=0.0)
    services = models.ManyToManyField(Service, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=7, null=True)
    latitude =models.DecimalField(max_digits=11, decimal_places=7, null=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.shopName
class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField( unique=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=7, null=True)
    latitude =models.DecimalField(max_digits=11, decimal_places=7, null=True)
   
    def __str__(self):
        return self.name
	

class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(Author, self).save()
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(Publisher, self).save()
    def __str__(self):
        return self.name
	
class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(Tag, self).save()
    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    def save(self):
        if not self.id:
           self.slug = slugify(self.name)
        super(Topic, self).save()
    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    code = models.CharField(max_length=4)
    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(University, self).save()

    def __str__(self):
        return self.name

class College(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    university = models.ForeignKey(University, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=7, null=True)
    latitude =models.DecimalField(max_digits=11, decimal_places=7, null=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(College, self).save()
    def __str__(self):
        return self.name


    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course)
    def __str__(self):
        return self.name


class DocType(models.Model):
    docType = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    def save(self):
        if not self.id:
            self.slug = slugify(self.docType)
        super(DocType, self).save()
    def __str__(self):
        return self.docType


def upload():
    return hashlib.sha256(str(time.time())).hexdigest() +"/"


class Document(models.Model):
    uuid = models.CharField(max_length=60, unique=True, blank=True)
    organization = models.ForeignKey('Organization',related_name='doc_owner', null=True, blank=True)
    # shop = models.ForeignKey(Shop)
    private_user = models.ForeignKey(User, blank=True, null =True)
    name = models.CharField(max_length=200)
    # doc = models .FileField(upload_to = upload())
    doc_type = models.ForeignKey(DocType)
    pageNoRange = models.CharField(max_length=100,null=True,blank=True)
    display_doc = models.FileField(upload_to="display_docs", blank =True)
    tags = models.ManyToManyField(Tag, blank=True) #used for searching docs. ee: tkm,parvathy,ECE,motor working,sem5
    topic = models.ManyToManyField(Topic, blank=True) 
    display = models.BooleanField(default=True) #for delete purposes
    is_public = models.BooleanField(default=False)
    is_user_private = models.BooleanField(default=False)
    pages = models.IntegerField() #should be auto filled
    price = models.DecimalField(max_digits=6,decimal_places=2) #should be auto filled
    uploadedDate = models.DateTimeField(auto_now_add=True,null=True) 
    updatedDate = models.DateTimeField(default=timezone.now,editable=False)
    course = models.ManyToManyField(Course, blank =True)
    edition = models.IntegerField(null =True, blank = True)
    author_names = models.TextField(null =True, blank = True)
    publisher = models.ForeignKey(Publisher, null =True, blank=True)
    university = models.ManyToManyField(University, blank =True)

    def __str__(self):
	    return self.name

class Order(models.Model):
    PRINT_TYPE_CHOICES = ((1,'one-side'),(2,'two-side'))
    # uuid(below)
    orderNo = models.CharField(max_length=60, unique=True, blank=True)
    customer = models.CharField(max_length=20)
    shop = models.ForeignKey(Shop)
    orderDate = models.DateTimeField(auto_now_add=True,null=True)
    qty = models.IntegerField(default=1)
    price = models.IntegerField()
    document = models.ManyToManyField(Document)
    printType = models.IntegerField(choices=PRINT_TYPE_CHOICES,default=1)
    is_new = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    is_printed = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)









	
