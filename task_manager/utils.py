# task_manager/functions.py
import os

from django.forms import (
    CheckboxInput,
    Select,
    SelectMultiple,
)

# расположение сервера: интернет-локальная сеть
SERVER_LOCATION = os.getenv('SERVER_LOCATION', 'local')


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


# # проверка расположения сервера (используется в шаблонах)
# def is_server_local(request):
#     return {'location': SERVER_LOCATION}


# Проверка булевых переменных из переменных окружения
def env_bool(name: str, default: bool = False) -> bool:
    val = os.getenv(name)
    if val is None:
        return default
    return val.strip().lower() in {"1", "true", "yes", "y", "on"}