from enum import Enum


class Action(str, Enum):
    CREATE_PAGE = "create page"
    CREATE_POST = "create post"
    CREATE_LIKE = "create like"
