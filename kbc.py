questions=[["what is developer name","ALOK","ADITYA","BHANU","RUCHIT",1],
           
[" what is Alok's favorite language","C++","JAVA","JS","PYTHON",4],
["what is alok's favorite color","RED","GREEN","BLUE","YELLOW",3],
["what is the largest organ in human body","SKIN","BRAIN","HEART","LEVER",1],
["how many legs does a spider have","9","8","12","14",2],
["how many floor exist in burj khalifa","153","159","163","170",3],
["largest river in world","AMOZON","MISSISSIPPI","NILE","YANGTZE",3],
["What is the full form of ATM?"," Automated Teller Machine","Automated Transaction Machine"," Automatic Transfer Machine",
"Automated Text Machine",1],
[" What is the name of the sacred bow that Lord Rama broke to win the hand of Sita?","Gandiva"," Pinaka","Sharanga"," Kodanda",2],
["In the Ramayana, who is the mother of Ravana, Kumbhakarna, and Vibhishana"," Kaikesi","Surpanakha ","Mandodari"," Vedavati",1],
["in which year was the first international morden olympiad held","1924","1896","1900","1912",2],
["which is the richest country in the world","QATAR","RUSSIA","THE USA","THE UAE",1],
["who is considered as father of table tennis","TENZIN GYASTO","DENG YAPING","ZHUANG ZEDONG","JAN-OVE WALDaNER",4],
["which country won the first -ever olympic gold medal in volleyball","USA","JAPAN","BRAZIL","SOVIET UNION",2],

]
level=[1000,2000,3000,4000,10000,12000,14000,16000,32000,50000,10000000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"question for RS.{level[i]}")
    print(question[0])
    print(f"a.{question[1]}                    b.{question[2]}")
    print(f"c.{question[3]}                    d.{question[4]}")
    userans= int(input("choose your option"))
    if userans == question[-1]:
        print(f"congrats! you choosed correct answer.now you win {level[i] } RS.")
        if(i==4):
            money=10000
        elif i==9:
            money=50000 
        elif i==14:
            money=1000000
    else:
      print("OOPS! you choose incorrect answer")   
      break        
print(f" Finally ! your winning price is {money}.")

        

