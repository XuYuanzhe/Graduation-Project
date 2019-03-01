from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm


def post_comment(request, post_pk):
    # 当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # 检查表单的数据是否符合格式要求
        if form.is_valid():
            # 仅利用表单的数据生成 Comment 模型类的实例 但还不保存评论数据到数据库
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)
