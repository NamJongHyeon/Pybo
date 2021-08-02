from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    # author # null 허용시 null=True로 설정
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')

    # 수정한 시간/일시 확인
    modify_date = models.DateTimeField(null=True, blank=True)

    # voter 추가
    voter = models.ManyToManyField(User, related_name="voter_question")


    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')


    modify_date = models.DateTimeField(null=True, blank=True)


    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)


# class Category(models.Model):
#     name = models.CharField(max_length=20, unique=True)
#     description = models.CharField(max_length=200, null=True, blank=True)
#     has_answer = models.BooleanField(default=True) # 답변 가능 여부

#     def __str__(self):
#         return self.name