class Timer:

    def __init__(self, hour=0, min=0, second=0):
        self.__hour = hour
        self.__min = min
        self.__second = second

    def __str__(self):

        return f"{self._format(self.__hour)}:{self._format(self.__min)}:{self._format(self.__second)}"

    def next_second(self):

        self.__second += 1
        if self.__second == 60:
            self.__second = 0

        self.__min += 1
        if self.__min == 60:
            self.__min = 0

        self.__hour += 1
        if self.__hour == 24:
            self.__hour = 0

    def prev_second(self):

        self.__second -= 1
        if self.__second == -1:
            self.__second = 59

        self.__min -= 1
        if self.__min == -1:
            self.__min = 59

        self.__hour -= 1
        if self.__hour == -1:
            self.__hour = 23

    def _format(self, format_spec):
        return str(format_spec).rjust(2, '0')


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
