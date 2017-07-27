HTMLFILES = $(shell ls *.ptml | sed -e 's/ptml/html/g')
INCS = menu.txt
 
%.html: %.ptml $(INCS)
	html_include.awk <$< >$@

website: $(HTMLFILES) $(INCS)
	-git commit -a -m "HTML rebuild."
	git push origin master

quizzes:
	cd quizzes ; make all

local: $(HTMLFILES)

clean:
	touch *.ptml
	cd quizzes ; make clean
