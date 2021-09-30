#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Talaba
class Shaxs:
    def __init__(self,ism,fami,ota,tyil,ID):
        self.ism = ism
        self.fami = fami
        self.ota = ota
        self.tyil = tyil
        self.ID = ID
    def get_fio(self):
        return f" {self.fami} {self.ism} {self.ota}"
    def get_ID(self):
        return f"{self.ID}"
    def update_fio(self,fio):
        self.fami,self.ism,self.ota = fio.split()
    def update_ID(self,newID):
        self.ID = newID
class Talaba(Shaxs):
    def __init__(self,fio,tyil,ID,talabaID,Univer,Fak,fanga_yozil):
        ism,fam,ota = fio.split()
        super().__init__(ism,fam,ota,tyil,ID)
        self.talabaID = talabaID
        self.Univer = Univer
        self.Fak = Fak
        self.kurs = 1
        self.fanga_yozil=A
        self.fanlari=[]
    def add_yangi_fan(self,yangi_fan):
        self.fanlari.append(yangi_fan)
    def fanga_yozish(self): 
        for i in A:
            self.fanlari.append(i)
    def 
    def get_fanlari(self):
        return self.fanlari
    def remove_fan(self,ochir_fan):
        if ochir_fan in A: 
            self.fanlari.remove(ochir_fan)
            A.remove(ochir_fan)
        else:
            print ("Siz bu fanga yozilmagansiz!")
    def get_info(self):
        return f"{super().get_fio()} StudentID :{self.talabaID} Universitet {self.Univer} Facultet : {self.Fak} bosqichi : {self.kurs}, Yozilgan fanlari {self.fanga_yozil} "
    def update_kurs(self):
        self.kurs +=1
    def update_fak(self,newFak):
        self.Fak = newFak
t_1 = Talaba("Jack Will Alisson",2000,"AA0000000","T00001","TATU","DI",f"{A}")
t_1.fanga_yozish()
t_1.remove_fan("matematika")
t_1.get_info()


# In[11]:


t_1.get_info()


# In[12]:


class Fan:
    def __init__(self,nomi,vaqt,teacher):
        self.nomi=nomi
        self.vaqt=vaqt
        self.teacher=teacher
        self.fanlar=[]
    def get_nomi(self):
        return self.nomi
    def set_vaqt(self,n_vaqt):
        self.vaqt=n_vaqt
    def get_vaqt(self):
        return self.vaqt
    def get_teacher(self):
        return self.teacher
    def add_fanlar_nomi(self,nomi):
        self.fanlar.append(nomi)
    def get_fanlar(self):
        return self.fanlar
    def get_info(self):
        return f"Fan nomi : {self.nomi} , Vaqti : {self.vaqt} , O'qituvchi ismi : {self.teacher}"
fan_1=Fan("fizika","9:00 10:30" ,"JK")
fan_2=Fan("Informatika","11:00 12:30" ,"AB" )
fan_3=Fan("Tarih","13:00 14:50","CHA")
fan_4=Fan("matematika","15:15 17:00" ,"RS")
fan_4.add_fanlar_nomi(fan_1.get_nomi())
fan_4.add_fanlar_nomi(fan_2.get_nomi())
fan_4.add_fanlar_nomi(fan_3.get_nomi())
fan_4.add_fanlar_nomi(fan_4.get_nomi())
A=fan_4.get_fanlar()
fan_4.get_fanlar()


# In[166]:


fan_3.get_info()


# In[9]:


class Shaxs:
    
    def __init__(self,ism,fami,ota,tyil,ID):
        self.ism = ism
        self.fami = fami
        self.ota = ota
        self.tyil = tyil
        self.ID = ID
    def get_fio(self):
        return f" {self.fami} {self.ism} {self.ota}"
    def get_ID(self):
        return f"{self.ID}"
    def update_fio(self,fio):
        self.fami,self.ism,self.ota = fio.split()
    def update_ID(self,newID):
        self.ID = newID
class Foydalanuvchi(Shaxs):
    def __init__(self,fio,tyil,ID,username,parol):
        ism,fam,ota = fio.split()
        super().__init__(ism,fam,ota,tyil,ID)
        self.parol=parol
        self.username=username
        self.users=[]
    def get_users(self):
        return [user.get_username() for user in self.users]
    def get_username(self):
        return username
    def add_usernames(self,username):
        self.users.append(username)
    def get_parol(self):
        return parol    
    def get_info(self):
        return f"{super().get_fio()} username : {self.username},  paroli : *****{str(self.parol)[3:]} "
    def update_parol(self,yangi_parol):
        self.parol =yangi_parol
    def update_username(self,new_username):
        self.username = new_username
F_1=Foydalanuvchi("Azizov Sardor Maliko'g'li",1995,"AA0000000","BackPack_95.", "Captain_1")
F_2=Foydalanuvchi("Jalilov Akmal Salimovich",1989,"AA0000999","aKaM_00.", "Kaka10")
F_3=Foydalanuvchi("Muratov Dovud Saido'g'li",1999,"Ab77700","Aza_44.", "Dovud99")
Admin_uchun=F_3.get_users()
F_1.get_info()
# Admin classi


# In[38]:


print(type(bool))


# In[4]:


# Admin classi
class Admin(Foydalanuvchi):
    def __init__(self,fio,admin_username,site_name):
        fio = fio.split()
        super().__init__(self,ism,fam,ota)
        self.site_name=site_name
        sekf.admin_username=admin_username
        self.users=[]
        self.banned_users=[]
    def get_site_name(self):
        return self.site_name
    def get_ban_user(self):
        """ban qilingan users"""
        return [ban_user.get_info() for user in self.banned_user]
    def add_yangi_user(self,yangi_user):
        self.user.append(yangi_user)
    def usersga_yozish(self): 
        for i in A:
            self.users.append(i)
    def get_users(self):
        return [user.get_info() for user in self.users]
    def ban_user(self,ban_user):
        if ban_user in self.users: 
            self.users.remove(ban_user)
        else:
            print ("bunday user yoq!")
    def get_info(self):
        f"FIO : {super().get_fio} username : {self.admin_username} Sayt nomi : {self.site_name}"
Admin_1=Admin('Murod Qobilov Ikromovich',1996,"Ab9888333","Terrace_admin","Terrace.uz")
Admin_1.get_info()


# In[43]:


class Shifohona:
    def __init__(self,ism,fam,ota,tyil,k_tarix):
        self.__ism=ism
        self.__fam=fam
        self.__ota=ota
        self.__tyil=tyil
        self.__k_tarix=k_tarix
    def update_ism(self,y_ism):
        self.__ism=y_ism
    def update_fam(self,y_fam):
        self.__fam=y_fam
    def update_ism(self,y_ism):
        self.__ota=y_ota
    def get_info(self):
        return f"{self.__ism} {self.__fam} {self.__ota} yili: {self.__tyil} kt: {self.__k_tarix}"
a=Shifohona("MMM","Hmmm","Mdd",1998,"C0VID19")
a.fut="sdhjfh"
print(a.get_info())
print(a.fut)


# In[14]:


class Futbolchi:
    def __init__(self,ism,fam,shartnoma,muddat,maosh):
        self.__ism=ism
        self.__fam=fam
        self.__shartnoma=shartnoma
        self.__muddat=muddat
        self.__maosh=maosh
    def update_shartnoma(self,y_shart,y_muddat):
        self.__shartnoma=y_shart
        self.__muddat=y_muddat
    def get_info(self):
        return f"Futbolchi : {self.__ism} , {self.__fam} Club shartnomasi {self.__shartnoma} shartnoma muddati {self.__muddat} "
a=Futbolchi("Eldor" ,"Shomurodov","AC Roma",2022,700000)
a.update_shartnoma("Real Madrid", 2023)
a.ism=('joma')
print(a.ism,a.get_info())


# In[99]:


from math import *
class dek:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    def __lt__(self,b):
        if sqrt(self.__x**2+self.__y**2)<sqrt(b.__x**2+b.__y**2):
            return True
        else:
            return False
a=dek(1,4)
b=dek(4,3)
print(a<b)


# In[ ]:


## __eq__,__lt__ larni ishlab kel

