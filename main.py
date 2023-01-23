import os
import json

bertram = []
bertram2 = []
bertram3 = []

number = 0
for i in os.listdir("./aclimdb/train/neg"):
  if(number >= 25):
      break
  with open("./aclimdb/train/neg/" + i, "r", encoding="utf-8") as f:
    lines = f.read()
    bertram.append(lines)
  f.close()
  number += 1

number2 = 0
for i in os.listdir("./aclimdb/train/pos"):
  if(number2 >= 25):
      break
  with open("./aclimdb/train/pos/" + i, "r", encoding="utf-8") as f:
    lines = f.read()
    bertram2.append(lines)
  f.close()
  number2 += 1

number3 = 0
for i in os.listdir("./aclimdb/train/unsup"):
  if(number3 >= 25): 
      break
  with open("./aclimdb/train/unsup/" + i, "r", encoding="utf-8") as f:
    lines = f.read()
    bertram3.append(lines)
  f.close()
  number3 += 1

data = {"negative": bertram}
data2 = {"positive": bertram2}
data3 = {"neutral": bertram3}

with open('./dataset2/data-neg.json', 'w', encoding='utf-8') as fort:
  json.dump(data, fort, ensure_ascii=False, indent=4)

with open('./dataset2/data-pos.json', 'w', encoding='utf-8') as nicka:
  json.dump(data2, nicka, ensure_ascii=False, indent=4)

with open('./dataset2/data-neu.json', 'w', encoding='utf-8') as monke:
  json.dump(data3, monke, ensure_ascii=False, indent=4)

for i in bertram:
  print(i + "\n")