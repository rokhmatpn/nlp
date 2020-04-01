import io
import datetime
import string
import json

char_set = string.ascii_uppercase + string.digits
size = 12

class StaticFile(object):
    def __init__(self):
        self.dirt = 'D:/MASTER/whatsappapi/file'

    def send(self, params):

        msg = params['msg']
        msg = msg.replace('<br>', '\n')

        params['msg'] = msg
        data = params
        
        file_name = str(datetime.datetime.now())
        file_name = file_name.replace(' ', '')
        file_name = file_name.replace(':', '')
        file_name = file_name.replace('-', '')
        file_name = file_name.replace('.', '')
        file_name = 'wa_'+file_name

        with io.open(self.dirt+"/msg/"+file_name+".json", 'w', encoding='utf-8') as f:
            f.write(unicode(json.dumps([data])))
            return "[WORKER] "+str(datetime.datetime.now())[:19]+": Add new file success"

    def add(self, params):

        data = params
        file_name = str(datetime.datetime.now())
        file_name = file_name.replace(' ', '')
        file_name = file_name.replace(':', '')
        file_name = file_name.replace('-', '')
        file_name = file_name.replace('.', '')
        file_name = 'wa_'+file_name

        with io.open(self.dirt+"/contact/"+file_name+".json", 'w', encoding='utf-8') as f:
            f.write(unicode(json.dumps([data])))
            return "[WORKER] "+str(datetime.datetime.now())[:19]+": Add new file success"



