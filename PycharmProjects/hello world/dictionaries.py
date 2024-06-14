phone_no={'RAM':1234,'SHYAM':6778,'VIDYA':9987}
print(phone_no)
hone_no={'RAM':1234,'SHYAM':6778,'RAM':9987}#DUPLICATION
print(hone_no)
phone_no={
    'RAM':1234,
    'SHYAM':6778,
    'VIDYA':9987
}#correct way of writing dict

#access particular key
print(phone_no["SHYAM"])

#METHOD TO CREATE
phone_no=dict({
    'RAM':1234,
    'SHYAM':6778,
    'VIDYA':9987
})

#mutable
phone_no['VIDYA']=8888888
print(phone_no)

#add of new element
phone_no['MADHAV']=87654
print(phone_no)

#NESTED DICTIONARIES
phone_no['JADHAV']={54632677,8866549}
phone_no['SHYAM']={'SHYAM_HOME':555555,"SHYAM_OFFICE":97765335}
print(phone_no)

#DELETE
del phone_no['JADHAV']
print(phone_no)
phone_no.pop('RAM')
print(phone_no)
print(phone_no.keys())
print(phone_no.values())
print(phone_no.items())

