import boto3

from app.main import settings
from app.services.values_dynamodb import VariablesDynamoDB


class DynamodbService:
    DYNAMODB_CONNECTION = boto3.resource('dynamodb',
                                         aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                         aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

    @staticmethod
    def create_item_dynamodb(table_name: str, user_id: int, total_likes=0, total_posts=0, total_pages=0):
        """Creating a new item in a table in DynamoDB"""

        table = DynamodbService.DYNAMODB_CONNECTION.Table(table_name)
        table.put_item(
            Item=VariablesDynamoDB.get_item(user_id, total_likes, total_posts, total_pages)
        )

    @staticmethod
    def get_data_dynamodb(table_name: str):
        """Getting all items from table in DynamoDB"""

        table = DynamodbService.DYNAMODB_CONNECTION.Table(table_name)
        response = table.scan()
        data = response['Items']
        return data

    @staticmethod
    def update_item_dynamodb(table_name: str, user_id: str, attribute: str):
        """Updating item from table in DynamoDB"""

        table = DynamodbService.DYNAMODB_CONNECTION.Table(table_name)
        response = table.update_item(
            Key=VariablesDynamoDB.get_key(user_id),
            UpdateExpression='SET stats.#s = stats.#s + :val',
            ExpressionAttributeNames=VariablesDynamoDB.get_expression_attribute_names(attribute),
            ExpressionAttributeValues=VariablesDynamoDB.get_expression_attribute_values(),
            ReturnValues="UPDATED_NEW"
        )
        return response
