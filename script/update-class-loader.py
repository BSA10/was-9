dep = AdminConfig.getid('/Deployment:HelloWorld/')

depObject = AdminConfig.showAttribute(dep, 'deployedObject')

myModules = AdminConfig.showAttribute(depObject, 'modules')
myModules = myModules[1:len(myModules)-1].split(" ")
print myModules

for module in myModules:
     if (module.find('WebModuleDeployment')!= -1):
        AdminConfig.modify(module, [['classloaderMode', 'PARENT_LAST']])

AdminConfig.save()

AdminConfig.showall(module)

