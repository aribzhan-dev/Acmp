from django.shortcuts import render, redirect
from main.models import Language, Tasks, Clue, Comment
from main.utils import get_translations


def indexHandler(request):
    # Barcha tillar
    language = Language.objects.filter(status=0)

    # Tanlangan til ID (default — 1)
    selected_lang_id = request.GET.get('lang', '1')
    lang_obj = Language.objects.filter(id=int(selected_lang_id)).first()
    selected_lang_code = lang_obj.code if lang_obj else 'ru'

    # Tilga mos tasklar
    tasks = Tasks.objects.filter(language=lang_obj, status=0) if lang_obj else Tasks.objects.filter(status=0)

    # Tarjimalar
    translations = get_translations(selected_lang_code)

    return render(request, 'index.html', {
        'language': language,
        'tasks': tasks,
        'selected_lang_id': selected_lang_id,
        'selected_lang_code': selected_lang_code,
        'translations': translations
    })


def index1Handler(request, index_id):
    # Barcha tillar
    language = Language.objects.filter(status=0)

    # Tanlangan til ID
    selected_lang_id = request.GET.get('lang', '1')
    lang_obj = Language.objects.filter(id=int(selected_lang_id)).first()
    selected_lang_code = lang_obj.code if lang_obj else 'ru'

    # Agar POST bo‘lsa — komment saqlaymiz
    if request.method == 'POST':
        new_comment = Comment()
        new_comment.advice = request.POST.get('advice', '')
        new_comment.index_id = index_id
        new_comment.save()
        return redirect(f'/{index_id}/?lang={selected_lang_id}')

    # Task, Clue va Kommentlarni olish
    task = Tasks.objects.get(id=int(index_id))
    clue = Clue.objects.filter(task=task, language=lang_obj)
    comment = Comment.objects.filter(index_id=index_id).order_by('-id')

    # Tarjimalar
    translations = get_translations(selected_lang_code)

    return render(request, 'index1.html', {
        'language': language,
        'task': task,
        'clue': clue,
        'comment': comment,
        'selected_lang_id': selected_lang_id,
        'selected_lang_code': selected_lang_code,
        'translations': translations
    })
