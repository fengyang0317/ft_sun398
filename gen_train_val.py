import random
import os

print(os.getcwd())

db_path = '/home/yfeng23/lab/dataset/SUN397/'

with open(db_path + 'files', 'r') as f:
  imgs = list(f)
with open(db_path + 'ClassName.txt', 'r') as f:
  classes = {}
  for i, j in enumerate(f):
    classes[j.strip()] = i

random.shuffle(imgs)
n = int(len(imgs) * 0.9)

with open('train.txt', 'w') as f:
  for i in imgs[:n]:
    p = i.rfind('/')
    label = classes[i[1:p]]
    f.write('%s,%d\n' % (i.strip(), label))
with open('val.txt', 'w') as f:
  for i in imgs[n:]:
    p = i.rfind('/')
    label = classes[i[1:p]]
    f.write('%s,%d\n' % (i.strip(), label))
