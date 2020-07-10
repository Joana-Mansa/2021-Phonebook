heading="Class of 2021 Phonebook"
print(heading)
import random
first_names=['Sharon','Sharon','Sarah','Mercy','Karen','Vickie','Aseda','James','Joana','Franklin','Kelly']
sur_names=['Nyabuti','Serwaa','Appiah','Owusu','Smith','Boateng','Pokua','Hope','Afriyie','Boabeng']
hall_name=['Africa Hall','Unity Hall','Republic Hall','Queens Hall','Independence Hall','University Hall','Brunei','Hall_7',]
college_name=['CoE','CoHSS','CABE','CoH','CANASA','ÇoS']

for num in range(50):
    first= random.choice( first_names)
    last= random.choice(sur_names)
    
    school_voda= f'050-165-{random.randint(0000,9999)}'
    hall_of_residence= random.choice(hall_name)
    
    college= random.choice(college_name)
    
    student_id= random.randint(00000000,99999999)
    
    print(f'Name: {first} {last}\n Hall of Residence: {hall_of_residence}\n College: {college}\n ID:{student_id} \n Number:{school_voda}')