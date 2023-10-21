# was-9
Docker image for WAS 9 and scripts to deploy spring boot application using wsadmin script

## Docker Image

[Docker Hub](https://hub.docker.com/r/ibmcom/websphere-traditional)

### Pull
```sh
docker pull ibmcom/websphere-traditional
```

### Run
```sh
docker run -p 9043:9043 -d ibmcom/websphere-traditional:latest
```

URL: https://localhost:9043/ibm/console/login.do?action=secure  
username: wsadmin  
password: ?  
_NOTE: password need to run this script to get it:_  
```sh
docker exec -it CONTAINER_ID cat /tmp/PASSWORD
```

## Exec
To get inside the container
```sh
docker exec -it CONTAINER_ID /bin/bash
```

## Deploy Spring Boot

It should package by `war`

Just add into the `pom.xml`:
```xml
    <packaging>war</packaging>
```

then, we need two files: `ibm-web-bnd.xml` `ibm-web-ext.xml`

#### [ibm-web-bnd.xml](/ibm-web-bnd.xml)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-bnd
        xmlns="http://websphere.ibm.com/xml/ns/javaee"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://websphere.ibm.com/xml/ns/javaee http://websphere.ibm.com/xml/ns/javaee/ibm-web-bnd_1_0.xsd"
        version="1.0">

    <virtual-host name="default_host"/>
</web-bnd>
```
#### [ibm-web-ext.xml](/ibm-web-ext.xml)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-ext
        xmlns="http://websphere.ibm.com/xml/ns/javaee"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://websphere.ibm.com/xml/ns/javaee http://websphere.ibm.com/xml/ns/javaee/ibm-web-ext_1_0.xsd"
        version="1.0">

    <context-root uri="/"/>
</web-ext>
```

then, yuo should put these files in your application by adding
the files inside the `main/webapp/WEB-INF/` _create the folders if 
it's not exists_

## Deployment Script

Now we get through the [wsadmin script docs](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-application-serving-environment-wsadmin) for deployment

The [IBM Docs](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-commands-adminapp-object-using-wsadmin) for the commands to install it's inside AdminApp object

For example of install app:
I wrote small script to install some app

### `wsadmin.sh` Path
`wsadmin.sh` in `/opt/IBM/WebSphere/AppServer/bin/wsadmin.sh`

In the below lab, a WAS Docker image is used to create a container 
as the running environment. In the image, WebSphere Application Server is installed 
in folder `/opt/IBM/WebSphere/AppServer`.

### Usage
```sh
$PATH_TO_WSADMIN/wsadmin.sh -username wsadmin -password wsadmin -lang jython # Logging
AdminApp.install('demo.war', '[-appname HelloWorld -cell DefaultCell01 -server server1]')
AdminConfig.save()

Sync1 = AdminControl.completeObjectName('type=NodeSync,process=nodeagent,node=AppSrvNode01,*')
AdminControl.invoke(Sync1, 'sync')
```
And you can put it as [Python file](/script/deploy.py)

Then, you need to just logged in to `wsadmin` and use this command:
```sh
execfile('deploy.py')
```

# Reference

- [Commands for the AdminApp object using wsadmin scripting](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-commands-adminapp-object-using-wsadmin)
- https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-application-serving-environment-wsadmin
- [ibm-web-bnd.xml IBM Docs](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=files-application-bindings)
- [ibm-web-ext.xml IBM Docs](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=parameters-jsp-engine-configuration)
- [Installing enterprise applications using wsadmin scripting](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-installing-enterprise-applications-using-wsadmin)