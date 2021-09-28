#!/usr/bin/env python
# coding: utf-8

# In[5]:


class odam:
    def __init__(self, name,lives_in,birthday,age,number,id_number,grade,study_at):
        self.name = name
        self.lives_in = lives_in
        self.birthday=birthday
        self.number=number
        self.id_number=id_number
        self.study_at=study_at
        self.grade=grade
        self.age=age
    def set_age(self,n_age):
        self.age=n_age
    def __iadd__(self,age,n_age):
        self.age=age+10
        return self.age
    def update_age(self):
        self.age+=1
    def set_grade(self,grade):
        self.grade=grade
    def update_grade(self):
        self.grade+=1
    def get_info(self):
        return f" Currently living : {self.lives_in},Name : {self.name},Birth of date : {self.birthday},Age : {self.age},  number: {self.number} , ID number : {self.id_number}, grade : {self.grade} , study at : {self.study_at} "
sh_1=odam("Said","Namangan","1998.01.01",23,"9998877","AB0676378",1,"PNU")
sh_2=odam("Azam","Toshkent","1996.01.01",25,"5551322","AB0600898",1, "TATU")
sh_3=odam("Sergey","Moskva","1994.01.01",27,"3321010","AB0673445",3,"MU")
sh_4=odam("KimSan","Seul","1993.01.01",28,"59264891","AB0456372"    ,2,"AIU")
#sh_1.update_age()
print((sh_1.get_info()))
print((sh_2.get_info()))
print((sh_3.get_info()))
print((sh_4.get_info()))


# In[ ]:




