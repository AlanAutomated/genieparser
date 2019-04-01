| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 19.0.2        |

--------------------------------------------------------------------------------
                                   BGP
--------------------------------------------------------------------------------
* IOSXE
    * Added parsers for:
        * 'show bgp all'
        * 'show bgp {address_family} all'
        * 'show bgp {address_family} rd {rd}'
        * 'show bgp {address_family} vrf {vrf}'
        * 'show ip bgp all'
        * 'show ip bgp {address_family} all'
        * 'show ip bgp'
        * 'show ip bgp {address_family}'
        * 'show ip bgp {address_family} rd {rd}'
        * 'show ip bgp {address_family} vrf {vrf}'
        * 'show bgp all detail'
        * 'show ip bgp all detail'
        * 'show bgp {address_family} vrf {vrf} detail'
        * 'show bgp {address_family} rd {rd} detail'
        * 'show ip bgp {address_family} vrf {vrf} detail'
        * 'show ip bgp {address_family} rd {rd} detail'
        * 'show bgp summary'
        * 'show bgp {address_family} summary'
        * 'show bgp {address_family} vrf {vrf} summary'
        * 'show bgp {address_family} rd {rd} summary'
        * 'show bgp all summary'
        * 'show bgp {address_family} all summary'
        * 'show ip bgp summary'
        * 'show ip bgp {address_family} summary'
        * 'show ip bgp {address_family} vrf {vrf} summary'
        * 'show ip bgp {address_family} rd {rd} summary'
        * 'show ip bgp all summary'
        * 'show ip bgp {address_family} all summary'
        * 'show bgp all neighbors'
        * 'show bgp all neighbors {neighbor}'
        * 'show bgp {address_family} all neighbors'
        * 'show bgp {address_family} all neighbors {neighbor}'
        * 'show bgp neighbors'
        * 'show bgp neighbors {neighbor}'
        * 'show bgp {address_family} neighbors'
        * 'show bgp {address_family} neighbors {neighbor}'
        * 'show bgp {address_family} vrf {vrf} neighbors'
        * 'show bgp {address_family} vrf {vrf} neighbors {neighbor}'
        * 'show ip bgp all neighbors',
        * 'show ip bgp all neighbors {neighbor}'
        * 'show ip bgp {address_family} all neighbors'
        * 'show ip bgp {address_family} all neighbors {neighbor}'
        * 'show ip bgp neighbors'
        * 'show ip bgp neighbors {neighbor}'
        * 'show ip bgp {address_family} neighbors'
        * 'show ip bgp {address_family} neighbors {neighbor}'
        * 'show ip bgp {address_family} vrf {vrf} neighbors'
        * 'show ip bgp {address_family} vrf {vrf} neighbors {neighbor}'
        * 'show bgp all neighbors {neighbor} advertised-routes'
        * 'show bgp {address_family} all neighbors {neighbor} advertised-routes'
        * 'show bgp neighbors {neighbor} advertised-routes'
        * 'show bgp {address_family} neighbors {neighbor} advertised-routes'
        * 'show ip bgp all neighbors {neighbor} advertised-routes'
        * 'show ip bgp {address_family} all neighbors {neighbor} advertised-routes'
        * 'show ip bgp neighbors {neighbor} advertised-routes'
        * 'show ip bgp {address_family} neighbors {neighbor} advertised-routes'
        * 'show bgp all neighbors {neighbor} received-routes'
        * 'show bgp {address_family} all neighbors {neighbor} received-routes'
        * 'show bgp neighbors {neighbor} received-routes'
        * 'show bgp {address_family} neighbors {neighbor} received-routes'
        * 'show ip bgp all neighbors {neighbor} received-routes'
        * 'show ip bgp {address_family} all neighbors {neighbor} received-routes'
        * 'show ip bgp neighbors {neighbor} received-routes'
        * 'show ip bgp {address_family} neighbors {neighbor} received-routes'
        * 'show bgp all neighbors {neighbor} routes'
        * 'show bgp {address_family} all neighbors {neighbor} routes'
        * 'show bgp neighbors {neighbor} routes'
        * 'show bgp {address_family} neighbors {neighbor} routes'
        * 'show ip bgp all neighbors {neighbor} routes'
        * 'show ip bgp {address_family} all neighbors {neighbor} routes'
        * 'show ip bgp neighbors {neighbor} routes'
        * 'show ip bgp {address_family} neighbors {neighbor} routes'

--------------------------------------------------------------------------------
                                   POLICY MAP
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowPolicyMapControlPlane Parser for:
       'show policy map control plane'

--------------------------------------------------------------------------------
                                   MONITOR
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowMonitor Parser for:
       'show monitor'
       'show monitor session all'
       'show monitor session {session}'
       'show monitor capture'


--------------------------------------------------------------------------------
                                   OSPF
--------------------------------------------------------------------------------
* IOSXE
    * Added parsers:
        * ShowIpOspfDatabase
        * ShowIpOspfMaxMetric
        * ShowIpOspfTraffic
    * Updated parsers:
        * ShowIpOspfMplsLdpInterface
        * ShowIpOspfDatabaseRouter
        * ShowIpOspfDatabaseExternal
        * ShowIpOspfDatabaseNetwork
        * ShowIpOspfDatabaseSummary
        * ShowIpOspfDatabaseOpaqueArea

--------------------------------------------------------------------------------
                                   SNMP
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowSnmpMib for:
        'show snmp mib'

--------------------------------------------------------------------------------
                                   PLATFORM
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowPlatformHardwarePlim for;
        'show platform hardware port {x/x/x} plim statistics'
        'show platform hardware slot {x} plim statistics'
        'show platform hardware slot {x} plim statistics internal'
        'show platform hardware subslot {x/x} plim statistics'
    * Add ShowPlatformHardware for 'show platform hardware qfp active infrastructure bqs queue output default all'
    * Add ShowVersionRp for;
        show version RP active running
        show version RP active installed
        show version RP active provisioned
        show version RP standby running
        show version RP standby installed
        show version RP standby provisioned
    * Add ShowPlatformPower for 'show platform power'
    * Add ShowPlatformHardwareQfpBqsOpmMapping for;
        show platform hardware qfp active bqs {x} opm mapping
        show platform hardware qfp standby bqs {x} opm mapping
    * Add ShowPlatformHardwareQfpBqsIpmMapping for;
        show platform hardware qfp active bqs {x} ipm mapping
        show platform hardware qfp standby bqs {x} ipm mapping
    * Add ShowPlatformHardwareQfpInterfaceIfnameStatistics for;
        show platform hardware qfp active interface if-name {interface} statistics
        show platform hardware qfp standby interface if-name {interface} statistics
    * Add ShowPlatformHardwareQfpStatisticsDrop for;
            show platform hardware qfp active statistics drop
            show platform hardware qfp standby statistics drop
    * Add ShowPlatformHardwareSerdes for 'show platform hardware slot {x} serdes statistics'
    * Add ShowPlatformHardwareSerdesInternal for 'show platform hardware slot {x} serdes statistics internal'
    * Add ShowProcessesCpuHistory for 'show processes cpu history'
    * Add ShowPlatformHardwareQfpBqsStatisticsChannelAll for:
        show platform hardware qfp active bqs {x} ipm statistics channel all
        show platform hardware qfp standby bqs {x} ipm statistics channel all
        show platform hardware qfp active bqs {x} opm statistics channel all
        show platform hardware qfp standby bqs {x} opm statistics channel all

    * Update ShowVersion to support more output

*IOS
    * Add ShowProcessesCpu for:
        show processes cpu
        show processes cpu | include {WORD}
    * Add ShowVersionRp for:
        show version RP active [running|provisioned|installed]
        show version RP standby [running|provisioned|installed]
    * Add ShowPlatform for:
        show platform
    * Add ShowPlatformPower for:
        show platform power
    * Add ShowProcessesCpuHistory for:
        show processes cpu history
    * Add ShowProcessesCpuPlatform for:
        show processes cpu platform
    * Add ShowPlatformSoftwareStatusControl for:
        show platform software status control-processor brief
    * Add ShowPlatformSoftwareSlotActiveMonitorMem for:
        show platform software process slot switch active R0 monitor | inc Mem :|Swap:
    * Add ShowPlatformHardware for:
        show platform hardware qfp active infrastructure bqs queue output default all
    * Add ShowPlatformHardwarePlim for:
        show platform hardware port {x/x/x} plim statistics
        show platform hardware slot {x} plim statistics
        show platform hardware slot {x} plim statistics internal
        show platform hardware subslot {x/x} plim statistics
    * Add ShowPlatformHardwareQfpBqsOpmMapping for:
        show platform hardware qfp active bqs {x} opm mapping
        show platform hardware qfp standby bqs {x} opm mapping
    * Add ShowPlatformHardwareQfpBqsIpmMapping for:
        show platform hardware qfp active bqs {x} ipm mapping
        show platform hardware qfp standby bqs {x} ipm mapping
    * Add ShowPlatformHardwareSerdes for:
        show platform hardware slot {x} serdes statistics
    * Add ShowPlatformHardwareSerdesInternal for:
        show platform hardware slot {x} serdes statistics internal
    * Add ShowPlatformHardwareQfpBqsStatisticsChannelAll for:
        show platform hardware qfp active bqs {x} ipm statistics channel all
        show platform hardware qfp standby bqs {x} ipm statistics channel all
        show platform hardware qfp active bqs {x} opm statistics channel all
        show platform hardware qfp standby bqs {x} opm statistics channel all
    * Add ShowPlatformHardwareQfpInterfaceIfnameStatistics for:
        show platform hardware qfp active interface if-name {interface} statistics
        show platform hardware qfp standby interface if-name {interface} statistics
    * Add ShowPlatformHardwareQfpStatisticsDrop for:
        show platform hardware qfp active statistics drop
        show platform hardware qfp standby statistics drop
* IOSXR
    * Add ShowInstallInactiveSummary for:
          show install inactive summary
    * Add ShowInstallCommitSummary for:
          show install commit summary
--------------------------------------------------------------------------------
                                   MPLS LDP
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowMplsLdpParameters for:
          show mpls ldp parameters
    * Add ShowMplsLdpNsrStatistic for:
          show mpls ldp nsr statistics
    * Add ShowMplsLdpNeighbor for:
          show mpls ldp neighbor
          show mpls ldp neighbor vrf {vrf}
    * Add ShowMplsLdpNeighborDetail for:
          show mpls ldp neighbor detail
          show mpls ldp neighbor vrf {vrf} detail
    * Add ShowMplsLdpBindings for:
          show mpls ldp bindings
          show mpls ldp bindings all
          show mpls ldp bindings all detail
    * Add ShowMplsLdpCapabilities for:
          show mpls ldp capabilities
          show mpls ldp capabilities all
    * Add ShowMplsLdpDiscovery for:
          show mpls ldp discovery
          show mpls ldp discovery detail
          show mpls ldp discovery all
          show mpls ldp discovery all detail
          show mpls ldp discovery vrf {vrf}
          show mpls ldp discovery vrf {vrf} detail
    * Add ShowMplsLdpIgpSync for:
          show mpls ldp igp sync
          show mpls ldp igp sync all
          show mpls ldp igp sync interface {interface}
          show mpls ldp igp sync vrf {vrf}
    * Add ShowMplsForwardingTable for:
          show mpls forwarding-table
          show mpls forwarding-table detail
          show mpls forwarding-table vrf {vrf}
          show mpls forwarding-table vrf {vrf} detail
    * Add ShowMplsInterface for:
          show mpls interfaces
          show mpls interfaces {interface}
          show mpls interfaces {interface} detail
          show mpls interfaces detail
    * Add ShowMplsL2TransportDetail for:
          show mpls l2transport vc detail
* IOS
    * Add ShowMplsL2TransportDetail for:
          show mpls l2transport vc detail
* IOSXR
    * Add ShowMplsLdpNeighborBrief for:
          show mpls ldp neighbor brief
---------------------------------------------------------------------------------
                                   BFD 
---------------------------------------------------------------------------------
* IOSXE
    * Add ShowBfdNeighborsDetails for:
        show bfd neighbors client {client} details
        show bfd neighbors details
----------------------------------------------------------------------------------
                                   ARP
----------------------------------------------------------------------------------
* IOSXE
    * Add ShowArpApplication for:
        show arp application
    * Add ShowArpSummary for:
        show arp summary
--------------------------------------------------------------------------------
                                   QOS
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowServiceGroupState for:
        show service-group state
    * Add ShowServiceGroupStats for:
        show service-group stats
    * Add ShowServiceGroupTrafficStats for:
        show service-group traffic-stats
        show service-group traffic-stats {group}
* IOS
    * Add ShowServiceGroupState for:
        show service-group state
    * Add ShowServiceGroupStats for:
        show service-group stats
--------------------------------------------------------------------------------
                                   CONFIG
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowArchiveConfigDifferences for:
        show archive config differences
        show archive config differences {fileA} {fileB}
        show archive config differences {fielA}
    * Add ShowArchiveConfigIncrementalDiffs for:
        show archive config incremental-diffs {fileA}
    * Add ShowConfigurationLock for:
        show configuration lock
* IOS
    * Add ShowArchiveConfigDifferences for:
        show archive config differences
        show archive config differences {fileA} {fileB}
        show archive config differences {fielA}
    * Add ShowArchiveConfigIncrementalDiffs for:
        show archive config incremental-diffs {fileA}
    * Add ShowConfigurationLock for:
        show configuration lock
--------------------------------------------------------------------------------
                                   L2VPN
--------------------------------------------------------------------------------
* IOSXE & IOS
    * Add ShowBridgeDomain for:
            show bridge-domain
            show bridge-domain {WORD}
            show bridge-domain | count {WORD}
    * Add ShowEthernetServiceInstanceDetail for:
            show ethernet service instance detail
            show ethernet service instance interface {interface} detail
    * Add ShowEthernetServiceInstanceStats for:
            show ethernet service instance stats
            show ethernet service instance interface {interface} stats
    * Add ShowEthernetServiceInstanceSummary for:
            show ethernet service instance summary
    * Add ShowL2vpnVfi for:
            show l2vpn vfi
    * Add ShowL2vpnServiceAll for:
            show l2vpn service all
--------------------------------------------------------------------------------
                                   LAG
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowEtherChannelLoadBalancing for:
        show etherchannel load-balancing
    * Add ShowLacpNeighborDetail for:
        show lacp neighbor detail
    * Fix for ShowPagpInternal
--------------------------------------------------------------------------------
                                   INTERFACE
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowInterfaceStats for:
        show interface {interface} stats
        show interface stats
    * Update ShowIpInterface to support more output
    * Update ShowIpInterfaceBrief for cli_command
----------------------------------------------------------------------------------
                                 NTP
----------------------------------------------------------------------------------
* IOSXE
    * Add ShowNtpAssociationsDetail for:
        show ntp associations detail
* IOS
    * Add ShowNtpAssociationsDetail for:
        show ntp associations detail
--------------------------------------------------------------------------------
                                   ISIS
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowIsisAdjacency for:
        show isis adjacency
    * Add ShowIsisNeighborsSchema for:
        show run isis neighbors
--------------------------------------------------------------------------------
                                   MRIB
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowMribVrfRouteSummary for:
        show mrib vrf {vrf} {address-family} route summary
--------------------------------------------------------------------------------
                                   RUNNING-CONFIG
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowRunKeyChain for:
        show run key chain
    * Add ShowRunRouterIsis for:
        show run router isis
--------------------------------------------------------------------------------
                                   ROUTING
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowIpRoute for different output
--------------------------------------------------------------------------------
                                   PROTOCOLS
--------------------------------------------------------------------------------
* IOSXE
    * Fix for ShowIpProtocols
--------------------------------------------------------------------------------
                                   RIP
--------------------------------------------------------------------------------
* IOSXE
    * Fix for ShowIpv6Rip