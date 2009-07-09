AUTOMAKE_OPTIONS = foreign dist-bzip2 no-dist-gzip
DISTCLEANFILES = ChangeLog
SUBDIRS = sugar gnome po
CWD=$(shell pwd)

rpm: dist
	rpmbuild --clean --define "_specdir $(CWD)" --define "_sourcedir $(CWD)" --define "_builddir $(CWD)" --define "_srcrpmdir $(CWD)" --define "_rpmdir $(CWD)" -bb olpc-switch-desktop.spec
.PHONY: rpm

srpm: dist
	rpmbuild --clean --define "_specdir $(CWD)" --define "_sourcedir $(CWD)" --define "_builddir $(CWD)" --define "_srcrpmdir $(CWD)" --define "_rpmdir $(CWD)" -bs olpc-switch-desktop.spec
.PHONY: srpm

ChangeLog:
	git --git-dir $(top_srcdir)/.git log > ChangeLog || touch ChangeLog
.PHONY: ChangeLog

dist-hook: ChangeLog

