import encodings
import json



def api_students(request):
    with open("data.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
    return '200 OK', json.dumps({'students': data['students']}, indent=4).encode("UTF-8")



def api_courses(request):
    with open("data.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
    return '200 OK', json.dumps({'courses': data['courses']}, indent=4).encode("UTF-8")


def api_categories(request):
    with open("data.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
    return '200 OK', json.dumps({'categories': data['categories']}, indent=4).encode("UTF-8")
