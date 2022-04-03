import os, sys
try:
    __import__("chats").black()
except Exception as e:
    exit(str(e))
