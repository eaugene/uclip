#!/usr/bin/env bash
if [[ $1 = "reg" ]];then
    python ~/uclip/reg.py;
elif [[ $1 = "sreg" ]];then
    python ~/uclip/sreg.py;
elif [[ $1 = "up" ]];then
    python ~/uclip/up.py;
elif [[ $1 = "down" ]];then
    python ~/uclip/down.py;
elif [[ $1 = "end" ]];then
    python ~/uclip/end.py;
else
    echo "Refer to docs @ https://github.com/eaugene/uclip/blob/master/README.md ";
fi
