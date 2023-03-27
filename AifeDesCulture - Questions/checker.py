import time

start = time.perf_counter()

with open('AifeDesCulture - Questions/questions.txt','r',encoding='utf-8') as file:
    data = file.read().split('\n')
    questions = int((len(data)-1)/8)
    for i in range (questions):
        if data[i*8+2] == '' and data[i*8+3] == '' and data[i*8+4] == '':
            print('Error : Missing wrong anwsers for question '+str(int(i+1))+' in lines '+str(int(i*8+2)+1)+', '+str(int(i*8+3)+1)+' and '+str(int(i*8+4)+1)+'.')
        if data[i*8+5] == '':
            print('Error : Missing theme for question '+str(int(i+1))+' in line '+str(int(i*8+5)+1)+'.')
print ("Check done in "+str(round((time.perf_counter()-start)*1000,3))+' ms.')