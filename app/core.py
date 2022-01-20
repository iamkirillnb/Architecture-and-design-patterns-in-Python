import app

def index_page(request):
    output = app.render(template_name="./templates/index.html", kwargs={"name": "user"})
    return '200 OK', output.encode('utf-8')


def about_page(request):
    output = app.render(template_name="./templates/about.html")
    return '200 OK', output.encode('utf-8')


def contact_page(request):
    output = app.render(template_name="./templates/contact.html")
    return '200 OK', output.encode('utf-8')


class NotFoundPage:
    def __call__(self, request):
        output = app.render(template_name="./templates/error.html")
        return '200 OK', output.encode('utf-8')


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if path in self.routes:
            controller = self.routes[path]
        else:
            controller = NotFoundPage()
        request = {}
        for front in self.fronts:
            front(request)
        answer, body = controller(request)
        start_response(answer, [('Content-Type', 'text/html')])
        return [body]