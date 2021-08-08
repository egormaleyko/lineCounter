def lineCounter(filepath):
    try:
        file = open(filepath, 'r')
        amount = 0
        for line in file:
            amount += 1
    except Exception:
        amount = -1
    return amount


def main():
    print("Введите путь к файлу")
    filepath = input()
    lineAmount = lineCounter(filepath)
    if lineAmount > -1:
        print("Количество строк в файле: ", lineAmount)
    else:
        print("Ошибка")
    print("Для выхода нажмите любую клавишу")
    input()


main()
