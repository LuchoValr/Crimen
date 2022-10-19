import pandas as pd
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
data=homi.merge(amen, how='left',on=['CODIGO DANE','Año','DEPARTAMENTO','MUNICIPIO'])
print(data)

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
data1=data.merge(deli, how='left',on=['CODIGO DANE','Año','DEPARTAMENTO','MUNICIPIO'])
print(data1)












