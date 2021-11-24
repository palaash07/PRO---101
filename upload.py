import dropbox

class Transferdata:
    def __init__(self,accesstoken):
        self.accestoken = accesstoken

    def uploadFile(self,filefrom,fileto):
        #upload a file to dropbox
        dbx = dropbox.Dropbox(self.accestoken)  
        with open(filefrom,'rb') as f:
            dbx.files_upload(f.read(),fileto)  
        
def main():
    accestoken = "iqT-mOWFKt4AAAAAAAAAAQCk0W8i3Ba1H_Gr-lSeXxxK53dRyrYpp4jNgC7IAA59"
    #object of class transfer data
    transferdata = Transferdata(accestoken)  
    #input file from user 
    filefrom = input("Enter the file path to transfer")
    fileto = input("Enter the full path to Dropbox")
    # call upload files to upload the data in dropbox
    transferdata.uploadFile(filefrom,fileto)

    print("file as been moved")

main()          