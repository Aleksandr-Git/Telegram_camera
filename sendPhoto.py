from time import sleep
from picamera import PiCamera
#from os import mkdir
#import datetime
from io import BytesIO

camera = PiCamera()
#today = datetime.datetime.today()



def photo():
#    DIR = today.strftime("%H_%M_%S_%d-%m-%Y")
#    mkdir(DIR)
#    camera.capture('./' + DIR + '/photo.1' + '.jpg')
    stream = BytesIO()
    camera.capture(stream, 'jpeg')
    buff_img = stream.getvalue()
    print('photo')
    return buff_img



