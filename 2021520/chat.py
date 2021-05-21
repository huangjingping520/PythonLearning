import itchat

itchat.auto_login()
words = '''
MyLove
''' 
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):

    r = "文本\n\n"
    return r

itchat.run()