from datetime import datetime
from src.models.repository.interface.orders_repository import OrdersRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_reponse import HttpResponse
from src.validators.registry_order_validator import registry_order_validator
from src.errors.error_handler import error_handler

class RegistryOrder:
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            self.__validate_body(body)

            new_order = self.__format_new_order(body)
            self.__registry_order(new_order)

            return self.__format_response()
        except Exception as exception:
            return error_handler(exception)

    def __validate_body(self, body: dict) -> None:
        registry_order_validator(body)

    def __format_new_order(self, body: dict) -> dict:
        new_order = body["data"]
        new_order = { **new_order, "created_at": datetime.now() }
        return new_order

    def __registry_order(self, new_order: dict) -> None:
        self.__orders_repository.insert_document(new_order)

    def __format_response(self) -> dict:
        return HttpResponse(
            body={
                "data": {
                    "type": "Order",
                    "count": 1,
                    "registry": True
                }
            },
            status_code=201
        )
