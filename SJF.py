# -*- coding: utf-8 -*-

# Mehmed Emirhan Amaç - 170420517


class SJF:

     def proccessData(self,no_proc):
         process_data = []
         for i in range(no_proc):
             temp = []
             p_name = input("Enter p_name:")
             p_arrival = int(input("Enter p_arrival:"))
             p_burst = int(input("Enter p_burst:"))
             temp.extend([p_name,p_arrival,p_burst,0])
             process_data.append(temp)
         SJF.schProc(self, process_data)

     def schProc(self,process_data):
          starting_time = []
          exit_time = []
          s_time = 0
          procces_data.sort(key = lambda x: x[1])
          for i in range(len(procces_data)):
              ready_que = []
              temp = []
              norm_que = []
              for j in range (len(process_data)):
                  if(process_data[j][1] <= s_time) and (process_data[j][3]==0):
                      temp.extend([process_data[j][0]], process_data[j][1], process_data[j][2])
                      ready_que.append(temp)
                      temp=[]
                  elif procces_data[j][3] == 0:
                      temp.extend([process_data[j][0]], process_data[j][1], process_data[j][2])
                      norm_que.append = (temp)
                      temp = []
              if len(ready_que) != 0:
                  ready_que.sort(key = lambda x:x[2]) #burst time a gore sıralama
                  starting_time.append(s_time)
                  s_time = s_time + ready_que[0][2]
                  e_time = s_time
                  exit_time.append(e_time)
                  for k in range(len(process_data)):
                      if process_data[k][0] == ready_que[0][0]:
                           break
                  process_data[k][3] = 1
                  process_data[k].append(e_time)
              elif len(ready_que)==0:

                 if s_time < norm_que[0][1]:
                     s_time = norm_que[0][1]
                 starting_time.append(s_time)
                 s_time = s_time + norm_que[0][2]
                 e_time = s_time
                 exit_time.append(e_time)
                 for k in range(len(procces_data)):
                     if process_data[k][0] == ready_que[0][0]:
                         break
                 process_data[k][3] = 1
                 process_data[k].append(e_time)
     

     def PrintData(self, process_data):
         process_data.sort(key = lambda x:x[0])
         print("p_name p_arrival p_burst")
     for i in range(len(process_data)):
         for j in range(len(process_data[i])):
             print(process_data[i][j],end="       ")
         print()

if __name__ == "__main__":
    no_proc=int(input("Enter number of processes:"))
    sjfobjeckt=SJF()
    sjfobjeckt.processData(no_proc)
