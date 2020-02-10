# Task 8.4 - 8.6
class NameError(Exception):
    def __init__(self, text):
        self.text = text


class Storehouse:

    def __init__(self, slots_total, slots_available):
        items_dict = dict(Printer=[], Computer=[], Screen=[], Total_amount=0)
        self.items_dict = items_dict
        self.slots_total = slots_total
        self.slots_available = slots_available

    def store(self, *args):
        for i in args:
            op_str = str(i.__class__)
            item_index = op_str[op_str.find('.') + 1:-2]
            self.items_dict[item_index].append(i.__dict__)
            self.items_dict['Total_amount'] += 1
            self.slots_available -= 1
        print(self.items_dict)
        print(f'{self.slots_available} slots are available now.')

    def send(self, department, *args):
        try:
            found = []
            for k in args:
                for j in self.items_dict.keys():
                    if j != 'Total_amount':
                        for i in self.items_dict[j]:
                            if i['name'] == k:
                                found.append(k)
                                self.items_dict[j].pop(self.items_dict[j].index(i))
                                print(f'Item {k} has been sent to {department} department.')
                                self.items_dict['Total_amount'] -= 1
                                self.slots_available += 1
            if len(args) > len(found):
                not_found = list(set(args) - set(found))
                raise NameError(f'These items were not found in database {not_found}. Please, check your input.')
        except NameError as err:
            print(err)

        finally:
            print(self.items_dict)
            print(f'{self.slots_available} slots are available now.')


Storage1 = Storehouse(200, 200)


class Office_Equip:
    def __init__(self, name, weight, volume):
        self.name = name
        self.weight = weight
        self.volume = volume

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if isinstance(weight, int):
            self._weight = str(weight) + ' kg'
        else:
            self._weight = weight

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        if isinstance(volume, float or int):
            self._volume = str(volume) + ' m3'
        else:
            self._volume = volume


class Printer(Office_Equip):
    def __init__(self, name, weight, volume, color_type, printing_type):
        super().__init__(name, weight, volume)
        self.color_type = color_type
        self.printing_type = printing_type


P1 = Printer('Canon S120', 10, 0.5, 'colorful', 'digital')


class Computer(Office_Equip):
    def __init__(self, name, weight, volume, ssd, ram, cpu):
        super().__init__(name, weight, volume)
        self.ssd = ssd
        self.ram = ram
        self.cpu = cpu


C1 = Computer('MacMini 2016', '11 kg', '0.6 m3', '500 gb', '32 gb', '4,5 Ghz')
C2 = Computer('Asus r50', '5 kg', '0.3 m3', '1 tb', '32 gb', '3,3 Ghz')


class Screen(Office_Equip):
    def __init__(self, name, weight, volume, inch, matrix, resolution):
        super().__init__(name, weight, volume)
        self.inch = inch
        self.matrix = matrix
        self.resolution = resolution


S1 = Screen('LG c233', '5 kg', '0.4m3', '24 inch', 'IPS', '1920x1080')

Storage1.store(C1, P1, S1, C2)
Storage1.send('IT', 'MacMini 2016', 'Asus')
print(P1.volume)
print(C1.volume)
