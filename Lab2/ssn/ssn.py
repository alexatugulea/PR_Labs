class DiffieHellman(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_first = public_key1
        self.public_second = public_key2
        self.private_key = private_key
        self.all_key = None

    def for_partial_key(self):
        partial_key = self.public_first ** self.private_key
        partial_key = partial_key % self.public_second
        return partial_key

    def for_all_key(self, partial_key_r):
        all_key = partial_key_r ** self.private_key
        all_key = all_key % self.public_second
        self.all_key = all_key
        return all_key

    def encrypt_message(self, msg):
        encrypted_msg = ""
        key = self.all_key
        for c in msg:
            encrypted_msg += chr(ord(c) + key)
        return encrypted_msg

    def decrypt_message(self, encrypted_msg):
        decrypted_msg = ""
        key = self.all_key
        for c in encrypted_msg:
            decrypted_msg += chr(ord(c) - key)
        return encrypted_msg


class Session:
    def __init__(self, tr, trans_handler, my_public, his_public, private, type, msg):
        self.encrypted = self.create.encrypt_message(msg)
        self.message = self.create.decrypt_message(self.tr.recv(self.trans_handler))
        self.msg = msg
        self.tr = tr
        self.trans_handler = trans_handler
        self.my_public = my_public
        self.private = private
        self.create = DiffieHellman(my_public, his_public, private)
        self.partial = self.create.for_partial_key()
        self.tr.give(self.trans_handler, str(self.partial))
        self.his_partial = int(self.tr.recv(self.trans_handler))
        self.full = self.create.for_all_key(self.his_partial)
        self.type = type

    def communicate(self, msg):
        if self.type == 'client':
            self.secure_give(msg)
            response = self.secureReceive()
            return response
        else:
            response = self.secure_get()
            self.secure_give(msg)
            return response


    def secure_give(self, msg):
        self.tr.give(self.trans_handler, msg)

    def secure_get(self):
        return self.message




