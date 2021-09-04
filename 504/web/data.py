from rest_framework import serializers

class FruitsData():

    def __init__(self):
        self.fruits = []
    
    def data_set(self, id, name, memo):
        self.fruits.append([id, name, memo])
    
    def data_delete(self, id):
        for listitem in self.fruits:
            if listitem[0] == str(id):
                self.fruits.remove(listitem)
    
    def data_update(self, id, name, memo):
        self.fruits[int(id) - 1][0] = id
        self.fruits[int(id) - 1][1] = name
        self.fruits[int(id) - 1][2] = memo

        return self.fruits

    def data_get(self, id):
        for listitem in self.fruits:
            if listitem[0] == str(id):
                param = {
                    'id': listitem[0],
                    'name': listitem[1],
                    'memo': listitem[2],
                }
                return param

    def data_list(self):
        return self.fruits

class ArticleSerializer(serializers.Serializer):
    """Article Serializer
    """
    id = serializers.IntegerField()
    name = serializers.CharField()
    memo = serializers.CharField()

 
    # def create(self, validate_data):
    #     ...
 
    # def update(self, instance, validated_data):
    #     ...
 
    # def validate(self, data):
    #     """Check that description and title are different"""
    #     if data["title"] == data["description"]:
    #         raise serializers.ValidationError(
    #    "Title and Description must be different from one another")
    #     return data


