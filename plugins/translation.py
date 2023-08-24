import json
import logging
import os

translations_cache = {}
FALLBACK_LANGUAGE = 'en'


def load_translations(language=None):
    global translations_cache

    languages_to_load = [language] if language else ['fr', 'en', 'de']
    for lang in languages_to_load:
        try:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            with open(f'{dir_path}/../i18n/{lang}.json', 'r', encoding='utf-8') as f:
                translations_cache[lang] = json.load(f)
                logging.info(f"Translations loaded for {lang}")
        except FileNotFoundError as e:
            logging.error(f"ERR 4651: Cannot load translations for {lang} -> {str(e)}")
            if language:
                raise e


def get_translation(language, key=None):
    global translations_cache

    if language not in translations_cache:
        load_translations(language)

    translations = translations_cache.get(language) or translations_cache.get(FALLBACK_LANGUAGE, {})
    if key:
        return translations.get(key, f"Translation missing for {key}")
    return translations
