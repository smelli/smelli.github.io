all: doc
doc:
	pdoc smelli --html --template-dir assets/_pdoc-template --overwrite
