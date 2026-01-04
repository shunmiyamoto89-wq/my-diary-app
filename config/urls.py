from django.contrib import admin
from django.urls import path, include, re_path # re_path を追加
from django.conf import settings
from django.views.static import serve # serve を追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]

# 本番環境（DEBUG=False）でも画像を無理やり表示させる設定
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]