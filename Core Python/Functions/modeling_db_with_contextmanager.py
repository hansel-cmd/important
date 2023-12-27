import contextlib

class Connection:

    def __init__(self):
        self.id = 0

    def _start_transaction(self):
        print("Starting transaction", self.id)
        id = self.id
        self.id += 1
        return id
    
    def _commit_transaction(self, id):
        print("Committing transaction", id)
    
    def _rollback_transaction(self, id):
        print("Rolling back transaction", id)

class Transaction:

    def __init__(self, conn):
        self.conn = conn
        self.id = conn._start_transaction()

    def commit(self):
        self.conn._commit_transaction(self.id)

    def rollback(self):
        self.conn._rollback_transaction(self.id)



@contextlib.contextmanager
def generator_cm(connection):
    transaction = Transaction(connection)

    try:
        yield
    except ValueError:
        transaction.rollback()
        raise

    transaction.commit()


my_connection = Connection()
try:
    with generator_cm(my_connection):
        raise ValueError()
except ValueError:
    print("Oops! Something went wrong.")