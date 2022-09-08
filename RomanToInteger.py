def solution(string):
    dict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
            "XL": 40, "L": 50, "XC": 90, "C": 100,
            "CD": 400, "D": 500, "CM": 900, "M": 1000}

    digits = []

    while len(string) != 0:
        if len(string) == 1:
            digits.append(dict[string])
            string = string[:-1]

        elif dict[string[-1]] <= dict[string[-2]]:
            digits.append(dict[string[-1]])
            string = string[:-1]

        else:
            digits.append(dict[string[-2:]])
            string = string[:-2]

    return sum(digits)


print(solution("MCMXCIV"))