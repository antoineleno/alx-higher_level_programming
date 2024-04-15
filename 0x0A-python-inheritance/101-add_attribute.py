def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible.

    Args:
    - obj: The object to which the attribute will be added.
    - attr_name: The name of the attribute.
    - attr_value: The value of the attribute.

    Raises:
    - TypeError: If the object cannot have new attributes.
    """
    if isinstance(obj, type):
        setattr(obj, attr_name, attr_value)
    elif hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
