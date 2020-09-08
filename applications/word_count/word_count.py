
def word_count(s):
    my_dict = {}

    for word in s.split():
        word = word.lower()
        leave_out = '":;,.-+=/\\|[]{}()*^&'

        for item in word:
            if item in leave_out:
                word = word.replace(item, "")
        
        if word in my_dict:
            my_dict[word] += 1
        elif word != "":
            my_dict.update({ word: 1 })
    return my_dict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))