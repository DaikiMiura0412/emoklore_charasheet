from django.contrib import admin

# Taskモデルをインポート
from .models import CharacterData

# 管理サイトへのモデルを登録
admin.site.register(CharacterData)