netsh interface ip set address "本地连接 2" static 192.168.0.207 255.255.255.0 192.168.0.1 1 
netsh interface ip set dns "本地连接 2" static 114.114.114.114
netsh interface ip add dns "本地连接 2" 8.8.4.4
pause
