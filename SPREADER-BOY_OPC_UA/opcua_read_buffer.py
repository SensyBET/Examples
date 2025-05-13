from opcua import Client
from time import sleep
from collections import deque

BUFFER = deque([])

add_to_buffer = True # Buffer boolean
def buffer_storage(value):
    """Store value only during lift"""
    float_value = value.Value.Value # Get only the float value from the OPC object
    if float_value > 1: # If we lift more than 1T
        if add_to_buffer == False:
            if BUFFER[0].Value.Value < float_value:
                BUFFER[0] = value
            return False # Don't add to buffer
        else: 
            BUFFER.appendleft(value)
            if len(BUFFER) > 5: # Limit buffer to 5
                BUFFER.pop()    
            return False # Don't add to buffer
    else: 
        return True

        
# url = "opc.tcp://192.168.130.191:4840"
url = "opc.tcp://192.168.82.245:4840"

NODES = []
# NODES.append('ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].measured_load')
NODES.append('ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].measured_load_tared')

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
        add_to_buffer = buffer_storage(value)
        
        print(f"Current value :{value}")

        try : print(f"Last value :{BUFFER[0]}") # Print buffer if exist
        except : pass
        
        # print(BUFFER) # Uncomment to print the full buffer
        
    sleep(1)
    
client.disconnect()


