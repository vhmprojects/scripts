key = input("conjunto de 6 letras:\n")

Alfa2 = ('a', 'b', 'c', 'd', 'e', 'f',
         'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x',
                             'y', 'z')
nums = '0 1 2 3 4 5 6 7 8 9'
nums = nums.split()
count = 0

for i1 in (Alfa2):
    for i2 in (Alfa2):
        for i3 in (Alfa2):
             for i4 in (Alfa2):
                 for i5 in (Alfa2):
                     for i6 in (Alfa2):
                         y = (i1 + i2 + i3 + i4 + i5 + i6)
                         count += 1
                         if(y == key):
                            print('Encontrada: ' + y + " at position " + str(count))
                            exit()
