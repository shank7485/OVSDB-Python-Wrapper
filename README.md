Python Wrapper to Query and retrive fields from the OVSDB schema of OpenVSwitch

==============================================================================

The OVSDB server needs to be listening for incoming connections. This came be done with the following:

ovs-appctl -t ovsdb-server ovsdb-server/add-remote ptcp:6640

Here, ptcp means passive. 

==============================================================================

The default name of OVSDB schema is 'Open_vSwitch'

Run test.py to get back JSONs.

  
