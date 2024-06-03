from rest_framework import serializers
from .models import Board,Comment
from django.utils import timezone

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model=Board

        fields=['id','title','body']
        

class PostResponseSerializer(serializers.ModelSerializer):
    created_at=serializers.SerializerMethodField()
    # 이미 존재하는 created_at을 변경하는 것임.
    
    class Meta:
        model=Board

        fields=['id','title','body','created_at']

    def get_created_at(self,obj):
        # get_형식으로 설정해야 함.
        # db는 안 바뀌고 클라이언트한테 보낼 때만 바뀜.
        time=timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d')




class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Board
        fields=['id','title','body']


class PostRequestSerializer(serializers.ModelSerializer):
    # post 할 때 필요한 것들 전용
    class Meta:
        model=Board
        fields=['title','body']





class CommentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['comment']

class CommentResponseSerializer(serializers.ModelSerializer):
    created_at=serializers.SerializerMethodField()
    class Meta:
        model=Comment
        fields=['id','post','created_at','comment']

    def get_created_at(self,obj):
    # get_형식으로 설정해야 함.
    # db는 안 바뀌고 클라이언트한테 보낼 때만 바뀜.
        time=timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d')



class PostDetailSerializer(serializers.ModelSerializer):
    created_at=serializers.SerializerMethodField()
    comments=CommentResponseSerializer(many=True,read_only=True)
    # many=True : 여러 개
    # read_only=True : 데이터베이스에서 
    # 사용자가 입력하는 데이터가 아니라 컴퓨터가? 알아서
    # 채워주는 데이터형?.
    
    # board가 comment를 역참조 하기 위한 장치

    # meta 안에 있는 board가 역참조 한 comments를 가져와서
    # commentResponsadfd 안에 넣은 것임?
    # models.py에서 related_name=comments 설정이 된 것을 ~

    # 

    class Meta:
        model=Board
        fields=['id','title','body','created_at','comments']
    
    def get_created_at(self,obj):
        # get_형식으로 설정해야 함.
        # db는 안 바뀌고 클라이언트한테 보낼 때만 바뀜.
        time=timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d')









class BoardSerializer02(serializers.ModelSerializer):
    class Meta:
        model=Board

        fields=['id','title','body','created_at']







