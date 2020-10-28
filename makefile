MODULENAME = tests 

autodoc:
	pdoc3 --force --html --output-dir ./docs $(MODULENAME)

lint:
	pylint $(MODULENAME) 

doclint:
	pydocstyle $(MODULENAME)

test:
	pytest -v $(MODULENAME) 

.PHONY: init doc lint test 
