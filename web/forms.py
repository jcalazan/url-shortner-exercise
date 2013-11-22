from django import forms

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Button, Submit, Fieldset, Field, HTML
from crispy_forms.bootstrap import FormActions

from .models import ShortenedUrl


class UrlShortenerForm(forms.ModelForm):
    """
    A simple form for shortening a given URL.
    """

    def __init__(self, *args, **kwargs):
        super(UrlShortenerForm, self).__init__(*args, **kwargs)

        self.fields['shortened'].required = False

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal col-xs-8'
        self.helper.field_class = 'col-lg-12'
        self.helper.form_show_labels = False

        self.helper.layout = Layout(
            Fieldset(
                'Please enter a URL to shorten',
                HTML("""
                {% if already_shortened %}
                    <p class="text-danger">
                    This URL is already shortened. Please try another!
                    </p>
                {% endif %}
                """),
                Field('original',
                      placeholder='e.g. https://www.payperks.com/help',
                      onclick='select_all("id_original");'),
                FormActions(
                    Submit('submit', 'Shorten URL'),
                    css_class='pull-right'
                ),
            ),
            Fieldset(
                'Shortened URL',
                Field('shortened',
                      readonly=True,
                      onclick='select_all("id_shortened");'),
                FormActions(
                    Button('go', 'Go!', css_class='btn-primary'),
                    css_class='pull-right'
                ),
            ),
            HTML("""<br><br><p class="text-center">"""),
            Button(
                'lucky',
                'I\'m Feeling Lucky',
                onclick='location.href="https://www.payperks.com/signup"',
                css_class='btn-success'
            ),
            HTML("""</p>"""),
        )

    class Meta:
        model = ShortenedUrl