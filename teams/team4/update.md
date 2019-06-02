# throw_control.py 

1. Updated by Jiaming Luo on May 24 

    Description: first edition. The connection of Pi and Arduino
    
2. Updated by Jiaming Luo on June 1
    
    Description: 1. fixed a bug of reading the website.
    
                 2. change the waiting time to make the Arduino and Python a little "synchronized".

# person.py    /05/24

人脸识别 并将识别的框的位置和原始图像大小写到html文件中
格式为 box_pos:[box_left, box_right, box_top, box_bottom] image_size: image.shape

文件需要在管理员权限下执行，或者修改/var/www/test.html的写权限

apache2也配置完成，可以先调试pc和树莓派的通信 

# throw.ino 

1. Updated by Jiaming Luo on June 1

    Description: this is a revision of the former file "servo4.ino", which is created by Shaojie Cui. Express my appreciation to him. We made the machine work more smoothly and also fixed some problems.
