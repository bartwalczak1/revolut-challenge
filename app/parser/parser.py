from typing import List, Union


class DataParser:
    """ Simple data parser class. """

    def __init__(self, keys, data):
        self.keys = keys
        self.data = data

    def parse_data(self) -> List:
        """
        Parse json data, into nested dict.

        :return: parsed json
        """
        parsed = []
        for group in self.data:
            group_keys = self.get_keys(group)
            for index in range(len(self.keys)):
                del group[self.keys[index]]
            nested_group = {}
            self._nest_dict(nested_group, group_keys, group)
            parsed.append(nested_group)

        return parsed

    def get_keys(self, data: dict) -> Union[List, Exception]:
        """
        Create a list of values from passed data dict.

        :param data: key, value data structure
        :return: list of values, or exception
        """
        return [data[key] for key in self.keys]

    @staticmethod
    def _nest_dict(nested_dict: dict, keys: list, non_grouped_dict: dict):
        """
        Nest dictionary from passed keys
        :param nested_dict: param used for nesting
        :param keys: keys to nest
        :param non_grouped_dict: key-value to add
        """
        for key in keys[:-1]:
            nested_dict = nested_dict.setdefault(key, {})
        nested_dict[keys[-1]] = [non_grouped_dict]
