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
