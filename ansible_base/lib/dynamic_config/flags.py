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


def get_platform_flags():
    flags = {}
    for flag in FEATURE_FLAGS:
        flags[flag['name']] = flag['conditions']
    return flags
