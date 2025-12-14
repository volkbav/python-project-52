# task_manager/functions.py
from django.forms import (
    CheckboxInput,
    Select,
    SelectMultiple,
)


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
