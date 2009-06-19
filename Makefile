VERSION=$(shell cat VERSION)
CWD=$(shell pwd)
DISTFILE=olpc-switch-desktop-$(VERSION).tar.bz2

FILES=COPYING README gnome sugar VERSION

all:

dist: $(DISTFILE)

rpms: dist
	rpmbuild --define "_sourcedir $(CWD)" --define "_specdir $(CWD)" --define "_builddir $(CWD)" --define "_srcrpmdir $(CWD)" --define "_rpmdir $(CWD)" -ba olpc-switch-desktop.spec

$(DISTFILE):
	-rm -rf .dist
	mkdir -p .dist/olpc-switch-desktop-$(VERSION)
	cp -a $(FILES) .dist/olpc-switch-desktop-$(VERSION)
	tar -cjf $@ -C .dist olpc-switch-desktop-$(VERSION)
	-rm -rf .dist

clean:
	-rm -rf $(DISTFILE) noarch *.src.rpm

