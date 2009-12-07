bin_SCRIPTS = olpc-switch-to-sugar

@INTLTOOL_DESKTOP_RULE@
desktopdir=$(datadir)/applications
desktop_in_files=olpc-switch-to-sugar.desktop.in
desktop_DATA = $(desktop_in_files:.desktop.in=.desktop) 

icondir=$(datadir)/icons/hicolor/scalable/apps
icon_DATA = olpc-switch-to-sugar.svg

EXTRA_DIST =			\
	    $(bin_SCRIPTS)	\
	    $(desktop_DATA)	\
	    $(icon_DATA)

DISTCLEANFILES =  $(desktop_DATA)
