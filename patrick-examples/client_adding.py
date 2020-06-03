import asyncio
import sys
sys.path.insert(0, "..")
import logging
from asyncua import Client, Node, ua

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger('asyncua')


async def main():
    # url = 'opc.tcp://localhost:4840/freeopcua/server/'

    url = "opc.tcp://admin@localhost:4840/freeopcua/server/"
    # url = 'opc.tcp://commsvr.com:51234/UA/CAS_UA_Server'
    async with Client(url=url) as client:
        
        
        var = await client.nodes.root.get_child(["0:Objects"])     
        print("My variable", var)#, await var.read_value())   

        folder = await var.add_folder("ns=2;i=30007", "2:Folder1")
        var = await folder.add_variable("ns=2;i=30008", "2:Variable1", 3.45)
        # # Now getting a variable node using its browse path
        # await var.write_value(9.89) # just to check it works

        # results = client.delete_nodes([folder, var])
        # try:
        #     #var.write_value(9.89) # just to check it does not work
        #     var.read_browse_name()
        # except ua.UaStatusCodeError:
        #     print("The variable has been removed OK")


if __name__ == '__main__':
    asyncio.run(main())
