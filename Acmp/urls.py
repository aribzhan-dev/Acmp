from django.urls import path
from django.contrib import admin
from main.views import indexHandler, index1Handler

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', indexHandler, name='index'),
    path('index/<int:index_id>/', index1Handler, name='index1'),  # ✅ To‘g‘ri URL ni qo‘shish
]
