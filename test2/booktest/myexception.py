from django.http import HttpResponse

class MyException:
    def process_exception(request, response, exception):
        """中间件： 当出现异常的时候执行"""
        return HttpResponse(exception)
