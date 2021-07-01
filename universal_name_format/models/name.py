from copy import deepcopy

from .orders import EASTERN_ORDER, WESTERN_ORDER


PLACEHOLDERS = ("family", "given", "middle", "prefix", "suffix")


class Name:
    __name = None
    __order = []
    __encode = "western"

    def __init__(self, source):
        self.__name = source["name"]
        self.__order = source["order"]
        self.__encode = source["encode"]

    def __repr__(self):
        if self.__name:
            return self.name()

        else:
            return "<Name>"

    def source(self):
        return {
            "name": self.get_name(),
            "order": self.get_order(),
            "encode": self.get_encode()
        }

    def get_name(self, placeholder=None) -> dict or str:
        if placeholder:
            if placeholder in self.__name:
                return self.__name[placeholder]
            else:
                return

        else:
            return self.__name

    def name(self, order=None) -> str:
        if isinstance(self.get_name(), str):
            return self.get_name()

        ordered_name = []

        if not order:
            order = self.get_order()

        elif order == "eastern" or order == "family-first":
            clone = deepcopy(self)
            clone.set_order(EASTERN_ORDER)

            return clone.name()

        elif order == "lexical":
            return ''.join([self.get_name("family"), ", ", self.get_name("given")])

        elif order == "western" or order == "given-first":
            clone = deepcopy(self)
            clone.set_order(WESTERN_ORDER)

            return clone.name()

        for placeholder in order:
            if placeholder in self.__name and self.get_name(placeholder):
                ordered_name.append(self.get_name(placeholder))

        return self.__get_space().join(ordered_name)

    def full_name(self) -> str:
        prefix = self.get_name("prefix")
        suffix = self.get_name("suffix")

        return f"{prefix + ' ' if prefix else ''}{self.name()}{' ' + suffix if suffix else ''}"

    def set_name(self, name, placeholder=None):
        if self.__is_mononym():
            return

        if not self.is_name_valid(name):
            raise False

        if placeholder:
            self.__name[placeholder] = name

        else:
            self.__name = name

        return self

    def get_order(self):
        return self.__order

    def set_order(self, order):
        if self.__is_mononym():
            return

        if not self.is_order_valid(order):
            raise False

        self.__order = order

        return self

    def get_encode(self):
        return self.__encode

    def set_encode(self, encode):
        if self.__is_mononym():
            return

        self.__encode = encode

        return self

    def capital_family_name(self):
        if self.__is_mononym() or self.get_encode() == "eastern":
            return self

        clone = deepcopy(self)
        clone.set_name(clone.get_name("family").upper(), "family")

        return clone

    def initial_middle_name(self):
        if self.__is_mononym() or self.get_encode() == "eastern" or not self.get_name("middle"):
            return self

        clone = deepcopy(self)
        initialized_name = f"{clone.get_name('middle')[:1]}."
        clone.set_name(initialized_name, "middle")

        return clone

    def initial_given_name(self, include_middle=False):
        if self.__is_mononym() or self.get_encode() == "eastern":
            return self

        clone = deepcopy(self)
        initialized_name = f"{clone.get_name('given')[:1]}."
        clone.set_name(initialized_name, "given")

        if not include_middle and self.get_name("middle"):
            middle_removed_order = clone.get_order()
            middle_removed_order.remove("middle")

            clone.set_order(middle_removed_order)

        return clone

    def prefix(self, custom_prefix: str):
        clone = deepcopy(self)
        clone.set_name(custom_prefix, "prefix")

        return clone

    def suffix(self, custom_suffix: str):
        clone = deepcopy(self)
        clone.set_name(custom_suffix, "suffix")

        return clone

    def __get_space(self):
        encode = self.get_encode()
        return ' ' if encode == "western" else ''

    def __is_mononym(self):
        return isinstance(self.get_name(), str) and len(self.get_order()) == 0

    @staticmethod
    def is_name_valid(name) -> bool:
        if isinstance(name, dict):
            placeholders = list(name.keys())

            if len(placeholders) < 1:
                return False

            for placeholder in placeholders:
                if placeholder not in PLACEHOLDERS:
                    return False

        elif isinstance(name, str):
            if not name:
                return False

        return True

    @staticmethod
    def is_order_valid(order) -> bool:
        if not isinstance(order, list):
            return False

        for placeholder in order:
            if placeholder not in PLACEHOLDERS:
                return False

        return True
