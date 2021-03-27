from universal_name_format.models.name import Name
from universal_name_format.models.orders import EASTERN_ORDER, WESTERN_ORDER


def eastern_to_name(name):
    return Name({
        "name": {
            "family": name[:-2],
            "given": name[-2:]
        } if len(name) > 2 else {
            "family": name[0],
            "given": name[1]
        },
        "order": EASTERN_ORDER,
        "encode": "eastern"
    })


def mononym_to_name(name):
    return Name({
        "name": name,
        "order": [],
        "encode": "mononym"
    })


def western_to_name(name):
    splitted_name = name.split(' ')

    return Name({
        "name": {
            "given": splitted_name[0],
            "family": splitted_name[1]
        } if len(splitted_name) == 2 else {
            "given": splitted_name[0],
            "middle": splitted_name[1],
            "family": splitted_name[2]
        },
        "order": WESTERN_ORDER,
        "encode": "western"
    })
