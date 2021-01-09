import trp.trp as tr
from trp.trp import App
import sys


if __name__ == "__main__":
    server_main = tr.server_socket("127.0.0.1", int(sys.argv[1]))
    tr.recv(server_main)
     = 197
    public_2 = 151
    public_1 = 199

    app = App(tr, server_main, public_1, public_2, public_1, 'server')
    app.transfer("Message for UDP Client")

    tr.give(server_main, "Is working")
    msg_new = tr.recv(server_main)
    print(msg_new)


