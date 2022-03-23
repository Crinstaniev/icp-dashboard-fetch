# /bin/bash
nohup python fetch_data.py >fetch.log 2>&1 &
nohup python plot_server.py >server.log 2>&1 &
