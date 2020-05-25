from main import *


logging.basicConfig(filename='Logs/example.log',
                    format='%(asctime)s %(levelname)s [%(module)s] [%(funcName)s]: %(message)s',
                    datefmt='[%Y.%m.%d] %H:%M:%S -', level=logging.DEBUG)


logging.info('Script has begun')


for iterations in range(1):
    try:
        windows_search('paint')

        windows_open()

        paint_blue()

        hello_h()

        hello_e()

        hello_l1()

        hello_l2()

        hello_o()

        paint_text()

        text_box_world()

        windows_close()

        windows_dont_save()

    except TypeError:
        print('Failed')
        logging.error('Failed')
        exit()

print('Finished')
logging.info('Script has finished')
