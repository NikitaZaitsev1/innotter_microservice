class VariablesDynamoDB:
    """Getting variables for DynamoDB"""

    @staticmethod
    def get_item(user_id: int, total_likes=0, total_posts=0, total_pages=0) -> dict:
        item = {'user_id': user_id,
                'stats': {'total_likes': total_likes, 'total_posts': total_posts, 'total_pages': total_pages}}
        return item

    @staticmethod
    def get_key(user_id: str) -> dict:
        key = {
            'user_id': user_id
        }
        return key

    @staticmethod
    def get_expression_attribute_names(attribute: str) -> dict:
        expression_attribute_names = {
            '#s': attribute  # 'total_likes', 'total_posts', 'total_pages'
        }
        return expression_attribute_names

    @staticmethod
    def get_expression_attribute_values() -> dict:
        expression_attribute_values = {
            ':val': 1
        }
        return expression_attribute_values
