def ops_check(expression_str):
    """Applies basic operators to sets of two numbers and returns the result."""

    # The operator module allows us to use operators as methods.
    import operator

    # Defines a dictionary that associates string operators with actual operators (from the module).
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        ">": operator.gt,
        "<": operator.lt,
    }

    # Appends all elements of the expression to a list. String integers are converted to integers.
    # All other characters are appended, as well. Whitespace is removed.
    list = []
    for i in expression_str:
        try:
            if isinstance(int(i), int):
                list.append(int(i))
        except TypeError:
            list.append(i)
        except ValueError:
            list.append(i)
        if i == ' ':
            list.remove(i)

    # Appends all integers only to a new list. Also checks to see if there are any string operators.
    # If so, it is used as a reference key in the ops dictionary, and then the two numbers in the
    # nums_only list are added as arguments into the corresponding operation associated with said
    # string operator. If using gt (>) or lt (<), Boolean values are returned.
    nums_only = []
    for i in list:
        if isinstance(i, int):
            nums_only.append(i)
    for i in list:
        if i in ops.keys():
            result = ops[i](nums_only[0], nums_only[1])  # Nums > 9 won't work because of indices.

    # Mathematical result is returned.
    return result


print(ops_check(" > 6"))
