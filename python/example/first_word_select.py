# Program to sort words

word_in_list =[]

with open("stats_SVT.txt", "r",  encoding='utf-8') as f:
    for line in f:
        word_in_list.append(line.split(None, 1)[0])





with open ("word_list_svt.txt", "w", encoding='utf-8') as f_done:
   for x in range(1100):
       f_done.write(word_in_list[x] + '\n')


