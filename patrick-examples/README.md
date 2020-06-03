# DA.Tute.OPC-UA

## Setup

Python enviro
- Setup a python environment
  - Easiest way is Anaconda https://www.anaconda.com/products/individual
    - Full Anaconda includes Python, pandas stack, and the kitchen sink
    - If you want a minimal enviro, probably better to setup miniconda and use `conda` to install python packages you want
- To isolate enviro I used and created a conda env
  - for the server: `conda create --name asyncopuca python=3.7 anaconda` 
    - note this installs all anaconda libs in enviro. You may want to ommit anaconda and just install dependencies as needed.
  - for client : `conda create --name asyncopuca python=3.7 opcuaclient` 
    - but this is a bit of overkill, you could just use the one enviro
    - **make sure you are running python<=3.7 if you want to use the graphing capability or you will run into issues**
- Another option would be to use Docker containers, but these examples and self-contained python so conda probably easier
- Still another option is to use WSL/WSL2 on windows 10.
  - You can install Anaconda here and get all the linux goodness, however doesn't add much benefit for simple examples

Install python opcua server and run minimal example
- activate your conda env in a terminal `conda activate asyncopcua`
- install lib `pip install asyncua`
- run server with
  - `python minimal-server/async-server.py`
- this will spin up a server on `opc.tcp://localhost:4840`
- you will need to open another terminal to run the client from

Install python opcua client and run minimal client
- open antoher terminal and `conda activate opcuaclient`
- `pip install opcua-client`
- for graphing `pip install pyqtgraph`
  - **make sure you are running python<=3.7 if you want to use the graphing capability or you will run into issues**
  - I haven't found this very useful
- then run `opcua-client` at command line
- make sure you have a server runnng and add `opc.tcp://localhost:4840` and you will connect to the OPC UA server and can read all the nodes

## Examples

In the `examples` folder there a subfolders with other examples

- These will have `README.md` that explain the example
- Run through adding nodes etc

