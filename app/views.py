from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

# httpメソッドがpostならcreate  getならレコード一覧or特定のレコード取得  put,patchなら更新   deleteなら削除
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer