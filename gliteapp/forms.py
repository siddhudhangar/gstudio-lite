from django import forms


class SearchForm(forms.Form):
    Search = forms.CharField(label='Search', max_length=100)


main_filters= (
    ('images,audios,videos', 'All'),
    ('images', 'Images'),
    ('audios', 'Audios'),
    ('videos', 'Videos'),
    ('documents', 'Documents'),

)

educationallevel_filters=(
    ('sel','Select Educational Level'),
   # ('primary,upper primary,secondary,senior secondary,tertiary','All'),
    ('primary','Primary'),
    ('upper primary','Upper Primary'),
    ('secondary','Secondary'),
    ('senior secondary','Senior Secondary'),
    ('tertiary','Tertiary'),
)

target_group_filters=(
    ('stg','Select Target Group'),
    ('teachers','Teachers'),
    ('students','Students'),
    ('teacher educators','Teacher Educators'),
)

class SearchTextForm(forms.Form):
    SearchText = forms.CharField(label='Search', max_length=100)
    filter_field = forms.ChoiceField(label='Filters', choices=main_filters)
    educational_filter_field = forms.ChoiceField(label='educational level', choices=educationallevel_filters)
    target_group_filter_field = forms.ChoiceField(label='Target Group', choices=target_group_filters)
