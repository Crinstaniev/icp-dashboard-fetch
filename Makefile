run:
	bash run.sh
	open http://127.0.0.1:8050/

stop:
	killall python

clean: stop
	rm fetch.log server.log record.csv