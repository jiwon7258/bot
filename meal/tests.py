from django.test import TestCase

# Create your tests here.
contents = open('/home/server/PycharmProjects/bot/meal/cal_list.txt', 'r', encoding='utf-8')
cont = contents.readlines()
filecon = ''
for list in cont :
    filecon = filecon+list
print(filecon)