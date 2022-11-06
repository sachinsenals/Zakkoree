import sys
import telepot


teleid = sys.argv[1]
teletoken = sys.argv[2]


def send(id, message):
    if tele_enable:
        print('正在使用Telebot进行消息推送……')
        bot.sendMessage(id, message, parse_mode=None, disable_web_page_preview=None, disable_notification=None,
                        reply_to_message_id=None, reply_markup=None)
        print('Telebot消息推送完成！')

if __name__ == "__main__":
    if teleid != "" and teletoken != "":
        tele_enable = True
        print('Telegram推送已配置！')
        bot = telepot.Bot(teletoken)
        teleinfomsg = '''
        成功执行Github签到脚本！
        '''
        send(teleid, teleinfomsg)
        print(teleinfomsg)
    else:
        print('未配置Telegram推送！')
    
