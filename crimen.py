import pandas as pd
import numpy as np
##Lectura de datos
#Homicidios
homi12='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2012_3.xlsx'
homi13='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2013_2.xlsx'
homi14='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2014_2.xlsx'
homi15='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2015_2.xlsx'
homi16='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2016_2.xlsx'
homi17='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2017_2.xlsx'
homi18='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2018_1.xlsx'
homi19='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2019_3.xlsx'
homi20='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_2020_0.xlsx'
homi21='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Homicidios\\homicidios_1.xlsx'
homi12_1=pd.read_excel(homi12)
homi13_1=pd.read_excel(homi13)
homi14_1=pd.read_excel(homi14)
homi15_1=pd.read_excel(homi15)
homi16_1=pd.read_excel(homi16)
homi17_1=pd.read_excel(homi17)
homi18_1=pd.read_excel(homi18)
homi19_1=pd.read_excel(homi19)
homi20_1=pd.read_excel(homi20)
homi21_1=pd.read_excel(homi21)
#limpieza
homi21_1=homi21_1[['DEPARTAMENTO ','MUNICIPIO','CODIGO_DANE','ARMAS_MEDIOS','FECHA ','GENERO','*AGRUPA_EDAD_PERSONA','CANTIDAD ']]
homi19_1=homi19_1.rename(columns={'AGRUPA EDAD PERSONA':'*AGRUPA EDAD PERSONA'})
homi20_1=homi20_1.rename(columns={'AGRUPA EDAD PERSONA':'*AGRUPA EDAD PERSONA'})
homi21_1=homi21_1.rename(columns={'*AGRUPA_EDAD_PERSONA':'*AGRUPA EDAD PERSONA','CODIGO_DANE':'CODIGO DANE','ARMAS_MEDIOS':'ARMAS MEDIOS','FECHA':'FECHA HECHO','DEPARTAMENTO ':'DEPARTAMENTO','CANTIDAD ':'CANTIDAD'})
homi12_1=homi12_1.drop(['FECHA HECHO'],axis=1)
homi12_1=homi12_1.assign(Año=2012)
homi13_1=homi13_1.drop(['FECHA HECHO'],axis=1)
homi13_1=homi13_1.assign(Año=2013)
homi14_1=homi14_1.drop(['FECHA HECHO'],axis=1)
homi14_1=homi14_1.assign(Año=2014)
homi15_1=homi15_1.drop(['FECHA HECHO'],axis=1)
homi15_1=homi15_1.assign(Año=2015)
homi16_1=homi16_1.drop(['FECHA HECHO'],axis=1)
homi16_1=homi16_1.assign(Año=2016)
homi17_1=homi17_1.drop(['FECHA HECHO'],axis=1)
homi17_1=homi17_1.assign(Año=2017)
homi18_1=homi18_1.drop(['FECHA HECHO'],axis=1)
homi18_1=homi18_1.assign(Año=2018)
homi19_1=homi19_1.drop(['FECHA HECHO'],axis=1)
homi19_1=homi19_1.assign(Año=2019)
homi20_1=homi20_1.drop(['FECHA HECHO'],axis=1)
homi20_1=homi20_1.assign(Año=2020)
homi21_1=homi21_1.drop(['FECHA '],axis=1)
homi21_1=homi21_1.assign(Año=2021)
#Union
homi=pd.concat([homi12_1,homi13_1,homi14_1,homi15_1,homi16_1,homi17_1,homi18_1,homi19_1,homi20_1,homi21_1])
homi=homi.drop(['ARMAS MEDIOS','GENERO','*AGRUPA EDAD PERSONA'],axis=1)
homi=homi.rename(columns={'CANTIDAD':'Homicidios'})
homi=homi.groupby(['DEPARTAMENTO','MUNICIPIO','CODIGO DANE','Año'])['Homicidios'].agg('sum')
homi=homi.to_frame()
homi=homi.reset_index()
homi['CODIGO DANE']=(homi['CODIGO DANE']/1000)
homi['CODIGO DANE']=homi['CODIGO DANE'].astype(int)
print(homi)

#Amenazas
amen12='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Amenazas\\amenazas_2012.xlsx'
amen13='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Amenazas\\amenazas_2013_0.xlsx'
amen14='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Amenazas\\amenazas_2014_0.xlsx'
amen15='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Amenazas\\amenazas_2015_0.xlsx'
amen16='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Amenazas\\amenazas_2016_0.xlsx'
amen17='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Amenazas\\amenazas_2017_0.xlsx'
amen18='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Amenazas\\amenazas_2018_1.xlsx'
amen19='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Amenazas\\amenazas_2019_1.xlsx'
amen20='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Amenazas\\amenazas_2020_0.xlsx'
amen21='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Amenazas\\amenazas_1.xlsx'
amen12_1=pd.read_excel(amen12)
amen13_1=pd.read_excel(amen13)
amen14_1=pd.read_excel(amen14)
amen15_1=pd.read_excel(amen15)
amen16_1=pd.read_excel(amen16)
amen17_1=pd.read_excel(amen17)
amen18_1=pd.read_excel(amen18)
amen19_1=pd.read_excel(amen19)
amen20_1=pd.read_excel(amen20)
amen21_1=pd.read_excel(amen21)
#Limpieza
amen21_1.info()
amen21_1=amen21_1[['DEPARTAMENTO','MUNICIPIO','CODIGO DANE','ARMAS MEDIOS','FECHA ','GENERO','*AGRUPA EDAD PERSONA','CANTIDAD']]
amen19_1=amen19_1.rename(columns={'AGRUPA EDAD PERSONA':'*AGRUPA EDAD PERSONA'})
amen20_1=amen20_1.rename(columns={'AGRUPA EDAD PERSONA':'*AGRUPA EDAD PERSONA'})
amen21_1=amen21_1.rename(columns={'*AGRUPA_EDAD_PERSONA':'*AGRUPA EDAD PERSONA','CODIGO_DANE':'CODIGO DANE','ARMAS_MEDIOS':'ARMAS MEDIOS','FECHA':'FECHA HECHO','DEPARTAMENTO ':'DEPARTAMENTO','CANTIDAD ':'CANTIDAD'})
amen12_1=amen12_1.drop(['FECHA HECHO'],axis=1)
amen12_1=amen12_1.assign(Año=2012)
amen13_1=amen13_1.drop(['FECHA HECHO'],axis=1)
amen13_1=amen13_1.assign(Año=2013)
amen14_1=amen14_1.drop(['FECHA HECHO'],axis=1)
amen14_1=amen14_1.assign(Año=2014)
amen15_1=amen15_1.drop(['FECHA HECHO'],axis=1)
amen15_1=amen15_1.assign(Año=2015)
amen16_1=amen16_1.drop(['FECHA HECHO'],axis=1)
amen16_1=amen16_1.assign(Año=2016)
amen17_1=amen17_1.drop(['FECHA HECHO'],axis=1)
amen17_1=amen17_1.assign(Año=2017)
amen18_1=amen18_1.drop(['FECHA HECHO'],axis=1)
amen18_1=amen18_1.assign(Año=2018)
amen19_1=amen19_1.drop(['FECHA HECHO'],axis=1)
amen19_1=amen19_1.assign(Año=2019)
amen20_1=amen20_1.drop(['FECHA HECHO'],axis=1)
amen20_1=amen20_1.assign(Año=2020)
amen21_1=amen21_1.drop(['FECHA '],axis=1)
amen21_1=amen21_1.assign(Año=2021)
#Union
amen=pd.concat([amen12_1,amen13_1,amen14_1,amen15_1,amen16_1,amen17_1,amen18_1,amen19_1,amen20_1,amen21_1])
amen=amen.drop(['ARMAS MEDIOS','GENERO','*AGRUPA EDAD PERSONA'],axis=1)
amen=amen.rename(columns={'CANTIDAD':'Amenazas'})
amen=amen.groupby(['DEPARTAMENTO','MUNICIPIO','CODIGO DANE','Año'])['Amenazas'].agg('sum')
amen=amen.to_frame()
amen=amen.reset_index()
amen['CODIGO DANE']=(amen['CODIGO DANE']/1000)
amen['CODIGO DANE']=amen['CODIGO DANE'].astype(int)
print(amen)
#Merge 
data=pd.merge(homi,amen,how='outer')
print(data)
data.info()

#Delitos sexuales
deli12='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Delitos sexuales\\delitos_sexuales_2012_0.xlsx'
deli13='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Delitos sexuales\\delitos_sexuales_2013_0.xlsx'
deli14='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Delitos sexuales\\delitos_sexuales_2014_0.xlsx'
deli15='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Delitos sexuales\\delitos_sexuales_2015_0.xlsx'
deli16='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Delitos sexuales\\delitos_sexuales_2016_0.xlsx'
deli17='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Delitos sexuales\\delitos_sexuales_2017_0.xlsx'
deli18='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Delitos sexuales\\delitos_sexuales_2018_0.xlsx'
deli19='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Delitos sexuales\\delitos_sexuales_2019_0.xlsx'
deli20='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Delitos sexuales\\delitos_sexuales_2020_0.xlsx'
deli21='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Delitos sexuales\\delitos_sexuales_1.xlsx'
deli12_1=pd.read_excel(deli12)
deli13_1=pd.read_excel(deli13)
deli14_1=pd.read_excel(deli14)
deli15_1=pd.read_excel(deli15)
deli16_1=pd.read_excel(deli16)
deli17_1=pd.read_excel(deli17)
deli18_1=pd.read_excel(deli18)
deli19_1=pd.read_excel(deli19)
deli20_1=pd.read_excel(deli20)
deli21_1=pd.read_excel(deli21)
deli19_1.info()
deli21_1=deli21_1[['DEPARTAMENTO','MUNICIPIO','CODIGO_DANE','ARMAS_MEDIOS','FECHA ','GENERO','*AGRUPA_EDAD_PERSONA','CANTIDAD ']]
print(deli19_1)
deli19_1=deli19_1.rename(columns={'AGRUPA EDAD PERSONA':'*AGRUPA EDAD PERSONA'})
deli20_1=deli20_1.rename(columns={'AGRUPA EDAD PERSONA':'*AGRUPA EDAD PERSONA'})
deli21_1=deli21_1.rename(columns={'*AGRUPA_EDAD_PERSONA':'*AGRUPA EDAD PERSONA','CODIGO_DANE':'CODIGO DANE','ARMAS_MEDIOS':'ARMAS MEDIOS','FECHA':'FECHA HECHO','DEPARTAMENTO ':'DEPARTAMENTO','CANTIDAD ':'CANTIDAD'})
deli12_1=deli12_1.drop(['FECHA HECHO'],axis=1)
deli12_1=deli12_1.assign(Año=2012)
deli13_1=deli13_1.drop(['FECHA HECHO'],axis=1)
deli13_1=deli13_1.assign(Año=2013)
deli14_1=deli14_1.drop(['FECHA HECHO'],axis=1)
deli14_1=deli14_1.assign(Año=2014)
deli15_1=deli15_1.drop(['FECHA HECHO'],axis=1)
deli15_1=deli15_1.assign(Año=2015)
deli16_1=deli16_1.drop(['FECHA HECHO'],axis=1)
deli16_1=deli16_1.assign(Año=2016)
deli17_1=deli17_1.drop(['FECHA HECHO'],axis=1)
deli17_1=deli17_1.assign(Año=2017)
deli18_1=deli18_1.drop(['FECHA HECHO'],axis=1)
deli18_1=deli18_1.assign(Año=2018)
deli19_1=deli19_1.drop(['FECHA HECHO'],axis=1)
deli19_1=deli19_1.assign(Año=2019)
deli20_1=deli20_1.drop(['FECHA HECHO'],axis=1)
deli20_1=deli20_1.assign(Año=2020)
deli21_1=deli21_1.drop(['FECHA '],axis=1)
deli21_1=deli21_1.assign(Año=2021)
deli=pd.concat([deli12_1,deli13_1,deli14_1,deli15_1,deli16_1,deli17_1,deli18_1,deli19_1,deli20_1,deli21_1])
deli=deli.drop(['ARMAS MEDIOS','GENERO','*AGRUPA EDAD PERSONA','AGRUPA EDAD PERSONA'],axis=1)
deli=deli.rename(columns={'CANTIDAD':'Delitos Sexuales'})
deli=deli.groupby(['DEPARTAMENTO','MUNICIPIO','CODIGO DANE','Año'])['Delitos Sexuales'].agg('sum')
deli=deli.to_frame()
deli=deli.reset_index()
deli['CODIGO DANE']=(deli['CODIGO DANE']/1000)
deli['CODIGO DANE']=deli['CODIGO DANE'].astype(int)
print(deli)
data1=deli.merge(data, how='outer')
print(data1)
#Extorsion
exto12='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Extorsion\\extorsion_2012_2.xlsx'
exto13='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Extorsion\\extorsion_2013_3.xlsx'
exto14='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Extorsion\\extorsion_2014_3.xlsx'
exto15='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Extorsion\\extorsion_2015_3.xlsx'
exto16='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Extorsion\\extorsion_2016_2.xlsx'
exto17='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Extorsion\\extorsion_2017_2.xlsx'
exto18='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Extorsion\\extorsion_2018_1.xlsx'
exto19='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Extorsion\\extorsion_2019_4.xlsx'
exto20='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Extorsion\\extorsion_2020_0.xlsx'
exto21='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Extorsion\\extorsion_1.xlsx'
exto12_1=pd.read_excel(exto12)
exto13_1=pd.read_excel(exto13)
exto14_1=pd.read_excel(exto14)
exto15_1=pd.read_excel(exto15)
exto16_1=pd.read_excel(exto16)
exto17_1=pd.read_excel(exto17)
exto18_1=pd.read_excel(exto18)
exto19_1=pd.read_excel(exto19)
exto20_1=pd.read_excel(exto20)
exto21_1=pd.read_excel(exto21)
exto21_1=exto21_1[['DEPARTAMENTO','MUNICIPIO','CODIGO_DANE','ARMAS_MEDIOS','FECHA ','GENERO','*AGRUPA_EDAD_PERSONA','CANTIDAD ']]
exto19_1=exto19_1.rename(columns={'AGRUPA EDAD PERSONA':'*AGRUPA EDAD PERSONA'})
exto20_1=exto20_1.rename(columns={'AGRUPA EDAD PERSONA':'*AGRUPA EDAD PERSONA'})
exto21_1=exto21_1.rename(columns={'*AGRUPA_EDAD_PERSONA':'*AGRUPA EDAD PERSONA','CODIGO_DANE':'CODIGO DANE','ARMAS_MEDIOS':'ARMAS MEDIOS','FECHA':'FECHA HECHO','DEPARTAMENTO ':'DEPARTAMENTO','CANTIDAD ':'CANTIDAD'})
exto12_1=exto12_1.drop(['FECHA HECHO'],axis=1)
exto12_1=exto12_1.assign(Año=2012)
exto13_1=exto13_1.drop(['FECHA HECHO'],axis=1)
exto13_1=exto13_1.assign(Año=2013)
exto14_1=exto14_1.drop(['FECHA HECHO'],axis=1)
exto14_1=exto14_1.assign(Año=2014)
exto15_1=exto15_1.drop(['FECHA HECHO'],axis=1)
exto15_1=exto15_1.assign(Año=2015)
exto16_1=exto16_1.drop(['FECHA HECHO'],axis=1)
exto16_1=exto16_1.assign(Año=2016)
exto17_1=exto17_1.drop(['FECHA HECHO'],axis=1)
exto17_1=exto17_1.assign(Año=2017)
exto18_1=exto18_1.drop(['FECHA HECHO'],axis=1)
exto18_1=exto18_1.assign(Año=2018)
exto19_1=exto19_1.drop(['FECHA HECHO'],axis=1)
exto19_1=exto19_1.assign(Año=2019)
exto20_1=exto20_1.drop(['FECHA HECHO'],axis=1)
exto20_1=exto20_1.assign(Año=2020)
exto21_1=exto21_1.drop(['FECHA '],axis=1)
exto21_1=exto21_1.assign(Año=2021)
exto=pd.concat([exto12_1,exto13_1,exto14_1,exto15_1,exto16_1,exto17_1,exto18_1,exto19_1,exto20_1,exto21_1])
exto.info()
exto=exto.drop(['ARMAS MEDIOS','GENERO','*AGRUPA EDAD PERSONA','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13'],axis=1)
exto=exto.rename(columns={'CANTIDAD':'Extorsion'})
exto=exto.groupby(['DEPARTAMENTO','MUNICIPIO','CODIGO DANE','Año'])['Extorsion'].agg('sum')
exto=exto.to_frame()
exto=exto.reset_index()
exto['CODIGO DANE']=(exto['CODIGO DANE']/1000)
exto=exto.drop(4169)
exto['CODIGO DANE']=exto['CODIGO DANE'].astype(int)
print(exto)
data2=data1.merge(exto, how='outer')
print(data2)
#Secuestro
secu12='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Secuestro\\secuestro_2012_2.xlsx'
secu13='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Secuestro\\secuestro_2013_2.xlsx'
secu14='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Secuestro\\secuestro_2014_2.xlsx'
secu15='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Secuestro\\secuestro_2015_2.xlsx'
secu16='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Secuestro\\secuestro_2016_2.xlsx'
secu17='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Secuestro\\secuestro_2017_2.xlsx'
secu18='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Secuestro\\secuestro_2018_2.xlsx'
secu19='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Secuestro\\secuestro_2019_3.xlsx'
secu20='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Secuestro\\secuestro_2020_0.xlsx'
secu21='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Secuestro\\secuestro_1.xlsx'
secu12_1=pd.read_excel(secu12)
secu13_1=pd.read_excel(secu13)
secu14_1=pd.read_excel(secu14)
secu15_1=pd.read_excel(secu15)
secu16_1=pd.read_excel(secu16)
secu17_1=pd.read_excel(secu17)
secu18_1=pd.read_excel(secu18)
secu19_1=pd.read_excel(secu19)
secu20_1=pd.read_excel(secu20)
secu21_1=pd.read_excel(secu21)
secu21_1.info()
secu21_1=secu21_1[['DEPARTAMENTO','MUNICIPIO','CODIGO_DANE','ARMAS MEDIOS','FECHA HECHO','GENERO','*AGRUPA_EDAD_PERSONA','CANTIDAD ']]
secu19_1=secu19_1.rename(columns={'AGRUPA EDAD PERSONA':'*AGRUPA EDAD PERSONA'})
secu20_1=secu20_1.rename(columns={'AGRUPA EDAD PERSONA':'*AGRUPA EDAD PERSONA'})
secu21_1=secu21_1.rename(columns={'*AGRUPA_EDAD_PERSONA':'*AGRUPA EDAD PERSONA','CODIGO_DANE':'CODIGO DANE','ARMAS_MEDIOS':'ARMAS MEDIOS','FECHA':'FECHA HECHO','DEPARTAMENTO ':'DEPARTAMENTO','CANTIDAD ':'CANTIDAD'})
secu12_1=secu12_1.drop(['FECHA HECHO'],axis=1)
secu12_1=secu12_1.assign(Año=2012)
secu13_1=secu13_1.drop(['FECHA HECHO'],axis=1)
secu13_1=secu13_1.assign(Año=2013)
secu14_1=secu14_1.drop(['FECHA HECHO'],axis=1)
secu14_1=secu14_1.assign(Año=2014)
secu15_1=secu15_1.drop(['FECHA HECHO'],axis=1)
secu15_1=secu15_1.assign(Año=2015)
secu16_1=secu16_1.drop(['FECHA HECHO'],axis=1)
secu16_1=secu16_1.assign(Año=2016)
secu17_1=secu17_1.drop(['FECHA HECHO'],axis=1)
secu17_1=secu17_1.assign(Año=2017)
secu18_1=secu18_1.drop(['FECHA HECHO'],axis=1)
secu18_1=secu18_1.assign(Año=2018)
secu19_1=secu19_1.drop(['FECHA HECHO'],axis=1)
secu19_1=secu19_1.assign(Año=2019)
secu20_1=secu20_1.drop(['FECHA HECHO'],axis=1)
secu20_1=secu20_1.assign(Año=2020)
secu21_1=secu21_1.drop(['FECHA HECHO'],axis=1)
secu21_1=secu21_1.assign(Año=2021)
secu=pd.concat([secu12_1,secu13_1,secu14_1,secu15_1,secu16_1,secu17_1,secu18_1,secu19_1,secu20_1,secu21_1])
secu.info()
secu=secu.drop(['ARMAS MEDIOS','GENERO','*AGRUPA EDAD PERSONA','AGRUPA EDAD PERSONA'],axis=1)
secu=secu.rename(columns={'CANTIDAD':'Secuestro'})
secu=secu.groupby(['DEPARTAMENTO','MUNICIPIO','CODIGO DANE','Año'])['Secuestro'].agg('sum')
secu=secu.to_frame()
secu=secu.reset_index()
secu['CODIGO DANE']=(secu['CODIGO DANE']/1000)
secu['CODIGO DANE']=secu['CODIGO DANE'].astype(int)
print(secu)
data3=data2.merge(secu, how='outer')
print(data3)
data3.info()
#Terrorismo
terr12='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Terrorismo\\terrorismo_2012_2.xlsx'
terr13='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Terrorismo\\terrorismo_2013_2.xlsx'
terr14='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Terrorismo\\terrorismo_2014_1.xlsx'
terr15='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Terrorismo\\terrorismo_2015_2.xlsx'
terr16='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Terrorismo\\terrorismo_2016_2.xlsx'
terr17='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Terrorismo\\terrorismo_2017_2.xlsx'
terr18='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Terrorismo\\terrorismo_2018_0.xlsx'
terr19='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Terrorismo\\terrorismo_2019_2.xlsx'
terr20='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Terrorismo\\terrorismo_2020_0.xlsx'
terr21='C:\\Users\\lucho\\OneDrive\\Documentos\\Proyectos\\Victimas-Crimen\\Valledupar\\Terrorismo\\terrorismo_1.xlsx'
terr12_1=pd.read_excel(terr12)
terr13_1=pd.read_excel(terr13)
terr14_1=pd.read_excel(terr14)
terr15_1=pd.read_excel(terr15)
terr16_1=pd.read_excel(terr16)
terr17_1=pd.read_excel(terr17)
terr18_1=pd.read_excel(terr18)
terr19_1=pd.read_excel(terr19)
terr20_1=pd.read_excel(terr20)
terr21_1=pd.read_excel(terr21)
terr12_1.info()
terr21_1=terr21_1[['Departamento','Municipio','CODIGO_DANE','ARMAS_MEDIOS','FECHA_HECHO','CANTIDAD']]
terr21_1=terr21_1.rename(columns={'CODIGO_DANE':'CODIGO DANE','ARMAS_MEDIOS':'ARMAS MEDIOS','FECHA':'FECHA HECHO','CANTIDAD ':'CANTIDAD'})
terr12_1=terr12_1.drop(['FECHA HECHO'],axis=1)
terr12_1=terr12_1.assign(Año=2012)
terr13_1=terr13_1.drop(['FECHA HECHO'],axis=1)
terr13_1=terr13_1.assign(Año=2013)
terr14_1=terr14_1.drop(['FECHA HECHO'],axis=1)
terr14_1=terr14_1.assign(Año=2014)
terr15_1=terr15_1.drop(['FECHA HECHO'],axis=1)
terr15_1=terr15_1.assign(Año=2015)
terr16_1=terr16_1.drop(['FECHA HECHO'],axis=1)
terr16_1=terr16_1.assign(Año=2016)
terr17_1=terr17_1.drop(['FECHA HECHO'],axis=1)
terr17_1=terr17_1.assign(Año=2017)
terr18_1=terr18_1.drop(['FECHA HECHO'],axis=1)
terr18_1=terr18_1.assign(Año=2018)
terr19_1=terr19_1.drop(['FECHA HECHO'],axis=1)
terr19_1=terr19_1.assign(Año=2019)
terr20_1=terr20_1.drop(['FECHA HECHO'],axis=1)
terr20_1=terr20_1.assign(Año=2020)
terr21_1=terr21_1.drop(['FECHA_HECHO'],axis=1)
terr21_1=terr21_1.assign(Año=2021)
terr=pd.concat([terr12_1,terr13_1,terr14_1,terr15_1,terr16_1,terr17_1,terr18_1,terr19_1,terr20_1,terr21_1])
terr.info()
terr=terr.drop(['ARMAS MEDIOS'],axis=1)
terr=terr.rename(columns={'CANTIDAD':'Terrorismo'})
terr=terr.groupby(['Departamento','Municipio','CODIGO DANE','Año'])['Terrorismo'].agg('sum')
terr=terr.to_frame()
terr=terr.reset_index()
terr['CODIGO DANE']=(terr['CODIGO DANE']/1000)
terr['CODIGO DANE']=terr['CODIGO DANE'].astype(int)
print(terr)
terr=terr.rename(columns={'Departamento':'DEPARTAMENTO','Municipio':'MUNICIPIO'})
data4=terr.merge(data3, how='outer',sort=True)
print(data4)
data4.info()

#Detalles
s2=pd.read_excel("Victimas-Crimen\\2018.xlsx")
s1=pd.read_excel("Victimas-Crimen\\1985-2017.xlsx")
s1=s1.drop([0,1,2,3,4,5,6,7,8,9,10,111089])
s2=s2.drop([0,1,2,3,4,5,6,7,8,9,10])
s2=s2[s2['Unnamed: 5'].str.contains('Total')==True]
s1=s1[s1['Unnamed: 5'].str.contains('Total')==True]
s2=s2.drop(['Unnamed: 0','Unnamed: 5','Unnamed: 1','Unnamed: 3'],axis=1)
s1=s1.drop(['Unnamed: 0','Unnamed: 5','Unnamed: 1','Unnamed: 3'],axis=1)
s2=s2.rename(columns={'Unnamed: 6':'Poblacion','Unnamed: 2':'CODIGO DANE','Unnamed: 4':'Año'})
s1=s1.rename(columns={'Unnamed: 6':'Poblacion','Unnamed: 2':'CODIGO DANE','Unnamed: 4':'Año'})
s1['CODIGO DANE']=s1['CODIGO DANE'].astype(int)
s2['CODIGO DANE']=s2['CODIGO DANE'].astype(int)

print(s2)
s=pd.concat([s1,s2])
datos=data4.merge(s,how='left',sort=True)
datos=datos.fillna(0)
datos['Terrorismo']=datos['Terrorismo'].astype(int)
datos['Delitos Sexuales']=datos['Delitos Sexuales'].astype(int)
datos['Homicidios']=datos['Homicidios'].astype(int)
datos['Amenazas']=datos['Amenazas'].astype(int)
datos['Extorsion']=datos['Extorsion'].astype(int)
datos['Secuestro']=datos['Secuestro'].astype(int)
datos['Total']=datos['Terrorismo']+datos['Delitos Sexuales']+datos['Homicidios']+datos['Amenazas']+datos['Extorsion']+datos['Secuestro']
datos['Total']=datos['Total'].astype(int)
datos.replace(0, np.nan)
datos['Indice100k']=(datos['Total']/datos['Poblacion'])*100000
print(datos)

datos.to_excel('datos.xlsx')





