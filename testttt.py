f=input()
with open('cli.txt', 'r') as file:
    #[l1, l2, l3, l4, l5]
    file_content=file.readlines()
    for line in file_content:
        print(line)