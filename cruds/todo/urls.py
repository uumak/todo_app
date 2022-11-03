from django.urls import path
from .views import TodoAppCreateView
from .views import TodoAppListView
from .views import TodoAppDetailView
from .views import TodoAppUpdateView
from .views import TodoAppDeleteView

urlpatterns = [
    path('', TodoAppCreateView.as_view(), name= 'home'),
    path('list/', TodoAppListView.as_view()),
     path('detail/<pk>/', TodoAppDetailView.as_view()),
     path('update/<pk>/', TodoAppUpdateView.as_view()),
      path('delete/<pk>/', TodoAppDeleteView.as_view()),
]
#<pk> is primary key used for identification