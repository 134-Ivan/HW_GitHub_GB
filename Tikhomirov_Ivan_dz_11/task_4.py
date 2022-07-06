# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self, name, tech_quantity, *tech_type):
        self.name = name
        self.technique_quantity = tech_quantity
        self.technique_type = tech_type

    def load(self):
        pass

    def discharge(self):
        pass

class OfficeEquipment(Warehouse):
    def __init__(self, name, tech_quantity, tech_type, model, page_format='A4', color='black&white'):
        super.__init__(name, tech_quantity, tech_type)
        self.model = model
        self.page_format = page_format
        self.color = color


class Printer(OfficeEquipment):
    def __init__(self, name, tech_quantity, tech_type, model, page_format='A4', color='black&white', portable=True):
        super.__init__(name, tech_quantity, tech_type, model, page_format, color)
        self.portable = portable


class Scanner(OfficeEquipment):
    def __init__(self, name, tech_quantity, tech_type, model, page_format='A4', color='black&white', wi_fi=False):
        super.__init__(name, tech_quantity, tech_type, model, page_format, color)
        self.wi_fi = wi_fi


class Xerox(OfficeEquipment):
    def __init__(self, name, tech_quantity, tech_type, model, page_format='A4', color='black&white', bluetooth=False):
        super.__init__(name, tech_quantity, tech_type, model, page_format, color)
        self.bluetooth = bluetooth
