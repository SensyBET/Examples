from opcua import Client
from time import sleep

url = "opc.tcp://192.168.130.191:4840"
# url = "opc.tcp://192.168.82.245:4840"

NODES = []
# NODES.append('ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].measured_load')
NODES.append('ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].measured_load_tared')
# NODES.append('ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].tare_value')
# NODES.append('ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].unit')

# NODES.append('ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].loadCells[0].measured_force')
# NODES.append('ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].loadCells[1].measured_force')
# NODES.append('ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].loadCells[2].measured_force')
# NODES.append('ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].loadCells[3].measured_force')

# NODES.append('ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].loadCells[0].raw_value_mVV')
# NODES.append('ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].loadCells[1].raw_value_mVV')
# NODES.append('ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].loadCells[2].raw_value_mVV')
# NODES.append('ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].loadCells[3].raw_value_mVV')


client = Client(url)
client.connect()

#test_node = 'ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].set_tare'
#test_node = client.get_node(test_node)
#test_node.set_value(True)

while True:
    for NODE in NODES:
        node = client.get_node(NODE)
        value = node.get_data_value()

        print(value)
    sleep(1)
    

client.disconnect()
