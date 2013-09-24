from utils import wsgi_wrapper
from webob import Response

@wsgi_wrapper
def hello_app(request, name=''):
    content = []
    content.append('Hello %s' % name)

    response = Response(body='\n'.join(content))
    response.headers['content-type'] = 'text/plain'
    return response

