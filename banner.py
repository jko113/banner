def print_banner(sentence):
    star = '*'

    sentence_length = len(sentence) + 4

    def print_box():
        print_first_last_line()
        print(star, sentence, star)
        print_first_last_line()

    def print_first_last_line():
        iterator = 0

        while iterator < sentence_length:
            print (star, end='')
            iterator += 1

        print('')

    print_box()