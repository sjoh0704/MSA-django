import os
import uuid

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
   
    class Meta:
        abstract = True


class Content(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default="")

    def __str__(self) -> str:   # amdin에서 display_list를 설정해주었기 때문에 없어도 된다. 
        return self.text


# 이미지를 업로드해주는 함수
def image_upload_to(instance, filename):
    ext = filename.split(".")[-1]
    return os.path.join(instance.UPLOAD_PATH, "{}.{}".format(uuid.uuid4(), ext))


class Image(BaseModel):
    UPLOAD_PATH = 'user-upload' # 업로드 위치 + 따로 media 파일을 생성해주자. + settings 설정
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = image_upload_to)
    order = models.SmallIntegerField()  #게시물 마다 있는 사진들의 순서를 결정하기 위해 있는 데이터

    # 해당 필드가 테이블에서 Unique함을 표시한다. 해당 컬럼에 대해 Unique Index를 생성한다.
    class Meta:
        unique_together = ['content', 'order']
        ordering = ['order']  # -를 두면 내림차순 

    def __str__(self) -> str:
        return "image" + str(self.order)

    