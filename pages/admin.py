# pages/admin.py
from django.contrib import admin
from .models import Diary  # 1. 自分で作ったDiaryを読み込む

# pages/admin.py
from .models import Diary, ContactMessage # ContactMessageを追加

admin.site.register(Diary)
admin.site.register(ContactMessage) # これを追記
