pofiles = $(wildcard $(srcdir)/*.po)
mofiles = $(patsubst %.po,%.mo,$(pofiles))

MOSTLYCLEANFILES = $(mofiles)
DISTCLEANFILES = $(notdir $(mofiles))
dist_noinst_DATA = $(pofiles)

%.mo: %.po
	msgfmt $^ -o $(builddir)/$(notdir $@)

install-data-hook: $(mofiles)
	for i in $(notdir $^); do \
		mkdir -p $(DESTDIR)$(datadir)/locale/$${i%.mo}/LC_MESSAGES; \
		install -m644 "$(builddir)/$${i}" $(DESTDIR)/$(datadir)/locale/$${i%.mo}/LC_MESSAGES/olpc-switch-desktop.mo; \
	done

uninstall-hook:
	for i in $(notdir $(mofiles)); do \
		rm -f $(DESTDIR)/$(datadir)/locale/$${i%.mo}/LC_MESSAGES/olpc-switch-desktop.mo; \
	done

