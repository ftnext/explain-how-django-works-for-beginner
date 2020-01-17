from django.shortcuts import render


def post_list(request):
    # 指定したテンプレート（HTML）をメッセージ本文に入れた
    # HTTPレスポンス（HttpResponse）を、render関数で作って返す
    return render(request, 'blog/post_list.html', {})
