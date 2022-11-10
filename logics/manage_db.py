from app.core.enum_classes import Action
from app.services.dynamodb_service import DynamodbService


def manage_db(db_table: str, user_id: str, action: str):
    users = set()

    update_actions = {
        Action.CREATE_LIKE: DynamodbService.update_item_dynamodb,
        Action.CREATE_POST: DynamodbService.update_item_dynamodb,
        Action.CREATE_PAGE: DynamodbService.update_item_dynamodb,
    }

    for item in DynamodbService.get_data_dynamodb(db_table):
        users.add(item['user_id'])

    if user_id in users:
        update_actions.get(action)(db_table, user_id, Action(action).attr)  # Update data in DynamoDB
    else:
        DynamodbService.create_item_dynamodb(db_table, user_id)  # Create new user in DynamoDB
