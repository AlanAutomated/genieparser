| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 3.1.17        |

--------------------------------------------------------------------------------
                                    FEATURE
--------------------------------------------------------------------------------
* Added the new `get_parser` feature

--------------------------------------------------------------------------------
                                    BGP
--------------------------------------------------------------------------------
* IOSXE
    * Fixed ShowBgpAllDetail and ShowBgpAllNeighbors in IOSXE to cover all types of vrf(s) and next_hop(s)

--------------------------------------------------------------------------------
                                    NTP
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowRunningConfigNtp for 'show running-config ntp'

--------------------------------------------------------------------------------
                                    INTERFACE
--------------------------------------------------------------------------------
* NXOS
  * Fixed show_interface - ShowInterfaceSwitchport

* IOSXR
  * Fixed parser 'show interface detail' to support non utf8 characters

--------------------------------------------------------------------------------
                                    OSPF
--------------------------------------------------------------------------------
* NXOS
    * Fixed ShowIpOspfInterface and ShowIpOspfDatabaseOpaqueAreaDetail to cover N7K output differences

--------------------------------------------------------------------------------
                                    HSRP
--------------------------------------------------------------------------------
* NXOS
    * Fixed ShowHsrpAll to cover N7K output differences