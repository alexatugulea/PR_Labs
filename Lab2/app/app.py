import ssn.ssn as session


class App:
    def __init__(self,s tr, trans_handler, public_1, public_2, private, type, msg):
        self.session = session.Session(tr, trans_handler, public_1, public_2, private, type, msg)

    def give(self, msg):
        self.session.secure_give(msg)

    def get(self):
        return self.session.secure_get()

    def transfer(self, msg):
        self.session.transfer(msg)
