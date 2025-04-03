from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a nem filed for testing our APIView"""
    # allows you to input any text that you can input on the computer and it gives it a max max_length
    # of 10 so it will accept any char inputs that are 10 or less characters
    name = serializers.CharField(max_length=10)
