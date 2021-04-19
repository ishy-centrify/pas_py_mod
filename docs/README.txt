#Need to install the 3 libraries (pandas, requests, configparser). I am working on making it a package and installing the libraries on install.
#How it is structured is to leverage an oauth service account in PAS and a web app to create a config file in the working user directory
#of the user. It assumes that the service account is made and has the necessary permissions.
#After the config file is made, all API calls are able to be made
#Need to install the 3 libraries (pandas, requests, configparser) the and then run the Make_Config.MakeConfig() Fucntion with 
the correct info of having a service account of an oauth 

#Example of MakeConfig:
#This is to make the config with the tenant ID, App ID, Scope, Service account UPN, and PW.
#MakeConfig(TenantID="ABD0458", AppID="hackerman", Scope="All", SvcAccount="apiuser@andrew.com", PW='TheBestPassword1')

#Ex of Utility Classes:
#Query_Request(SQL = """SELECT Server.DomainId, Server.DomainName, Server.ID, Server.Name FROM Server""", Debug=True)#
#Call1 = URL(Call= "/ServerManage/AddResource").new_url
#Other_Request(Call="/ServerManage/AddResource",Debug= True, FQDN = "Gotem.net", ComputerClass= "Unix", \
    #Sessiontype= "Ssh", Description="Test", Name="test.test.net")

#Ex of connector Function:
#This gets 
#Connector_Info(Print=True, ExportPath="/home/a/Desktop/test1.csv")

#Ex of Query Function:
#This handles all basic Queries and can print them as a dataframe and/or Export it to a directory
#Query(SQLQuery = """SELECT Server.DomainId, Server.DomainName, Server.ID, Server.Name FROM Server""", Print=True, ExportPath = "/home/a/Desktop/testtest.csv")

#Ex of Secret Class:
#Ex on how to use clases/functions:
#Get_Secret('test')
#Add_Secret_Folder( Name="Test", Description="Test")
#Delete_Secret(Secret='text')

#Ex of System functions:

#Add_System(Name = "Test" ,FQDN="test.test.net", Description="test", ComputerClass="Unix", SessionType="Ssh")
#Get_System(Name = "Test")
#Get_System() -> Gets all systems and IDs and Domains with IDs
#Delete_System("Test")

#Ex of Account Functions:
#Add_Account(User='Test', DomainName='test.net', Password='Password1')
#Delete_Account(Name="Test")
#Get_Vault_Account("testadmin")
#Get_Vault_Account() # Returns all accounts


SDK is providing function call to programmer... for example, programmer should use your class to connect to PAS\
 and in the connect, programmer provide the tenantId, userId, password, etc.\ 
 Or programmer provide the token via the centrify.dmc's gettoken function call.

Restructure the class to do go out and get the bearer token of account and then build the headers. Keep the config 
def connect(Tenant ID, Password):

Return AND NOT print. Remove Print as much and use return


