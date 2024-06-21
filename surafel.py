class Personality:
    def persons_name(self, name):
        self.name = name
        return name

    def person_age(self, age):
        self.age = age
        return age

    def sex(self, sex):
        self.sex = sex

    def details(self):
        print(self.name, self.age, self.sex)


new_person = Personality()
new_person.name = "Surafel"
new_person.age = 56
new_person.sex = "Male"

Personality.details(new_person)
