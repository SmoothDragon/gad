# Install dependencies
# pip install -r requirements.txt

install:
	cp gad-rm ~/bin
	cp gad-rm.py ~/bin
	./TextFileModifier.py --action add

uninstall:
	/bin/rm ~/bin/gad-rm
	/bin/rm ~/bin/gad-rm.py
	./TextFileModifier.py --action delete

