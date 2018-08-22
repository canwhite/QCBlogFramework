#这个是我们需要的views_if

from django.http import JsonResponse
from blog.models import CommonData
# from django.core.exceptions import ValidationError,ObjectDoesNotExist #格式错误,和数据不存在
# from django.db.utils import IntegrityError #手机号问题
import time




def get_common_data(request):

    datas = []
    results = CommonData.objects.all()

    if results:
        for r in results:
            data = {}
            data["title"] = r.title
            data["content"] = r.content
            data["time"] = r.time

            datas.append(data)


        return JsonResponse({'status':200,'message':'success','data':datas})

