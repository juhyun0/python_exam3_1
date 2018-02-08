# 주 석

'''여러
줄저
젖자
젖저
젖저
젖2ㅓ2;2
'''

'''
*****
 ****
  ***
   **
    *
   '''

for i in range(0,5):

    for j in range(0,5):

        if j>=i:
            print("*", end="", )
        else :
            print(" ", end="", )

    print()


'''
     *
    **
   ***
  ****
 *****    
'''

for i in range(0,5):

    for j in range(0,5):

        if i<=3-j:
            print(" ", end="", )
        else:
            print("*", end="",)

    print()
