#Create by Seth Johnson on 9/11/2025

standards = int(input('Enter your standards: '))

if standards >= 53:
    print('A')
elif standards >= 51:
    print('A-')
elif standards >= 49:
    print('B+')
elif standards >= 47:
    print('B')
elif standards >=45 :
    print('you passed with a B-')
elif standards >=43 :
    print('you passed with a C+')
elif standards >=40 :
    print('you passed with a C')
elif standards >=35 :
    print ('you might have passed this class')
elif standards <=34 :
    print('you failed with a D+')


