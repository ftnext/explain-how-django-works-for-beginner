from django.http import HttpResponse


def post_list(request):
    # 引数requestはHttpRequest（Django流のHTTPリクエストの扱い方）
    # request.methodでHTTPメソッドを確認できる
    if request.method == 'GET':
        # HttpResponseはDjango流のHTTPレスポンスの扱い方
        # メッセージ本文を指定して，HttpResponseを返す（→ブラウザに表示される）
        return HttpResponse('GETリクエストへのレスポンスです')
    else:
        return HttpResponse('レスポンスです')
