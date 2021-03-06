from blockchain.blockchain import Blockchain

from unittest.mock import Mock

class MockBlockchain(Blockchain):

    def __str__(self):
        return "MockBlockChain"

    def create_payment_request(self, amount):
        return {
                "address"   : "ADDRESS_FOR_PAYMENT",
                "token_amount_cent" : amount,
                "provider" : "blockchain",
                "timeout" : 3000,
                }

    def get_connection_info(self):
        return None

    def get_available_balance(self):
        return 100

    def get_identity(self):
        return "id"

    def initiate_payment(self, connection_data, amount, payment_id):
        return Mock()

    def list_transactions(self):
        return list()

    def payment_request_status(self, payment_id):
        return "done"

    def register_with_identity(self):
        pass

    def attempt_payment_done(self, id):
        return ""
