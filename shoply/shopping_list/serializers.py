from rest_framework import serializers

from shopping_list.models import ShoppingItem

class ShoppingItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = ShoppingItem
    fields = ["id", "name", "sku", "price", "description", "quantity", "status"]