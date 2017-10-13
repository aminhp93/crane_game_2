from rest_framework.views import exception_handler

def customer_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code
        if response.status_code == 400:
            response.data['detail'] = "You were hacked"

        if response.status_code == 401:
            response.data['detail'] = "You were hacked"

        if response.status_code == 404:
            response.data['detail'] = "page not found"

        if response.status_code == 405:
            response.data['detail'] = "Error 405"
    
    return response