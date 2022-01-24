from re import A
import app

def index_page(request, *args):
    output = app.render(template_name="./templates/app/index.html", kwargs={"name": "user"})
    return '200 OK', output.encode('utf-8')

def users_page(request, *args):
    output = app.render(template_name="./templates/app/users.html", users=args)
    return '200 OK', output.encode('utf-8')


def about_page(request, *args):
    output = app.render(template_name="./templates/app/about.html")
    return '200 OK', output.encode('utf-8')


def contact_page(request, *args):
    output = app.render(template_name="./templates/app/contact.html")
    return '200 OK', output.encode('utf-8')


class NotFoundPage:
    def __call__(self, request, *args):
        output = app.render(template_name="./templates/app/error.html")
        return '200 OK', output.encode('utf-8')
