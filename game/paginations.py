from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page'
    max_page_size = 10000

