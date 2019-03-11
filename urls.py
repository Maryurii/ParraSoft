from django.conf.urls import url

from django.conf import settings

from home import views



app_name = "home_app"

urlpatterns = [
	url(r'^index/$', views.index, name="index"),
	url(r'^activities/$', views.activity_view, name="activities"),
	url(r'^positions/$', views.position_view, name="positions"),
	url(r'^performance/$', views.performance_view, name="performance"),
	url(r'^personal/$', views.personal_view, name="personal"),
	url(r'^status/$', views.status_view, name="status"),
	url(r'^jobs/$', views.jobs_view, name="jobs"),

	url(r'^registeractivity/$', views.registeractivity_view, name="registeractivity"),
	url(r'^registerposition/$', views.registerposition_view, name="registerposition"),
	url(r'^registerperformance/$', views.registerperformance_view, name='registerperformance'),
	url(r'^registerpersonal/$', views.registerpersonal_view, name="registerpersonal"),
	url(r'^registerstatus/$', views.registerstatus_view, name="registerstatus"),





	]