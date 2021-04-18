from bitcoinrpc.authproxy import AuthServiceProxy
user = input("user: ")
password = input("password: ")
access = AuthServiceProxy("http://" + user + ":" + password + "@127.0.0.1:8832")
getblockchaininfo = access.getblockchaininfo()
getnewaddress = access.getnewaddress()
getbestblockhash = access.getbestblockhash()
