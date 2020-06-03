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
        
        
        folder = client.get_node("ns=2;i=3007")     
        print("My variable", folder)#, await var.read_value())   
        results = await client.delete_nodes([folder])

        folder = client.get_node("ns=2;i=30007")     
        print("My variable", folder)#, await var.read_value())   
        results = await client.delete_nodes([folder])


if __name__ == '__main__':
    asyncio.run(main())
