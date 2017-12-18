from django import forms


class SearchForm(forms.Form):
    Search = forms.CharField(label='Search', max_length=100)


Filters= (
    ('images,audios,videos', 'All'),
    ('images', 'Images'),
    ('audios', 'Audios'),
    ('videos', 'Videos'),
    ('documents', 'Documents'),

)


class SearchTextForm(forms.Form):
    SearchText = forms.CharField(label='Search', max_length=100)
    filter_field = forms.ChoiceField(label='Filters', choices=Filters)
