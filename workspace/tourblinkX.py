import pyrebase

config = {
  "apiKey": "AIzaSyD4bR4ftpXUfVrnj12xQ8OU_TrDR-z6398",
  "authDomain": "tourblink.firebaseapp.com",
  "databaseURL": "https://tourblink.firebaseio.com",
  "storageBucket": "tourblink.appspot.com",
  "messagingSenderId": "19313768876"
}

# config = {
#     "apiKey": "AIzaSyBXskeikWr_uDkIEmOl21YnO2zonlzIlUI",
#     "authDomain": "prueba-a4679.firebaseapp.com",
#     "databaseURL": "https://prueba-a4679.firebaseio.com",
#     "storageBucket": "prueba-a4679.appspot.com",
#     "messagingSenderId": "454315014961"
# }
firebase = pyrebase.initialize_app(config)
databaseTourBlink = firebase.database()
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("javierborregocejudo@gmail.com", "javier")
valuesDatabase = databaseTourBlink.child("Items").child("data").get()
value = 0

storageTourBlink = firebase.storage()

for key, list_item in valuesDatabase.__dict__.iteritems():
    if key == "pyres":
        for item in list_item:
            value+=1
            print item.val()
            folderPathImg = storageTourBlink.child(str(item.val()))
            #no hace falta porque ya tenemos el valor del archivo en
            ext_item = str(value)[5:]
            name_item = str(value)[:10]
            folderPathImg.download(name_item+ext_item)         

            print item

# db = firebase.database()

# data to save
# data = {
#     "name": "Mortimer 'Morty' Smith"
# }

# Pass the user's idToken to the push method
# results = db.child("users").push(data, user['idToken'])
#

# storageTourBlink = firebase.storage()
# folderPathImg = storageTourBlink.child("LOU_20170312_192755_Android SDK built for x86/data/loremipsum.json")
# folderPathImg.download("jsonDescargado.json")

# print storageTourBlink.child("20170110_013639_SM-G900M/14/IMG20170114_222812.jpg").get_url()
# esta variable se necesita para algunas cosas ""user['idToken']""
