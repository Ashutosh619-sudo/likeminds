from collections import defaultdict

class Access:
    def __init__(self,type) -> None:
        self.type = type

class Resource:
    def __init__(self,name) -> None:
        self.access = []
        self.name = name
    
    def addAccess(self,access):
        self.access.append(access)
    
    def checkAccess(self,user,access):
        if self in user.role.resource.keys() and access in user.role.resource[self] and access in self.access:
            return "YES"
        else:
            return "NO"

class Role:
    def __init__(self,name) -> None:
        self.name = name
        self.resource = defaultdict(list)
    
    def addAccessOnResourceToRole(self,access,resource):
        self.resource[resource].append(access)

class User:
    def __init__(self,name) -> None:
        self.name = name
        self.role = None
    
    def addRole(self,role):
        self.role = role


read_access = Access("READ")
write_acess = Access("WRITE")

Image_resource = Resource("IMAGE")
Image_resource.addAccess(read_access)
Image_resource.addAccess(write_acess)

video_resource = Resource("VIDEO")
video_resource.addAccess(read_access)

admin_role = Role("ADMIN")
admin_role.addAccessOnResourceToRole(read_access,Image_resource)
admin_role.addAccessOnResourceToRole(write_acess,Image_resource)
admin_role.addAccessOnResourceToRole(read_access,video_resource)


admin_user = User("ADMINUSER")
admin_user.addRole(admin_role)

print(Image_resource.checkAccess(admin_user,read_access))
print(Image_resource.checkAccess(admin_user,write_acess))
print(video_resource.checkAccess(admin_user,read_access))
print(video_resource.checkAccess(admin_user,write_acess))

