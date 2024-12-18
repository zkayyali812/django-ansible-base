from flags.sources import get_flags
from flags.state import flag_enabled

FEATURE_FLAGS = [
    {
        'name': 'SOME_PLATFORM_FLAG',
        'conditions': [],
        'components': ['eda', 'hub', 'controller', 'gateway'],
        "description": "This is a dummy flag, shown as an example.",
    },
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
        "description": "If true, analytics functionality is enabled in Event-Driven Ansible. (Default: True)",
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


def get_flag_description(flag_name):
    description = ""
    for flag in FEATURE_FLAGS:
        if flag["name"] == flag_name and 'description' in flag:
            description = flag["description"]
            break
    return description


def get_feature_flags_detail():
    response = {}
    flags = get_flags()
    for name, flag in flags.items():
        response[name] = {"state": flag_enabled(name), "description": get_flag_description(name)}
    return response
