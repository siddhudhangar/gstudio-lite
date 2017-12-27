from django.shortcuts import render
import json
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SearchForm,SearchTextForm
from django.core.urlresolvers import reverse
from elasticsearch import Elasticsearch
from django import template

register = template.Library()



def view_json(request):


    if request.method=='POST':

        #data=json.load(open('/home/siddhu/gstudio/data/rcs-repo/Nodes/0/1/d/57c7c1ad16b51c39fe82dc10.json'))
        form = SearchForm(request.POST)
        if form.is_valid():
            Search = form.cleaned_data['Search']
            data = json.load(open('/home/siddhu/gstudio/data/glite-rcs-repo/Nodes/f/1/1/'+Search+'.json'))
            #return HttpResponseRedirect('/views_json/')
            #t = loader.get_template('test.html')
            #c = RequestContext(request, {'data123': json.dumps(data)})
            #return HttpResponse(t.render(c), content_type="application/json")
            #return render_to_response('test.html',context_instance=RequestContext(request, {'data123': data, 'form': form})) ... django 1.7
            return render(request, 'test.html', {'data123': data, 'form': form})

    #else:
        #form = SearchForm()
        #return HttpResponseRedirect('/')

    #return render_to_response('test.html', context_instance=RequestContext(request, {'data123': data,'form':form}))
    return render(request, 'test.html', {})



def search(request):
    if request.method=='POST':
        form = SearchTextForm(request.POST)

        if form.is_valid():
            es = Elasticsearch('http://10.1.0.229:9200')

            Search = form.cleaned_data['SearchText']

            Search.encode('utf8')
            filter_field = form.cleaned_data['filter_field']
            educational_filter_field = form.cleaned_data['educational_filter_field']
            target_group_filter_field = form.cleaned_data['target_group_filter_field']
            source_filter_field = form.cleaned_data['source_filter_field']
            language_filter_field = form.cleaned_data['language_filter_field']
            educationalsubject_filter_field = form.cleaned_data['educationalsubject_filter_field']

            allfilters={"filter_field":filter_field,"educational_filter_field":educational_filter_field ,"target_group_filter_field":target_group_filter_field,"source_filter_field":source_filter_field
                        ,"language_filter_field":language_filter_field, "educationalsubject_filter_field":educationalsubject_filter_field}
            selected_filters={}

            temp = ''

            if filter_field == 'all' :
                filter_field=('audios','videos','images')

            for key,value in allfilters.items():
                if value !=  'sel' and value != 'stg' and value != 'ss' and value != 'sl' and value != 'ses':
                    selected_filters.update({key:value})


            for key,value in selected_filters.items():
                if key == 'educational_filter_field' :
                    temp_educational_filter_field='{"term":{"attribute_set.educationallevel":'+'"'+educational_filter_field+'"'+'}},'
                    temp=temp+temp_educational_filter_field
                    print(temp)
                elif key == 'target_group_filter_field':
                    temp_target_group_filter_field='{"term":{"attribute_set.audience":'+'"'+target_group_filter_field+'"'+'}},'
                    temp=temp+temp_target_group_filter_field
                elif key == 'source_filter_field':
                    temp_source_filter_field = '{"term":{"attribute_set.source":' + '"' + source_filter_field + '"' + '}},'
                    temp = temp + temp_source_filter_field
                elif key == 'language_filter_field':
                    temp_language_filter_field = '{"term":{"language":' + '"' + language_filter_field + '"' + '}},'
                    temp = temp + temp_language_filter_field
                elif key == 'educationalsubject_filter_field':
                    temp_educationalsubject_filter_field = '{"term":{"attribute_set.educationalsubject":' + '"' + educationalsubject_filter_field + '"' + '}},'
                    temp = temp + temp_educationalsubject_filter_field



            if (( Search not in [None, ''] and selected_filters['filter_field'] == 'all' or selected_filters['filter_field'] == 'videos' or selected_filters['filter_field'] == 'audios' or selected_filters['filter_field'] == 'documents' or selected_filters['filter_field'] == 'images')
                 and educational_filter_field == 'sel' and target_group_filter_field == 'stg' and source_filter_field == 'ss' and language_filter_field == 'sl' and educationalsubject_filter_field == 'ses'):

                res = es.search(index="gstudio-lite", doc_type=filter_field, body={"query": { "multi_match":{ "query": Search, "fields": [ "name", "tags","content" ]}  } }
                            ,scroll="10m",size="30")

                #print("%d documents found:" % res['hits']['total'])

            elif ( Search in [None, ''] ):
                print('elif')
                if ((selected_filters['filter_field'] == 'all' or selected_filters['filter_field'] == 'videos' or selected_filters['filter_field'] == 'audios' or selected_filters['filter_field'] == 'documents' or selected_filters['filter_field'] == 'images')
                 and educational_filter_field == 'sel' and target_group_filter_field == 'stg' and source_filter_field == 'ss' and language_filter_field == 'sl' and educationalsubject_filter_field == 'ses'):
                    res = es.search(index="gstudio-lite", doc_type=filter_field, body={
                        "query": {"bool": {"must": [{"term": {"status": "published"}}]}}},
                                    scroll="10m", size="30")

                else:
                    res = es.search(index="gstudio-lite", doc_type=filter_field, body={
                        "query": {"bool": {"must": [{"term": {"status": "published"}}, eval(str(temp))]}}},
                                    scroll="10m", size="30")
            else:
                print(temp)
                res = es.search(index="gstudio-lite", doc_type=filter_field, body={"query": {"bool": {"must":[{"multi_match": {"query": Search, "fields": ["name", "tags", "content"]}}, {"term": { "status": "published" }}, eval(str(temp)) ]}}}, scroll="10m", size="30",)

            doc={}

            #for doc in res['hits']['hits']:
                #print("%s) %s" % (doc['_id'], doc['_source']['content']))
             #   print()
            return render(request, 'search.html', {'hits':res['hits']['hits'],'total_hits': res['hits']['total'],'form': form})
    else:
        form = SearchTextForm()
        #return HttpResponseRedirect('/')

    return render(request, 'search.html', {'form': form})

