import os
import json

bertram = []

number = 0
for i in os.listdir("./dataset18/"):
  if(number >= 25):
      break
  with open("./dataset18/" + i, "r", encoding="utf-8") as f:
    lines = f.read()
    bertram.append(lines)
  f.close()
  number += 1

data = {"": bertram}

with open('./dataset19/captain-knowledge.json', 'w', encoding='utf-8') as fort:
  json.dump(data, fort, ensure_ascii=False, indent=4)

for i in bertram:
  print(i + "\n")