from controller import hello_app

mappings = [('/hello/{name}', {'GET':hello_app})]
