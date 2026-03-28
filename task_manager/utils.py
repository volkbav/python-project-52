# task_manager/functions.py
import os

import markdown as md
from django.forms import (
    CheckboxInput,
    Select,
    SelectMultiple,
)
from django.utils.safestring import mark_safe

# расположение сервера: интернет-локальная сеть
SERVER_LOCATION = os.getenv('SERVER_LOCATION', 'local')


# # проверка расположения сервера (используется в шаблонах)
def is_server_local(request):
    return {'location': SERVER_LOCATION}


def attrs_add(fields, placeholders=None, widget_classes=None):
    placeholders = placeholders or {}
    widget_classes = widget_classes or {}

    for name, field in fields.items():
        widget = field.widget

        # placeholder
        if name in placeholders:
            widget.attrs.setdefault("placeholder", placeholders[name])

        # class
        if name in widget_classes:
            widget.attrs["class"] = widget_classes[name]
            continue

        if isinstance(widget, (Select, SelectMultiple)):
            widget.attrs.setdefault("class", "form-select")
        elif isinstance(widget, CheckboxInput):
            widget.attrs.setdefault("class", "form-check-input")
        else:
            widget.attrs.setdefault("class", "form-control")


# Проверка булевых переменных из переменных окружения
def env_bool(name: str, default: bool = False) -> bool:
    val = os.getenv(name)
    if val is None:
        return default
    return val.strip().lower() in {"1", "true", "yes", "y", "on"}


def render_markdown(text: str) -> str:
    html = md.markdown(
        text,
        extensions=[
            'nl2br',  # преобразование \n в <br>
            'fenced_code',  # 'fenced_code' - code
            'tables',
            'codehilite',  # подсветка кода
            'pymdownx.extra',  # без него не работала подсветка кода
            'pymdownx.tasklist',  # списки
        ],
        extension_configs={
            "codehilite": {
                "use_pygments": True,
                "guess_lang": False,   # Отключаем угадывание
                "css_class": "codehilite",
            },
            "pymdownx.tasklist": {"custom_checkbox": True}
        },
    )
    return mark_safe(html)