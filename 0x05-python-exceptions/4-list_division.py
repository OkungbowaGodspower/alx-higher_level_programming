#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.
    Args:
        my_list (list): The first list.
        my_list_1 (list): The second list.
        list_length (int): The number of elements to divide.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    add_list = []
    for i in range(0, list_length):
        try:
            divide = my_list[i] / my_list_1[i]
        except TypeError:
            print("wrong type")
            divide = 0
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except IndexError:
            print("out of range")
            divide = 0
        finally:
            add_list.append(divide)
    return (add_list)
