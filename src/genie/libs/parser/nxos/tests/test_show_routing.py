# Python
import unittest
from unittest.mock import Mock

# Ats
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# nxos show_routing
from genie.libs.parser.nxos.show_routing import ShowRoutingVrfAll, ShowRoutingIpv6VrfAll,\
                                     ShowIpRoute, ShowIpv6Route

# =====================================
#  Unit test for 'show routing vrf all'
# =====================================

class test_show_routing_vrf_all(unittest.TestCase):
    
    '''Unit test for show routing vrf all'''
    
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'vrf':
            {'VRF1':
                {'address_family':
                    {'vpnv4 unicast':
                        {'bgp_distance_internal_as': 33,
                        'bgp_distance_local': 55,
                        'ip':
                            {'10.121.0.0/8':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'Null0':
                                                {'protocol':
                                                    {'bgp':
                                                        {'uptime': '5w0d',
                                                        'preference': '55',
                                                        'metric': '0',
                                                        'protocol_id': '100',
                                                        'attribute': 'discard',
                                                        'tag': '100'}}}}}}},
                            '10.205.0.1/32':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'attach': 'attached',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'10.205.0.1':
                                                {'protocol':
                                                    {'local':
                                                        {'uptime': '2w6d',
                                                        'interface': 'Bdi1255',
                                                        'preference': '0',
                                                        'metric': '0'}}}}}}},
                            '10.189.1.0/24':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'10.55.130.3':
                                                {'protocol':
                                                    {'bgp':
                                                        {'uptime': '3d10h',
                                                        'preference': '33',
                                                        'metric': '0',
                                                        'protocol_id': '1',
                                                        'attribute': 'internal',
                                                        'tag': '1',
                                                        'evpn': True,
                                                        'segid': 50051,
                                                        'route_table': 'default',
                                                        'tunnelid': '0x64008203',
                                                        'encap': 'vxlan'}}}}}}},
                            '10.21.33.33/32':
                                {'ubest_num': '1',
                                'mbest_num': '1',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'10.36.3.3':
                                                {'protocol':
                                                    {'bgp':
                                                        {'uptime': '5w0d',
                                                        'preference': '33',
                                                        'metric': '0',
                                                        'protocol_id': '100',
                                                        'attribute': 'internal',
                                                        'route_table': 'default',
                                                        'mpls_vpn': True,
                                                        'tag': '100'}}}}},
                                    'multicast':
                                        {'nexthop':
                                            {'10.36.3.3':
                                                {'protocol':
                                                    {'bgp':
                                                        {'uptime': '5w0d',
                                                        'preference': '33',
                                                        'metric': '0',
                                                        'protocol_id': '100',
                                                        'attribute': 'internal',
                                                        'route_table': 'default',
                                                        'mpls_vpn': True,
                                                        'tag': '100'}}}}}}},
                            "10.16.2.2/32": {
                               "mbest_num": "0",
                               "ubest_num": "1",
                               "best_route": {
                                    "unicast": {
                                         "nexthop": {
                                              "10.2.4.2": {
                                                   "protocol": {
                                                        "ospf": {
                                                             "preference": "110",
                                                             "protocol_id": "1",
                                                             "uptime": "00:18:35",
                                                             "metric": "41",
                                                             "mpls": True,
                                                             "attribute": "intra",
                                                             "interface": "Ethernet2/4"}}}}}}},
                            "10.4.1.1/32": {
                               "mbest_num": "0",
                               "ubest_num": "2",
                               "best_route": {
                                    "unicast": {
                                         "nexthop": {
                                              "10.2.4.2": {
                                                   "protocol": {
                                                        "ospf": {
                                                             "preference": "110",
                                                             "protocol_id": "1",
                                                             "uptime": "00:18:35",
                                                             "metric": "81",
                                                             "mpls": True,
                                                             "attribute": "intra",
                                                             "interface": "Ethernet2/4"}}},
                                              "10.3.4.3": {
                                                   "protocol": {
                                                        "ospf": {
                                                             "preference": "110",
                                                             "protocol_id": "1",
                                                             "uptime": "00:18:35",
                                                             "metric": "81",
                                                             "mpls": True,
                                                             "attribute": "intra",
                                                             "interface": "Ethernet2/1"}}}}}}},
                            '10.229.11.11/32':
                                {'ubest_num': '2',
                                'mbest_num': '0',
                                'attach': 'attached',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'10.229.11.11':
                                                {'protocol':
                                                    {'local':
                                                        {'uptime': '5w4d',
                                                        'preference': '0',
                                                        'metric': '0',
                                                        'interface': 'Loopback1'},
                                                    'direct':
                                                        {'uptime': '5w4d',
                                                        'preference': '0',
                                                        'metric': '0',
                                                        'interface': 'Loopback1'}}}}}}}}}}},
            'default':
                {'address_family':
                    {'ipv4 unicast':
                        {'bgp_distance_extern_as': 20,
                        'bgp_distance_internal_as': 200,
                        'ip':
                            {'10.106.0.0/8':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'vrf default':
                                                {'protocol':
                                                    {'bgp':
                                                        {'uptime': '18:11:28',
                                                        'preference': '20',
                                                        'metric': '0',
                                                        'protocol_id': '333',
                                                        'attribute': 'external',
                                                        'tag': '333',
                                                        'interface': 'Null0'}}}}}}},
                            '10.16.1.0/24':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'fec1::1002':
                                                {'protocol':
                                                    {'bgp':
                                                        {'uptime': '15:57:39',
                                                        'preference': '200',
                                                        'metric': '4444',
                                                        'protocol_id': '333',
                                                        'attribute': 'internal',
                                                        'route_table': 'default',
                                                        'tag': '333',
                                                        'interface': 'Ethernet1/1'}}}}}}},
                            '10.106.0.5/8':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'Null0':
                                                {'protocol':
                                                    {'static':
                                                        {'uptime': '18:47:42',
                                                        'preference': '1',
                                                        'metric': '0'}}}}}}}}}}}}}

    golden_output = {'execute.return_value': '''
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        10.106.0.0/8, ubest/mbest: 1/0
            *via vrf default, Null0, [20/0], 18:11:28, bgp-333, external, tag 333
        10.16.1.0/24, ubest/mbest: 1/0
            *via fec1::1002%default, Eth1/1, [200/4444], 15:57:39, bgp-333, internal, tag 333
        10.106.0.5/8, ubest/mbest: 1/0
            *via Null0, [1/0], 18:47:42, static


        IP Route Table for VRF "management"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        IP Route Table for VRF "VRF1"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        10.121.0.0/8, ubest/mbest: 1/0
            *via Null0, [55/0], 5w0d, bgp-100, discard, tag 100
        10.205.0.1/32, ubest/mbest: 1/0 time, attached
            *via 10.205.0.1, Bdi1255, [0/0], 2w6d, local
        10.21.33.33/32, ubest/mbest: 1/1
            *via 10.36.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
            **via 10.36.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
        10.189.1.0/24, ubest/mbest: 1/0 time
            *via 10.55.130.3%default, [33/0], 3d10h, bgp-1, internal, tag 1 (evpn), segid: 50051 tunnelid: 0x64008203 encap: VXLAN
        10.229.11.11/32, ubest/mbest: 2/0, attached
            *via 10.229.11.11, Lo1, [0/0], 5w4d, local
            *via 10.229.11.11, Lo1, [0/0], 5w4d, direct
        10.4.1.1/32, ubest/mbest: 2/0
            *via 10.2.4.2, Eth2/4, [110/81], 00:18:35, ospf-1, intra (mpls)
            *via 10.3.4.3, Eth2/1, [110/81], 00:18:35, ospf-1, intra (mpls)
        10.16.2.2/32, ubest/mbest: 1/0
            *via 10.2.4.2, Eth2/4, [110/41], 00:18:35, ospf-1, intra (mpls)
        '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        bgp_obj = ShowRoutingVrfAll(device=self.device)
        parsed_output = bgp_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_obj = ShowRoutingVrfAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_obj.parse()

# ===========================================
#  Unit test for 'show routing ipv6  vrf all'
# ===========================================

class test_show_routing_ipv6_vrf_all(unittest.TestCase):
    
    '''Unit test for show routing ipv6  vrf all'''
    
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output_1 = {
        "vrf": {
            "default": {
               "address_family": {
                    "ipv6 unicast": {
                         "bgp_distance_internal_as": 200,
                         "ip": {
                              "2001:db8:1:1::1/128": {
                                   "attach": "attached",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "2001:db8:1:1::1": {
                                                       "protocol": {
                                                            "local": {
                                                                 "interface": "Ethernet1/1",
                                                                 "metric": "0",
                                                                 "uptime": "00:15:46",
                                                                 "preference": "0"}}}}}},
                                   "mbest_num": "0",
                                   "ubest_num": "1"
                              },
                              "2001:db8:1:1::/64": {
                                   "attach": "attached",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "2001:db8:1:1::1": {
                                                       "protocol": {
                                                            "direct": {
                                                                 "interface": "Ethernet1/1",
                                                                 "metric": "0",
                                                                 "uptime": "00:15:46",
                                                                 "preference": "0"}}}}}},
                                   "mbest_num": "0",
                                   "ubest_num": "1"
                              },
                              "2001:db8:2:2::2/128": {
                                   "attach": "attached",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "2001:db8:2:2::2": {
                                                       "protocol": {
                                                            "local": {
                                                                 "interface": "Ethernet1/1",
                                                                 "metric": "0",
                                                                 "tag": "222",
                                                                 "uptime": "00:15:46",
                                                                 "preference": "0"}}}}}},
                                   "mbest_num": "0",
                                   "ubest_num": "1"
                              },
                              "2001:db8::5054:ff:fed5:63f9/128": {
                                   "attach": "attached",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "2001:db8::5054:ff:fed5:63f9": {
                                                       "protocol": {
                                                            "local": {
                                                                 "interface": "Ethernet1/1",
                                                                 "metric": "0",
                                                                 "uptime": "00:15:46",
                                                                 "preference": "0"}}}}}},
                                   "mbest_num": "0",
                                   "ubest_num": "1"
                              },
                              "2001:db8::/64": {
                                   "attach": "attached",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "2001:db8::5054:ff:fed5:63f9": {
                                                       "protocol": {
                                                            "direct": {
                                                                 "interface": "Ethernet1/1",
                                                                 "metric": "0",
                                                                 "uptime": "00:15:46",
                                                                 "preference": "0"}}}}}},
                                   "mbest_num": "0",
                                   "ubest_num": "1"
                              },
                              "615:11:11::/64": {
                                   "mbest_num": "0",
                                   "ubest_num": "1",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "::ffff:10.4.1.1": {
                                                       "protocol": {
                                                            "bgp": {
                                                                 "uptime": "00:35:51",
                                                                 "tag": "200",
                                                                 "route_table": "default:IPv4",
                                                                 "attribute": "internal",
                                                                 "mpls": True,
                                                                 "metric": "2219",
                                                                 "preference": "200",
                                                                 "protocol_id": "100"}}}}}}},
                              "2001:db8:2:2::/64": {
                                   "attach": "attached",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "2001:db8:2:2::2": {
                                                       "protocol": {
                                                            "direct": {
                                                                 "interface": "Ethernet1/1",
                                                                 "metric": "0",
                                                                 "tag": "222",
                                                                 "uptime": "00:15:46",
                                                                 "preference": "0"}}}}}},
                                   "mbest_num": "0",
                                   "ubest_num": "1"}}}}},
            "VRF1": {
               "address_family": {
                    "vpnv6 unicast": {
                         "bgp_distance_internal_as": 200,
                         "ip": {
                              "615:11:11:1::/64": {
                                   "mbest_num": "0",
                                   "ubest_num": "1",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "::ffff:10.4.1.1": {
                                                       "protocol": {
                                                            "bgp": {
                                                                 "uptime": "00:35:51",
                                                                 "tag": "200",
                                                                 "mpls_vpn": True,
                                                                 "attribute": "internal",
                                                                 "route_table": "default:IPv4",
                                                                 "metric": "2219",
                                                                 "preference": "200",
                                                                 "protocol_id": "100"}}}}}}}}}}}}
    }

    golden_output_1 = {'execute.return_value': '''
        IPv6 Routing Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        2001:db8::/64, ubest/mbest: 1/0, attached
            *via 2001:db8::5054:ff:fed5:63f9, Eth1/1, [0/0], 00:15:46, direct, 
        2001:db8::5054:ff:fed5:63f9/128, ubest/mbest: 1/0, attached
            *via 2001:db8::5054:ff:fed5:63f9, Eth1/1, [0/0], 00:15:46, local
        2001:db8:1:1::/64, ubest/mbest: 1/0, attached
            *via 2001:db8:1:1::1, Eth1/1, [0/0], 00:15:46, direct, 
        2001:db8:1:1::1/128, ubest/mbest: 1/0, attached
            *via 2001:db8:1:1::1, Eth1/1, [0/0], 00:15:46, local
        2001:db8:2:2::/64, ubest/mbest: 1/0, attached
            *via 2001:db8:2:2::2, Eth1/1, [0/0], 00:15:46, direct, , tag 222
        2001:db8:2:2::2/128, ubest/mbest: 1/0, attached
            *via 2001:db8:2:2::2, Eth1/1, [0/0], 00:15:46, local, tag 222
        615:11:11::/64, ubest/mbest: 1/0
            *via ::ffff:10.4.1.1%default:IPv4, [200/2219], 00:35:51, bgp-100, internal, tag 200  (mpls)

        IPv6 Routing Table for VRF "VRF1"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        615:11:11:1::/64, ubest/mbest: 1/0
            *via ::ffff:10.4.1.1%default:IPv4, [200/2219], 00:35:51, bgp-100, internal, tag 200  (mpls-vpn)
        '''}

    golden_parsed_output_2 = {
        'vrf': {
            'otv-vrf139': {
                'address_family': {
                    'vpnv6 unicast': {
                        'ip': {
                            '2001:112:1:2b3::/64': {
                                'attach': 'attached',
                                'best_route': {
                                    'unicast': {
                                        'nexthop': {
                                            '2001:112:1:2b3::2': {
                                                'protocol': {
                                                    'direct': {
                                                        'interface': 'Vlan1191',
                                                        'metric': '0',
                                                        'preference': '0',
                                                        'uptime': '20:58:10'}}}}}},
                                'mbest_num': '0',
                                'ubest_num': '1'},
                            '2001:112:1:2b3::1/128': {
                                'attach': 'attached',
                                'best_route': {
                                    'unicast': {
                                        'nexthop': {
                                            '2001:112:1:2b3::1': {
                                                'protocol': {
                                                    'hsrp': {
                                                        'interface': 'Vlan1191',
                                                         'metric': '0',
                                                         'preference': '0',
                                                         'uptime': '20:57:53'}}}}}},
                                'mbest_num': '0',
                                'ubest_num': '1'},
                            '2001:112:1:2b3::2/128': {
                                'attach': 'attached',
                                'best_route': {
                                    'unicast': {
                                        'nexthop': {
                                            '2001:112:1:2b3::2': {
                                                'protocol': {
                                                    'local': {
                                                    'interface': 'Vlan1191',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                                'mbest_num': '0',
                                'ubest_num': '1'},
                        '2001:112:1:2b4::/64': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b4::2': {
                                            'protocol': {
                                                'direct': {
                                                    'interface': 'Vlan1192',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b4::1/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b4::1': {
                                            'protocol': {
                                                'hsrp': {
                                                    'interface': 'Vlan1192',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:57:53'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b4::2/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b4::2': {
                                            'protocol': {
                                                'local': {
                                                    'interface': 'Vlan1192',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b5::/64': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                    '2001:112:1:2b5::2': {
                                        'protocol': {
                                            'direct': {
                                                'interface': 'Vlan1193',
                                                'metric': '0',
                                                'preference': '0',
                                                'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b5::1/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b5::1': {
                                            'protocol': {
                                                'hsrp': {
                                                    'interface': 'Vlan1193',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:57:52'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b5::2/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b5::2': {
                                            'protocol': {
                                                'local': {
                                                    'interface': 'Vlan1193',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b6::/64': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b6::2': {
                                            'protocol': {
                                                'direct': {
                                                    'interface': 'Vlan1194',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b6::1/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b6::1': {
                                            'protocol': {
                                                'hsrp': {
                                                    'interface': 'Vlan1194',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:57:52'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b6::2/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b6::2': {
                                            'protocol': {
                                                'local': {
                                                    'interface': 'Vlan1194',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b7::/64': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b7::2': {
                                            'protocol': {
                                                'direct': {
                                                    'interface': 'Vlan1195',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b7::1/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b7::1': {
                                            'protocol': {
                                                'hsrp': {
                                                    'interface': 'Vlan1195',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:57:52'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b7::2/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b7::2': {
                                            'protocol': {
                                                'local': {
                                                    'interface': 'Vlan1195',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'}}}}}}}

    golden_output_2 = {'execute.return_value': '''
        IPv6 Routing Table for VRF "otv-vrf139"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        2001:112:1:2b3::/64, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b3::2, Vlan1191, [0/0], 20:58:10, direct, 
        2001:112:1:2b3::1/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b3::1, Vlan1191, [0/0], 20:57:53, hsrp
        2001:112:1:2b3::2/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b3::2, Vlan1191, [0/0], 20:58:10, local
        2001:112:1:2b4::/64, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b4::2, Vlan1192, [0/0], 20:58:10, direct, 
        2001:112:1:2b4::1/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b4::1, Vlan1192, [0/0], 20:57:53, hsrp
        2001:112:1:2b4::2/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b4::2, Vlan1192, [0/0], 20:58:10, local
        2001:112:1:2b5::/64, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b5::2, Vlan1193, [0/0], 20:58:10, direct, 
        2001:112:1:2b5::1/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b5::1, Vlan1193, [0/0], 20:57:52, hsrp
        2001:112:1:2b5::2/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b5::2, Vlan1193, [0/0], 20:58:10, local
        2001:112:1:2b6::/64, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b6::2, Vlan1194, [0/0], 20:58:10, direct, 
        2001:112:1:2b6::1/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b6::1, Vlan1194, [0/0], 20:57:52, hsrp
        2001:112:1:2b6::2/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b6::2, Vlan1194, [0/0], 20:58:10, local
        2001:112:1:2b7::/64, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b7::2, Vlan1195, [0/0], 20:58:10, direct, 
        2001:112:1:2b7::1/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b7::1, Vlan1195, [0/0], 20:57:52, hsrp
        2001:112:1:2b7::2/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b7::2, Vlan1195, [0/0], 20:58:10, local
    '''}


    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowRoutingIpv6VrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowRoutingIpv6VrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowRoutingIpv6VrfAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================
# Unit tests for:
#   show ip route
#   show ip route vrf {vrf}
#   show ip route vrf all
# =============================================
class test_show_ip_route(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': ''' \
        R2# show ip route
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        2.2.2.2/32, ubest/mbest: 2/0, attached
            *via 2.2.2.2, Lo1, [0/0], 00:41:07, local
            *via 2.2.2.2, Lo1, [0/0], 00:41:07, direct
        6.6.6.6/32, ubest/mbest: 2/0
            *via 10.2.4.4, Eth1/1, [110/81], 00:20:04, ospf-10, intra
            *via 10.2.5.5, Eth1/2, [110/81], 00:20:04, ospf-10, intra
        10.2.5.0/24, ubest/mbest: 1/0, attached
            *via 10.2.5.2, Eth1/2, [0/0], 00:45:10, direct
        10.2.5.2/32, ubest/mbest: 1/0, attached
            *via 10.2.5.2, Eth1/2, [0/0], 00:45:10, local
        20.6.7.0/24, ubest/mbest: 2/0
            *via 10.2.4.4, Eth1/1, [110/20], 00:20:04, ospf-10, type-2
            *via 10.2.5.5, Eth1/2, [110/20], 00:20:04, ospf-10, type-2
        23.23.23.23/32, ubest/mbest: 2/0, attached
            *via 23.23.23.23, Lo1, [0/0], 00:41:07, local
            *via 23.23.23.23, Lo1, [0/0], 00:41:07, direct
    '''}

    golden_parsed_output = {
        'vrf':{  
            'default':{  
                'address_family':{  
                    'ipv4':{  
                        'routes':{  
                            '2.2.2.2/32':{  
                                'route':'2.2.2.2/32',
                                'ubest':2,
                                'mbest':0,
                                'attached':True,
                                'active':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'2.2.2.2',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:41:07',
                                            'source_protocol':'local',
                                            'outgoing_interface':'Loopback1'
                                        },
                                        2:{  
                                            'index':2,
                                            'next_hop':'2.2.2.2',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:41:07',
                                            'source_protocol':'direct',
                                            'outgoing_interface':'Loopback1'
                                        }
                                    }
                                }
                            },
                            '6.6.6.6/32':{  
                                'route':'6.6.6.6/32',
                                'ubest':2,
                                'mbest':0,
                                'active':True,
                                'metric':81,
                                'route_preference':110,
                                'process_id':'10',
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'10.2.4.4',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:20:04',
                                            'source_protocol':'ospf',
                                            'source_protocol_status':'intra',
                                            'outgoing_interface':'Ethernet1/1'
                                        },
                                        2:{  
                                            'index':2,
                                            'next_hop':'10.2.5.5',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:20:04',
                                            'source_protocol':'ospf',
                                            'source_protocol_status':'intra',
                                            'outgoing_interface':'Ethernet1/2'
                                        }
                                    }
                                }
                            },
                            '10.2.5.0/24':{  
                                'route':'10.2.5.0/24',
                                'ubest':1,
                                'mbest':0,
                                'attached':True,
                                'active':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'10.2.5.2',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:45:10',
                                            'source_protocol':'direct',
                                            'outgoing_interface':'Ethernet1/2'
                                        }
                                    }
                                }
                            },
                            '10.2.5.2/32':{  
                                'route':'10.2.5.2/32',
                                'ubest':1,
                                'mbest':0,
                                'attached':True,
                                'active':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'10.2.5.2',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:45:10',
                                            'source_protocol':'local',
                                            'outgoing_interface':'Ethernet1/2'
                                        }
                                    }
                                }
                            },
                            '20.6.7.0/24':{  
                                'route':'20.6.7.0/24',
                                'active':True,
                                'ubest':2,
                                'mbest':0,
                                'metric':20,
                                'route_preference':110,
                                'process_id':'10',
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'10.2.4.4',
                                            'source_protocol':'ospf',
                                            'source_protocol_status':'type-2',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:20:04',
                                            'outgoing_interface':'Ethernet1/1'
                                        },
                                        2:{  
                                            'index':2,
                                            'next_hop':'10.2.5.5',
                                            'source_protocol':'ospf',
                                            'source_protocol_status':'type-2',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:20:04',
                                            'outgoing_interface':'Ethernet1/2'
                                        }
                                    }
                                }
                            },
                            '23.23.23.23/32':{  
                                'route':'23.23.23.23/32',
                                'ubest':2,
                                'mbest':0,
                                'attached':True,
                                'active':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'23.23.23.23',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:41:07',
                                            'source_protocol':'local',
                                            'outgoing_interface':'Loopback1'
                                        },
                                        2:{  
                                            'index':2,
                                            'next_hop':'23.23.23.23',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:41:07',
                                            'source_protocol':'direct',
                                            'outgoing_interface':'Loopback1'
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': ''' \
        R2# show ip route vrf vni_10100
        IP Route Table for VRF "vni_10100"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        100.101.0.0/16, ubest/mbest: 1/0, attached
            *via 100.101.0.1, Vlan101, [0/0], 00:46:14, direct
        100.101.0.1/32, ubest/mbest: 1/0, attached
            *via 100.101.0.1, Vlan101, [0/0], 00:46:14, local
        100.101.1.3/32, ubest/mbest: 1/0, attached
            *via 100.101.1.3, Vlan101, [190/0], 00:35:43, hmm
        100.101.3.4/32, ubest/mbest: 1/0, attached
            *via 100.101.3.4, Vlan101, [190/0], 00:26:50, hmm
        100.101.8.3/32, ubest/mbest: 1/0
            *via 66.66.66.66%default, [200/2000], 00:20:43, bgp-100, internal, tag 200 (
        evpn) segid: 10100 tunnelid: 0x42424242 encap: VXLAN
        
        100.101.8.4/32, ubest/mbest: 1/0
            *via 66.66.66.66%default, [200/2000], 00:20:43, bgp-100, internal, tag 200 (
        evpn) segid: 10100 tunnelid: 0x42424242 encap: VXLAN
        
        100.102.0.0/16, ubest/mbest: 1/0, attached
            *via 100.102.0.1, Vlan102, [0/0], 00:46:13, direct
        100.102.0.1/32, ubest/mbest: 1/0, attached
            *via 100.102.0.1, Vlan102, [0/0], 00:46:13, local
    '''}

    golden_parsed_output_2 = {
        'vrf':{  
            'vni_10100':{  
                'address_family':{  
                    'ipv4':{  
                        'routes':{  
                            '100.101.0.0/16':{  
                                'route':'100.101.0.0/16',
                                'active':True,
                                'ubest':1,
                                'mbest':0,
                                'attached':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'100.101.0.1',
                                            'source_protocol':'direct',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:46:14',
                                            'outgoing_interface':'Vlan101'
                                        }
                                    }
                                }
                            },
                            '100.101.0.1/32':{  
                                'route':'100.101.0.1/32',
                                'active':True,
                                'ubest':1,
                                'mbest':0,
                                'attached':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'100.101.0.1',
                                            'source_protocol':'local',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:46:14',
                                            'outgoing_interface':'Vlan101'
                                        }
                                    }
                                }
                            },
                            '100.101.1.3/32':{  
                                'route':'100.101.1.3/32',
                                'active':True,
                                'ubest':1,
                                'mbest':0,
                                'attached':True,
                                'metric':0,
                                'route_preference':190,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'100.101.1.3',
                                            'source_protocol':'hmm',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:35:43',
                                            'outgoing_interface':'Vlan101'
                                        }
                                    }
                                }
                            },
                            '100.101.3.4/32':{  
                                'route':'100.101.3.4/32',
                                'active':True,
                                'ubest':1,
                                'mbest':0,
                                'attached':True,
                                'metric':0,
                                'route_preference':190,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'100.101.3.4',
                                            'source_protocol':'hmm',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:26:50',
                                            'outgoing_interface':'Vlan101'
                                        }
                                    }
                                }
                            },
                            '100.101.8.3/32':{  
                                'route':'100.101.8.3/32',
                                'active':True,
                                'ubest':1,
                                'mbest':0
                            },
                            '100.101.8.4/32':{  
                                'route':'100.101.8.4/32',
                                'active':True,
                                'ubest':1,
                                'mbest':0
                            },
                            '100.102.0.0/16':{  
                                'route':'100.102.0.0/16',
                                'active':True,
                                'ubest':1,
                                'mbest':0,
                                'attached':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'100.102.0.1',
                                            'source_protocol':'direct',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:46:13',
                                            'outgoing_interface':'Vlan102'
                                        }
                                    }
                                }
                            },
                            '100.102.0.1/32':{  
                                'route':'100.102.0.1/32',
                                'active':True,
                                'ubest':1,
                                'mbest':0,
                                'attached':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'100.102.0.1',
                                            'source_protocol':'local',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:46:13',
                                            'outgoing_interface':'Vlan102'
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_3 = {'execute.return_value': ''' \
        R3_nxosv# show ip route vrf all
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        1.1.1.1/32, ubest/mbest: 2/0
            *via 10.1.3.1, Eth1/2, [1/0], 01:01:30, static
            *via 20.1.3.1, Eth1/3, [1/0], 01:01:30, static
        3.3.3.3/32, ubest/mbest: 2/0, attached
            *via 3.3.3.3, Lo0, [0/0], 01:01:31, local
            *via 3.3.3.3, Lo0, [0/0], 01:01:31, direct
        10.1.2.0/24, ubest/mbest: 4/0
            *via 10.1.3.1, Eth1/2, [110/41], 01:01:18, ospf-1, intra
        10.2.3.0/24, ubest/mbest: 1/0, attached
            *via 10.2.3.3, Eth1/4, [0/0], 01:01:33, direct
        10.2.3.3/32, ubest/mbest: 1/0, attached
            *via 10.2.3.3, Eth1/4, [0/0], 01:01:33, local
        13.13.13.13/32, ubest/mbest: 2/0, attached
            *via 13.13.13.13, Lo1, [0/0], 01:01:30, local
            *via 13.13.13.13, Lo1, [0/0], 01:01:30, direct
        20.1.2.0/24, ubest/mbest: 4/0
            *via 10.1.3.1, Eth1/2, [110/41], 01:01:18, ospf-1, intra
            *via 20.2.3.2, Eth1/1, [110/41], 01:01:18, ospf-1, intra
        20.2.3.0/24, ubest/mbest: 1/0, attached
            *via 20.2.3.3, Eth1/1, [0/0], 01:01:35, direct
        20.2.3.3/32, ubest/mbest: 1/0, attached
            *via 20.2.3.3, Eth1/1, [0/0], 01:01:35, local
        21.21.21.21/32, ubest/mbest: 2/0
            *via 10.1.3.1, Eth1/2, [115/50], 01:01:22, isis-1, L1
            *via 20.1.3.1, Eth1/3, [115/50], 01:01:16, isis-1, L1
        31.31.31.31/32, ubest/mbest: 1/0
            *via 11.11.11.11, [200/0], 01:01:12, bgp-100, internal, tag 100

        IP Route Table for VRF "VRF1"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        1.1.1.1/32, ubest/mbest: 2/0, attached
            *via 1.1.1.1, Lo4, [0/0], 00:00:10, local
            *via 1.1.1.1, Lo4, [0/0], 00:00:10, direct
    '''}

    golden_parsed_output_3 = {
        'vrf':{  
            'default':{  
                'address_family':{  
                    'ipv4':{  
                        'routes':{  
                            '1.1.1.1/32':{  
                                'route':'1.1.1.1/32',
                                'active':True,
                                'ubest':2,
                                'mbest':0,
                                'metric':0,
                                'route_preference':1,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'10.1.3.1',
                                            'source_protocol':'static',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:30',
                                            'outgoing_interface':'Ethernet1/2'
                                        },
                                        2:{  
                                            'index':2,
                                            'next_hop':'20.1.3.1',
                                            'source_protocol':'static',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:30',
                                            'outgoing_interface':'Ethernet1/3'
                                        }
                                    }
                                }
                            },
                            '3.3.3.3/32':{  
                                'route':'3.3.3.3/32',
                                'active':True,
                                'ubest':2,
                                'mbest':0,
                                'attached':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'3.3.3.3',
                                            'source_protocol':'local',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:31',
                                            'outgoing_interface':'Loopback0'
                                        },
                                        2:{  
                                            'index':2,
                                            'next_hop':'3.3.3.3',
                                            'source_protocol':'direct',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:31',
                                            'outgoing_interface':'Loopback0'
                                        }
                                    }
                                }
                            },
                            '10.1.2.0/24':{  
                                'route':'10.1.2.0/24',
                                'active':True,
                                'ubest':4,
                                'mbest':0,
                                'metric':41,
                                'route_preference':110,
                                'process_id':'1',
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'10.1.3.1',
                                            'source_protocol':'ospf',
                                            'source_protocol_status':'intra',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:18',
                                            'outgoing_interface':'Ethernet1/2'
                                        }
                                    }
                                }
                            },
                            '10.2.3.0/24':{  
                                'route':'10.2.3.0/24',
                                'active':True,
                                'ubest':1,
                                'mbest':0,
                                'attached':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'10.2.3.3',
                                            'source_protocol':'direct',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:33',
                                            'outgoing_interface':'Ethernet1/4'
                                        }
                                    }
                                }
                            },
                            '10.2.3.3/32':{  
                                'route':'10.2.3.3/32',
                                'active':True,
                                'ubest':1,
                                'mbest':0,
                                'attached':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'10.2.3.3',
                                            'source_protocol':'local',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:33',
                                            'outgoing_interface':'Ethernet1/4'
                                        }
                                    }
                                }
                            },
                            '13.13.13.13/32':{  
                                'route':'13.13.13.13/32',
                                'active':True,
                                'ubest':2,
                                'mbest':0,
                                'attached':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'13.13.13.13',
                                            'source_protocol':'local',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:30',
                                            'outgoing_interface':'Loopback1'
                                        },
                                        2:{  
                                            'index':2,
                                            'next_hop':'13.13.13.13',
                                            'source_protocol':'direct',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:30',
                                            'outgoing_interface':'Loopback1'
                                        }
                                    }
                                }
                            },
                            '20.1.2.0/24':{  
                                'route':'20.1.2.0/24',
                                'active':True,
                                'ubest':4,
                                'mbest':0,
                                'metric':41,
                                'route_preference':110,
                                'process_id':'1',
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'10.1.3.1',
                                            'source_protocol':'ospf',
                                            'source_protocol_status':'intra',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:18',
                                            'outgoing_interface':'Ethernet1/2'
                                        },
                                        2:{  
                                            'index':2,
                                            'next_hop':'20.2.3.2',
                                            'source_protocol':'ospf',
                                            'source_protocol_status':'intra',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:18',
                                            'outgoing_interface':'Ethernet1/1'
                                        }
                                    }
                                }
                            },
                            '20.2.3.0/24':{  
                                'route':'20.2.3.0/24',
                                'active':True,
                                'ubest':1,
                                'mbest':0,
                                'attached':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'20.2.3.3',
                                            'source_protocol':'direct',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:35',
                                            'outgoing_interface':'Ethernet1/1'
                                        }
                                    }
                                }
                            },
                            '20.2.3.3/32':{  
                                'route':'20.2.3.3/32',
                                'active':True,
                                'ubest':1,
                                'mbest':0,
                                'attached':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'20.2.3.3',
                                            'source_protocol':'local',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:35',
                                            'outgoing_interface':'Ethernet1/1'
                                        }
                                    }
                                }
                            },
                            '21.21.21.21/32':{  
                                'route':'21.21.21.21/32',
                                'active':True,
                                'ubest':2,
                                'mbest':0,
                                'metric':50,
                                'route_preference':115,
                                'process_id':'1',
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'10.1.3.1',
                                            'source_protocol':'isis',
                                            'source_protocol_status':'L1',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:22',
                                            'outgoing_interface':'Ethernet1/2'
                                        },
                                        2:{  
                                            'index':2,
                                            'next_hop':'20.1.3.1',
                                            'source_protocol':'isis',
                                            'source_protocol_status':'L1',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:16',
                                            'outgoing_interface':'Ethernet1/3'
                                        }
                                    }
                                }
                            },
                            '31.31.31.31/32':{  
                                'route':'31.31.31.31/32',
                                'active':True,
                                'ubest':1,
                                'mbest':0,
                                'metric':0,
                                'route_preference':200,
                                'process_id':'100',
                                'tag':100,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'11.11.11.11',
                                            'source_protocol':'bgp',
                                            'source_protocol_status':'internal',
                                            'best_ucast_nexthop':True,
                                            'updated':'01:01:12'
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            'VRF1':{  
                'address_family':{  
                    'ipv4':{  
                        'routes':{  
                            '1.1.1.1/32':{  
                                'route':'1.1.1.1/32',
                                'active':True,
                                'ubest':2,
                                'mbest':0,
                                'attached':True,
                                'metric':0,
                                'route_preference':0,
                                'next_hop':{  
                                    'next_hop_list':{  
                                        1:{  
                                            'index':1,
                                            'next_hop':'1.1.1.1',
                                            'source_protocol':'local',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:00:10',
                                            'outgoing_interface':'Loopback4'
                                        },
                                        2:{  
                                            'index':2,
                                            'next_hop':'1.1.1.1',
                                            'source_protocol':'direct',
                                            'best_ucast_nexthop':True,
                                            'updated':'00:00:10',
                                            'outgoing_interface':'Loopback4'
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }        
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRoute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_route(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_ip_route_vrf_vrf(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse(vrf="vni_10100")
        print(parsed_output)
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

    def test_show_ip_route_vrf_all(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse(vrf="all")
        print(parsed_output)
        self.assertEqual(parsed_output,self.golden_parsed_output_3)

# ============================================
# unit test for 'show ipv6 route'
# =============================================
class test_show_ipv6_route(unittest.TestCase):
    """
       unit test for show ipv6 route
    """
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output_1 = {'execute.return_value': '''
    R3_nxosv# show ipv6 route vrf all
    IPv6 Routing Table for VRF "default"
    '*' denotes best ucast next-hop
    '**' denotes best mcast next-hop
    '[x/y]' denotes [preference/metric]

    2001:1:1:1::1/128, ubest/mbest: 2/0
        *via 2001:10:1:3::1, Eth1/2, [1/0], 01:02:00, static
        *via 2001:20:1:3::1, Eth1/3, [1/0], 01:02:00, static
    2001:10:1:2::/64, ubest/mbest: 4/0
        *via fe80::5054:ff:fe64:bd2e, Eth1/3, [110/41], 01:01:10, ospfv3-1, intra
        *via fe80::5054:ff:fea5:6e95, Eth1/2, [110/41], 01:01:10, ospfv3-1, intra
        *via fe80::5054:ff:fea7:1341, Eth1/4, [110/41], 01:01:10, ospfv3-1, intra
        *via fe80::5054:ff:feb3:b312, Eth1/1, [110/41], 01:01:10, ospfv3-1, intra

    2001:31:31:31::31/128, ubest/mbest: 1/0
        *via ::ffff:10.229.11.11%default:IPv4, [200/0], 01:01:43, bgp-100, internal,
    tag 100
    2001:32:32:32::32/128, ubest/mbest: 2/0
        *via fe80::5054:ff:fea7:1341, Eth1/4, [200/0], 01:01:24, bgp-100, internal,
    tag 100
        *via fe80::5054:ff:feb3:b312, Eth1/1, [200/0], 01:01:24, bgp-100, internal,
    tag 100
    2001:33:33:33::33/128, ubest/mbest: 2/0, attached
        *via 2001:33:33:33::33, Lo3, [0/0], 01:02:01, direct,
        *via 2001:33:33:33::33, Lo3, [0/0], 01:02:01, local

    IPv6 Routing Table for VRF "VRF1"
    '*' denotes best ucast next-hop
    '**' denotes best mcast next-hop
    '[x/y]' denotes [preference/metric]

    2001:1:1:1::1/128, ubest/mbest: 2/0, attached
        *via 2001:1:1:1::1, Lo4, [0/0], 00:00:35, direct,
        *via 2001:1:1:1::1, Lo4, [0/0], 00:00:35, local

    IPv6 Routing Table for VRF "management"
    '*' denotes best ucast next-hop
    '**' denotes best mcast next-hop
    '[x/y]' denotes [preference/metric]

    '''
}
    golden_parsed_output_1 = {
        'vrf':{
            'default':{
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:1:1:1::1/128': {
                                'route': '2001:1:1:1::1/128',
                                'active': True,
                                'ubest':2,
                                'mbest':0,
                                'route_preference': 1,
                                'metric': 0,
                                'source_protocol':'static',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '2001:10:1:3::1',
                                            'outgoing_interface': 'Ethernet1/2',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:02:00',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '2001:20:1:3::1',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/3',
                                            'updated': '01:02:00',
                                        },
                                    },
                                },
                            },
                            '2001:10:1:2::/64': {
                                'route': '2001:10:1:2::/64',
                                'active': True,
                                'ubest': 4,
                                'mbest': 0,
                                'route_preference': 110,
                                'metric': 41,
                                'source_protocol': 'ospfv3',
                                'process_id': '1',
                                'source_protocol_status': 'intra',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fe64:bd2e',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/3',
                                            'updated': '01:01:10',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': 'fe80::5054:ff:fea5:6e95',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/2',
                                            'updated': '01:01:10',
                                        },
                                        3: {
                                            'index': 3,
                                            'next_hop': 'fe80::5054:ff:fea7:1341',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/4',
                                            'updated': '01:01:10',
                                        },
                                        4: {
                                            'index': 4,
                                            'next_hop': 'fe80::5054:ff:feb3:b312',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/1',
                                            'updated': '01:01:10',
                                        },
                                    },
                                },
                            },
                            '2001:31:31:31::31/128': {
                                'route': '2001:31:31:31::31/128',
                                'active': True,
                                'ubest': 1,
                                'mbest': 0,
                                'route_preference': 200,
                                'source_protocol': 'bgp',
                                'source_protocol_status': 'internal',
                                'process_id': '100',
                                'tag': 100,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '::ffff:10.229.11.11',
                                            'next_hop_vrf': 'default',
                                            'next_hop_af': 'ipv4',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:01:43',
                                        },

                                    },
                                },
                            },
                            '2001:32:32:32::32/128': {
                                'route': '2001:32:32:32::32/128',
                                'active': True,
                                'ubest': 2,
                                'mbest': 0,
                                'route_preference': 200,
                                'source_protocol': 'bgp',
                                'source_protocol_status': 'internal',
                                'process_id': '100',
                                'tag': 100,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fea7:1341',
                                            'outgoing_interface': 'Ethernet1/4',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:01:24',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': 'fe80::5054:ff:feb3:b312',
                                            'outgoing_interface': 'Ethernet1/1',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:01:24',
                                        },
                                    },
                                },
                            },
                            '2001:33:33:33::33/128': {
                                'route': '2001:33:33:33::33/128',
                                'active': True,
                                'attached': True,
                                'ubest': 2,
                                'mbest': 0,
                                'route_preference': 0,
                                'source_protocol': 'local',
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '2001:33:33:33::33',
                                            'outgoing_interface': 'Loopback3',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:02:01',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '2001:33:33:33::33',
                                            'outgoing_interface': 'Loopback3',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:02:01',
                                        },
                                    },
                                },
                            },

                        },
                    },
                },
            },
            'VRF1': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:1:1:1::1/128': {
                                'route': '2001:1:1:1::1/128',
                                'attached': True,
                                'active': True,
                                'ubest': 2,
                                'mbest': 0,
                                'route_preference': 0,
                                'metric': 0,
                                'source_protocol': 'local',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '2001:1:1:1::1',
                                            'outgoing_interface': 'Loopback4',
                                            'best_ucast_nexthop': True,
                                            'updated': '00:00:35',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '2001:1:1:1::1',
                                            'outgoing_interface': 'Loopback4',
                                            'best_ucast_nexthop': True,
                                            'updated': '00:00:35',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


    golden_output_3 = {'execute.return_value': '''
        R3_nxosv# show ipv6 route vrf VRF3
        No IP Route Table for VRF "VRF3"
    '''}


    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6Route(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ipv6_route_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpv6Route(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='VRF3')

    def test_show_ipv6_route_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6Route(device=self.device)
        parsed_output = obj.parse(vrf="all")
        self.assertEqual(parsed_output,self.golden_parsed_output_1)



if __name__ == '__main__':
    unittest.main()
