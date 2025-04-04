from django.urls import path
from django.contrib import admin
from main.views import indexHandler, index1Handler

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexHandler, name='index'),
    path('<int:index_id>/', index1Handler, name='index1'),  # ✅ To‘g‘ri URL ni qo‘shish
]
