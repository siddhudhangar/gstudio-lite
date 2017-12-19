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

            if educational_filter_field == 'sel':

                res = es.search(index="gstudio-lite", doc_type=filter_field, body={"query":   { "multi_match":{ "query": Search, "fields": [ "name", "tags","content" ]}  } }
                            ,scroll="10m",size="100")
            #print("%d documents found:" % res['hits']['total'])



            else:
                res = es.search(index="gstudio-lite", doc_type=filter_field, body={"query": {"bool": {"must":[{"term": { "attribute_set.educationallevel": educational_filter_field }},{"multi_match": {"query": Search, "fields": ["name", "tags", "content"]}}]}}}, scroll="10m", size="100")
            doc={}

            for doc in res['hits']['hits']:
                print("%s) %s" % (doc['_id'], doc['_source']['content']))
            return render(request, 'search.html', {'hits':res['hits']['hits'],'total_hits': res['hits']['total'],'form': form})
    else:
        form = SearchTextForm()
        #return HttpResponseRedirect('/')

    return render(request, 'search.html', {'form': form})

