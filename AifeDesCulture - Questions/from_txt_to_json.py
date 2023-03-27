import time

start = time.perf_counter()

with open ("AifeDesCulture - Questions/questions.txt", "r", encoding='utf-8') as file:
    lines = file.read().split('\n')
    data = []
    for i in range (len(lines)):
        if lines[i] != "------------------------------":
            if lines[i] != "":
                data.append(lines[i])

with open("AifeDesCulture - Questions/data.json","w",encoding="utf-8") as jsonfile:
    jsonfile.write("[\n")
    questions = int(len(data)/7)
    for i in range(questions):
        jsonfile.write('   {\n')
        jsonfile.write('      "question":"'+data[i*7]+'",\n')
        jsonfile.write('      "answers":{\n')
        jsonfile.write('         "true":"'+data[i*7+1]+'",\n')
        jsonfile.write('         "wrong":["'+data[i*7+2]+'", "'+data[i*7+3]+'", "'+data[i*7+4]+'"]\n')
        jsonfile.write('      },\n')
        jsonfile.write('      "theme":"'+data[i*7+5]+'",\n')
        jsonfile.write('      "difficulty":'+data[i*7+6]+'\n')
        if questions-1 == i:
            jsonfile.write('   }\n')
        else:
            jsonfile.write('   },\n')
    jsonfile.write(']')
print(str((time.perf_counter()-start)*1000))