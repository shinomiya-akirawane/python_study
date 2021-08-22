#mags=['alice','david','carol']
#for x in mags:     for item in list_of_items
  #  print(x)

#for x in range(1,5):    #左包含右不包含
    #print(x)


#numbers=list(range(1,5,2)) #2是步长
#print(numbers)


#squares=[]
#for x in range(1,11):
    #squares.append(x**2)
#squares=[x**2 for x in range(1,11)]
#print(squares)
#print(min(squares))
#print(max(squares))
#print(sum(squares))

#numbers=['1','4','2','5','3']
#number_1=numbers #这不行，两个会一起被修改
#numbers.append('6')
#print(number_1)
#print('1' in numbers)
'''
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
        }
    }
for user,user_info in users.items():
    print('Username: '+user.title())
    print('first: '+user_info['first'])
    print('last: '+user_info['last'])
    print('location: '+user_info['location'])
    '''
'''
def build(fir_name,sec_name,**user_info):
    profile={}
    profile['first name']=fir_name
    profile['second name']=sec_name
    for k,v in user_info.items():
        profile[k]=v
    return profile
user=build('albert','einstein',location='princeton',field='physics')
print(user)
'''
#from modele1 import make_pizza as mp
#from module1 import *
'''
from users import *

admin=Admin('lily','li',12,'london')
admin.privileges.show_privileges()
'''
with open('Pi_digits.txt')as file_object:
    contents=file_object.read()
    print(contents)