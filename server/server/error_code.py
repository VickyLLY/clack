# error_message 是前端需要展示出来的错误信息

# 成功
CLACK_SUCCESS = {"error_code": 0, "error_message": "OK"}

# 未知错误
CLACK_UNEXPECTED_ERROR = {"error_code": -1, "error_message": "未知错误"}

# 请求方法不是POST
CLACK_POST_REQUIRED = {"error_code": 1, "error_message": "请求方法不是POST,触发该错误应该是前端写挂了"}

# 请求JSON中部分必须的对象不存在
CLACK_REQUEST_JSON_ERROR = {"error_code": 2, "error_message": "请求JSON中部分必须的对象不存在,触发该错误应该是前端写挂了"}

# 注册账号的用户名已经存在
CLACK_USER_NAME_EXISTS = {"error_code": 3, "error_message": "用户名已存在"}

# 登录错误
CLACK_USER_LOGIN_FAILED = {"error_code": 4, "error_message": "登录失败,用户名或密码错误"}

# 用户未登录
CLACK_LOGIN_REQUIRED = {"error_code": 5, "error_message": "请先登录"}

# 需要系统管理员权限
CLACK_ADMIN_REQUIRED = {"error_code": 6, "error_message": "只有系统管理员才能进行此操作"}

# 创建Model失败
CLACK_CREATE_NEW_MODELS_FAILED = {"error_code": 7, "error_message": "创建失败"}

# 接口还未实现
CLACK_UNIMPLEMENTED_API = {"error_code": 8, "error_message": "API接口尚未实现"}

# 没有权限
CLACK_NO_PERMISSION = {"error_code": 9, "error_message": "没有调用这个接口的权限"}

# student不存在
CLACK_STUDENT_NOT_EXISTS = {"error_code": 10, "error_message": "查询的学生不存在"}

# teacher不存在
CLACK_TEACHER_NOT_EXISTS = {"error_code": 11, "error_message": "查询的教师不存在"}

#学生选题限选一个且已经选择课题
CLACK_STUDENT_SELECT_DST_EXISTS = {"error_code": 16, "error_message": "已经选择课题"}
