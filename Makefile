install:
	cp gad-rm ~/bin
	cp gad-rm.py ~/bin
	./add_alias.sh

uninstall:
	/bin/rm ~/bin/gad-rm
	/bin/rm ~/bin/gad-rm.py
	./del_alias.sh

