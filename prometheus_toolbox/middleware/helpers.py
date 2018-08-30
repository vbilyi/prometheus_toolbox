# -*- coding: utf-8 -*-


def get_method_name(request):
    m = request.method
    if m not in ('GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE',
                 'OPTIONS', 'CONNECT', 'PATCH'):
        return '<invalid method>'
    return m