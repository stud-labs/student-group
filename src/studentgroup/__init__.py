from pyramid.config import Configurator

# from .serv import main

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        config.include('.serv.routes')
        config.include('cornice')
        config.scan()
    return config.make_wsgi_app()
