import turtle as t
t.speed(100)
t.pu()
t.rt(150)
t.fd(200)
t.lt(150)
t.pd()
i=0
n=0
lay=[]
def findmove(s):
  if s==0:
    lay.clear()
  if s < i:
    for q in range(3):
      findmove(s+1)
  lay.append(800/2**s)
def centretri(size):
  t.fd(200/2**size)
  t.lt(60)
  t.begin_fill()
  for p in range(3):
    t.fd(200/2**size)
    t.lt(120)
  t.end_fill()
  t.lt(120)
  t.fd(200/2**size)
  t.lt(180)
for k in range(3):
  t.fd(400)
  t.lt(120)
while 1: 
  findmove(0)
  lay.remove(800)
  centretri(i)
  if not len(lay) == 0:
    t.fd(lay.pop(0))
    t.lt(120)
  while not len(lay) == 0:
    centretri(i)
    t.fd(lay.pop(0))
    t.lt(120)
  i+=1
