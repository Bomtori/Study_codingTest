while True:
  lt1 = list(map(int, input().split()))
  if(lt1 == [0, 0, 0]):
    break

  heru = max(lt1)
  lt1.remove(heru)

  heru_squre = heru * heru
  auset = lt1[0] * lt1[0]
  ausar = lt1[1] * lt1[1]

  if(heru_squre == auset + ausar):
    print('right')
  else:
    print('wrong')