
class unit6:

    def shift_left(self,my_list):
        return my_list[1:] + [my_list[0]]

    def format_list(self,my_list):
        return ', '.join(my_list[::2]) + ', and ' + my_list[-1]

    def extend_list_x(self,list_x, list_y):

        new_list = [*list_y, *list_x]

        return new_list

    def are_lists_equal(self,list1, list2):

        # Sort the lists in ascending order
        list1_sort = sorted(list1)
        list2_sort= sorted(list2)

        # Check if the sorted lists are equal
        if list1_sort == list2_sort:
            return True
        else:
            return False

    def longest(self,my_list):

        return  max(my_list,key=len)


def main():
    uni=unit6()
    print(uni.shift_left(['monkey', 2.0, 1]))
    print(uni.format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))
    print(uni.extend_list_x([4, 5, 6],[1, 2, 3]))
    print(uni.are_lists_equal([0.6, 1, 2, 3],[9, 0, 5, 10.5]))
    print(uni.longest(["111", "234", "2000", "goru", "birthday", "09"]))
if __name__ == '__main__':

    main()

