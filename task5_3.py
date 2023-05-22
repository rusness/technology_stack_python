

investment_amount = int(input("Сумма инвестиций: "))
mike_amount = int(input("Сумма Майкла: "))
ivan_amount = int(input("Сумма Ивана: "))

# 1 Майкл и Иван могут вложиться оба
if mike_amount >= investment_amount and ivan_amount >= investment_amount:
    print("2")

# 2 если только Майк
if mike_amount >= investment_amount and ivan_amount < investment_amount:    
    print("Mike")

# 3 если только Иван
if mike_amount < investment_amount and ivan_amount >= investment_amount:
    print("Ivan")

# 4 если не могут по отдельности но вместе могут
if (mike_amount < investment_amount and ivan_amount < investment_amount) and (mike_amount + ivan_amount >= investment_amount):
    print("1")

# 5 никто не может
if  (mike_amount + ivan_amount < investment_amount):
    print("0")