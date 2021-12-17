f = open('club.txt', 'a')
while True:
    name = input('name:')
    if not name:break
    f.write(name+'\n')
    f.close()
