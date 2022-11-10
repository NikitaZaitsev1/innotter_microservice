from enum import Enum


class Action(str, Enum):
    CREATE_PAGE = "create page"
    CREATE_POST = "create post"
    CREATE_LIKE = "create like"

    @property
    def attr(self):
        attrs = {
            self.CREATE_PAGE: "total_pages",
            self.CREATE_POST: "total_posts",
            self.CREATE_LIKE: "total_likes",
        }
        return attrs[self.value]
