expected_output = {
    'backbone_fast': False,
    'bpdu_filter': False,
    'bpdu_guard': False,
    'bridge_assurance': True,
    'configured_pathcost': {
        'method': 'long',
    },
    'etherchannel_misconfig_guard': True,
    'extended_system_id': True,
    'loop_guard': True,
    'mode': {
        'mst': {
            'MST0': {
                'blocking': 0,
                'forwarding': 53,
                'learning': 0,
                'listening': 0,
                'stp_active': 53,
            },
            'MST1': {
                'blocking': 0,
                'forwarding': 30,
                'learning': 0,
                'listening': 0,
                'stp_active': 30,
            },
            'MST2': {
                'blocking': 0,
                'forwarding': 34,
                'learning': 0,
                'listening': 0,
                'stp_active': 34,
            },
            'MST3': {
                'blocking': 0,
                'forwarding': 20,
                'learning': 0,
                'listening': 0,
                'stp_active': 20,
            },
            'MST4': {
                'blocking': 0,
                'forwarding': 16,
                'learning': 0,
                'listening': 0,
                'stp_active': 16,
            },
            'MST5': {
                'blocking': 0,
                'forwarding': 15,
                'learning': 0,
                'listening': 0,
                'stp_active': 15,
            },
            'MST6': {
                'blocking': 1,
                'forwarding': 14,
                'learning': 0,
                'listening': 0,
                'stp_active': 15,
            },
            'MST7': {
                'blocking': 0,
                'forwarding': 29,
                'learning': 0,
                'listening': 0,
                'stp_active': 29,
            },
            'MST8': {
                'blocking': 0,
                'forwarding': 15,
                'learning': 0,
                'listening': 0,
                'stp_active': 15,
            },
        },
    },
    'platform_pvst_simulation': True,
    'portfast_default': False,
    'pvst_simulation': True,
    'root_bridge_for': 'MST0-MST5, MST7-MST8',
    'total_statistics': {
        'blockings': 1,
        'forwardings': 226,
        'learnings': 0,
        'listenings': 0,
        'num_of_msts': 9,
        'stp_actives': 227,
    },
    'uplink_fast': False,
}