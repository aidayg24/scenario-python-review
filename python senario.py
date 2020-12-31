class ExtendedList:
    def __init__(self, the_list):
        self.the_list = the_list

    def __lt__(self, other):  # <
        m1, m2 = 0, 0
        for i in self.the_list:
            m1 += i
        for i in other:
            m2 += i
        m1 /= len(self.the_list)
        m2 /= len(other)
        return m1 < m2

    def __gt__(self, other):  # >
        m1, m2 = 0, 0
        for i in self.the_list:
            m1 += i
        for i in other:
            m2 += i
        m1 /= len(self.the_list)
        m2 /= len(other)
        return m1 > m2

    def __le__(self, other):  # <=
        m1, m2 = 0, 0
        for i in self.the_list:
            m1 += i
        for i in other:
            m2 += i
        m1 /= len(self.the_list)
        m2 /= len(other)
        return m1 <= m2

    def __ge__(self, other):  # >=
        m1, m2 = 0, 0
        for i in self.the_list:
            m1 += i
        for i in other:
            m2 += i
        m1 /= len(self.the_list)
        m2 /= len(other)
        return m1 >= m2

    def __eq__(self, other):  # ==
        m1, m2 = 0, 0
        for i in self.the_list:
            m1 += i
        for i in other:
            m2 += i
        m1 /= len(self.the_list)
        m2 /= len(other)
        return m1 == m2

    def __ne__(self, other):  # !=
        m1, m2 = 0, 0
        for i in self.the_list:
            m1 += i
        for i in other:
            m2 += i
        m1 /= len(self.the_list)
        m2 /= len(other)
        return m1 != m2

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
    def __eq__(self, other):
        return self.the_list[len(self.the_list) - 1] == other[len(other) - 1]

    def __ne__(self, other):
        return self.the_list[len(self.the_list) - 1] != other[len(other) - 1]
