import trp.trp as tr
import app.app as application
import sys


if __name__ == "__main__":
    public_2 = 197
    public_1 = 151
    private_1 = 157
    trans_handler = tr.socket()
    tr.connect_to(trans_handler, "127.0.0.1", int(sys.argv[1]))

    app = application.App(tr, trans_handler, public_1, public_2, private_1, 'client', "message")
    app.transfer("Is working")
    message = app.transfer()

    msg = tr.recv(trans_handler)
    print(msg)

    tr.give(trans_handler, " UDP Server is working.")
    msg_new = tr.recv(trans_handler)
    print(msg_new)
