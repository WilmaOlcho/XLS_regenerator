
def calculate_medium(working_range: list, values: list, maxchange=0.0, maxchangerequest=False) -> float:
    """Calculate the medium value of a list of values.

    :param working_range: The range of values to be used to calculate the medium.
    :param values: The list of values.
    :return: The medium value.
    """
    medium = list()
    for i, val in enumerate(values):
        if val >= working_range[0] and val <= working_range[1]:
            if any(medium):
                if maxchangerequest:
                    if ischangedTooQuickly(val, medium[-1], medium[-1], maxchange):
                        continue
            medium.append(val)
    return sum(medium) / len(medium)

def find_good_previous_value(working_range: list, values: list, current_index:int, maxchange=0.0, maxchangerequest=False) -> float:
    """Find the good previous value.

    :param working_range: The range of values to be used to calculate the medium.
    :param values: The list of values.
    :return: The good previous value.
    """
    if current_index == 0:
        return 0.0
    good_previous_values = list()
    previndex = 0
    if current_index >= 10:
        previndex = current_index - 10
    for i in values[previndex:current_index-1]:
        if i >= working_range[0] and i <= working_range[1]:
            if maxchangerequest:
                if any(good_previous_values):
                    if ischangedTooQuickly(i, good_previous_values[-1], good_previous_values[-1], maxchange):
                        continue
            good_previous_values.append(i)
    if not any(good_previous_values):
        return 0.0
    return good_previous_values[-1]

def find_good_next_value(working_range: list, values: list, current_index:int, maxchange=0.0, maxchangerequest=False) -> float:
    """Find the good next value.

    :param working_range: The range of values to be used to calculate the medium.
    :param values: The list of values.
    :return: The good next value.
    """
    if current_index == len(values):
        return 0.0
    good_next_values = list()
    nextindex = len(values)-1
    if current_index < nextindex - 10:
        nextindex = current_index + 10
    for i in values[current_index:nextindex]:
        if i >= working_range[0] and i <= working_range[1]:
            if maxchangerequest:
                if any(good_next_values):
                    if ischangedTooQuickly(i, good_next_values[-1], good_next_values[-1], maxchange):
                        continue
            good_next_values.append(i)
            if len(good_next_values) > 1:
                return i
    if not any(good_next_values):
        nextindex = len(values)-1
        if current_index < nextindex - 100:
            nextindex = current_index + 100
        for i in values[current_index:nextindex]:
            if i >= working_range[0] and i <= working_range[1]:
                if maxchangerequest:
                    if any(good_next_values):
                        if ischangedTooQuickly(i, good_next_values[-1], good_next_values[-1], maxchange):
                            continue
                good_next_values.append(i)
                if len(good_next_values) > 1:
                    return i
    return good_next_values[0]
    
def ischangedTooQuickly(current_value: float, previous_value: float, next_value: float, maxchange: float) -> bool:
    if abs(current_value - previous_value) > maxchange:
        return True
    if abs(current_value - next_value) > maxchange:
        return True
    return False