def get_full_name(first_name: str, last_name: str) -> str:
    # full_name = first_name.title() + " " + last_name.title()
    full_name = first_name.title() + " " + last_name.title()
    return full_name


# print(get_full_name("john", "doe"))

import typing


def get_items(items: typing.List[str]):
    return items


def get_items2(items: typing.Dict[str, typing.Any]):
    return items

def get_items2(items: typing.Set[typing.Union[int, str]]):
    return items

def get_items3(items: typing.Union[None, typing.List[str]]):
    return items

def get_items4(items: typing.Optional[typing.List[str]]):
    return items


