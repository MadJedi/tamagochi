class Tamagochi(object):
    """Игра Тамагочи"""
    def __init__(self, name, hunger = 0, bored = 0):
        self.name = name
        self.hunger = hunger
        self.bored = bored

    def __pass_time(self):
        self.hunger += 1
        self.bored += 1

    @property
    def mood(self):
        unhappy = self.hunger + self.bored
        if unhappy < 5:
            m = 'Всё хорошо'
        elif 5 <= unhappy <= 10:
            m = 'Нормально'
        elif 11 <= unhappy <= 15:
            m = 'Я чувствую себя плохо'
        else:
            m = 'Я в депрессии...'
        return m

    def talk(self):
        print("Меня зовут", self.name, "я чувствую себя", self.mood, "\n")
        self.__pass_time()

    def eat(self, food = 4):
        print("Ням. Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Урааа!")
        self.bored -= fun
        if self.bored < 0:
            self.bored = 0
        self.__pass_time()

def main():
    tama_name = input("Как вы хотите назвать своего тамагоча?: ")
    tama = Tamagochi(tama_name)
    
    choice = None
    while choice != '0':
        print("""
        Меню игры. Что вы хотите сделать?
        0 - Выйти
        1 - Узнать как дела у тамагочи
        2 - Покормить
        3 - Поиграть
        """)

        choice = input("Ваш выбор: ")
        print()

        # условия выхода, доделать меню выхода
        if choice == "0":
            print(input("Вы точно хотите выйти? Тамагочи может быть голоден или в депрессии? Нажмите Enter чтобы выйти "))
            print("До скорой встречи. Не забывайте о тамагочи")
        elif choice == "1":
            tama.talk()
        elif choice == "2":
            tama.eat()
        elif choice == "3":
            tama.play()
        else:
            print("\nИзвините но пункта", choice, "нет в меню.")

main()
