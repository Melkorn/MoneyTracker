import sys
import sqlite3
import tkinter as tk
from tkinter import ttk
from gui import BudgetYearMonthMenu
from peewee import *

# Connect to the SQLite database
db = SqliteDatabase('moneyTracker.db')

class BaseModel(Model):
    class Meta:
        database = db

menu_start_1 = "Stwórz nowy Budżet"
menu_start_2 = "Wczystaj Budżet"
menu_start_3 = "Lista budżetów"
menu_start_4 = "Opcje"
menu_start_5 = "Wyjdz"

menu_options_1 = "Waluty"
menu_options_2 = "Dodaj Walute"
menu_options_3 = "Cofnij"

menu_budzet_1 = "Dodaj nowy rok"
menu_budzet_2 = "Wybierz rok"
menu_budzet_3 = "Podsumowanie budżetu roczne"
menu_budzet_4 = "Podsumowanie budżetu miesięczne"
menu_budzet_5 = "Zmień ustawienia budżetu"
menu_budzet_6 = "Cofnij"
menu_budzet_7 = "Zakończ"


menu_2_1 = "Wybierz Miesiąc"
menu_2_2 = "Brak"
menu_2_3 = "Wyświetl podsumowanie roku"
menu_2_4 = "Brak"
menu_2_5 = "Brak"
menu_2_6 = "Cofnij"

menu_month_1 = "Dodaj prognozowany przychód"
menu_month_2 = "Dodaj prognozowany wydatek"
menu_month_3 = "Dodaj rzeczywisty przychód"
menu_month_4 = "Dodaj rzeczwisty wydatek"
menu_month_5 = "Wyświetl szczegóły miesiąca"
menu_month_6 = "Podsumowanie miesiąca"
menu_month_7 = "Zamknij miesiac"
menu_month_8 = "Cofnij"

yes = "Tak"
no = "Nie"

class Waluta:
    def __init__(self, name: str, matchcode: str, ratio_dolar: float):
        self.name = name
        self.matchcode = matchcode
        ratio_dolar = ratio_dolar

class List_Walut():
    
    def __init__(self):
        self.waluty = []
    
    def add_currency(self, waluta: Waluta):
        self.waluty.append(waluta)
    
    def show(self):
        for i in range(len(self.waluty)):
                    print(f"{i+1}. {self.waluty[i].name} {self.waluty[i].matchcode}")
        
    def chose_currency(self):
        self.show()
        again = True
        while again:
            i = int(input("Wybierz walute: "))
            if(i <=  (len(self.waluty))):
                currency = self.waluty[i-1]
                again = False
            else:
                print("brak takiej pozycji")
            
        return currency

class Budget():
    
    def __init__(self, lista_walut: List_Walut):
        self.name: str
        self.years = []
        self.create(lista_walut)

    def name_show(self):
        return self.name

    def create(self, lista_currency: List_Walut):
        
       self.name = str(input("Nazwij Budzet"))
       print("Tworzenie Budzetu: " + self.name)
        
       self.currency = lista_currency.chose_currency()
    
    def list_years(self):
        year_list = []
        for i in range(len(self.years)):
            year_list.append(self.years[i].name())
        return year_list
            


class Year():
    
    def __init__(self, year: int, waluta_yr: Waluta, budzet: Budget):

        self.year = year
        self.months = [Month(i) for i in range(1, 13)]
        self.waluta_yr = waluta_yr
        self.budget = budzet
        budzet.years.append(self)
    
    def name(self):
        return str(self.year)

def menu_budzet(budzet: Budget):
    while True:
            print()
            print("Menu")
            print(menu_budzet_1)
            print(menu_budzet_2)
            print(menu_budzet_3)
            print(menu_budzet_4)
            print(menu_budzet_5)
            print(menu_budzet_6)
            print(menu_budzet_7)

            choice = int(input("wybieram: "))
            if choice == 1:

                print()
                print(menu_budzet_1)
                year = int(input("Podaj Rok"))
                print()
                nw_yr = Year(year, budzet.currency, budzet)               
            

            elif choice == 2:
                print()
                print(menu_budzet_2)
                for i in range(len(budzet.years)):
                    print("Rok: " + str(budzet.years[i].year))

                wybor =int(input(menu_budzet_2))
                #otworz dany rok w budzecie
                menu_2(budzet.years[wybor-1])

            elif choice ==3:
                print()
                print(menu_budzet_3)
            elif choice == 4:
                print()
                print(menu_budzet_4)
            elif choice ==5:
                print()
                print(menu_budzet_5)
            elif choice ==6:
                print()
                print(menu_budzet_6)
            elif choice ==7:
                print()
                print(menu_budzet_7)
            else:
                print("Wybór nieznany")


class Lista:
    def __init__(self):
        self.lista_budzetow = []

    def __init__(self, lista_walut: List_Walut):
        self.lista_walut = lista_walut
        self.lista_budzetow = []

    def add(self, budzet: Budget):
        self.lista_budzetow.append(budzet)

    def show(self):
        for i in range(len(self.lista_budzetow)):
           
            print("Budzet: " + self.lista_budzetow[i].name_show())
            print()
        return
    
    def name_list(self):
        list_names = []
        for i in range(len(self.lista_budzetow)):
            list_names.append(self.lista_budzetow[i].name_show())

        return list_names

    def create_buget(self):
        budzet = Budget(lista_walut)
        self.lista_budzetow.append(budzet)


    def ilosc(self):
        return len(self.lista_budzetow)

    def menu_start(self):
        # self.lista_walut = lista_walut
        while True:
            print()
            print("Menu")
            print(menu_start_1)
            print(menu_start_2)
            print(menu_start_3)
            print(menu_start_4)
            print(menu_start_5)


            choice = int(input("wybieram: "))
            if(choice == 1):
                self.create_buget()
            

            elif choice == 2:
                    print(self.show())
                    
                    choice = int(input("wybierz budzet"))
                    if choice <= self.ilosc():
                        menu_budzet(self.lista_budzetow[choice-1])
                    else:
                        print("Nie ma takiego budżetu")
            elif choice ==3:
                print(self.show())
            elif choice == 4:
                print()
            elif choice ==5:
                print()
            else:
                print("Wybór nieznany")

class Kwota:
    def __init__(self, waluta: Waluta, kwota: float):
        self.waluta = waluta
        self.kwota = kwota

class Pozycja:
    def __init__(self, wartosc: Kwota, cel: str):
        self.wartosc = wartosc
        self.cel = cel
    
    def show(self):
        print(str(self.wartosc.kwota) + " : " + self.wartosc.waluta.matchcode + " : " + self.cel)

    def calc(self):
        return self.wartosc.kwota   

class Month: 
    def __init__(self, number: int):
        self.number = number
        self.closed = False

    income_exp = []
    income_real = []
    outcome_exp = []
    outcome_real = []
    closed = False

    wynik: Kwota

    def close_month(self):
        self.closed = True

    def add_exp_inc(self, amount, currency, cel: str):
        kwota = Kwota(currency, amount)
        pozycja = Pozycja(kwota, cel)
        self.income_exp.append(pozycja)

    def add_real_inc(self, amount, currency, cel: str):
        kwota = Kwota(currency, amount)
        pozycja = Pozycja(kwota, cel)
        self.income_real.append(pozycja)

    def add_exp_out(self, amount, currency, cel: str):
        kwota = Kwota(currency, amount)
        pozycja = Pozycja(kwota, cel)
        self.outcome_exp.append(pozycja)

    def add_real_out(self, amount, currency, cel: str):
        kwota = Kwota(currency, amount)
        pozycja = Pozycja(kwota, cel)
        self.outcome_real.append(pozycja)

    def show(self):
        
        print("------------") 
        print("Wpływy spodziewane: ")
        if len(self.income_exp)>0:
            for i in range(len(self.income_exp)):
                self.income_exp[i].show()
        else:
            print("Brak")
            print()
        
        print("------------") 
        print("Wpływy: ")
        
        if len(self.income_real)>0:
            for i in range(len(self.income_real)):
                self.income_real[i].show()
        else:
            print("Brak")
            print()

        print("------------") 
        print("Wydatki spodziewane: ")

        if len(self.outcome_exp)>0:
            for i in range(len(self.outcome_exp)):
                self.outcome_exp[i].show()
        else:
            print("Brak")
            print()

        print("------------") 
        print("Wydatki: ")

        if len(self.outcome_real)>0:
            for i in range(len(self.outcome_real)):
                self.outcome_real[i].show()
        else:
            print("Brak")
            print()
    
    def calculate_sum(self, positions: list[Pozycja] ):
        wynik = 0.0
        if len(positions) > 0:
            for i in range (len(positions)):
                wynik = wynik + positions[i].calc()
        
        return wynik

    def inc_sum_ex_rl(self):
        wynik_exp = self.calculate_sum(self.income_exp)
        wynik_real = self.calculate_sum(self.income_real)
        roznica = wynik_exp - wynik_real
        return roznica
        # Roznica miedzy spodziewanym dochodem a dochodem rzeczywistym

    def out_sum_ex_rl(self):
        wynik_exp = self.calculate_sum(self.outcome_exp)
        wynik_real = self.calculate_sum(self.outcome_real)
        roznica = wynik_exp - wynik_real
        return roznica
        # Roznica miedzy spodziewanymi wydatkami a wydatkami rzeczywistymi

    def exp_sum(self):
        wynik_inc = self.calculate_sum(self.income_exp)
        wynik_out = self.calculate_sum(self.outcome_exp)
        roznica = wynik_inc - wynik_out
        return roznica
        # Roznica miedzy oczekiwanym przychodem a odczekiwanym wydatkiem

    def real_sum(self):
        wynik_inc = self.calculate_sum(self.income_real)
        wynik_out = self.calculate_sum(self.outcome_real)
        roznica = wynik_inc - wynik_out
        return roznica
        # Roznica miedzy rzeczywistym przychodem a rzeczywistym wydatkiem

    def sumAll(self):

        print("Podsumowanie Miesiaca " + str(self.number -1) + " :")
        print()

        print("Spodziewany Przychod: ")
        print(str(self.calculate_sum(self.income_exp)))
        print()
        print("------------------------------------")
        print()
        print("Rzeczwystisty Przychod: ")
        print(str(self.calculate_sum(self.income_real)))
        print()
        print("------------------------------------")
        print()
        print("Spodziewane Wydatki: ")
        print(str(self.calculate_sum(self.outcome_exp)))
        print()
        print("------------------------------------")
        print()
        print("Rzeczywiste Wydatki: ")
        print(str(self.calculate_sum(self.outcome_real)))
        print()
        print("------------------------------------")
        print()

        print("Wynik Spodziewany: ")
        print(str(self.exp_sum()))
        print()
        print("------------------------------------")
        print()

        print("Wynik Rzeczwysity: ")
        print(str(self.real_sum()))
        print()
        print("------------------------------------")
        print()


        if(self.inc_sum_ex_rl() > 0):
            print("Rzeczywisty dochod niższy od spodziewanego o: " + str(self.inc_sum_ex_rl()))
        elif(self.inc_sum_ex_rl() == 0):
            print("Progonzowany dochod zostal calkowicie zrealizowany")
        else:
            print("Dochod rzeczywisty wyzszy niz spodziewano: " + str(self.inc_sum_ex_rl()))

        if(self.out_sum_ex_rl() > 0):
            print("Rzeczywiste wydatki niższe od spodziewanych o: " + str(self.out_sum_ex_rl()))
        elif(self.out_sum_ex_rl() == 0):
            print("Progonzowane wydatki byly calkowicie dokladnie")
        else:
            print("Wydatki rzeczywiste przekroczyly spodziewane 0 : " + str(self.out_sum_ex_rl()))

        print("")

        print()

    def real_sum_in_ou(self):
        print()
        # t




class Currency_Base(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    matchcode = CharField()
    exchangeRate = DecimalField()

class Budget_Base(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    currency = CharField() # Waluta to obiekt a nie String, potem zmienie
    @classmethod
    def create_budget(cls, budget: Budget):
        cls.create(name=budget.name, currency=budget.currency)

    @classmethod
    def update_budget(cls, budget: Budget):
        budget_db = cls.get(cls.id == budget.id)
        budget_db.name = budget.name
        budget_db.currency = budget.currency
        budget_db.save()
    
    @classmethod
    def delete_budget(cls, budget: Budget):
        cls.delete().where(cls.id == budget.id).execute()

class Year_Base(BaseModel):
    
    id = PrimaryKeyField()
    number = IntegerField()
    currency = ForeignKeyField(Currency_Base, backref='year')
    budget = ForeignKeyField(Budget_Base, backref='years')

class Month_Base(BaseModel):
    id = PrimaryKeyField()
    number = IntegerField()
    year = ForeignKeyField(Year_Base, backref='months')
    income_exp_sum = DecimalField()
    income_real_sum = DecimalField()
    outcome_exp_sum = DecimalField()
    outcome_real_sum = DecimalField()

class Income_Exp_Base(BaseModel):
    id = PrimaryKeyField()
    month = ForeignKeyField(Month_Base, backref='Income_Exp')
    currency = ForeignKeyField(Currency_Base, backref='Income_Exp')
    purpose = CharField()

class Income_Real_Base(BaseModel):
    id = PrimaryKeyField()
    month = ForeignKeyField(Month_Base, backref='Income_Real')
    currency = ForeignKeyField(Currency_Base, backref='Income_Real')
    purpose = CharField()

class Outcome_Exp_Base(BaseModel):
    id = PrimaryKeyField()
    month = ForeignKeyField(Month_Base, backref='Outcome_Exp')
    currency = ForeignKeyField(Currency_Base, backref='Outcome_Exp')
    purpose = CharField()

class Outcome_Real_Base(BaseModel):
    id = PrimaryKeyField()
    month = ForeignKeyField(Month_Base, backref='Outcome_Real')
    currency = ForeignKeyField(Currency_Base, backref='Outcome_Real')
    purpose = CharField()


db.connect()
db.create_tables([Budget_Base, Year_Base, Month_Base, Income_Exp_Base, Income_Real_Base, Outcome_Exp_Base, Outcome_Real_Base, Currency_Base])

def menu_2(rok: Year):
    while True:

        print("Menu")
        print(menu_2_1)
        print(menu_2_2)
        print(menu_2_3)
        print(menu_2_4)
        print(menu_2_5)
        print(menu_2_6)
            
        wybor = int(input("Wybieram"))

        if wybor == 1:
            print(menu_2_1)
            month = int(input("wybierz miesiąc: 1 - 12: "))
            if month not in range(1,12):
                print("Brak lub zły wybór")
            else:
                print("Wybrano miesiąc: " + str(month))
                menu_month(rok.months[month], rok)
        elif wybor ==2:
            print()
        elif wybor ==3:
            print()
        elif wybor ==4:
            print()
        elif wybor ==5:
            print()
        elif wybor ==6:
            print()
        else:
            print("Wybór nieznany")

def menu_month(month: Month, rok: Year):
        repeat = True
        while repeat:
            print()
            print("Menu")
            print(menu_month_1)
            print(menu_month_2)
            print(menu_month_3)
            print(menu_month_4)
            print(menu_month_5)
            print(menu_month_6)
            print(menu_month_7)
            print(menu_month_8)
            wybor = int(input("Wybierz opcje"))

            if wybor == 1:
                print("Dodaj spodziewany przychód w walucie " + rok.waluta_yr.name)
                print()
                kwota = float(input("Kwota"))
                cel = str(input("Zrodlo"))

                month.add_exp_inc(kwota, rok.waluta_yr, cel)
                print()
            # income = pozycja
            elif wybor == 2:
                print("Dodaj planowany wydatek w walucie " + rok.waluta_yr.name)
                print()
                kwota = float(input("Kwota"))
                cel = str(input("Cel"))

                month.add_exp_out(kwota, rok.waluta_yr, cel)
                print()
            elif wybor == 3:
                print("Dodaj rzeczywisty przychód w walucie " + rok.waluta_yr.name)
                print()
                kwota = float(input("Kwota"))
                cel = str(input("Zrodlo"))

                month.add_real_inc(kwota, rok.waluta_yr, cel)
                print()
            elif wybor == 4:
                print("Dodaj rzeczywisty wydatek w walucie " + rok.waluta_yr.name)
                print()
                kwota = float(input("Kwota"))
                cel = str(input("Cel"))

                month.add_real_out(kwota, rok.waluta_yr, cel)
                print()
            elif wybor == 5:
                month.show()
                print()

            elif wybor == 6:
                month.sumAll()
                print()

            elif wybor == 7:
                rep = True
                while rep:
                    sure =str(input("Czy jesteś pewien, że chcesz zamknąć ten miesiąc? y - Tak, n- Nie"))

                    if sure == "y":
                        month.close_month()
                        print("Miesiąc " + str(month.number) + " zostal zamknięty, nie można dodawać dalszych pozycji")
                        print()
                        rep = False
                    elif sure == "n":
                        print("Zrezygnowałeś z zamknięcia miesiąca")
                        print()
                        rep = False
                    else:
                        print("Błąd, nierozpoznany wybór")
                        print()

            elif wybor == 8:
                print("cofnij")
                repeat = False
            else:
                print("wybór nieznany")


lista_walut = List_Walut()
lista_walut.add_currency(Waluta("Polski Zloty", "PLN", 4.50))
lista_walut.add_currency(Waluta("Euro", "EUR", 1.01))
lista_walut.add_currency(Waluta("Dolar Amerykanski", "USD", 1.00))
lista_walut.add_currency(Waluta("Funt", "GBP", 1.3))



print()


lista = Lista(lista_walut)

wybor = int(input("wybrac startowa liste budzetow i lat? 1 - Tak, 2 = Nie"))
if(wybor != 1):
    print()
else:
    budzet_test_1 = Budget(lista_walut)
    budzet_test_2 = Budget(lista_walut)
    budzet_test_3 = Budget(lista_walut)

    rok1 = Year(2021, budzet_test_1.currency, budzet_test_1)
    rok2 = Year(2022, budzet_test_1.currency, budzet_test_1)
    rok3 = Year(2023, budzet_test_1.currency, budzet_test_1)

    rok11 = Year(2021, budzet_test_2.currency, budzet_test_2)
    rok21 = Year(2022, budzet_test_2.currency, budzet_test_2)
    rok31 = Year(2023, budzet_test_2.currency, budzet_test_2)

    rok12 = Year(2021, budzet_test_3.currency, budzet_test_3)
    rok22 = Year(2020, budzet_test_3.currency, budzet_test_3)
    rok32 = Year(2023, budzet_test_3.currency, budzet_test_3)
    rok42 = Year(2024, budzet_test_3.currency, budzet_test_3)
    rok52 = Year(2025, budzet_test_3.currency, budzet_test_3)


 

    lista.add(budzet_test_1)
    lista.add(budzet_test_2)
    lista.add(budzet_test_3)

if __name__ == "__main__":

    root = tk.Tk()
    BudgetYearMonthMenu(root, lista.lista_budzetow)
    root.mainloop()

if int(input("Zapisac testowe budzety do bazy? 1 - tak, 2 - nie")) == 1:

    Budget_Base.create_budget(budzet_test_1)
    Budget_Base.create_budget(budzet_test_2)
    Budget_Base.create_budget(budzet_test_3)
else:
    print("Brak Zapisu")

print()
    
lista.menu_start()


