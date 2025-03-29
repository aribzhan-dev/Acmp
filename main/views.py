from django.shortcuts import render, redirect
from main.models import Language, Tasks, Clue, Comment

# Statik matnlar uchun tarjimalar
TRANSLATIONS = {
    'ru': {
        'site_title': 'Платформа задач',
        'choose_language': 'Выберите язык',
        'clue': '🧐 Подсказка',
        'solution': 'Решение задачи',
        'user_comments': '📢 Комментарии пользователей',
        'leave_comment': '✍️ Оставить комментарий',
        'new_comment': '✍️ Новый комментарий',
        'write_comment': 'Напишите ваш комментарий...',
        'send': 'Отправить'
    },
    'kk': {
        'site_title': 'Тапсырма платформасы',
        'choose_language': 'Тілді таңдаңыз',
        'clue': '🧐 Кеңес',
        'solution': 'Тапсырманың шешімі',
        'user_comments': '📢 Пайдаланушылар пікірлері',
        'leave_comment': '✍️ Пікір қалдыру',
        'new_comment': '✍️ Жаңа пікір',
        'write_comment': 'Пікіріңізді жазыңыз...',
        'send': 'Жіберу'
    },
    'uz': {
        'site_title': 'Misollar platformasi',
        'choose_language': 'Tilni tanlang',
        'clue': '🧐 Yordam',
        'solution': 'Misolning javobi',
        'user_comments': '📢 Foydalanuvchilar izohlari',
        'leave_comment': '✍️ Izoh qoldirish',
        'new_comment': '✍️ Yangi izoh',
        'write_comment': 'Izohingizni yozing...',
        'send': 'Yuborish'
    }
}



def indexHandler(request):
    language = Language.objects.filter(status=0)

    # Tanlangan tilni olish (agar yo‘q bo‘lsa, rus tili)
    selected_lang_id = request.GET.get('lang', '1')  # Agar hech narsa kelmasa, rus tili ('1')

    # Agar til ID sifatida kelsa, uni `code` formatiga o‘giramiz
    lang_obj = Language.objects.filter(id=int(selected_lang_id)).first()
    selected_lang_code = lang_obj.code if lang_obj else 'ru'  # Agar til topilmasa, 'ru' bo‘ladi

    # Tanlangan tilga mos misollarni olish
    tasks = Tasks.objects.filter(language=lang_obj, status=0) if lang_obj else Tasks.objects.filter(status=0)

    return render(request, 'index.html', {
        'language': language,
        'tasks': tasks,
        'selected_lang_id': selected_lang_id,  # ID shaklida til
        'selected_lang_code': selected_lang_code,  # Matn shaklida til ('ru' yoki 'kk')
        'translations': TRANSLATIONS[selected_lang_code]  # Statik matnlar
    })


def index1Handler(request, index_id):
    language = Language.objects.filter(status=0)

    # Tanlangan tilni olish
    selected_lang_id = request.GET.get('lang', '1')
    lang_obj = Language.objects.filter(id=int(selected_lang_id)).first()
    selected_lang_code = lang_obj.code if lang_obj else 'ru'

    if request.POST:
        new_comment = Comment()
        new_comment.advice = request.POST.get('advice', '')
        new_comment.index_id = index_id
        new_comment.save()
        return redirect(f'/index/{index_id}/?lang={selected_lang_id}')

    task = Tasks.objects.get(id=int(index_id))
    clue = Clue.objects.filter(task=task, language=lang_obj)
    comment = Comment.objects.filter(index_id=index_id).order_by('-id')

    return render(request, 'index1.html', {
        'language': language,
        'task': task,
        'clue': clue,
        'comment': comment,
        'selected_lang_id': selected_lang_id,
        'selected_lang_code': selected_lang_code,
        'translations': TRANSLATIONS[selected_lang_code]
    })
