from django.conf.urls import include,url

from django.conf.urls import url
from . import views


urlpatterns = [
	
	url(r'^$',views.index,name="main"),
	url(r'^shop$',views.indexEmp,name="EmployeeMain"),
	url(r'^dashboard$',views.indexOwner,name="OwnerMain"),
	url(r'^doc-list$',views.docList,name="documentListOwner"),
	url(r'^doc-list$',views.docList,name="documentListEmp"),
	url(r'^doc-detail/(?P<docid>\d+)/$',views.docDetail,name="documentDetail"),
	url(r'^doc-edit/(?P<docid>\d+)/$',views.docEditSave,name="documentEdit"),
	url(r'^doc-upload-owner$',views.docUpload,name="documentUploadOwner"),
	url(r'^doc-upload$',views.docUpload,name="documentUploadEmp"),
	url(r'^shop-profile$',views.shopProfile,name="shopProfile"),
	url(r'^shop-profile-save$',views.shopEditSave,name="shopEditSave"),
	url(r'^shop-profile/$',views.shopProfile,name="shopProfile"),
	url(r'^shop-list/$',views.shopList,name="shopList"),
	url(r'^shop-list/shop/(?P<shopid>\d+)/$',views.indexEmp,name="shopPage"),
	url(r'^shop-create/$',views.shopCreate,name="shopCreate"),
	url(r'^order-list/$',views.ordersList,name="ordersList"),

	# data providers
	
	url(r'^get_universitys/$',views.get_universitys,name="get_universitys"),
	url(r'^get_publishers/$',views.get_publishers,name="get_publishers"),
	url(r'^get_courses/$',views.get_courses,name="get_courses"),
	url(r'^get_topics/$',views.get_topics,name="get_topics"),
	url(r'^get_tags/$',views.get_tags,name="get_tags"),
	url(r'^get_services/$',views.get_services,name="get_services"),
    url(r'^get_colleges/$',views.get_colleges,name="get_colleges"),
    url(r'^get_cities/$',views.get_cities,name="get_cities"),

	]
