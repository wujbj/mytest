#!/usr/bin/env python

from wsgiref import simple_server
from webob import Request, Response
      
@wsgi_wrapper
def hello_world_app(request):  
    content = []
    content.append('Hello %s' % request.GET['name'])
    
    for key, value in request.environ.items():
        content.append('%s: %s' % (key, value))

    response = Response(body='\n'.join(content))
    response.headers['content-type'] = 'text/plain'
    return response

def wsgi_wrapper(func):
    def new_func(environ, start_response):
        request = Request(environ)
        response = func(request)
        return response(environ, start_response)
    
    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    return new_func

      
server = simple_server.make_server('', 8000, wsgi_wrapper)
server.serve_forever()  
