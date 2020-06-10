from django.db import models

# Create your models here.
class PythonJob(models.Model):
    positionName = models.CharField(max_length=200, default='', verbose_name='职位名称')
    companyFullName = models.CharField(max_length=200, default='', verbose_name='公司名称')
    companySize = models.CharField(max_length=200, default='', verbose_name='公司规模')
    education = models.CharField(max_length=200, default='', verbose_name='学历需求')
    workYear = models.CharField(max_length=200, default='', verbose_name='工作经验')
    skillLables = models.CharField(max_length=200, default='', verbose_name='所需技能')
    salary = models.CharField(max_length=200, default='', verbose_name='工资待遇')
    address = models.CharField(max_length=200, default='', verbose_name='办公地址')
    createTime = models.CharField(max_length=200, default='', verbose_name='职位发布时间')

