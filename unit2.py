class unit2:

    def targil233(self,num):
        pig1=int(num%10)
        pig2=int(num/10%10)
        pig3=int(num/100)
        print(pig3+pig2+pig1)
        print(int((pig3+pig2+pig1)/3))
        print((pig3 + pig2 + pig1) % 3)
        return (pig3 + pig2 + pig1) % 3==0

def main():
    uni=unit2()
    print(uni.targil233(124))
if __name__ == '__main__':

    main()

