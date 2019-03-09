from django.shortcuts import render
from django.views.generic import ListView

from index.models import Dynamic, Song


def rankingView(request):
    # 热搜歌曲
    search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
    # 歌曲分类列表
    all_list = Song.objects.values('song_type').distinct()
    # 歌曲信息列表
    song_type = request.GET.get('type','')
    if song_type:
        song_info = Dynamic.objects.select_related('song').filter(song__song_type=song_type).order_by('-dynamic_plays').all()[:10]
    else:
        song_info = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:10]
    return render(request,'ranking.html',locals())

class RankingList(ListView):
    # context_object_name设置HTML模板的某一个变量名称
    context_object_name = 'song_info'
    #设置模板文件
    template_name = 'ranking.html'
    #查询变量song_info的数据
    def get_queryset(self):
        song_type = self.request.GET.get('type', '')
        if song_type:
            song_info = Dynamic.objects.select_related('song').filter(song__song_type=song_type).order_by(
                '-dynamic_plays').all()[:10]
        else:
            song_info = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:10]
        return song_info

    #添加其他变量
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_song'] = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
        context['all_list'] = Song.objects.values('song_type').distinct()
        return context