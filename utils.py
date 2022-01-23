import re


def get_variable_from_polynomial_equation(s):
    dict = {
        8304: "0",
        185: "1",
        178: "2",
        179: "3",
        8308: "4",
        8309: "5",
        8310: "6",
        8311: "7",
        8312: "8",
        8313: "9",
    }
    # Remove spaces
    s = re.sub(r"\s", "", s)
    # Replace exponents by ^ format
    s = re.sub(
        r"([⁰¹²³⁴⁵⁶⁷⁸⁹]+)",
        lambda x: f"""^{''.join([dict[ord(i)] for i in x.group()])}""",
        s,
    )
    # Add 1 as exponent for x
    s = re.sub(r"(x(?!\^))", "\\1^1", s)
    # Add 1 as factor when x is alone
    s = re.sub(r"((?:(?<=[+-])|^)x)", "1x", s)

    factorexponent = re.finditer(r"([+-]?\d+)x\^(\d+)", s)
    const = sum(map(int, re.findall(r"(?:(?<=[+-])|^)\d+(?:(?=[+-])|$)", s)))
    data = [
        tuple(i)
        for i in map(
            lambda x: map(lambda x: int(x), x), [i.groups() for i in factorexponent]
        )
    ]

    dict = {}
    for i in sorted(data, key=lambda x: x[1], reverse=True):
        if i[1] in dict:
            dict[i[1]] += i[0]
        else:
            dict[i[1]] = i[0]
    if const != 0:
        dict[0] = const

    # return variables in a dynamic form as shown : {max exponent: factor, .... , constant(or 0 exponent): factor}
    return dict
