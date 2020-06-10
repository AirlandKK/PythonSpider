from django.shortcuts import render
from django.views.generic import View
from utils import make_wordcloud
from .models import PythonJob


# Create your views here.

class IndexView(View):
    # 首页展示
    def get(self, request):
        obj = PythonJob.objects.all()
        return render(request, 'index.html', locals())


class CiyunView(View):
    # 词云展示
    def get(self, request):
        # make_wordcloud.run()
        return render(request, 'ciyun.html')


class Ciyun2View(View):
    # 词云2展示
    def get(self, request):
        # make_wordcloud.run()
        return render(request, 'ciyun2.html')


class FenxiView(View):
    # 数据分析展示
    def get(self, request):
        # 生成一个PythonJob对象，里面存着所有的数据
        obj = PythonJob.objects.all()
        skill_data = []
        edu_data_li = []
        for i in obj:
            # 所需技能筛选
            skill_data.append(i.skillLables)
            # 所需学历
            edu_data_li.append(i.education)

        # 柱状图数据
        # 学历去重(该数据需要传递到前台，柱状图)
        edu_data = [i for i in set(edu_data_li)]
        edu_count = []
        for item in edu_data:
            # 统计重复次数(该数据需要传递到前台，柱状图)
            edu_count.append(edu_data_li.count(item))

        # 饼图数据
        # 技能数据清洗，将多个技能拆分成单个用于统计
        skill_data = [i for i in skill_data if ',' in i for i in i.split(',')]
        # 技能数据去重
        set_skill = [i for i in set(skill_data)]
        res_data = {}
        for i in set_skill:
            # 技能数据统计重复的次数
            res_data[i] = skill_data.count(i)
        # print(skill_data)
        # print(sorted(res_data.items(), key = lambda kv:(kv[1], kv[0]))[-10:])
        # 筛选出最高的10个技能(该数据需要传递到前台，饼图)
        top_10 = dict(sorted(res_data.items(), key=lambda kv: (kv[1], kv[0]))[-10:])
        # 筛选出最高的10个技能的名字(该数据需要传递到前台，饼图)
        skill_list = [i for i in top_10.keys()]

        return render(request, 'fenxi.html', locals())
