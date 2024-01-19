print ('''
           ___________
           / |       | |
        ,' ,'         \/',_    __
     ,'__/             |    ',|  "'-,,,,,,,
   ,/  _|',            |                |   \
   |  |   |',           \               |    \
   |__|   |  ',          ',             |     \
  /       |     ',        ,_"""""---'-_,'______\
 /        |        ',,_-'"    |        |        ',
|_________|         |         /        |        / ',,'""""|
|__  |        ,____/         |        _|       /    |___  /
'\___|      ,'_,'|_,-,_______|         |       /      , '/
  \,' _', _/  ,, ,',|        |          \       |   '" ,'
   \ / |_ ,  |  \||||       ,' |      ,'|    _""    |,'
    ' ,'  ', |  ||||| __ ,'   _|_ ,'    |    |""---/
       ' ,"""','"""""" |     /           \"""|    /
                      |_____|_      __''"    \   |
                     |  |  /  """"""   |      \ /
                      \ / |            |       /
                       \--'            |      /
                       |   \__        _|__    |
                       |      |__     |   ',,,|
                       |         |____|   /   |
                       /         _|    ,,'_   |
                      |__________|___,'  ,,' /
                       \      ---'    \,/  ,'
                        \     |    ,,,' \_/
                         |    |_,''      |/
                         |    |       []_|
                          \___'        /
                           \       __,'
                            \_____/     
''')

print('Welcome to explore Nairobi with Kimathi')

print('Your Mission is to Survive Nairobi without being broke the capital city');

transport = input('What means of transportation will you be utlizing : Taxi or Uber? ')

Taxi = 'taxi'
if transport == 'Taxi' or transport == Taxi.lower():
   print('Game over you are dead broke')
elif transport == 'uber' or transport == 'Uber':
      Place = input('Which place will you use to stay: Hotel or AirBnb ? ')
      if Place == 'Hotel' or Place =='hotel':
         print('Game over you are broke spent all your funds')
      elif Place == 'AirBnb' or Place == 'airbnb':
         Location = input('which location will you choose as your point of location: Kasarani, Westlands or Ngong-Road?')
         if Location == 'Kasarani' or Location == 'kasarani':
            print('You just became a drunk and live for the weekend')
         elif Location == 'Westlands' or Location == 'westland':
            print('You have become a yahoo boy anxiety levels are always on the high')
         elif Location == 'Ngong Road' or Location == 'ngong road':
            print('Congratulation you just became a Tech Bro next step is landing Tech funding')   
        
else:
    print('You didnt pick a right choice' )

