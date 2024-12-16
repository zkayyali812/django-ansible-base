FEATURE_FLAGS = [
    {'name': 'SOME_PLATFORM_FLAG', 'conditions': [], 'components': ['eda', 'hub', 'controller', 'gateway']},
    {
        'name': "EDA_ANALYTICS",
        'conditions': [
            {
                "condition": "boolean",
                "value": True,
                "required": True,
            }
        ],
        "components": ['eda'],
    },
]


def get_component_flags(component):
    flags = {}
    for flag in FEATURE_FLAGS:
        if component in flag["components"]:
            flags[flag['name']] = flag['conditions']
    return flags


EDA_FLAGS = get_component_flags('eda')
CONTROLLER_FLAGS = get_component_flags('controller')
HUB_FLAGS = get_component_flags('hub')
GATEWAY_FLAGS = get_component_flags('gateway')


def get_platform_flags():
    return EDA_FLAGS | CONTROLLER_FLAGS | HUB_FLAGS | GATEWAY_FLAGS
