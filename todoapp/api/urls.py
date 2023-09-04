from django.urls import path
from . import views

urlpatterns = [
    path('TareaList', views.TareaList.as_view()),
    path('TareaList/<int:tarea_id>', views.TareaList.as_view()),
    path('TareaCreate', views.TareaCreate.as_view()),
    path('TareaCreate/<int:tarea_id>', views.TareaCreate.as_view()),
    path('TareaUpdate', views.TareaUpdate.as_view()),
    path('TareaUpdate/<int:tarea_id>', views.TareaUpdate.as_view()),
    path('TareaDelete', views.TareaDelete.as_view()),
    path('TareaDelete/<int:tarea_id>', views.TareaDelete.as_view())

]