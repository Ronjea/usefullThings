#To use this script please follow the Readme file in the folder
import pyrebase
import os

# Config to connect to the app
config = {
  "apiKey": "**************************",
  "authDomain": "***************************",
  "databaseURL": "***********************",
  "storageBucket": "****************",
  "messagingSenderId": "**********"
}
# We initialize the app with this using the config
firebase = pyrebase.initialize_app(config)
# We use those variables to have access to the services in this case database or storage
databaseYourFirebase = firebase.database()
storageYourFirebase = firebase.storage()


#Functions to use in the script

# def for calculate_progress in the download
def calculate_progress(list_of_item, number_item):
    progress = float(number_item) / len(list_of_item) * 100
    return progress
#List of values will be pulled from the database
#
def get_all_ref_folder():
  folders_name_database = []
  values_database = databaseYourFirebase.child("Items").get()
  for key, list_item in values_database.__dict__.iteritems():
    if key == 'pyres':
      for item in list_item:
        folders_name_database.append(item.key())
  return folders_name_database

def download_from_storage(folders):
  for folder in folders:
    #Create the folder if it is not created
    if not os.path.exists(folder):
        os.makedirs(folder)
    # number of items we are counting inside of the loop
    number_item = 0
    # Percentage of progress in the download
    percentage = 0
    # Get all list of the folder we have in database
    list_values = databaseYourFirebase.child("Items").child(folder).get()
    #Download from storage in firebase
    for key, list_item in list_values.__dict__.iteritems():
        if key == "pyres":
            for item in list_item:
                number_item+=1
                unique_id = str(item.key())
                ext_item = str(item.val())[-5:]
                name_item = str(item.val())[:19]
                # This gave us the route in the database for the item
                folderPathItem = storageYourFirebase.child(str(item.val()))
                # This method downloads the item and give a unique name for each of the items
                folderPathItem.download(folder+"/"+name_item+unique_id+ext_item)
                # Calculate the progress
                #print str(calculate_progress(list_item,number_item))+"%"
    print "The folder %s has been downloaded succesfully"%(folder)
  print "All the download has been done Thank you!"  
  
#Get all the reference from the folder in the storage
#Is store in an array nd we can initialize tis like folder_reference = []

folder_reference = get_all_ref_folder()

# Download all the files from the folders stored in firebase using the reference fro the database
download_from_storage(folder_reference)

raw_input("Press enter to continue...")
