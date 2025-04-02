
def writeScore():
    name = input("Öğrenci Adı: ")
    surname = input("Öğrenci Soyadı: ")
    score1 = input("Not 1: ")
    score2 = input("Not 2: ")
    score3 = input("Not 3: ")

    with open("exam_scores.txt","a", encoding="utf-8") as file:
        file.write(name + ' ' + surname + ':' + score1 + ',' + score2 + ',' + score3 + '\n')

def calculateScore(line):
    line = line[:-1]
    studentList = line.split(":")

    studentName = studentList[0]
    scores = studentList[1].split(",")

    score1 = int(scores[0])
    score2 = int(scores[1])
    score3 = int(scores[2])

    avg = (score1 + score2 + score3) / 3

    if avg >= 90 and avg <= 100:
        lecture = "AA"
    elif avg >= 80 and avg <= 89:
        lecture = "BA" 
    elif avg >= 75 and avg <= 79:
        lecture = "BB" 
    elif avg >= 70 and avg <= 74:
        lecture = "CB" 
    elif avg >= 65 and avg <= 69:
        lecture = "CC" 
    elif avg >= 60 and avg <= 64:
        lecture = "DC" 
    elif avg >= 50 and avg <= 59:
        lecture = "DD" 
    elif avg >= 40 and avg <= 49:
        lecture = "FD" 
    elif avg >= 0 and avg <= 39:
        lecture = "FF" 

    return f"{studentName} : + {lecture}  ({avg})\n"



def readScore():
    with open("exam_scores.txt","r", encoding="utf-8") as file:
        for line in file:
            print(calculateScore(line))

def saveScore():
    with open("exam_scores.txt","r", encoding="utf-8") as file:
        resultList = []

        for line in file:
            resultList.append(calculateScore(line))

        with open("result_exam_scores.txt","w",encoding="utf-8") as file2:
            file2.writelines(resultList)

    

while True:
    process = input("1- Write Score\n2-Read Score\n3-Save Score\n4-Exit\n")

    if process == "1":
        writeScore()
    elif process == "2":
        readScore()
    elif process == "3":
        saveScore()
    else:
        break