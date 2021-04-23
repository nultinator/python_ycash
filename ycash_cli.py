from bitcoinrpc.authproxy import AuthServiceProxy
user = input("user: ")
password = input("password: ")
port = input("port: ")
access = AuthServiceProxy("http://" + user + ":" + password + "@127.0.0.1:" + port)
getblockchaininfo = access.getblockchaininfo()
getnewaddress = access.getnewaddress()
getbestblockhash = access.getbestblockhash()
