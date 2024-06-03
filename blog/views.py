from django.shortcuts import render

from .models import Blog
from .serializers import BlogSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status


from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from .permissions import IsOwnerOrReadOnly






# '''
# 전체 블로그를 조회
# '''
# @api_view(['GET','POST']) # GET 요청만 받겠다.
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticatedOrReadOnly])

# def blog_list(request):
#     if request.method=='GET':
#         blogs=Blog.objects.all()
#         serializer=BlogSerializer(blogs,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     elif request.method=='POST':
#         serializer=BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
#     # blogs = Blog.objects.all()
#     # serializer = BlogSerializer(blogs, many=True)
#     # return Response(serializer.data, status=status.HTTP_200_OK)







# '''
# 한 블로그 조회
# '''

# @api_view(['GET','PUT','DELETE'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsOwnerOrReadOnly])

# def blog_detail(request, pk):

#     try:
#         blog = Blog.objects.get(pk=pk)

#         if request.method=='GET':
#             serializer = BlogSerializer(blog)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         elif request.method=='PUT':
#             serializer=BlogSerializer(blog,data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(status=status.HTTP_200_OK)
#             return Response(status=status.HTTP_400_BAD_REQUEST)
        
#         elif request.method=='DELETE':
#             blog.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

#     except Blog.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)





from rest_framework.views import APIView


# class BlogList(APIView):
#     authentication_classes=[JWTAuthentication]
#     permission_classes=[IsAuthenticatedOrReadOnly]


#     def get(self,request):
#         # 클래스 내부에서 self는 일단 써주고 시작해야 함
#         # self를 안 써도 쓰고 시작
#         blogs=Blog.objects.all()
#         serializer=BlogSerializer(blogs,many=True)
#         return Response(serializer.data)


#     def post(self,request):
#         serializer=BlogSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=request.user)
#             return Response(serializer.data,status=status.HTTP_201_CREATED)

#         return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)
    

from rest_framework.generics import ListCreateAPIView

class BlogList(ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        # ListCreateAPIView의 함수인 perform_create를
        # 내 입맛대로 수정한 거임.
        # 원래는 serializer 저장하는 함수였음
        user=self.request.user
        serializer.save(user=user)









    


from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.shortcuts import get_object_or_404



# class BlogDetail(APIView):
#     authentication_classes=[JWTAuthentication]
#     permission_classes=[IsAuthenticatedOrReadOnly]

#     def get_object(self, pk):
#         blog = get_object_or_404(Blog, pk=pk)
#         return blog

#     def get(self,request,pk):
#         blogs=self.get_object(pk)
#         serializer=BlogSerializer(blogs)
#         return Response(serializer.data)


#     def put(self,request,pk):
#         blog=self.get_object(pk)
#         serializer=BlogSerializer(blog,data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

#     def delete(self,request,pk):
#         blog=self.get_object(pk)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
        




        

from rest_framework.generics import RetrieveUpdateDestroyAPIView

class BlogDetail(RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsOwnerOrReadOnly]


