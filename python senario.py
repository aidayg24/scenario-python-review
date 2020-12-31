class ExtendedList(list):
    def __init__(self, the_list):
        super().__init__()
        self.the_list = the_list

    def __lt__(self, other):  # <
        return sum(self.the_list) / len(self.the_list) < sum(other.test_list) / len(other.test_list)

    def __gt__(self, other):  # >
        return sum(self.the_list) / len(self.the_list) > sum(other.test_list) / len(other.test_list)

    def __le__(self, other):  # <=
        return sum(self.the_list) / len(self.the_list) <= sum(other.test_list) / len(other.test_list)

    def __ge__(self, other):  # >=
        return sum(self.the_list) / len(self.the_list) >= sum(other.test_list) / len(other.test_list)

    def __eq__(self, other):  # ==
        return sum(self.the_list) / len(self.the_list) == sum(other.test_list) / len(other.test_list)

    def __ne__(self, other):  # !=
        return sum(self.the_list) / len(self.the_list) != sum(other.test_list) / len(other.test_list)

    def __add__(self, other):
        return self.the_list.extend(other)

    @staticmethod
    def next_val(a_list):
        try:
            for i in a_list:
                yield int(i)
        except IndexError:
            return "index is wrong!"
        except ValueError:
            return "this is not an integer!"


class TypeList(ExtendedList):
    def __init__(self, the_list):
        super().__init__(the_list)

    def __eq__(self, other):
        return self.the_list[len(self.the_list) - 1] == other[len(other.the_list) - 1]

    def __ne__(self, other):
        return self.the_list[len(self.the_list) - 1] != other[len(other.the_list) - 1]
