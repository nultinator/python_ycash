# python_ycash
A python3 native Ycash/Zcash rpc client


This is forked from bitcoinrpc. Fully functional commands are listed inside of ycash_cli.py.
Most commands (including "z" commands) do execute, but at the moment only return an object similar to this:
<bitcoinrpc.authproxy.AuthServiceProxy object at 0x7f00abe670d0>
Any pointers as to how to read these objects would be greatly appreciated.

All that being said, to use this script, simply run ycash_cli.py inside of your python3 interpreter after downloading the package.
If running properly, the interpreter should ask you to input "user", "password", and "port." These refer to your rpcusername,rpcpassword, and rpcport.
The interpreter then remembers these inputs as objects until the script is killed (so you only have to sign in once per session).
Unlisted commands may be executed in the form of access.your_command_here, for example access.z_gettotalbalance.
If you receive an error for a command, try to run it again as a function, access.z_gettotalbalance().
