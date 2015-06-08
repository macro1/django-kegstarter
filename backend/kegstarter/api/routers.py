from rest_framework import routers


class AppRouter(routers.DefaultRouter):
    def __init__(self, *args, **kwargs):
        self._children = []
        self._args = args
        self._kwargs = kwargs
        return super().__init__(*args, **kwargs)

    def app_router(self, app):
        arc = AppRouterChild(app, *self._args, **self._kwargs)
        self._children.append(arc)
        return arc

    def get_urls(self):
        urls= list(url for suburls in self._children
                    for url in suburls.get_urls())
        return urls


class AppRouterChild(routers.DefaultRouter):
    def __init__(self, app, *args, **kwargs):
        self.app = app
        return super().__init__(*args, **kwargs)

    def get_default_base_name(self, viewset):
        return '{app}-{name}'.format(app=self.app, name=super().get_default_base_name(viewset))


api_router = AppRouter()
