import random
import os
import tensorflow as tf

ipath = tf.placeholder(tf.string, [])
image = tf.read_file('/home/yfeng23/lab/dataset/SUN397/' + ipath)
image = tf.image.decode_image(image, 3)
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

with tf.Session() as sess:
  with open('train.txt', 'w') as f:
    for i in imgs[:n]:
      i = i.strip()
      p = i.rfind('/')
      label = classes[i[1:p]]
      try:
        data = sess.run(image, feed_dict={ipath: i})
      except tf.errors.InvalidArgumentError:
        print(i, 'error')
        continue
      if len(data.shape) != 3:
        print(i, data.shape)
        continue
      f.write('%s,%d\n' % (i, label))
  with open('val.txt', 'w') as f:
    for i in imgs[n:]:
      i = i.strip()
      p = i.rfind('/')
      label = classes[i[1:p]]
      try:
        data = sess.run(image, feed_dict={ipath: i})
      except tf.errors.InvalidArgumentError:
        print(i, 'error')
        continue
      if len(data.shape) != 3:
        print(i, data.shape)
        continue
      f.write('%s,%d\n' % (i, label))
