#1
class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value.lower()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if '@' in value:
            self.__email = value
        else:
            print("Email noto‘g‘ri kiritildi!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value
        else:
            print("Yosh manfiy bo‘lishi mumkin emas!")

info = User('Lobar', 'farxodva@gmail.com', 20)

print(info.username)
print(info.email)
print(info.age)
