import random


class Keg:
    def __init__(self) -> None:
        self.numbers = list(range(1, 91))

    def __str__(self) -> str:
        return ' '.join(map(str, self.numbers))
    
    def get_keg(self) -> int:
        result = random.sample(self.numbers, 1)[0]
        self.numbers.remove(result)
        print(f"\n********************\n Выпало число: {result} \n********************\n")
        return result


if __name__ == '__main__':
    my_keg = Keg()
    print(my_keg)

    print(f"Вы вытянули боченок: {my_keg.get_keg()}")
    print(f"Вы вытянули боченок: {my_keg.get_keg()}")
    print(f"Вы вытянули боченок: {my_keg.get_keg()}")
    print(f"Вы вытянули боченок: {my_keg.get_keg()}")
    print(f"Вы вытянули боченок: {my_keg.get_keg()}")
    print(my_keg)
    