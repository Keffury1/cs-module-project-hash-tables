def no_dups(s):
    my_dict = {}
    string = ""

    for word in s.split():
        if word in my_dict:
            pass
        else:
            if string == "":
                string += word
                my_dict.update({ word: 1 })
            else:
                string += f' {word}'
                my_dict.update({ word: 1 })

    return string



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))