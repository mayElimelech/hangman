import calendar
class unit4:

    def targil422(self):
        input_string = input("enter  string: ")
        new_string = input_string.replace(" ", "").lower()
        if input_string == input_string[::-1]:
            print("ok")
        else:
            print("not")

    def targil423(self):
        temp = input("insert ")

        if temp[-1] in ['c', 'C']:
            cel= float(temp[:-1])
            fahrenheit = cel * 9 / 5 + 32
            print(f"{fahrenheit:}F")

        elif temp[-1] in ['f', 'F']:
            # Convert from Fahrenheit to Celsius
            fahrenheit = float(temp[:-1])
            cel = (fahrenheit - 32) * 5 / 9
            print(f"{cel:}C")

    def targil424(self):
        str1 = input("Enter a date : ")

        day, month, year = map(int, str1.split('/'))
        day1 = calendar.weekday(year, month, day)
        day_name = calendar.day_name[day1]

        print(day_name)


def main():
    uni=unit4()
    print(uni.targil422())
    uni.targil423()
    uni.targil424()
if __name__ == '__main__':

    main()

