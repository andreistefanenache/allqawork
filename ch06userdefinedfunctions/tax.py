def get_income_tax(gross_income):
    if gross_income <= 11_850:
        return 0
    tax=0
    gross_income -= 11_850
    tax+=min(gross_income,34_500)*0.2
    if gross_income <= 34_500:
        return tax
    gross_income -= 34500
    tax += min(gross_income,150_000-34_500)*0.4
    if gross_income <= 150_000-34_500:
        return tax
    gross_income-=150_000-34_500
    tax += gross_income * 0.45
    return tax
print(get_income_tax(int(input("Please enter your gross yearly income: "))))
