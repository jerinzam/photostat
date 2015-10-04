from django.conf.urls import include,url

from django.conf.urls import url
from . import views


urlpatterns = [
	
	url(r'^$',views.index,name="main"),
	url(r'^shop$',views.indexEmp,name="EmployeeMain"),
	url(r'^dashboard$',views.indexOwner,name="OwnerMain"),
	url(r'^doc-list-owner$',views.docListOwner,name="documentListOwner"),
	url(r'^doc-list$',views.docList,name="documentList"),
	url(r'^doc-detail/(?P<docid>\d+)/$',views.docDetail,name="documentDetail"),
	url(r'^doc-edit/(?P<docid>\d+)/$',views.docEditSave,name="documentEdit"),
	url(r'^doc-upload-owner$',views.docUploadOwner,name="documentUploadOwner"),
	url(r'^doc-upload$',views.docUpload,name="documentUpload"),
	url(r'^shop-profile$',views.shopProfile,name="shopProfile"),
	url(r'^shop-profile-save$',views.shopEditSave,name="shopEditSave"),
	url(r'^shop-profile/$',views.shopProfile,name="shopProfile"),
	url(r'^shop-list/$',views.shopList,name="shopList"),
	url(r'^shop-list/shop/(?P<shopid>\d+)/$',views.indexEmp,name="shopPage"),
	url(r'^shop-create/$',views.shopCreate,name="shopCreate"),
	url(r'^order-list/$',views.ordersList,name="ordersList"),
	]
