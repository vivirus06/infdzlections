def format_list(items):
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " и " + items[-1]

if __name__ == "__main__":
    items = []
    while (item := input("Введите элемент (или Enter): ")):
        items.append(item)
    print(format_list(items))
