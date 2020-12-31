class ExtendedList(list):
    def __init__(self, the_list):
        super().__init__(the_list)
        self.the_list = the_list

    def __lt__(self, other):  # <
        return sum(self.the_list) / len(self.the_list) < sum(other.the_list) / len(other.the_list)

    def __gt__(self, other):  # >
        return sum(self.the_list) / len(self.the_list) > sum(other.the_list) / len(other.the_list)

    def __le__(self, other):  # <=
        return sum(self.the_list) / len(self.the_list) <= sum(other.the_list) / len(other.the_list)

    def __ge__(self, other):  # >=
        return sum(self.the_list) / len(self.the_list) >= sum(other.the_list) / len(other.the_list)

    def __eq__(self, other):  # ==
        return sum(self.the_list) / len(self.the_list) == sum(other.the_list) / len(other.the_list)

    def __ne__(self, other):  # !=
        return sum(self.the_list) / len(self.the_list) != sum(other.the_list) / len(other.the_list)

    def __add__(self, other):
        ans = []
        ans.extend(self.the_list)
        ans.extend(other.the_list)
        return ans

    # def __str__(self):
    #     return str(self.the_list)

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
        return self.the_list[- 1] == other.the_list[- 1]

    def __ne__(self, other):
        return self.the_list[- 1] != other.the_list[- 1]

    # def __str__(self):
    #     return str(self.the_list)
