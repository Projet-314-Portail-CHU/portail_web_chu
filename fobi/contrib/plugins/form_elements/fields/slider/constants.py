from django.utils.translation import gettext_lazy as _

__title__ = 'fobi.contrib.plugins.form_elements.fields.slider.constants'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'SLIDER_TOOLTIP_SHOW',
    'SLIDER_TOOLTIP_HIDE',
    'SLIDER_TOOLTIP_ALWAYS',
    'SLIDER_DEFAULT_TOOLTIP',
    'SLIDER_TOOLTIP_CHOICES',

    'SLIDER_HANDLE_ROUND',
    'SLIDER_HANDLE_SQUARE',
    'SLIDER_HANDLE_TRIANGLE',
    'SLIDER_HANDLE_CUSTOM',
    'SLIDER_HANDLE_CHOICES',

    'SLIDER_SHOW_ENDPOINTS_AS_LABELED_TICKS',
    'SLIDER_SHOW_ENDPOINTS_AS_LABELS',
    'SLIDER_SHOW_ENDPOINTS_AS_TICKS',
    'SLIDER_DEFAULT_SHOW_ENDPOINTS_AS',
    'SLIDER_SHOW_ENDPOINTS_AS_CHOICES',
)

SLIDER_TOOLTIP_SHOW = 'show'
SLIDER_TOOLTIP_HIDE = 'hide'
SLIDER_TOOLTIP_ALWAYS = 'always'
SLIDER_DEFAULT_TOOLTIP = SLIDER_TOOLTIP_SHOW

SLIDER_TOOLTIP_CHOICES = (
    (SLIDER_TOOLTIP_SHOW, _("Show")),
    (SLIDER_TOOLTIP_HIDE, _("Hide")),
    (SLIDER_TOOLTIP_ALWAYS, _("Always")),
)

SLIDER_HANDLE_ROUND = 'round'
SLIDER_HANDLE_SQUARE = 'square'
SLIDER_HANDLE_TRIANGLE = 'triangle'
SLIDER_HANDLE_CUSTOM = 'custom'
SLIDER_DEFAULT_HANDLE = SLIDER_HANDLE_ROUND
SLIDER_HANDLE_CHOICES = (
    (SLIDER_HANDLE_ROUND, _("Round")),
    (SLIDER_HANDLE_SQUARE, _("Square")),
    (SLIDER_HANDLE_TRIANGLE, _("Triangle")),
    (SLIDER_HANDLE_CUSTOM, _("Custom")),
)

SLIDER_SHOW_ENDPOINTS_AS_LABELED_TICKS = 'labeled_ticks'
SLIDER_SHOW_ENDPOINTS_AS_LABELS = 'labels'
SLIDER_SHOW_ENDPOINTS_AS_TICKS = 'ticks'
SLIDER_DEFAULT_SHOW_ENDPOINTS_AS = SLIDER_SHOW_ENDPOINTS_AS_LABELS
SLIDER_SHOW_ENDPOINTS_AS_CHOICES = (
    (SLIDER_SHOW_ENDPOINTS_AS_LABELS, _("Labels")),
    (SLIDER_SHOW_ENDPOINTS_AS_TICKS, _("Ticks without labels")),
    (SLIDER_SHOW_ENDPOINTS_AS_LABELED_TICKS, _("Labeled ticks")),
)
