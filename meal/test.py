filecon = ''
contents = open('/home/server/PycharmProjects/bot/meal/cal_list.txt', 'r')
cont = contents.readlines()
for list in cont :
    filecon = filecon+list
result = filecon