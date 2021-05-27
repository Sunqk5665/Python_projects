import random
def fun(match):
   idx = 0
   while match > 1:
      idx += 1
      if idx % 2 == 1:
         gamer = 'A'
         choice = random.choice(range(1,5)) if match >= 5 else random.choice(range(1, match+1))
      else:
         gamer = 'B'
         if match > 5:
            for x in range(1, 5):
               if (match - x) % 5 == 1:
                  choice = x
                  break
         else:
           choice = match - 1
      match -= choice
      print(gamer, choice, match)
   another = 'A' if gamer == 'B' else 'B'
   loser = gamer if match == 0 else another
   print('%s 胜利!' % loser)
fun(21)