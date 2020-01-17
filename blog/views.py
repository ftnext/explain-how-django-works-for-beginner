from django.shortcuts import render
from django.utils import timezone

from .models import Post


def post_list(request):
    # ブログ投稿のうち、published_date（公開日）が現在より前のものを取得し。
    # 公開日の昇順（以前に公開されたものほど上）に並べ替える
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 取得した投稿データpostsをテンプレートでpostsという名前で扱えるように渡す
    return render(request, 'blog/post_list.html', {'posts': posts})
