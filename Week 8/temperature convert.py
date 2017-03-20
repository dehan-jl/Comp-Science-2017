def convert_temp(t, src, trg):
    if src == 'k' or "kel" or "kelvin":
        tk = t
    elif src == 'c':# or "cel" or "celcius":
        tk = t + 273.15
    elif src == "f" or "fah" or "fahrenheit":
        tk = (t + 459.67) * (5 / 9)
    elif src == "ra" or "ran" or "rankine":
        tk = t * (5 / 9)
    elif src == "d" or "del" or "delisle":
        tk = 373.15 - (t * (2 / 3))
    elif src == "n" or "new" or "newton":
        tk = (t * (100 / 300)) - 273.15
    elif src == "re" or "rea" or "reaumur":
        tk = t * 1.25 + 273.15
    elif src == "ro" or "rom" or "romer":
        tk = (t - 7.5) * (40 / 21) + 273.15

    return tk


src = str(input("Source: "))
t = float(input("Temp: "))
trg = str(input("Target: "))

print(convert_temp(t, src, trg))
print(src, trg)

