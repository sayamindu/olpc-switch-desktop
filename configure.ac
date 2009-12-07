AC_INIT([olpc-switch-desktop], [0.6])
AM_INIT_AUTOMAKE
AC_CONFIG_SRCDIR([sugar/model.py])
AC_PREREQ([2.59])

GNOME_COMMON_INIT

IT_PROG_INTLTOOL([0.35.0])
GETTEXT_PACKAGE=olpc-switch-desktop
AC_SUBST([GETTEXT_PACKAGE])
AC_DEFINE_UNQUOTED([GETTEXT_PACKAGE],["$GETTEXT_PACKAGE"],[Gettext package])
AM_GLIB_GNU_GETTEXT


AC_CONFIG_FILES([Makefile po/Makefile.in sugar/Makefile gnome/Makefile])
AC_OUTPUT

