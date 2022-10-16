from wtforms import widgets
from wtforms.widgets import html_params
from markupsafe import escape, Markup


class SelectWidget(widgets.Select):
    """Overrides WTForm's Select widget to insert placeholder options"""

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        if self.multiple:
            kwargs['multiple'] = True
        if 'required' not in kwargs and 'required' in getattr(field, 'flags', []):
            kwargs['required'] = True
        html = ['<select %s>' % html_params(name=field.name, **kwargs)]

        html.append(self.render_option('', 'Select...', field.data in [None, ''], disabled=True))
        html.append(self.render_option('', '----------', False, disabled=True))

        for val, label, selected in field.iter_choices():
            html.append(self.render_option(val, label, selected))
        html.append('</select>')
        return Markup(''.join(html))


class DateTimeWidget(widgets.html5.DateTimeInput):
    pass