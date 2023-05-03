class unit3:

    def targil321(self):
        str1="\"Shuffle, Shuffle, Shuffle\", say it together!\n Change colors and directions,\n Don't back down and stop the player! \n\t\tDo you want to play Taki?\n\t\t Press y\\n"
        return str1
    def targil342(self):
        str1=input("enter string")
        first_char=str1[0]
        new_string=first_char+str1[1:].replace(first_char,'e')
        return new_string
    def targil343(self):
        enter_string = input("Enter a string: ")
        length_string = len(enter_string)
        mid = length_string // 2
        new_string = enter_string[:mid].lower() + enter_string[mid:].upper()
        print(new_string)


def main():
    uni=unit3()
    print(uni.targil321())
    print(uni.targil342())
    print(uni.targil343())
if __name__ == '__main__':

    main()

