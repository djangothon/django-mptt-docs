from django.http import Http404
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from docs.models import HackerearthDoc


def view_doc(request, namespace=None):
    template = 'index.html'
    ctx = {}

    # Restricted document list
    restricted_documents_slug = []

    # Redirecting if namespace is None
    # YOu can set a custom page to show anything you like
    if namespace is None:
        return redirect('/')
    else:
        # Checking if url is published
        node = HackerearthDoc.objects.filter(
            full_slug=namespace,
            published=True,
        )
        if node:
            node = node[0]
            # If a published document found render it.
            if node.is_document:
                ctx.update({'body_html': node.body_html})

                # Get the parent of the document
                parent_node = HackerearthDoc.objects.filter(
                    full_slug='/'.join(namespace.split('/')[:-1]),
                    published=True
                )
                if parent_node:
                # Get the document tree including parent
                    document_tree = parent_node[0].get_descendants(
                        include_self=True).filter(published=True)
                else:
                    document_tree = []
            else:
                # Get the document tree for the node
                document_tree = node.get_descendants(include_self=True)

                # Redirect to the first child of the document tree for rendering
                # when user accesses a parent node
                if document_tree:
                    try:
                        slug = document_tree[1].slug + '/'
                        return redirect(slug, permanent=True)
                    except IndexError:
                        raise Http404
        else:
            raise Http404

    anon_flag = True
    if request.user.is_authenticated():
        if request.user.is_superuser:
            anon_flag = False

    # Removing restricted documents if user unauthorized
    if anon_flag:
        for restricted_document in restricted_documents_slug:
            document_tree = document_tree.exclude(slug=restricted_document)
        if node.slug in restricted_documents_slug:
            raise Http404

    ctx.update({
        'title': 'HackerEarth Docs',
        'nodes': document_tree,
        'current_node': node,
    })

    ctx = RequestContext(request, ctx)
    return render_to_response(template, ctx)
