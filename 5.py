количество_маленьких = int(input("Введите количество бутылок объемом 1 литр и меньше: "))
количество_больших = int(input("Введите количество бутылок объемом более 1 литра: "))
депозит_маленький = 0.10
депозит_большой = 0.25
сумма = (количество_маленьких * депозит_маленький) + (количество_больших * депозит_большой)
print(f"Сумма возврата: ${сумма:.2f}")
