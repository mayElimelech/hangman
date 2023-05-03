
class unit9:

    def are_files_equal(self,file1, file2):
        f1=open(file1, 'r')
        f2=open(file2, 'r')

        content1 = f1.read()
        content2 = f2.read()

        if content1 == content2:
            return True
        else:
            return False



    def sort_words(self,file_path):
        f=open(file_path, 'r')
        lines = f.readlines()

        words = set()
        for line in lines:
            words.update(line.strip().split())
        sorted_words = sorted(list(words))
        print(sorted_words)

    def rev_lines(self,file_path):
        f = open(file_path, 'r')
        lines = f.readlines()

        for line in lines:
            reversed_line = line.strip()[::-1]
            print(reversed_line)

    def print_last_n_lines(self,file_path, n):
        f = open(file_path, 'r')
        lines = f.readlines()
        for line in lines[-n:]:
            print(line.strip())
    def targil912(self,word,file_path):
        if word == "sort":
            self.sort_words(file_path)
        elif word == "rev":
            self.rev_lines(file_path)
        elif word == "last":
            n = int(input("Enter number of lines: "))
            self.print_last_n_lines(file_path, n)

    def copy_file_content(self,source, destination):
        f1=open(source, 'r')
        f2=open(destination, 'w')
        content = f1.read()
        f2.write(content)

    def who_is_missing(self,file_name,f2,n):
        f=open(file_name, 'r')
        data = f.read().strip().split(',')
        data = list(map(int, data))
        for i in range(1,n+1,1):
            if((i in data)==False):
                file2=open(f2,'w')
                file2.write(str(i))

    def my_mp3_playlist(self,file_path):

        f= open(file_path,'r')
        lines = f.read().splitlines()
        max_len = 0
        long_song = ""
        singers = {}

        for line in lines:

            name, singer, length,non = line.split(";")
            minutes, seconds = map(int, length.split(":"))
            total_seconds = minutes * 60 + seconds
            if total_seconds > max_len:
                max_len = total_seconds
                long_song = name
            num_songs = len(lines)
            if singer  in singers:
                singers[singer] += 1
            else:
                singers[singer] = 1
        most_common_performer = max(singers, key=singers.get)

        return (long_song, num_songs, most_common_performer)

    def my_mp4_playlist(self,file_path, new_song):
        f=open(file_path, 'r')
        lines = f.read().splitlines()

        if len(lines) < 3:
            lines += ['\n'] * (3 - len(lines))

        lines[2] = new_song + ';' + lines[2].split(';')[1] + ';' + lines[2].split(';')[2]

        f=open(file_path, 'w')
        f.writelines(lines)

        f=open(file_path, 'r')
        print(f.read())


def main():
    uni=unit9()
    #print(uni.are_files_equal('C:\\Users\\claude\\PycharmProjects\\pythonProject\\f1test.txt','C:\\Users\\claude\\PycharmProjects\\pythonProject\\f2test.txt'))
    #uni.targil912("sort",'C:\\Users\\claude\\PycharmProjects\\pythonProject\\f1test.txt')
    #uni.copy_file_content('C:\\Users\\claude\\PycharmProjects\\pythonProject\\f1test.txt','C:\\Users\\claude\\PycharmProjects\\pythonProject\\f2test.txt')
    #uni.who_is_missing('C:\\Users\\claude\\PycharmProjects\\pythonProject\\f1test.txt','C:\\Users\\claude\\PycharmProjects\\pythonProject\\f2test.txt',9)
    #print(uni.my_mp3_playlist('C:\\Users\\claude\\PycharmProjects\\pythonProject\\f1test.txt'))
    uni.my_mp4_playlist('C:\\Users\\claude\\PycharmProjects\\pythonProject\\f1test.txt',"may may may")
if __name__ == '__main__':

    main()

