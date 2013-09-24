from webob import Request

def wsgi_wrapper(func):
    def new_func(environ, start_response):
        request = Request(environ)
        position_args, keyword_args = environ.get('wsgiorg.routing_args', ((), {}))
        response = func(request, *position_args, **keyword_args)
        return response(environ, start_response)
    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    return new_func
