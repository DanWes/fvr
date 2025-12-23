# Makefile for Sphinx documentation
# sphinx (one of): pip install sphinx, pacman -S python-sphinx

SPHINXOPTS  ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR    = src
BUILDDIR     = _build

# first-target, will also run without arguments (like: make help).
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(0)

.PHONY: help Makefile

# catch-all target: route all unknown targets to Sphinx. $(0) is shortcut for
# $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(0)
