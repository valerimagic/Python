term_dogovor = input()
type_dogovor = input()
internet = input()
monts_for_payment = int(input())

count = 0

if term_dogovor == "one":
    if type_dogovor == "Small":
        if internet == "yes":
            count = (9.98 + 5.5) * monts_for_payment
        else:
            count = 9.98 * monts_for_payment
    elif type_dogovor == "Middle":
        if internet == "yes":
            count = (18.99 + 4.35) * monts_for_payment
        else:
            count = 18.99 * monts_for_payment
    elif type_dogovor == "Large":
        if internet == "yes":
            count = (25.98 + 4.35) * monts_for_payment
        else:
            count = 25.98 * monts_for_payment
    elif type_dogovor == "ExtraLarge":
        if internet == "yes":
            count = (35.99 + 3.85) * monts_for_payment
        else:
            count = 35.99 * monts_for_payment
elif term_dogovor == "two":
    if type_dogovor == "Small":
        if internet == "yes":
            count = ((8.58 + 5.5) * monts_for_payment) * 0.9625
        else:
            count = (8.58 * monts_for_payment) * 0.9625
    elif type_dogovor == "Middle":
        if internet == "yes":
            count = ((17.09 + 4.35) * monts_for_payment) * 0.9625
        else:
            count = (17.09 * monts_for_payment) * 0.9625
    elif type_dogovor == "Large":
        if internet == "yes":
            count = ((23.59 + 4.35) * monts_for_payment) * 0.9625
        else:
            count = (23.59 * monts_for_payment) * 0.9625
    elif type_dogovor == "ExtraLarge":
        if internet == "yes":
            count = ((31.79 + 3.85) * monts_for_payment) * 0.9625
        else:
            count = (31.79 * monts_for_payment) * 0.9625




print(f"{count:.2f} lv.")