# jabber = open("E:/061 sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end=' ')
#
# jabber.close()

# with open("E:/061 sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end = '')
# with open("E:/061 sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readLine()

# with open("E:/061 sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
#     print(lines)
#
# for line in lines:
#     print(line, end = '')

with open("E:/061 sample.txt", 'r') as jabber:
        lines = jabber.readlines()
        print(lines)

for line in lines[::-1]:
    print(line, end = '')

with open("E:/061 sample.txt", 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end = '')