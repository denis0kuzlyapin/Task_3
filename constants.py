class Url:

    BASE_URL = "https://stellarburgers.education-services.ru/"

    PROFILE_URL = "https://stellarburgers.education-services.ru/account/profile"

    AUTH_URL = "https://stellarburgers.education-services.ru/login"

    ORDER_HISTORY = "https://stellarburgers.education-services.ru/account/order-history"

    ORDER_TAPE = "https://stellarburgers.education-services.ru/feed"


class Endpoint:

    ORDER_CREATE = "/api/orders"

    USER_CREATE = "/api/auth/register"

    DEL_USER = "/api/auth/user"

    USER_LOGIN = "/api/auth/login"

    GET_USER_DATA = "/api/auth/user"

    PATCH_USER_DATA = "/api/auth/user"

    GET_USER_ORDERS = "/api/orders"

    GET_INGREDIENTS = "/api/ingredients"
