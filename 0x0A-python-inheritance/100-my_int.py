#!/usr/bin/python3
"""my_int module"""


class MyInt(int):
    """my_int_class

    Args:
        int (_type_): _description_
    """
    def __eq__(self, other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        return super().__eq__(other)
