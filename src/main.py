from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=20)



# class Shop:
#     def __init__(self, name, date_of_create, type_of_shop):
#         self.name = name
#          --self.date_of_create = date_of_create
#         self.balance = 50000
#         self.type_of_shop = type_of_shop
#
#
# class Director:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.type_of_work = 'manage'
#
#
# class Personal:
#     def __init__(self,name,age,experiance,want_earn,type_of_work):
#         self.name = name
#         self.age = age
#         self.experiance = experiance
#         self.want_earn = want_earn
#         self.type_of_work = type_of_work
#         GetWork(name,age,experiance,want_earn,type_of_work)
#
#
# class GetWork:
#         def __init__(self,name,age,experiance,want_earn,type_of_work):
#             self.name = name
#             self.age = age
#             self.experiance = experiance
#             self.want_earn = want_earn
#             self.type_of_work = type_of_work
#             self.get_job = False
#             choice(self)
#
#
# def choice(self):
#         if self.type_of_work == 'shop assistant':
#             if self.experiance >=5:
#                 if self.want_earn <= 2500:
#                    self.get_job = True
#                    self.salary = self.want_earn
#                    print(f'Продавець - Вітаю ,{self.name},вас прийнято.Ваша заробітня плата {self.want_earn}')
#                 else:
#                     print(f"Продавець - Нас не влаштовує запропонована вам  заробітня плата!")
#             else:
#                 print(f'Продавець - Ваш досвіт роботи: {self.experiance} ,нам не підходить')
#
#         elif self.type_of_work == "loader":
#             if self.want_earn <= 1500:
#                 self.get_job = True
#                 self.salary = self.want_earn
#                 print(f'Гружчик - Вітаю ,{self.name},вас прийнято.Ваша заробітня плата {self.want_earn}')
#             else:
#                 print(f"Гружчик - Нас не влаштовує запропонована вам  заробітня плата!")
#
#         elif self.type_of_work == "guardian":
#             if self.want_earn <= 2500:
#                 self.get_job = True
#                 self.salary = self.want_earn
#                 print(f'Охоронець - Вітаю ,{self.name},вас прийнято.Ваша заробітня плата {self.want_earn}')
#             else:
#                 print(f"Охоронець - Нас не влаштовує запропонована вам  заробітня плата!")
#         elif self.type_of_work == "administrator":
#             if self.experiance >=10:
#                 if self.want_earn <= 3500:
#                    self.get_job = True
#
#                    print(f'Адміністратор - Вітаю ,{self.name},вас прийнято.Ваша заробітня плата {self.want_earn}')
#                 else:
#                     print(f"Адміністратор - Нас не влаштовує запропонована вам  заробітня плата!")
#             else:
#                 print(f'Адміністратор - Ваш досвіт роботи: {self.experiance} ,нам не підходить')
#
#         else:
#             print("Дана ваканція на даний момент не потрібна")
#
#
# def pay_salary(shop,shop_assistant,loader,guardian,administrator):
#     sum_salary = shop_assistant.want_earn+loader.want_earn+guardian.want_earn+administrator.want_earn
#     print(f'Магазину потрібно заплатити робітникам:{sum_salary}')
#     shop.balance-=sum_salary
#     print(f'Зарплата  робітникам виплачена баланс магазину:{shop.balance}')
#
#
# class Products:
#     def __init__(self,name_products,price,quantity,balance):
#         self.cost = price*quantity
#         self.name_products = name_products
#         balance-=self.cost
#         print(f'{self.name_products} - куплено на суму:{self.cost}')
#         print(f"Баланс магазину {balance}")
#
#
# def main():
#     director = Director('Dima','35')
#     shop = Shop('TelBlog','20.03.1999','grocery store')
#     shop_assistant = Personal('Olga',23,5,1500,'shop assistant')
#     loader = Personal('Oleg', 25, 0, 1500, 'loader')
#     guardian = Personal('Dima', 33,0, 2500, 'guardian')
#     administrator = Personal('Erick', 46, 15, 3500, 'administrator')
#     programer = Personal('Anna', 23, 5, 2500, 'Programmer')
#     print(f'Баланс магазину:{shop.balance}')
#     pay_salary(shop,shop_assistant,loader,guardian,administrator)
#     buy_product = Products('Помідор',20,100,shop.balance)
#
# main()
