# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# iosxe show ip eigrp
from genie.libs.parser.iosxe.show_eigrp import ShowIpEigrpNeighborsDetail,\
						ShowIpEigrpNeighbors,\
						ShowIpv6EigrpNeighbors

class test_show_eigrp_neighbors(unittest.TestCase):

    device = Device(name='aDevice')

    expected_parsed_output_1 = {
	    "eigrp_instance": {
	        "": {
	            "vrf": {
	                "default": {
	                    "address_family": {
	                        "ipv4": {
	                            "eigrp_interface": {
	                                "GigabitEthernet0/0": {
	                                    "eigrp_nbr": {
	                                        "10.1.1.2": {
	                                            "peer_handle": 0,
	                                            "hold": 13,
	                                            "uptime": "00:00:03",
	                                            "srtt": 1996.0,
	                                            "rto": 5000,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 5
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
	}  

    device_output_1 = {'execute.return_value': '''
        Device# show ip eigrp neighbors
        H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
                                    (sec)           (ms)          Cnt Num
        0   10.1.1.2     Gi0/0      13    00:00:03  1996   5000   0   5
    '''}

    expected_parsed_output_2 = {
	    "eigrp_instance": {
	        "": {
	            "vrf": {
	                "default": {
	                    "address_family": {
	                        "ipv4": {
	                            "eigrp_interface": {
	                                "GigabitEthernet0/0": {
	                                    "eigrp_nbr": {
	                                        "10.1.1.9": {
	                                            "peer_handle": 2,
	                                            "hold": 14,
	                                            "uptime": "00:02:24",
	                                            "srtt": 206.0,
	                                            "rto": 5000,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 5
	                                        },
	                                        "10.1.1.2": {
	                                            "peer_handle": 0,
	                                            "hold": 13,
	                                            "uptime": "00:00:03",
	                                            "srtt": 1996.0,
	                                            "rto": 5000,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 5
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
	}

    device_output_2 = {'execute.return_value': '''
        Device# show ip eigrp neighbors
        H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
                                    (sec)           (ms)          Cnt Num
        2   10.1.1.9     Gi0/0      14    00:02:24  206    5000   0   5
        0   10.1.1.2     Gi0/0      13    00:00:03  1996   5000   0   5
    '''}

    expected_parsed_output_3 = {
	    "eigrp_instance": {
	        "": {
	            "vrf": {
	                "default": {
	                    "address_family": {
	                        "ipv4": {
	                            "eigrp_interface": {
	                                "GigabitEthernet0/0": {
	                                    "eigrp_nbr": {
	                                        "10.1.1.9": {
	                                            "peer_handle": 2,
	                                            "hold": 14,
	                                            "uptime": "00:02:24",
	                                            "srtt": 206.0,
	                                            "rto": 5000,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 5
	                                        }
	                                    }
	                                },
	                                "GigabitEthernet0/1": {
	                                    "eigrp_nbr": {
	                                        "10.1.2.3": {
	                                            "peer_handle": 1,
	                                            "hold": 11,
	                                            "uptime": "00:20:39",
	                                            "srtt": 2202.0,
	                                            "rto": 5000,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 5
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
	}

    device_output_3 = {'execute.return_value': '''
        Device# show ip eigrp neighbors
        H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
                                    (sec)           (ms)          Cnt Num
        2   10.1.1.9     Gi0/0      14    00:02:24  206    5000   0   5
        1   10.1.2.3     Gi0/1      11    00:20:39  2202   5000   0   5
    '''}

    expected_parsed_output_4 ={
	    "eigrp_instance": {
	        "": {
	            "vrf": {
	                "default": {
	                    "address_family": {
	                        "ipv4": {
	                            "eigrp_interface": {
	                                "GigabitEthernet0/0": {
	                                    "eigrp_nbr": {
	                                        "10.1.1.2": {
	                                            "peer_handle": 0,
	                                            "hold": 13,
	                                            "uptime": "00:00:03",
	                                            "srtt": 1996.0,
	                                            "rto": 5000,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 5
	                                        },
	                                        "10.1.1.9": {
	                                            "peer_handle": 2,
	                                            "hold": 14,
	                                            "uptime": "00:02:24",
	                                            "srtt": 206.0,
	                                            "rto": 5000,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 5
	                                        }
	                                    }
	                                },
	                                "GigabitEthernet0/1": {
	                                    "eigrp_nbr": {
	                                        "10.1.2.3": {
	                                            "peer_handle": 1,
	                                            "hold": 11,
	                                            "uptime": "00:20:39",
	                                            "srtt": 2202.0,
	                                            "rto": 5000,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 5
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
	}

    device_output_4 = {'execute.return_value': '''
        Device# show ip eigrp neighbors

        H   Address     Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                        (sec)         (ms)       Cnt Num
        0   10.1.1.2     Gi0/0           13 00:00:03  1996   5000  0  5
        2   10.1.1.9     Gi0/0           14 00:02:24   206   5000  0  5
        1   10.1.2.3     Gi0/1           11 00:20:39  2202   5000  0  5

    '''}

    expected_parsed_output_5 = {
	    "eigrp_instance": {
	        "": {
	            "vrf": {
	                "default": {
	                    "address_family": {
	                        "ipv4": {
	                            "eigrp_interface": {
	                                "GigabitEthernet0/0": {
	                                    "eigrp_nbr": {
	                                        "10.1.1.2": {
	                                            "peer_handle": 0,
	                                            "hold": 13,
	                                            "uptime": "00:00:03",
	                                            "srtt": 1996.0,
	                                            "rto": 5000,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 5
	                                        },
	                                        "10.1.1.9": {
	                                            "peer_handle": 2,
	                                            "hold": 14,
	                                            "uptime": "00:02:24",
	                                            "srtt": 206.0,
	                                            "rto": 5000,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 5
	                                        }
	                                    }
	                                },
	                                "GigabitEthernet0/1": {
	                                    "eigrp_nbr": {
	                                        "10.1.2.3": {
	                                            "peer_handle": 1,
	                                            "hold": 11,
	                                            "uptime": "00:20:39",
	                                            "srtt": 2202.0,
	                                            "rto": 5000,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 5
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
	}

    device_output_5 = {'execute.return_value': '''
        Device# show ip eigrp neighbors

        H   Address     Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                        (sec)         (ms)       Cnt Num
        0   10.1.1.2     Gi0/0           13 00:00:03  1996   5000  0  5
        2   10.1.1.9     Gi0/0           14 00:02:24   206   5000  0  5
        1   10.1.2.3     Gi0/1           11 00:20:39  2202   5000  0  5

    '''}        

    expected_parsed_output_6 = {
	    "eigrp_instance": {
	        "": {
	            "vrf": {
	                "default": {
	                    "address_family": {
	                        "ipv4": {
	                            "eigrp_interface": {
	                                "Ethernet0/0": {
	                                    "eigrp_nbr": {
	                                        "10.1.1.2": {
	                                            "peer_handle": 0,
	                                            "hold": 13,
	                                            "uptime": "00:00:03",
	                                            "srtt": 1996.0,
	                                            "rto": 5000,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 5
	                                        },
	                                        "10.1.1.9": {
	                                            "peer_handle": 2,
	                                            "hold": 14,
	                                            "uptime": "00:02:24",
	                                            "srtt": 206.0,
	                                            "rto": 5000,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 5
	                                        }
	                                    }
	                                },
	                                "Ethernet0/1": {
	                                    "eigrp_nbr": {
	                                        "10.1.2.3": {
	                                            "peer_handle": 1,
	                                            "hold": 11,
	                                            "uptime": "00:20:39",
	                                            "srtt": 2202.0,
	                                            "rto": 5000,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 5
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
	}

    device_output_6 = {'execute.return_value': '''
        Router# show ip eigrp neighbors

        H   Address     Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                        (sec)         (ms)       Cnt Num
        0   10.1.1.2     Et0/0             13 00:00:03 1996  5000  0  5
        2   10.1.1.9     Et0/0             14 00:02:24 206   5000  0  5
        1   10.1.2.3     Et0/1             11 00:20:39 2202  5000  0  5

    '''}

    expected_parsed_output_7 ={
	    "eigrp_instance": {
	        "1100": {
	            "vrf": {
	                "VRF1": {
	                    "address_family": {
	                        "ipv4": {
	                            "eigrp_interface": {
	                                "GigabitEthernet3": {
	                                    "eigrp_nbr": {
	                                        "10.1.2.2": {
	                                            "peer_handle": 0,
	                                            "hold": 13,
	                                            "uptime": "00:01:01",
	                                            "srtt": 2.0,
	                                            "rto": 100,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 2
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
	}

    device_output_7 = {'execute.return_value': '''
        R1#show ip eigrp vrf VRF1 neighbors

        EIGRP-IPv4 Neighbors for AS(1100) VRF(VRF1)
        H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                           (sec)         (ms)       Cnt Num
        0   10.1.2.2                Gi3                      13 00:01:01    2   100  0  2
    '''}

    expected_parsed_output_8 = {
	    "eigrp_instance": {
	        "100": {
	            "vrf": {
	                "default": {
	                    "address_family": {
	                        "ipv6": {
	                            "eigrp_interface": {
	                                "GigabitEthernet2": {
	                                    "eigrp_nbr": {
	                                        "FE80::F816:3EFF:FE7D:7953": {
	                                            "peer_handle": 0,
	                                            "hold": 14,
	                                            "uptime": "00:00:12",
	                                            "srtt": 2.0,
	                                            "rto": 100,
	                                            "q_cnt": 0,
	                                            "last_seq_number": 2
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
	}

    device_output_8 = {'execute.return_value': '''
    	R1#show ipv6 eigrp neighbors 
		
		EIGRP-IPv6 Neighbors for AS(100) 
		H Address Interface Hold Uptime SRTT RTO Q Seq (sec) (ms) Cnt Num 
		Link-local address:
		0 FE80::F816:3EFF:FE7D:7953 Gi2 14 00:00:12 2 100 0 2 
    '''}

    device_output_empty = {'execute.return_value': ''}

    def test_show_eigrp_neighbors_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_eigrp_neighbors_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_show_eigrp_neighbors_3(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_3)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_3)

    def test_show_eigrp_neighbors_4(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_4)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_4)

    def test_show_eigrp_neighbors_5(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_5)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_5)

    def test_show_eigrp_neighbors_6(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_6)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_6)

    def test_show_eigrp_neighbors_7(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_7)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_7)

    def test_show_eigrp_neighbors_8(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_8)
        obj = ShowIpv6EigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_8)

    def test_show_eigrp_neighbors_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_empty)
        obj = ShowIpEigrpNeighbors(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_eigrp_neighbors_detail(unittest.TestCase):

    device = Device(name='aDevice')

    expected_parsed_output_1 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv4': {
                                'eigrp_interface': {
                                    'Ethernet1/0': {
                                        'eigrp_nbr': {
                                            '10.1.2.1': {
                                                'hold': 11,
                                                'last_seq_number': 6,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 5,
                                                    'os_minorver': 1,
                                                    'tlv_majorrev': 3,
                                                    'tlv_minorrev': 0},
                                                'peer_handle': 0,
                                                'prefixes': 1,
                                                'q_cnt': 0,
                                                'retransmit_count': 2,
                                                'retry_count': 0,
                                                'rto': 200,
                                                'srtt': 12.0,
                                                'topology_ids_from_peer': 0,
                                                'uptime': '00:02:31'}}}}}}}}}}}

    device_output_1 = {'execute.return_value': '''
        Device# show ip eigrp neighbors detail

        EIGRP-IPv4 Neighbors for AS(100)
        H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                            (sec)         (ms)       Cnt Num
        0   10.1.2.1                 Et1/0             11 00:00:25   10   200  0  5
        Version 5.1/3.0, Retrans: 2, Retries: 0, Prefixes: 1
        Topology-ids from peer - 0

        EIGRP-IPv4 Neighbors for AS(100)
        H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                            (sec)         (ms)       Cnt Num
        0   10.1.2.1                 Et1/0             11 00:02:31   12   200  0  6

        Time since Restart 00:01:34
        Version 5.1/3.0, Retrans: 2, Retries: 0, Prefixes: 1
        Topology-ids from peer - 0
    '''}

    expected_parsed_output_2 = {
        'eigrp_instance': {
            '1': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv4': {
                                'eigrp_interface': {
                                    'GigabitEthernet2/0': {
                                        'eigrp_nbr': {
                                            '192.168.10.1': {
                                                'peer_handle': 0, 
                                                'hold': 12, 
                                                'uptime': '00:00:21', 
                                                'srtt': 1600.0, 
                                                'rto': 5000, 
                                                'q_cnt': 0, 
                                                'last_seq_number': 3, 
                                                'nbr_sw_ver': {
                                                    'os_majorver': 8, 
                                                    'os_minorver': 0, 
                                                    'tlv_majorrev': 2, 
                                                    'tlv_minorrev': 0}, 
                                                'retransmit_count': 0, 
                                                'retry_count': 0, 
                                                'prefixes': 1, 
                                                'topology_ids_from_peer': 0}}}}}}}}}}}

    device_output_2 = {'execute.return_value': '''
        Device# show ip eigrp neighbors detail

        EIGRP-IPv4 VR(foo) Address-Family Neighbors for AS(1)
        H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                            (sec)         (ms)       Cnt Num
        0   192.168.10.1                 Gi2/0       12 00:00:21 1600  5000  0  3
        Version 8.0/2.0, Retrans: 0, Retries: 0, Prefixes: 1
        Topology-ids from peer - 0
    '''}

    expected_parsed_output_3 = {
        'eigrp_instance': {
            '1100': {
                'vrf': {
                    'VRF1': {
                        'address_family': {
                            'ipv4': {
                                'eigrp_interface': {
                                    'GigabitEthernet3': {
                                        'eigrp_nbr': {
                                            '10.1.2.2': {
                                                'hold': 11,
                                                'last_seq_number': 2,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 23,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0},
                                                'peer_handle': 0,
                                                'prefixes': 0,
                                                'q_cnt': 0,
                                                'retransmit_count': 0,
                                                'retry_count': 0,
                                                'rto': 100,
                                                'srtt': 2.0,
                                                'topology_ids_from_peer': 0,
                                                'uptime': '00:01:03'}}}}}}}}}}}

    device_output_3 = {'execute.return_value': '''
        R1#show ip eigrp vrf VRF1 neighbors detail 
        EIGRP-IPv4 Neighbors for AS(1100) VRF(VRF1)
        H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                   (sec)         (ms)       Cnt Num
        0   10.1.2.2                Gi3                      11 00:01:03    2   100  0  2
        Version 23.0/2.0, Retrans: 0, Retries: 0
        Topology-ids from peer - 0 
        Topologies advertised to peer:   base

        Max Nbrs: 0, Current Nbrs: 0
    '''}

    expected_parsed_output_4 = {
        'eigrp_instance': {
            '1100': {
                'vrf': {
                    'VRF1': {
                        'address_family': {
                            'ipv4': {
                                'eigrp_interface': {
                                    'GigabitEthernet3': {
                                        'eigrp_nbr': {
                                            '10.1.2.2': {
                                                'hold': 11,
                                                'last_seq_number': 2,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 23,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0},
                                                'peer_handle': 0,
                                                'prefixes': 0,
                                                'q_cnt': 0,
                                                'retransmit_count': 0,
                                                'retry_count': 0,
                                                'rto': 100,
                                                'srtt': 2.0,
                                                'topology_ids_from_peer': 0,
                                                'uptime': '00:01:03'}}}}}}}}}}}

    device_output_4 = {'execute.return_value': '''
        R1#show ip eigrp vrf VRF1 neighbors detail 
        EIGRP-IPv4 VR(foo) Address-Family Neighbors for AS(1) VRF(VRF1)
        H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                   (sec)         (ms)       Cnt Num
        0   10.1.2.2                Gi3                      11 00:01:03    2   100  0  2
        Version 23.0/2.0, Retrans: 0, Retries: 0
        Topology-ids from peer - 0 
        Topologies advertised to peer:   base

        Max Nbrs: 0, Current Nbrs: 0
    '''}

    device_output_empty = {'execute.return_value': ''}

    def test_show_eigrp_neighbors_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowIpEigrpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_eigrp_neighbors_detail_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowIpEigrpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_show_eigrp_neighbors_detail_3(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_3)
        obj = ShowIpEigrpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_3)


    def test_show_eigrp_neighbors_detail_4(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_3)
        obj = ShowIpEigrpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_4)

    def test_show_eigrp_neighbors_detail_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_empty)
        obj = ShowIpEigrpNeighborsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
