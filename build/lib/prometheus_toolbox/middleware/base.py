from abc import ABC, abstractmethod


class BaseMonitoringMiddleware(ABC):

    @abstractmethod
    def process_request(self, request):
        """Method that should process request."""

    @abstractmethod
    def process_response(self, response):
        """Method that should process response."""

    @abstractmethod
    def process_exception(self, request, exception):
        """Method that should process exception."""
