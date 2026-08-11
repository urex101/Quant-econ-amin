with open('newfile.txt', 'w') as f:  
    f.write('Testing\n')         
    f.write('Testing again')



with open('newfile.txt', 'r') as fo:
    out = fo.read()
    print(out)



with open("newfile.txt", "r") as f:
    file = f.readlines()
    with open("output.txt", "w") as fo:
        for i, line in enumerate(file):
            fo.write(f'Line {i}: {line} \n')




with open("newfile.txt", "r") as f, open("output2.txt", "w") as fo:
        for i, line in enumerate(f):
            fo.write(f'Line {i}: {line} \n')