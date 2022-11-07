import os

import boto3

from app.schemas.stats import Stats


class DynamodbService:
    @classmethod
    def _dynamodb_connect(cls):
        """Creating connection to DB"""

        dynamodb = boto3.resource('dynamodb',
                                  aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                  aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

        return dynamodb

    @staticmethod
    def create_item_dynamodb(table_name: str, user_id: str, action: str):
        """Service for creating a new item in a table in DynamoDB"""

        table = DynamodbService()._dynamodb_connect().Table(table_name)
        table.put_item(
            Item={'user_id': user_id, 'action': action}
        )
