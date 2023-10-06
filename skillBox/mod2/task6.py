a = input()
string = ''
while 1:
    if len(a) > 0:
        st = a[0]
        if st!= '.':
            string += st
            a = a[1::]
        else:
            print(string)
            a = a[1::]
            string = ''
    else:
        print(string)
        break
