entity_teacher = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "user_name": {
            "type": "string"
        },
        "user_token": {
            "type": "string"
        },
        "teacher": {
            "type": "object",
            "properties": {
                "teacher_number": {
                    "type": "string"
                }
            },
            "required": [
                "teacher_number"
            ]
        }
    },
    "required": [
        "user_name",
        "user_token",
        "teacher"
    ]
}
entity_student = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "user_name": {
            "type": "string"
        },
        "user_token": {
            "type": "string"
        },
        "student": {
            "type": "object",
            "properties": {
                "student_number": {
                    "type": "string"
                }
            },
            "required": [
                "student_number"
            ]
        }
    },
    "required": [
        "user_name",
        "user_token",
        "student"
    ]
}
entity_banji_list = {
    "type": "object",
    "title": "empty object",
    "properties": {},
    "required": []
}
entity_major_list = {
    "type": "object",
    "title": "empty object",
    "properties": {
        "major": {
            "type": "object",
            "properties": {
                "major_department_id": {
                    "type": "integer",
                    "mock": {
                        "mock": "1"
                    }
                }
            },
            "required": [
                "major_department_id"
            ]
        }
    }
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
entity_new_major = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "user_name": {
            "type": "string"
        },
        "user_token": {
            "type": "string"
        },
        "major": {
            "type": "object",
            "properties": {
                "major_name": {
                    "type": "string"
                },
                "major_department_id": {
                    "type": "integer"
                }
            },
            "required": [
                "major_name",
                "major_department_id"
            ]
        }
    },
    "required": [
        "user_name",
        "user_token",
        "major"
    ]
}
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
        "classroom": {
            "type": "object",
            "properties": {
                "classroom_name": {
                    "type": "string"
                },
                "classroom_capacity": {
                    "type": "integer"
                }
            },
            "required": [
                "classroom_name",
                "classroom_capacity"
            ]
        }
    },
    "required": [
        "user_name",
        "user_token",
        "classroom"
    ]
}
entity_new_department = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "user_name": {
            "type": "string"
        },
        "user_token": {
            "type": "string"
        },
        "department": {
            "type": "object",
            "properties": {
                "department_name": {
                    "type": "string"
                }
            },
            "required": [
                "department_name"
            ]
        }
    },
    "required": [
        "user_name",
        "user_token",
        "department"
    ]
}
entity_new_banji = {
    "type": "object",
    "title": "empty object",
    "properties": {
        "user_name": {
            "type": "string"
        },
        "user_token": {
            "type": "string"
        },
        "banji": {
            "type": "object",
            "properties": {
                "banji_name": {
                    "type": "string"
                },
                "banji_major_id": {
                    "type": "integer"
                }
            },
            "required": [
                "banji_name",
                "banji_major_id"
            ]
        }
    },
    "required": [
        "user_name",
        "banji",
        "user_token"
    ]
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
user_signup_student = {
    "type": "object",
    "title": "empty object",
    "properties": {
        "user": {
            "type": "object",
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
        },
        "student": {
            "type": "object",
            "properties": {
                "student_name": {
                    "type": "string"
                },
                "student_number": {
                    "type": "string"
                },
                "student_email": {
                    "type": "string"
                },
                "student_start_year": {
                    "type": "integer"
                },
                "student_end_year": {
                    "type": "integer"
                },
                "student_banji_id": {
                    "type": "integer"
                }
            },
            "required": [
                "student_name",
                "student_number",
                "student_email",
                "student_start_year",
                "student_end_year",
                "student_banji_id"
            ]
        }
    },
    "required": [
        "user",
        "student"
    ]
}
user_signup_teacher = {
    "type": "object",
    "title": "empty object",
    "properties": {
        "user": {
            "type": "object",
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
        },
        "teacher": {
            "type": "object",
            "properties": {
                "teacher_name": {
                    "type": "string"
                },
                "teacher_number": {
                    "type": "string"
                },
                "teacher_email": {
                    "type": "string"
                },
                "teacher_department_id": {
                    "type": "integer"
                }
            },
            "required": [
                "teacher_name",
                "teacher_number",
                "teacher_email",
                "teacher_department_id"
            ]
        }
    },
    "required": [
        "user",
        "teacher"
    ]
}
user_signup_admin = {
    "type": "object",
    "title": "empty object",
    "properties": {
        "user": {
            "type": "object",
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
    },
    "required": [
        "user"
    ]
}
user_login_status = {
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
user_logout = {
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
scoremng_teacher_upload = {
    "type": "object",
    "title": "empty object",
    "properties": {
        "\u5b66\u751f\u5b66\u53f7": {
            "type": "string"
        },
        "\u6240\u9009\u8bfe\u7a0b\u8bfe\u53f7": {
            "type": "string"
        },
        "\u5206\u6570": {
            "type": "integer"
        }
    },
    "required": [
        "\u5b66\u751f\u5b66\u53f7",
        "\u6240\u9009\u8bfe\u7a0b\u8bfe\u53f7",
        "\u5206\u6570"
    ]
}
