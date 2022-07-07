import turtle as t
t.speed(5)
t.pu()
t.rt(150)
t.fd(200)
t.lt(150)
t.pd()
i=0
n=0
global lay
lay=[]
def findmove(s):
  print(f"findmove s={s}")
  if s==0:
    lay.clear()
  if s < i:
    for q in range(3):
      findmove(s+1)
  lay.append(800/2**s)
def centretri():
  t.fd(200/2**i)
  t.lt(60)
  t.begin_fill()
  for p in range(3):
    t.fd(200/2**i)
    t.lt(120)
  t.end_fill()
  t.lt(120)
  t.fd(200/2**i)
  t.lt(180)
for k in range(3):
  t.fd(400)
  t.lt(120)
while 1: 
  findmove(0)
  lay.remove(800)
  centretri()
  if not len(lay) == 0:
    t.fd(lay.pop(0))
    t.lt(120)
  while not len(lay) == 0:
    centretri()
    t.fd(lay.pop(0))
    t.lt(120)
  i+=1
