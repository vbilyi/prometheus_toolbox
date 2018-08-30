# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class BaseMetricsMiddleware(ABC):

    @abstractmethod
    def process_request(self, request):
        """Method that should process request."""
        raise NotImplemented

    @abstractmethod
    def process_response(self, request, response):
        """Method that should process response."""
        raise NotImplemented

    @abstractmethod
    def process_exception(self, request, exception):
        """Method that should process exception."""
        raise NotImplemented
