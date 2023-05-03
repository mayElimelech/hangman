
class unit7:

    def squared_numbers(self,start, stop):
        squares = []
        i = start
        while i <= stop:
            squares.append(i ** 2)
            i += 1

        return squares

    def is_greater(self,my_list, n):

        greater_list = []

        for i in my_list:
            if i > n:
                greater_list.append(i)

        return greater_list

    def numbers_letters_count(self,my_str):

        digits_count = 0
        letters_count = 0

        for ch in my_str:
            if ch.isdigit():
                digits_count += 1
            elif ch.isalpha() or ch.isspace() or ch in ['.', ',', '?', '!']:
                letters_count += 1

        return [digits_count, letters_count]

    def seven_boom(self,end_number):
        result = []
        for i in range(end_number + 1):
            if i % 7 == 0 or '7' in str(i):
                result.append('BOOM')
            else:
                result.append(i)
        return result

    def sequence_del(self,my_str):
        result = ''
        prev= ''
        for ch in my_str:
            if ch != prev:
                result += ch
                prev = ch
        return result

    def print_products(self,products):
       print(products)

    def print_number_products(self, products):
        products_list = products.split(",")
        num_products = len(products_list)
        print(num_products)

    def print_is_exist_products(self, products,productName):
        if products.lower().find(productName) != -1:
            print(" found!")
        else:
            print("not found.")
    def print_how_many_times_appeared(self,products,product):
        count = products.lower().count(product.lower())
        print(count)
    def delete_from_products(self,products,product):
         new_list=products.replace(product, "", 1)
         return new_list
    def append_to_products(self,products,product):
        new_list = ','.join([products, product])
        return new_list

    def print_invalid_products(self,products):
        products_list = products.split(",")
        invalid_products=[]
        for product in products_list:
            if(len(product)<3):
                invalid_products.append(product)
            for i in product:
                if i.isalpha()==False:
                    invalid_products.append(product)
                    break
        if len(invalid_products) > 0:
            for product in invalid_products:
                print(product)
        else:
            print("No invalid products.")
    def delete_duplicate(self,products):
        products_list = products.split(',')
        products_set = set(products_list)
        new_list = ','.join(products_set)
        return new_list
    def products_list(self):
        products=input("enter list: ")
        number=int(input("enter number: "))
        while(number!=9):
            if(number==1):
                self.print_products(products)
            if (number == 2):
                self.print_number_products(products)
            if (number == 3):
                productname=input("enter product name: ")
                self.print_is_exist_products(products,productname)
            if (number == 4):
                productname = input("enter product name: ")
                self. print_how_many_times_appeared(products,productname)
            if (number == 5):
                productname = input("enter product name: ")
                products= self.delete_from_products(products,productname)

            if (number == 6):
                productname = input("enter product name: ")
                products=self.append_to_products(products,productname)

            if (number == 7):
                self.print_invalid_products(products)
            if (number == 8):
                products=self.delete_duplicate(products)
            number = int(input("enter number: "))

    def arrow(self,my_char, max_length):
        arrow_str = ""
        for i in range(1, max_length + 1):
            line = my_char * i
            arrow_str += line + "\n"
        for i in range(max_length - 1, 0, -1):
            line = my_char * i
            arrow_str += line + "\n"
        return arrow_str[:-1]



def main():
    uni=unit7()
    print(uni.squared_numbers(-3, 3))
    print(uni.is_greater([1, 30, 25, 60, 27, 28], 28))
    print(uni.numbers_letters_count("Python 3.6.3"))
    print(uni.seven_boom(17))
    print(uni.sequence_del("ppyyyyythhhhhooonnnnn"))
    uni.products_list()
    print(uni.arrow('*', 5))
if __name__ == '__main__':

    main()

