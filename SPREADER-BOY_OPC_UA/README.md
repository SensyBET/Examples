
# Containers (0-1)
## Attributs

* **measured_load** : REAL; // Sum of all sensors weight
* **measured_load_tared** : REAL; // Sum of all sensors - tare
* **tare_value** : REAL; // Tare value of the whole system

* **LoadCell** : Load cell objects (0-3)

## Loadcell attributs
* **raw_value_mVV** : REAL; // Sensor value mV/V
* **measured_weight** : REAL; // Sensor value in unit


# Example of OPC-UA object request :

	GVL_Input.containers[0].loadCells[0].measured_force


GVL_Input.containers[0] <- From object container 1

.loadCells[0] <- From loadcell 1 of container 1

.measured_force <- Get measured force


A full request may look like :

	'ns=4;s=|var|ecomatDisplay/4.3"/STD./E.Application.GVL_Input.containers[0].measured_load_tared'

Check UAEXPERT for more details:
https://www.unified-automation.com/index.html
