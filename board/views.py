from django.shortcuts import render

from .models import Board
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status






'''
전체 블로그를 조회
'''

@api_view(['GET']) # GET 요청만 받겠다.
def board_list(request):

    if request.method=='GET':

        boards=Board.objects.all()
        serializer=PostListSerializer(boards,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

   
    return Response(status=status.HTTP_400_BAD_REQUEST)
    


#########



@api_view(['POST'])
def board_third(request):

    if request.method=='POST':
        serializer=PostRequestSerializer(data=request.data)
        # 역직렬화 실행

        if serializer.is_valid():


            #
            post=serializer.save()
            # post 객체로 저장하는 것을 잡아줌
            # 요청과 응답을 다르게 하기 위해

            response=PostResponseSerializer(post)
            # 프론트엔드에 넘겨주기 위해서는 직렬화를 해야 함.
            # 입력 받은 PostRequestSerializer와 다르게
            # Response하기 위해 덮어씌워주는 거임
            
            return Response(response.data,status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    





############


    
    



'''
한 블로그 조회
'''
@api_view(['GET'])
def board_detail(request, pk):

    try: 
        board = Board.objects.get(pk=pk)

        if request.method=='GET':
            ######
            # 상세조회 serializer 수정
            serializer = PostDetailSerializer(board)
            return Response(serializer.data, status=status.HTTP_200_OK)


    

    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def create_comment(request,post_id):
    post=Board.objects.get(pk=post_id)
    # Board는 models.py에서 옴
    # =왼쪽과 오른쪽이 같은 객체를 가져오라는 뜻
    # 가져와서 post에 저장



    if request.method=='POST':

        serializer=CommentRequestSerializer(data=request.data)

        if serializer.is_valid():
            comment=serializer.save(post=post)
            # 외래키 필드가 연결이 됨?
            # 왼쪽 post는 댓글의 post필드(외래키 필드)
            # 오른쪽 post는 위에서 만든 post
            # comment의 post부분을 내가 원하는 대로 설정한 거임.

            response=CommentResponseSerializer(comment)

            return Response(response.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)




# drf 공식 문서
# query


#수정

@api_view(['PUT'])
def board_fix(request,pk):
    try: 
        board = Board.objects.get(pk=pk)

        if request.method=='PUT':

            serializer=PostRequestSerializer(board,data=request.data)


            if serializer.is_valid():
                post=serializer.save()
                response=PostResponseSerializer(post)
                return Response(response.data,status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    except Board.DoesNotExist: # 예외(오류) 발생 시 아래 코드 실행
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
def board_delete(request,pk):
    try:
        board = Board.objects.get(pk=pk)

        if request.method=='DELETE':

            board.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    except Board.DoesNotExist: # 예외(오류) 발생 시 아래 코드 실행
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
# GET : 조건에 맞는 객체를 DB에서 가져옴 - 직렬화 - ...

def get_comments(request,post_id):
    # post=Post.objects.get(pk=post_id)

    post=Board.objects.get(pk=post_id)
    # 조건에 맞는 보드 가져오기
    # 파라미터와 post_id가 같으면 가져와라

    comments=Comment.objects.filter(post=post)
    # Comment의 외래키 필드 중에 post가 같은 Comment를 가져옴.
    # get 이 아닌 filter는 여러 개 가져오려고.

    serializer=CommentResponseSerializer(comments,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)




# @api_view(['GET'])
# def board_comment(request):

#     if request.method=='POST':
#         serializer=BoardSerializer02(data=request.data)
#         # 역직렬화 실행

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)

#         return Response(status=status.HTTP_400_BAD_REQUEST)

