
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import CatPost
from .forms import CatPostForm
from django.db.models import Q
from .forms import CommentForm
from django.shortcuts import get_object_or_404, redirect, render

class CatPostListView(ListView):
    model = CatPost
    template_name = 'cats/list.html'
    context_object_name = 'posts'
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset().order_by('-created_at')
        q = self.request.GET.get('q')
        status = self.request.GET.get('status')
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(location__icontains=q))
        if status in ('Lost', 'Found'):
            qs = qs.filter(status=status)
        return qs

class CatPostCreateView(CreateView):
    model = CatPost
    form_class = CatPostForm
    template_name = 'cats/create.html'
    success_url = reverse_lazy('cats:list')

class CatPostDetailView(DetailView):
    model = CatPost
    template_name = 'cats/detail.html'
    context_object_name = 'post'


def cat_detail(request, pk):
    post = get_object_or_404(CatPost, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('cats:post_detail', pk=pk) 
    else:
        form = CommentForm()

    return render(request, "cats/detail.html", {
        "post": post,
        "form": form,
    })