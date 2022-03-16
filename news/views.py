from django.views.generic import ListView, DetailView

from .models import Post
from .filters import PostFilter


class PostList(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news'
    paginate_by = 5


class PostSearch(PostList):
    template_name = 'news_search.html'

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
        }


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
