PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

help:
	@echo 'Available commands:'
	@echo '  html      - (re)generate the web site for local preview'
	@echo '  serve     - serve site at http://localhost:8000/'
	@echo '  clean     - remove the generated files'
	@echo '  publish   - generate using production settings'
	@echo '  github    - deploy to GitHub Pages (user site → main branch)'

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	rm -rf $(OUTPUTDIR)

serve:
	cd $(OUTPUTDIR) && $(PY) -m http.server

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

github: publish
	ghp-import -b main $(OUTPUTDIR)
	git push origin main

.PHONY: html help clean serve publish github
