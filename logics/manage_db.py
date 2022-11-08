from app.core.enum_classes import Action
from app.services.dynamodb_service import DynamodbService


def manage_db(db_table: str, user_id: str, action: str):
    users = set()
    for item in DynamodbService.get_data_dynamodb(db_table):  # Receive all user_id from DynamoDB
        users.add(item['user_id'])
    if user_id in users:
        if action == Action.CREATE_LIKE:
            DynamodbService.update_item_dynamodb(db_table, user_id, 'total_likes')  # Update total_likes in DynamoDB
        if action == Action.CREATE_POST:
            DynamodbService.update_item_dynamodb(db_table, user_id, 'total_posts')  # Update total_posts in DynamoDB
        if action == Action.CREATE_PAGE:
            DynamodbService.update_item_dynamodb(db_table, user_id, 'total_pages')  # Update total_pages in DynamoDB
    else:
        DynamodbService.create_item_dynamodb(db_table, user_id)  # Create new user in DynamoDB
