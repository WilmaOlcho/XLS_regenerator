
def calculate_medium(working_range: list, values: list) -> float:
    """Calculate the medium value of a list of values.

    :param working_range: The range of values to be used to calculate the medium.
    :param values: The list of values.
    :return: The medium value.
    """
    medium = list()
    for i in values:
        if i >= working_range[0] and i <= working_range[1]:
            medium.append(i)
    return sum(medium) / len(medium)

def find_good_previous_value(working_range: list, values: list, current_index:int) -> float:
    """Find the good previous value.

    :param working_range: The range of values to be used to calculate the medium.
    :param values: The list of values.
    :return: The good previous value.
    """
    if current_index == 0:
        return 0.0
    good_previous_values = list()
    for i in values[:current_index-1]:
        if i >= working_range[0] and i <= working_range[1]:
            good_previous_values.append(i)
    if len(good_previous_values) == 0:
        return 0.0
    return good_previous_values[-1]

def find_good_next_value(working_range: list, values: list, current_index:int) -> float:
    """Find the good next value.

    :param working_range: The range of values to be used to calculate the medium.
    :param values: The list of values.
    :return: The good next value.
    """
    if current_index == len(values):
        return 0.0
    good_next_values = [0]
    for i in values[current_index+1:]:
        if i >= working_range[0] and i <= working_range[1]:
            good_next_values.append(i)
    if len(good_next_values) == 0:
        return 0.0
    return good_next_values[0]
    
