from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ArticleAPIListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20

    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'total_objects': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'previous_page_number': self.previous_page_number(),
            'current_page_number': self.page.number,
            'next_page_number': self.next_page_number(),
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

    def previous_page_number(self):
        current_page_number = self.page.number

        if current_page_number > 1:
            return current_page_number - 1
        return None

    def next_page_number(self):
        current_page_number = self.page.number
        total_pages = self.page.paginator.num_pages

        if total_pages > current_page_number:
            return current_page_number + 1
        return None
