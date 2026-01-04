# pages/context_processors.py
from .models import Diary

def archive_months(request):
    # データベースから、日記がある「月」だけを重複なく、新しい順に取得する魔法の1行
    months = Diary.objects.dates('date', 'month', order='DESC')
    return {
        'archive_months': months,
    }