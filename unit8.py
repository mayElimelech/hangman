
class unit8:

    def targil821(self):
        data = ("self", "py", 1.543)
        format_string = "Hello {}.{} learner, you have only {:.1f} units left before you master the course!"
        print(format_string.format(*data))

    def sort_prices(self,list_of_tuples):
        sorted_list = sorted(list_of_tuples, key=lambda x: float(x[1]), reverse=True)
        return sorted_list

    def mult_tuple(self,tuple1, tuple2):
        result = []
        for i in tuple1:
            for j in tuple2:
                result.append((i, j))
                result.append((j, i))
        return tuple(result)

    def sort_anagrams(self,list_of_strings):
        bigger_list=[]
        sub_list=[]

        for i in list_of_strings:

            sorted_i=''.join(sorted(i))

            for j in list_of_strings:
               sorted_j=''.join(sorted(j))
               if sorted_i==sorted_j:
                    sub_list.append(j)
                    list_of_strings.remove(j)
            bigger_list.append(sub_list)
            sub_list=[]
        return bigger_list
    def targil832(self):
        mariah = {
            'first_name': 'Mariah',
            'last_name': 'Carey',
            'birth_date': '27.03.1970',
            'hobbies': ['Sing', 'Compose', 'Act']
        }
        choice = int(input("Enter : "))
        if choice == 1:
            print(mariah['last_name'])
        elif choice == 2:
            birth_month = mariah['birth_date'].split('.')[1]
            print(birth_month)
        elif choice == 3:
            num_hobbies = len(mariah['hobbies'])
            print(num_hobbies)
        elif choice == 4:
            last_hobby = mariah['hobbies'][-1]
            print(last_hobby)
        elif choice == 5:
            mariah['hobbies'].append('Cooking')
        elif choice == 6:
            birth_date_tuple = tuple(mariah['birth_date'].split('.'))
            print(birth_date_tuple)
        elif choice == 7:
            birth_year = int(mariah['birth_date'].split('.')[2])
            current_year = 2023  # Update with current year
            age = current_year - birth_year
            mariah['age'] = age

    def count_chars(self,my_str):
        char_count = {}
        for ch in my_str:
            if ch != " ":
                if ch in char_count:
                    char_count[ch] += 1
                else:
                    char_count[ch] = 1
        return char_count

    def inverse_dict(self,my_dict):
        new_dict = {}
        for key, value in my_dict.items():
            new_dict.setdefault(value, []).append(key)
        for value in new_dict.values():
            value.sort()
        return new_dict


def main():
    uni=unit8()
    uni.targil821()
    print(uni.sort_prices([('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]))
    print(uni.mult_tuple((1, 2),(4, 5)))
    print(uni.sort_anagrams(['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']))
    uni.targil832()
    print(uni.count_chars( "abra cadabra"))
    print(uni.inverse_dict({'I': 3, 'love': 3, 'self.py!': 2}))
if __name__ == '__main__':

    main()

