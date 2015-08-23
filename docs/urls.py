from django.conf.urls.defaults import patterns, url

import docs.views

urlpatterns = patterns('',

    url(r'^$',
            docs.views.view_doc,
            name='view_doc'),

    url(r'^(?P<namespace>[\w\-\.\/]+)/$',
            docs.views.view_doc,
            name='view_doc_namespace'),
)


