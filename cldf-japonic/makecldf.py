import csv

with open('dat.csv','r') as infile:
    reader=csv.reader(infile)
    parameters=[]
    dat=[]
    firstline=True
    for row in reader:
        if firstline:
            firstline=False
        else:
            parameter=row[0]
            language=row[3]
            form=row[4]
            cognate=row[8]
            parameters.append(parameter)
            dat.append((parameter,language,form,cognate))

infile.close()

parameters=set(parameters)

parameters_d={}
n=1
for item in parameters:
    parameters_d[item]=str(n)
    n+=1

with open('languages.csv','r') as infile:
    reader=csv.reader(infile)
    languages_d={}
    firstline=True
    for row in reader:
        if firstline:
            firstline=False
        else:
            key=row[1]
            value=row[0]
            languages_d[key]=str(value)
infile.close()

parameters_file=[]
for item in parameters:
    ID=parameters_d[item]
    Name=item
    Description=''
    parameters_file.append([ID,Name,Description])

with open ('parameters.csv','w',newline='') as outfile:
    writer=csv.writer(outfile)
    writer.writerow(["ID","Name","Description"])
    for item in parameters_file:
        writer.writerow(item)
outfile.close()

forms_file=[]
# ID, Language_ID, Parameter_ID, Form
n=1
for item in dat:
    par=item[0]
    lang=item[1]
    form=item[2]
    language_ID=languages_d[lang]
    parameter_ID=parameters_d[par]
    forms_file.append([n,language_ID,parameter_ID,form])
    n+=1

with open ('forms.csv','w',newline='') as outfile:
    writer=csv.writer(outfile)
    writer.writerow(["ID","Language_ID","Parameter_ID","Form"])
    for item in forms_file:
        writer.writerow(item)
outfile.close()
    
forms_dict={}
for item in forms_file:
    form=item[3]
    form_ID=item[0]
    forms_dict[form]=form_ID

cognates_file=[]
#ID, Form_ID, Cognateset_ID
# dat is: (parameter,language,form,cognate))
for item in dat:
    Form_ID=str(forms_dict[item[2]])
    ID=Form_ID+'-1'
    cognate=item[3]
    if '?' in cognate:
        cognate="?"
    parameter_ID=str(parameters_d[item[0]])
    cognate_ID=parameter_ID+'-'+cognate
    if 'NA' in cognate_ID:
        cognate_ID='NA'
    if '?' in cognate_ID:
        cognate_ID='?'
    cognates_file.append([ID,Form_ID,cognate_ID])

with open ('cognates.csv','w',newline='') as outfile:
    writer=csv.writer(outfile)
    writer.writerow(["ID","Form_ID","Cognateset_ID"])
    for item in cognates_file:
        writer.writerow(item)
outfile.close()

    
        
    





    
