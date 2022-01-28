import framework


def index_page(request, *args):
    output = framework.render(template_name="app/index.html", kwargs={"name": "user"})
    return '200 OK', output.encode('utf-8')

def users_page(request, dict):
    output = framework.render(template_name="app/users.html", users=dict)  
    return '200 OK', output.encode('utf-8')


def about_page(request, *args):
    output = framework.render(template_name="app/about.html")
    return '200 OK', output.encode('utf-8')


def contact_page(request, *args):
    if request['method'] == 'POST':
        body = framework.get_wsgi_input_data(request['env'])
        result = framework.parse_wsgi_input_data(body)
        print(result)
    output = framework.render(template_name="app/contact.html")
    return '200 OK', output.encode('utf-8')



