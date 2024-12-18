from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (TodolistViewSet, CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView, TagViewSet,
                    CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView)

app_name = 'tasks'

router = DefaultRouter()
router.register(r'tasks', TodolistViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
                  path('comments/', CommentListCreateAPIView.as_view()),
                  path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view()),
                  path('category/', CategoryListCreateAPIView.as_view()),
                  path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view()),

              ] + router.urls
