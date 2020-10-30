import socket
from threading import Thread
import random


questiondic = {"question 1":"1","question 2":"2","question 3":"3","question 4":"4","question 5":"5","question 6":"6","question 7":"7","question 8":"8","question 9":"9","question 10":"10","question 11":"11","question 12":"12","question 13":"13","question 14":"14","question 15":"15","question 16":"16","question 17":"17","question 18":"18","question 19":"19","question 20":"20"}

questionlist = ["q1","q2","q3","q4","q5","q6","q7","q8","q9","q10","q11","q12","q13","q14","q15","q16","q17","q18","q19","q20"]

client_list = []
port_list = []
buzzer = [0]
no = [0]


random.shuffle(questionlist)

def startquiz():
    client,addr=server.accept()
    client_list.append(client)
    port_list.append(address[1])
    count = 0
    print "connected to ",address[0],":",address[1]
    client.send("Get ready to play the quiz.\n")
    client.send("Instructions to play-There are 20 questions coming for you.If you know the answer for the question , type bz. If you buzzer before all the other players, you get a chance to answer.For each question, you get 1 point.If you score 5 points before all the other players, you win the quiz.")
    while count<5:
        if(len(client_list)==3 and buzzer[0]==0) :
            sendthequestion(questionlist[no[0]])
            no[0]=no[0]+1
        data=client.recv(1024)
	client.send("yayy! You know the answer!")
	client.send("Let's see if you were the first one!")

        if(data[0:2]=="bz" and bz[0]!=1 ):
            buzzer[0]=1
	    client.send("You can answer!")
            ans=client.recv(1024)
            
            if (len(questiondic[questionlist[no[0]-1]])==2 and ans[0:2]==questiondic[qnlist[no[0]-1]]) or (len(questiondic[questionlist[no[0]-1]])==1 and ans[0:1]==questiondic[questionlist[no[0]-1]]):
                count=count+1
                print "score of ",addr[0],",",addr[1],"is ",count
		client.send("you score is ",count)
                buzzer[0]=0

                if count==5:
                    print "game won by",addr[0],":",addr[1]
		    client.send("You Won!")
                    for client in clientlist:
                        client.close()
                        break

            else:
                print "Wrong Answer"
                bz[0]=0

        elif(data=="quit"):
            client.send("Goodbyeeeee")
            client.close()
            break

        else:
            client.send("You were late! You cant answer!")

        
        
            
        
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
port=7653
address=(ip,port)
server.bind(address)

n=20
def sendthequestion(message):
    for client in clientlist:
        client.send(message)


print "ready to get connected ",ip,":",port
server.listen(3)

for i in range(3):
    Thread(target=startquiz).start()
server.close()
