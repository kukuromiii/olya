class Student:

    def init(self, name, firstname, age, growth, phone_num, mail, mama_name, papa_name, mama_phone_num, papa_phone_num, mama_mail, papa_mail, mama_age, papa_age, class_num, level_class, classroom, num_student_in_class, place_in_class, num_in_class, progress_place_in_class, gpa, attendance, favorite_teacher, favorite_leson, money, today_mood, today_satiety, today_clothes, today_energy ):

        super().init()
        self.name = name
        self.firstname = firstname
        self.age = age
        self.growth = growth
        self.phone_num = phone_num
        self.mail = mail
        self.mama_name = mama_name
        self.papa_name = papa_name
        self.mama_phone_num = mama_phone_num
        self.papa_phone_num = papa_phone_num
        self.mama_mail = mama_mail
        self.papa_mail = papa_mail
        self.mama_age = mama_age
        self.papa_age = papa_age
        self.class_num = class_num

        self.level_class = level_class

        self.classroom = classroom

        self.num_student_in_class = num_student_in_class

        self.place_in_class = place_in_class

        self.num_in_class = num_in_class

        self.progress_place_in_class = progress_place_in_class

        self.gpa = gpa

        self.attendance = attendance

        self.favorite_teacher = favorite_teacher

        self.favorite_leson = favorite_leson

        self.money = money

        self.today_mood = today_mood

        self.today_satiety = today_satiety

        self.today_clothes = today_clothes

        self.today_energy = today_energy

        self.math_knowledge = 0

        self.biology_knowledge = 0

        self.geography_knowledge = 0

        self.english_knowledge = 0

        self.german_knowledge = 0

        self.chinese_knowledge = 0

        self.spanish_knowledge = 0

        self.history_knowledge = 0

        self.business_knowledge = 0

        self.physics_knowledge = 0

        self.chemistry_knowledge = 0

        self.python_knowledge = 0

        self.blender_knowledge = 0

        self.ukr_literature_knowledge = 0

        self.world_literature_knowledge = 0

        self.ukr_language_knowledge = 0

        self.civil_education_knowledge = 0

        self.national_defense_knowledge_knowledge = 0

class Lessons(Student):

    def math(self):
        self.math_knowledge += 1
        self.today_mood -= 1
        self.today_energy -= 1.5

    def biology(self):
        self.biology_knowledge += 1
        self.today_mood -= 0.5
        self.today_energy -= 1.5

    def geography(self):
        self.geography_knowledge += 1
        self.today_mood -= 0.5
        self.today_energy -= 1.5

    def english(self):
        self.english_knowledge += 1
        self.today_mood -= 1
        self.today_energy -= 1.5

    def german(self):
        self.german_knowledge += 0.5
        self.today_mood -= 1
        self.today_energy -= 1.5

    def chinese(self):
        self.chinese_knowledge += 0.5
        self.today_mood -= 1
        self.today_energy -= 1.5

    def spanish(self):
        self.spanish_knowledge += 1
        self.today_mood -= 1
        self.today_energy -= 1.5

    def pe(self):
        self.today_mood += 1
        self.today_energy -= 3

    def history(self):

        self.history_knowledge += 1

        self.today_mood -= 1

        self.today_energy -= 1.5

    def business(self):

        self.business_knowledge += 1

        self.today_energy -= 1

    def physics(self):

        self.physics_knowledge += 1

        self.today_energy -= 1

    def chemistry(self):

        self.chemistry_knowledge += 0.5

        self.today_mood -= 1

        self.today_energy -= 1.5

    def python(self):

        self.python_knowledge += 1

        self.today_mood += 5

        self.today_energy -= 0

    def blender(self):

        self.blender_knowledge += 0.5

        self.today_energy -= 1

    def ukr_literature(self):

        self.ukr_literature_knowledge += 1

        self.today_mood += 1

        self.today_energy -= 1

def world_literature(self):

        self.world_literature_knowledge += 2

        self.today_mood += 1

        self.today_energy -= 1

def ukr_language(self):

        self.ukr_language_knowledge += 1

        self.today_mood += 1

        self.today_energy -= 1

    def civil_education(self):

        self.civil_education_knowledge += 1

        self.today_mood -= 1

        self.today_energy -= 1.5

    def national_defense(self):

        self.national_defense_knowledge += 1

        self.today_mood -= 1

        self.today_energy -= 1.5

class Pause(Lessons):

    def rest_time(self):

        print('Time to rest')

        self.today_mood += 2

        self.today_energy += 1

    def sleep(self):

        print('Time to sleep')

        self.today_energy += 2

    def pause(self):

        if self.today_mood < 5:

            self.rest_time()

        elif self.today_energy < 5:

            self.sleep()

class Time:

    def init(self):

        super(Time, self).init()

        self.lesson_time = 2700

        self.progect_time = 9000

        self.break1_time = 300

        self.break2_time = 600

        self.dinner = 1500

        def rest_time(self):

            print('Time to rest')

            self.knowledge -= 0.5

            self.mood += 2

            self.energy += 1

        def sleep(self):

            print('Time to sleep')

            self.energy += 2

        def pause(self):

            if self.mood < 5:

                self.rest_time()

            elif self.energy < 5:

                self.sleep()

student = Student('Alex', 'Ber', 15, 160, '0982937743', 'bora38290@gnail.com', 'Julia', 'Ivan', '0979151652', '097161553', 'aboabaasda@gmail.com', 'aboabaasda@gmail.com', 39, 40, 1, 9, 22, 12, 5, 4, 98, 'Abosfsdus', 'Math', 'Normal')

print(student.age)