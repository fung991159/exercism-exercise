def convert(number):
    factors = {
        3: "Pling",
        5: "Plang",
        7: "Plong"
    }
    output = ''
    for k in factors.keys():
        if number % k == 0:
            output += factors[int(k)]

    return output or str(number)