from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user==request.user


# admin
#qewr1234qwer
# 127.0.0.1:8000/blog/
# 내 컴퓨터 접근
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MjA0MTQyLCJpYXQiOjE3MTYyMDA1NDIsImp0aSI6ImE0Y2ZjZWNhMjE3YTQzN2Q5MDVlZTdhOTdkM2NlOTEzIiwidXNlcl9pZCI6Nn0.6QkvZX43IV5497ANinI3zcgZ_FrGNhT9ROe-j3IpehQ