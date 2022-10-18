import pandas as pd
##Lectura de datos
#Homicidios
#2012
homi12='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2012_3.xlsx'
homi12_1=pd.read_excel(homi12)
homi12_1=homi12_1.drop([0,1,2,3,4,5,6,7,8,12417,12418,12419,12420,12421])
homi12_1=homi12_1.rename(columns={'MINISTERIO DE DEFENSA NACIONAL':'Departamento','Unnamed: 1':'Municipio','Unnamed: 2':'Dane','Unnamed: 4':'GENERO','Unnamed: 5':'Sexo','Unnamed: 6':'Edad','Unnamed: 7':'Homicidios','GENERO':'Fecha'})
print(homi12_1)
homi12_1.info()
homi12_2=homi12_1.groupby(['Departamento','Municipio','Dane'])['Homicidios'].agg('sum')
print(homi12_2)
homi12_2=homi12_2.to_frame()
homi12_2=homi12_2.reset_index()
homi12_2=homi12_2.assign(Año=2012)
#2013
homi13='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2013_2.xlsx'
homi13_1=pd.read_excel(homi13)
print(homi13_1)
homi13_1=homi13_1.drop([0,1,2,3,4,5,6,7,8,9,11733,11734,11735,11736,11737])
homi13_1=homi13_1.rename(columns={'MINISTERIO DE DEFENSA NACIONAL':'Departamento','Unnamed: 1':'Municipio','Unnamed: 2':'Dane','Unnamed: 4':'GENERO','Unnamed: 5':'Sexo','Unnamed: 6':'Edad','Unnamed: 7':'Homicidios','GENERO':'Fecha'})
homi13_2=homi13_1.groupby(['Departamento','Municipio','Dane'])['Homicidios'].agg('sum')
print(homi13_2)
homi13_2=homi13_2.to_frame()
homi13_2=homi13_2.reset_index()
homi13_2=homi13_2.assign(Año=2013)
#2014
homi14='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2014_2.xlsx'
homi14_1=pd.read_excel(homi14)
print(homi14_1)
homi14_1=homi14_1.drop([0,1,2,3,4,5,6,7,8,9,10558,10559,10560,10561,10562])
homi14_1=homi14_1.rename(columns={'MINISTERIO DE DEFENSA NACIONAL':'Departamento','Unnamed: 1':'Municipio','Unnamed: 2':'Dane','Unnamed: 4':'GENERO','Unnamed: 5':'Sexo','Unnamed: 6':'Edad','Unnamed: 7':'Homicidios','GENERO':'Fecha'})
homi14_2=homi14_1.groupby(['Departamento','Municipio','Dane'])['Homicidios'].agg('sum')
homi14_2=homi14_2.to_frame()
homi14_2=homi14_2.reset_index()
homi14_2=homi14_2.assign(Año=2014)
print(homi14_2)
#2015
homi15='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2015_2.xlsx'
homi15_1=pd.read_excel(homi15)
print(homi15_1)
homi15_1=homi15_1.drop([0,1,2,3,4,5,6,7,8,9,10246,10247,10248,10249,10250])
homi15_1=homi15_1.rename(columns={'MINISTERIO DE DEFENSA NACIONAL':'Departamento','Unnamed: 1':'Municipio','Unnamed: 2':'Dane','Unnamed: 4':'GENERO','Unnamed: 5':'Sexo','Unnamed: 6':'Edad','Unnamed: 7':'Homicidios','GENERO':'Fecha'})
homi15_2=homi15_1.groupby(['Departamento','Municipio','Dane'])['Homicidios'].agg('sum')
homi15_2=homi15_2.to_frame()
homi15_2=homi15_2.reset_index()
homi15_2=homi15_2.assign(Año=2015)
print(homi15_2)
#2016
homi16='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2016_2.xlsx'
homi16_1=pd.read_excel(homi16)
print(homi16_1)
homi16_1=homi16_1.drop([0,1,2,3,4,5,6,7,8,9,10056,10057,10058,10059,10060])
homi16_1=homi16_1.rename(columns={'MINISTERIO DE DEFENSA NACIONAL':'Departamento','Unnamed: 1':'Municipio','Unnamed: 2':'Dane','Unnamed: 4':'GENERO','Unnamed: 5':'Sexo','Unnamed: 6':'Edad','Unnamed: 7':'Homicidios','GENERO':'Fecha'})
homi16_2=homi16_1.groupby(['Departamento','Municipio','Dane'])['Homicidios'].agg('sum')
homi16_2=homi16_2.to_frame()
homi16_2=homi16_2.reset_index()
homi16_2=homi16_2.assign(Año=2016)
print(homi16_2)
#2017
homi17='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2017_2.xlsx'
homi17_1=pd.read_excel(homi17)
print(homi17_1)
homi17_1=homi17_1.drop([0,1,2,3,4,5,6,7,8,9,10171,10172,10173,10174,10175])
homi17_1=homi17_1.rename(columns={'MINISTERIO DE DEFENSA NACIONAL':'Departamento','Unnamed: 1':'Municipio','Unnamed: 2':'Dane','Unnamed: 4':'GENERO','Unnamed: 5':'Sexo','Unnamed: 6':'Edad','Unnamed: 7':'Homicidios','GENERO':'Fecha'})
homi17_2=homi17_1.groupby(['Departamento','Municipio','Dane'])['Homicidios'].agg('sum')
homi17_2=homi17_2.to_frame()
homi17_2=homi17_2.reset_index()
homi17_2=homi17_2.assign(Año=2017)
print(homi17_2)
#2018
homi18='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2018_1.xlsx'
homi18_1=pd.read_excel(homi18)
print(homi18_1)
homi18_1=homi18_1.drop([0,1,2,3,4,5,6,7,8,9,10652,10653,10654,10655,10656])
homi18_1=homi18_1.rename(columns={'MINISTERIO DE DEFENSA NACIONAL':'Departamento','Unnamed: 1':'Municipio','Unnamed: 2':'Dane','Unnamed: 4':'GENERO','Unnamed: 5':'Sexo','Unnamed: 6':'Edad','Unnamed: 7':'Homicidios','GENERO':'Fecha'})
homi18_2=homi18_1.groupby(['Departamento','Municipio','Dane'])['Homicidios'].agg('sum')
homi18_2=homi18_2.to_frame()
homi18_2=homi18_2.reset_index()
homi18_2=homi18_2.assign(Año=2018)
print(homi18_2)
#2019
homi19='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2019_3.xlsx'
homi19_1=pd.read_excel(homi19)
print(homi19_1)
homi19_1=homi19_1.drop([0,1,2,3,4,5,6,7,8,9,12620,12621,12622,12623,12624])
homi19_1=homi19_1.rename(columns={'MINISTERIO DE DEFENSA NACIONAL':'Departamento','Unnamed: 1':'Municipio','Unnamed: 2':'Dane','Unnamed: 4':'GENERO','Unnamed: 5':'Sexo','Unnamed: 6':'Edad','Unnamed: 7':'Homicidios','GENERO':'Fecha'})
homi19_2=homi19_1.groupby(['Departamento','Municipio','Dane'])['Homicidios'].agg('sum')
homi19_2=homi19_2.to_frame()
homi19_2=homi19_2.reset_index()
homi19_2=homi19_2.assign(Año=2019)
print(homi19_2)
#2020
homi20='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2020_0.xlsx'
homi20_1=pd.read_excel(homi20)
print(homi20_1)
homi20_1=homi20_1.drop([0,1,2,3,4,5,6,7,8,11977,11978,11979,11980,11981])
homi20_1=homi20_1.rename(columns={'MINISTERIO DE DEFENSA NACIONAL':'Departamento','Unnamed: 1':'Municipio','Unnamed: 2':'Dane','Unnamed: 4':'GENERO','Unnamed: 5':'Sexo','Unnamed: 6':'Edad','Unnamed: 7':'Homicidios','GENERO':'Fecha'})
homi20_2=homi20_1.groupby(['Departamento','Municipio','Dane'])['Homicidios'].agg('sum')
homi20_2=homi20_2.to_frame()
homi20_2=homi20_2.reset_index()
homi20_2=homi20_2.assign(Año=2020)
print(homi20_2)
#2021
homi21='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_1.xlsx'
homi21_1=pd.read_excel(homi21)
print(homi21_1)
homi21_1=homi21_1.drop([0,1,2,3,4,5,6,7,8,11537,11538,11539,11540,11541])
homi21_1=homi21_1.rename(columns={'Unnamed: 1':'Departamento','Unnamed: 2':'Municipio','Unnamed: 6':'Dane','Unnamed: 4':'SEXO','Unnamed: 5':'EDAD','Unnamed: 7':'Homicidios','Unnamed: 3':'Fecha'})
homi21_2=homi21_1.groupby(['Departamento','Municipio','Dane'])['Homicidios'].agg('sum')
homi21_2=homi21_2.to_frame()
homi21_2=homi21_2.reset_index()
homi21_2=homi21_2.assign(Año=2021)
print(homi21_2)
#Amenazas



