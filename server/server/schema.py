entity_new_classroom = {
    "type": "object",
    "title": "empty object",
    "properties": {
        "user_name": {
            "type": "string"
        },
        "user_token": {
            "type": "string"
        },
        "classroom_name": {
            "type": "string"
        },
        "classroom_capacity": {
            "type": "integer"
        }
    },
    "required": [
        "user_name",
        "classroom_capacity",
        "classroom_name",
        "user_token"
    ]
}
entity_classroom_list = {
    "type": "object",
    "title": "empty object",
    "properties": {
        "capacity_range": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "min_capacity": {
                        "type": "integer"
                    },
                    "max_capacity": {
                        "type": "integer"
                    }
                }
            },
            "description": "capacity \u5728 [min_capacity, max_capacity] \u4e2d"
        },
        "limit": {
            "type": "integer",
            "description": "\u6700\u591a\u8fd4\u56de\u7684\u6559\u5ba4\u6570\u76ee"
        }
    },
    "required": []
}
entity_new_course = {
    "type": "object",
    "title": "empty object",
    "properties": {
        "user_name": {
            "type": "string"
        },
        "user_token": {
            "type": "string"
        },
        "course_name": {
            "type": "string"
        },
        "course_start": {
            "type": "integer"
        },
        "course_end": {
            "type": "integer"
        },
        "course_credit": {
            "type": "integer"
        },
        "course_type": {
            "type": "integer"
        },
        "course_classroom_id": {
            "type": "integer"
        },
        "course_year": {
            "type": "integer"
        },
        "course_semester": {
            "type": "integer"
        }
    },
    "required": [
        "user_name",
        "course_start",
        "course_end",
        "course_name",
        "course_credit",
        "user_token",
        "course_type",
        "course_classroom_id",
        "course_year",
        "course_semester"
    ]
}
user_signup = {
    "type": "object",
    "title": "empty object",
    "properties": {
        "user_name": {
            "type": "string"
        },
        "user_password": {
            "type": "string"
        },
        "user_type": {
            "type": "integer",
            "enum": [
                0,
                1,
                2
            ]
        }
    },
    "required": [
        "user_name",
        "user_password",
        "user_type"
    ]
}
user_test_status = {
    "type": "object",
    "title": "empty object",
    "properties": {
        "user_name": {
            "type": "string"
        },
        "user_token": {
            "type": "string"
        }
    },
    "required": [
        "user_name",
        "user_token"
    ]
}
user_login = {
    "type": "object",
    "title": "empty object",
    "properties": {
        "user_name": {
            "type": "string"
        },
        "user_password": {
            "type": "string"
        }
    },
    "required": [
        "user_name",
        "user_password"
    ]
}
