import json
import requests

from django.shortcuts import render


URL = "https://gist.githubusercontent.com/chancock09/6d2a5a4436dcd488b8287f3e3e4fc73d/raw/" + \
      "fa47d64c6d5fc860fabd3033a1a4e3c59336324e/employees.json"


def list_employees(request):
    """List all employees"""
    try:
        res = requests.get(URL)
        employees_data = json.loads(res.text)
        context = {"employees_data": employees_data}
        return render(request, "index.html", context)
    except ConnectionError:
        return render(request, "index.html", {"error_message": "Something went wrong :/"})
