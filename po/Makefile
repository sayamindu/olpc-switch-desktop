pofiles = $(wildcard *.po)
mofiles = $(patsubst %.po,%.mo,$(pofiles))

default: $(mofiles)

%.mo: %.po
	msgfmt $^ -o $@

install: $(mofiles)
	for i in $^; do \
		mkdir -p $(DESTDIR)/usr/share/locale/$${i%.mo}/LC_MESSAGES; \
		install -m644 "$${i}" $(DESTDIR)/usr/share/locale/$${i%.mo}/LC_MESSAGES/olpc-switch-desktop.mo; \
	done

clean:
	rm -f $(mofiles)

