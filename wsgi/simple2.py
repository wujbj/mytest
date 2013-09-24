#!/usr/bin/env python

from wsgiref import simple_server
from webob import Request, Response
      
def hello_world_app(request):  
    content = []
    content.append('Hello %s' % request.GET['name'])
    
    for key, value in request.environ.items():
        content.append('%s: %s' % (key, value))

    response = Response(body='\n'.join(content))
    response.headers['content-type'] = 'text/plain'
    return response

def wsgi_wrapper(environ, start_response):
    request = Request(environ)
    response = hello_world_app(request)
    return response(environ, start_response)

      
server = simple_server.make_server('', 8000, wsgi_wrapper)
server.serve_forever()  
