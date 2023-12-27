# importing path to power URL pattern
from django.urls import path
from .views import home_page_view

# three parts to the url pattern
# empty string
# reference to the view called home_page_view
# an optional named URL pattern called "home"
urlpatterns = [path("", home_page_view, name="home")]