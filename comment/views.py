import time

from django.core.paginator import Paginator

from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from index.models import *


def commentView(request,song_id):
    search_song=Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:6]
    if request.method == 'POST':
        comment_text = request.POST.get('comment','')
        comment_user = request.user.username if request.user.username else '匿名用户'
        if comment_text:
            comment = Comment()
            comment.comment_text = comment_text
            comment.comment_user = comment_user
            comment.comment_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            comment.song_id = song_id
            comment.save()
        return redirect('/comment/%s.html'%(str(song_id)))
    else:
        song_info = Song.objects.filter(song_id=song_id).first()
        if not song_info:
            raise Http404
        comment_all = Comment.objects.filter(song_id=song_id).order_by('comment_date')
        song_name = song_info.song_name
        page = int(request.GET.get('page',1))
        paginator = Paginator(comment_all,2)
        try:
            contacts = paginator.page(page)
        except :
            contacts = paginator.page(paginator.num_pages)
        return render(request,'comment.html',locals())