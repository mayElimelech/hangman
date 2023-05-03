
class unit5:

    def last_early(self,my_str):
        my_str = my_str.lower()
        last_char = my_str[-1]
        if last_char in my_str[:-1]:
            return True
        return False

    def distance(self,num1, num2, num3):
        if abs(num1 - num2) <= 1 and abs(num1 - num3) >= 2 and abs(num2 - num3) >= 2:
            return True
        elif abs(num1 - num3) <= 1 and abs(num1 - num2) >= 2 and abs(num3 - num2) >= 2:
            return True
        else:
            return False

    def fix_age(self,age):
        if age in [13, 14, 17, 18, 19]:
            return 0
        else:
            return age
    def filter_teens(self,a=13, b=13, c=13):


        a = self.fix_age(a)
        b = self.fix_age(b)
        c = self.fix_age(c)

        return a + b + c

    def chocolate_maker(self,small, big, x):
        max_big=int(x/5)
        if small>=x%5:
            return True
        return False



def main():
    uni=unit5()
    print(uni.last_early("happy birthday"))
    print(uni.distance(1, 2, 10))
    print(uni.filter_teens(1, 2, 3))
    print(uni.chocolate_maker(3, 2, 10))
if __name__ == '__main__':

    main()

