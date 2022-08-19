# التكليف 03

#     قم بكتابة محتويات ال Class لتظهر النتيجة كما في المثال

# class Message:
#   # Write Class Content

# print(Message.print_message())

# # Output
# # Hello From Class Message
# ===================================================


class Message:
  # Write Class Content
    @classmethod
    def print_message(cls):
        return "Hello From Class Message"


print(Message.print_message())

# Output
# Hello From Class Message
