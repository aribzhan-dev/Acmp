from .models import Trans, Language

def get_translations(lang_code):
    trans_dict = {}
    lang = Language.objects.filter(code=lang_code).first()
    if lang:
        entries = Trans.objects.filter(language=lang)
        for entry in entries:
            trans_dict[entry.key] = entry.value
    return trans_dict
