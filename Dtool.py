import time as t
from datetime import *
hpny = """
                 __  __                                        
                /\ \/\ \                                       
                \ \ \_\ \     __     _____   _____   __  __    
                 \ \  _  \  /'__`\  /\ '__`\/\ '__`\/\ \/\ \   
                  \ \ \ \ \/\ \L\.\_\ \ \L\ \ \ \L\ \ \ \_\ \  
                   \ \_\ \_\ \__/.\_\\ \ ,__/\ \ ,__/\/`____ \ 
                    \/_/\/_/\/__/\/_/ \ \ \/  \ \ \/  `/___/> \
                                       \ \_\   \ \_\     /\___/
                                        \/_/    \/_/     \/__/ 
      ____                __    __          ____                          
     /\  _`\    __       /\ \__/\ \        /\  _`\                        
     \ \ \L\ \ /\_\  _ __\ \ ,_\ \ \___    \ \ \/\ \     __     __  __    
      \ \  _ <'\/\ \/\`'__\ \ \/\ \  _ `\   \ \ \ \ \  /'__`\  /\ \/\ \   
       \ \ \L\ \\ \ \ \ \/ \ \ \_\ \ \ \ \   \ \ \_\ \/\ \L\.\_\ \ \_\ \  
        \ \____/ \ \_\ \_\  \ \__\\ \_\ \_\   \ \____/\ \__/.\_\\/`____ \ 
         \/___/   \/_/\/_/   \/__/ \/_/\/_/    \/___/  \/__/\/_/ `/___/> \
                                                                    /\___/
                                                                    \/__/ 
"""
phaohoa = """
       .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
jgs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
f="----------------------------------------------------------"
def write(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
icon = "\033[1;92m[\033[1;91m•\033[1;92m]"
gio = "giờ"
phut = "phút"
giay = "giây"
#time còn lại
new=datetime(2022,1,19)
limit=timedelta(seconds=1)
end_while=timedelta(microseconds=0.000000001)
while True:
    now_t=new-datetime.now()
    sec_left=now_t.total_seconds()
    hours,sec_r=divmod(sec_left,60*60)
    min,sec=divmod(sec_r,60)
    time=(f'{icon} {int(hours)} {gio}:{int(min)} {phut}:{int(sec)} {giay}')
    if now_t<limit:
        print(hpny)
        print(f)
        write("Happy Birth Day Bro")
        write("Dạo này công việc hơi khó khắn nên khi khác tôi bù cho nhaaaa :), hoặc nếu thích j kêu tôi tôi tặng cho(miễn phù hợp là đc) =)))))")
        write("Code vẫn hơi ngu nên thế th -.- ")
        write("Chúc bro 1 ngày sinh nhật vui vẻ nha")
        if now_t<end_while:
            break
    else:
        print('\033[1;93mCòn lại: '+time)
    t.sleep(1)