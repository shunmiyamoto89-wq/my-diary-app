# pages/views.py
from django.views.generic import ListView, DetailView, FormView 
from django.urls import reverse_lazy
from .models import Diary, ContactMessage 
from .forms import ContactForm

# 1. お問い合わせフォームのビュー
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        # データベースに保存する処理
        data = form.cleaned_data
        ContactMessage.objects.create(
            name=data['name'],
            email=data['email'],
            message=data['message']
        )
        return super().form_valid(form)

# 2. トップページ（日記一覧）
class HomePageView(ListView):
    model = Diary
    template_name = 'home.html'
    context_object_name = 'diary_list'
    ordering = ['-date']

# 3. 日記の詳細ページ
class DiaryDetailView(DetailView):
    model = Diary
    template_name = 'diary_detail.html'
    context_object_name = 'diary'

# 4. 月別アーカイブ
class MonthArchiveView(ListView):
    model = Diary
    template_name = 'home.html'
    context_object_name = 'diary_list'

    def get_queryset(self):
        return Diary.objects.filter(
            date__year=self.kwargs['year'],
            date__month=self.kwargs['month']
        ).order_by('-date')