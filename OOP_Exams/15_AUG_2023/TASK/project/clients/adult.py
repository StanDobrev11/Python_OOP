from project.clients.base_client import BaseClient


class Adult(BaseClient):

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, 4.0)
