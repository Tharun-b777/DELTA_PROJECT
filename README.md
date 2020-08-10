# DELTA_PROJECT
Use url localhost:8080/app1/api/post_office

GET METHODS

/api/post_office/all

returns all the data in a json Format

/api/post_office?Officetype=B.O&Dstats=Delivery

returns post office data (the data consists of all the info of post office given in the querry parameters) with having officetype as B.O and deliverystatus as Delivery
If the data is not present for the given query parameters it returns an empty String

Querry parameters:

id

Officename

Pincode

Officetype

Dstats  (deliverystatus)

Divname (division name)

Regname (Region name)

Circlename

Taluk

Distname (district name)

Statename

Phnum    (Telephone number)

RHO      (Regional Head Office)

RSO      (Regional Sub Ofiice)

All the querry parameters are strings except for id which integer

DELETE METHOD

/api/post_office/id

/api/post_office/2

returns the JSON object of deleted post office of id 2

{
    "Officename":"BEERNADI B.O",

    "Pincode":"631502",

    "Officetype": "B.O",

    "Dstats": "DELIVERY",

    "Divname": "ADILABAD",

    "Regname": "HYDERABAD",

    "Circlename": "ANDHRA PRADESH",

    "Taluk": "CHENNUR",

    "Distname": "ADILABAD",

    "Statename": "TELANGANA",

    "Phnum": "08733-279530",

    "RHO": "JAINOOR S.O",

    "RSO": "MANCHERIAL H.O"

    "id": 2
}

 if the id given is not present or is aldready deleted
 {
     'data':"not existing"
 }

 The above json object is returned

 POST METHOD:

 /api/post_office

 It should contain a json body with all info specified in querry parameters except id.

 http://0.0.0.0:32783/api/post_office

 JSON body:
 {

    "Officename":"Beernandi B.O",

    "Pincode":"631502",

    "Officetype": "b.o",

    "Dstats": "delivery",

    "Divname": "Adilabad",

    "Regname": "Hyderabad",

    "Circlename": "Andhra Pradesh",

    "Taluk": "Chennur",

    "Distname": "Adilabad",

    "Statename": "TELANGANA",

    "Phnum": "08733-279530",

    "RHO": "Jainoor S.O",

    "RSO": "Mancherial H.O"
}

 It returns the json object of the posted data along with it's id

 The above data returns the below JSON object

 {

     "Officename":"BEERNADI B.O",

     "Pincode":"631502",

     "Officetype": "B.O",

     "Dstats": "DELIVERY",

     "Divname": "ADILABAD",

     "Regname": "HYDERABAD",

     "Circlename": "ANDHRA PRADESH",

     "Taluk": "CHENNUR",

     "Distname": "ADILABAD",

     "Statename": "TELANGANA",

     "Phnum": "08733-279530",

     "RHO": "JAINOOR S.O",

     "RSO": "MANCHERIAL H.O"

     "id": 154798

 }

 PUT METHOD:

 /api/post_office/id

 http://0.0.0.0:32783/api/post_office/154798

 JSON body:

 {

    "Officename":"BERNADI",

    "Pincode":"631501",

    "Officetype": "H.O"

}

 It should contain a json body only with parameters to be changed

 It returns the json object of the changed data

 {
     "Officename":"BERNADI",

     "Pincode":"631501",

     "Officetype": "H.O",

     "Dstats": "DELIVERY",

     "Divname": "ADILABAD",

     "Regname": "HYDERABAD",

     "Circlename": "ANDHRA PRADESH",

     "Taluk": "CHENNUR",

     "Distname": "ADILABAD",

     "Statename": "TELANGANA",

     "Phnum": "08733-279530",

     "RHO": "JAINOOR S.O",

     "RSO": "MANCHERIAL H.O"

     "id": 154798
 }

if the id given is not present or is deleted

{
    'data':"not existing"
}

The above json object is returned

Use the below command to run multiple containers of api service

docker-compose up --build --scale api=2
