from rest_framework.decorators import api_view
from rest_framework.exceptions import (
        APIException, 
        NotFound, 
        ParseError, 
        PermissionDenied
    )

@api_view()
def error400(request):
    raise ParseError('Bad request')

@api_view()
def error403(request):
    raise PermissionDenied('PermissionDenied')

@api_view()
def error404(request):
    raise NotFound('Not found')

@api_view()
def error500(request):
    raise APIException(detail='Server error')
