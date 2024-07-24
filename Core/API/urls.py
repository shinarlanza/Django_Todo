from rest_framework.routers import DefaultRouter
from django.urls import path, include
from todo.api.urls import todo_router

router = DefaultRouter()

router.registry.extend(todo_router.registry)

urlpatterns = [
    path('', include(router.urls)),

]
