from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict

class CustomPagination(pagination.LimitOffsetPagination):

    default_limit = 2
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 50


    def get_paginated_response(self, data):
        return Response(OrderedDict({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            "pagination": {
                "count": self.count,
                "offset": self.offset,
                "limit": self.limit
            },
            'results': data
        }))