from django import forms


class SearchForm(forms.Form):
    Search = forms.CharField(label='Search', max_length=100)


main_filters= (
    ('all', 'All'),
    ('images', 'Images'),
    ('audios', 'Audios'),
    ('videos', 'Videos'),
    ('documents', 'Documents'),

)

educationallevel_filters=(
    ('sel','Select Educational Level'),
   # ('primary,upper primary,secondary,senior secondary,tertiary','All'),
    ('Primary','Primary'),
    ('Upper Primary','Upper Primary'),
    ('Secondary','Secondary'),
    ('Senior Secondary','Senior Secondary'),
    ('Tertiary','Tertiary'),

)

target_group_filters=(
    ('stg','Select Target Group'),
    ('Teachers','Teachers'),
    ('Students','Students'),
    ('Teacher Educators','Teacher Educators'),
)

source_filters=(
    ('ss','Select Source'),
    ('CIET, NCERT','CIET, NCERT'),
    ('NCERT','NCERT'),
    ('Vidya Online','Vidya Online'),
    ('Arvind Gupta','Arvind Gupta'),
    ('CCRT','CCRT'),
    ('Vigyan Prasar','Vigyan Prasar'),
    ('Expositive','Expositive'),
    ('Gandhi Darshan','Gandhi Darshan'),
    ('UNICFF','UNICFF'),
    ('GIET, Gujarat','GIET, Gujarat'),
    ('RIE, Mysore','RIE, Mysore'),
    ('Gandhi Heritage Portal','Gandhi Heritage Portal'),
    ('SCERT, Bihar','SCERT, Bihar'),
    ('SIET Hyderabad','SIET Hyderabad'),
    ('SIET, Kerala','SIET, Kerala'),
    ('SIET, UP','SIET, UP'),
    ('SCERT, UP','SCERT, UP'),
    ('ASI','ASI'),
    ('DAE','DAE'),
    ('SCERT Bihar','SCERT Bihar'),
    ('Azim Premji University','Azim Premji University'),
    ('Eklavya','Eklavya'),
    ('SIET, Pune','SIET, Pune'),
    ('Jean-Pierre Petit','Jean-Pierre Petit'),
    ('SCERT, Solan','SCERT, Solan'),

)

language_filters=(
    ('sl','Select Language'),
    ('english','English'),
    ('gujarati','Gujarati'),
    ('hindi','Hindi'),
    ('manipuri','Manipuri'),
    ('marathi','Marathi'),
    ('mizo','Mizo'),
    ('telugu','Telugu'),
)

educationalsubject_filters=(
    ('ses','Select Educational Subject'),
    ('Language','Language'),
    ('Mathematics','Mathematics'),
    ('Environmental Studies','Environmental Studies'),
    ('Science','Science'),
    ('Chemistry','Chemistry'),
    ('Physics','Physics'),
    ('Biology','Biology'),
    ('Social Science','Social Science'),
    ('History','History'),
    ('Geography','Geography'),
    ('Political Science','Political Science'),
    ('Economics','Economics'),
    ('Sociology','Sociology'),
    ('Psychology','Psychology'),
    ('Commerce','Commerce'),
    ('Business Studies','Business Studies'),
    ('Accountancy','Accountancy'),
    ('Art','Art'),
    ('Education','Education'),

)



class SearchTextForm(forms.Form):
    SearchText = forms.CharField(required=False, label='Search', max_length=200)
    filter_field = forms.ChoiceField(label='Filters', choices=main_filters)
    educational_filter_field = forms.ChoiceField(label='Educational level', choices=educationallevel_filters)
    target_group_filter_field = forms.ChoiceField(label='Target Group', choices=target_group_filters)
    source_filter_field = forms.ChoiceField(label='Source', choices=source_filters)
    language_filter_field = forms.ChoiceField(label='Language', choices=language_filters)
    educationalsubject_filter_field = forms.ChoiceField(label='Educational Subject', choices=educationalsubject_filters)