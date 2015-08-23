================
django-mptt-docs
================

`django-mptt-docs` is a simple app which you can use to manage documentations for your django project.

HackerEarth's documentation is powered by `django-mptt-docs`, see it in action here::
    
    https://www.hackerearth.com/docs/

Why use it?
-----------

1. You love markdown.

2. Easy to use: It's true there is static tools like `sphinx` to handle documentation, there
you need create dirs, files etc. Say you have to move an entire dir to another
parent directory you need to cut-paste, it's too mainstream so to use this
package, you need to set a parent and hit save in admin panel. That's it, it
will regenerate all the urls and deploy.

3. It's highly customizable. You don't need to write htmls or css for different
pages manually, just do it once.

Installation
------------

1. This app depends on `django-mptt` so download `django-mptt` to your project directory or install it from pip. Add `docs` and `django-mptt` to your INSTALLED_APPS settings like this::

   INSTALLED_APPS = [
        ...
        'docs',
        'django-mptt',
   ]

2. Include the `docs` URLconf in your project like this::

   url(r'^docs/', include('docs.urls')),

3. Add `/docs/static` to your STATICFILES_DIRS settings like this::

   STATICFILES_DIRS = (
        '/docs/static/',
   )

4. Migrate docs application to create the models.

5. Visit django-admin panel to create docs and see it live here::
   http://localhost:8000/docs/parent/child/


