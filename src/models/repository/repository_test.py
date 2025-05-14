import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {
        "client": "Celina",
        "cupom": False,
        "items": {
            "hamburguer": {"tipo":"meg-90", "quantidade":1},
            "bebida": {"tipo":"coca-cola", "quantidade":1}
        },
        "status": "Entregue",
        "pagamento": "pix",
        "preco": 40.90
    }
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_insert_list_of_document():
    orders_repository = OrdersRepository(conn)
    my_doc = [{ "elem1": "aqui1" }, { "elem2": "aqui2" }, { "elem3": "aqui3" }]
    orders_repository.insert_list_of_documents(my_doc)
