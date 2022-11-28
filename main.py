import random

class Student:
    def __init__(self, first_name):
        self.first_name = first_name
        self.knowledge = 0
        self.today_mood = 10
        self.energy = 10
        self.today_satiety = 10
        self.alive = True


# усі предмети

class Lessons(Student):
    def math(self):
        self.knowledge += 1
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def biology(self):
        self.knowledge += 1
        self.today_mood -= 0.5
        self.energy -= 1.5
        self.today_satiety -= 1

    def geography(self):
        self.knowledge += 1
        self.today_mood -= 0.5
        self.energy -= 1.5
        self.today_satiety -= 1

    def english(self):
        self.knowledge += 1
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def german(self):
        self.knowledge += 0.5
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def chinese(self):
        self.knowledge += 0.5
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def spanish(self):
        self.knowledge += 1
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def pe(self):
        self.today_mood += 1
        self.energy -= 5
        self.today_satiety -= 3

    def history(self):
        self.knowledge += 1
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def business(self):
        self.knowledge += 1
        self.today_mood -= 1
        self.energy -= 1
        self.today_satiety -= 1

    def physics(self):
        self.knowledge += 0.5
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def chemistry(self):
        self.knowledge += 0.5
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def python(self):
        self.knowledge += 1
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def blender(self):
        self.knowledge += 0.5
        self.today_mood -= 1
        self.energy -= 1
        self.today_satiety -= 1

    def ukr_literature(self):
        self.knowledge += 1
        self.today_mood += 1
        self.energy -= 1
        self.today_satiety -= 1

    def world_literature(self):
        self.knowledge += 1
        self.today_mood += 1
        self.energy -= 1
        self.today_satiety -= 1

    def ukr_language(self):
        self.knowledge += 1
        self.today_mood += 1
        self.energy -= 2
        self.today_satiety -= 1

    def civil_education(self):
        self.knowledge += 0.5
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1

    def national_defense(self):
        self.knowledge += 0.5
        self.today_mood -= 1
        self.energy -= 1.5
        self.today_satiety -= 1


class Pause(Lessons):
    def rest_time(self):
        print('Час відпочивати')
        self.today_mood += 2
        self.energy += 2


    def sleep(self):
        print('Час спати')
        self.knowledge -= 1
        self.energy += 2


    def lunch(self):
        print('Час їсти')
        self.today_satiety += 2


    # рандомні предмети

    def study(self):
        print(f'День {day:^5d} з життя {self.first_name}а')
        print('Час вчитися')
        cube = random.randint(1, 19)
        if cube == 1:
            self.math()
        elif cube == 2:
            self.biology()
        elif cube == 3:
            self.geography()
        elif cube == 4:
            self.english()
        elif cube == 5:
            self.german()
        elif cube == 6:
            self.chemistry()
        elif cube == 7:
            self.spanish()
        elif cube == 8:
            self.pe()
        elif cube == 9:
            self.history()
        elif cube == 10:
            self.business()
        elif cube == 11:
            self.physics()
        elif cube == 12:
            self.chemistry()
        elif cube == 13:
            self.python()
        elif cube == 14:
            self.blender()
        elif cube == 15:
            self.ukr_literature()
        elif cube == 16:
            self.world_literature()
        elif cube == 17:
            self.ukr_language()
        elif cube == 18:
            self.civil_education()
        elif cube == 19:
            self.national_defense()


    def get_today(self, day):
        print(f'Настрій = {self.today_mood}')
        print(f'Енергія = {self.energy}')
        print(f'Ситість = {self.today_satiety}')
        print(f'Знання = {round(self.knowledge, 2)}')


    def pause(self):
        if self.today_mood < 5:
            self.rest_time()
        elif self.energy < 5:
            self.sleep()
        elif self.knowledge < 5:
            self.study()
        elif self.today_satiety < 5:
            self.lunch()


    def life(self):
        if self.knowledge > 10:
            print('Склав іспит')
        elif self.knowledge < -10:
            print('Відрахований')
        elif self.today_satiety < -10:
            print('Вмер...')
            self.alive = False
        elif self.energy < -10:
            print('Вмер...')
            self.alive = False
        elif self.today_mood < -10:
            print('Депресія...')
            self.alive = False


student = Pause('школярик')
for day in range(1, 100):
    if student.alive == False:
        break
    student.get_today(day)
    student.pause()