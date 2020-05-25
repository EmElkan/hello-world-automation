from main import *


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
        exit()

print('Finished')
