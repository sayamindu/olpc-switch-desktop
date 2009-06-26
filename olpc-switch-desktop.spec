Name:		olpc-switch-desktop
Version:	0.4
Release:	1%{?dist}
Summary:	OLPC desktop switching utilities

Group: System Environment/Base
License: GPL
URL: http://dev.laptop.org/git/users/dsd/olpc-switch-desktop
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: python, sugar, gtk2, desktop-file-utils, dbus
BuildArch: noarch


%description
This package contains a Sugar control panel extension for switching to GNOME,
and a GNOME program for switching back to Sugar.

%prep
%setup

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/share/applications
install -d $RPM_BUILD_ROOT/usr/share/icons/hicolor/scalable/apps
install -d $RPM_BUILD_ROOT/etc/skel/Desktop
install -m755 gnome/olpc-switch-to-sugar $RPM_BUILD_ROOT/usr/bin
install -m644 gnome/olpc-switch-to-sugar.desktop $RPM_BUILD_ROOT/usr/share/applications
install -m644 gnome/olpc-switch-to-sugar.desktop $RPM_BUILD_ROOT/etc/skel/Desktop
install -m644 gnome/olpc-switch-to-sugar.svg $RPM_BUILD_ROOT/usr/share/icons/hicolor/scalable/apps

install -d $RPM_BUILD_ROOT/usr/share/sugar/extensions/cpsection/switchdesktop
install -d $RPM_BUILD_ROOT/usr/share/sugar/data/icons
install -m644 -t $RPM_BUILD_ROOT/usr/share/sugar/extensions/cpsection/switchdesktop sugar/__init__.py sugar/view.py sugar/model.py sugar/gnome.png sugar/sugar.png
install -m644 sugar/module-switch-desktop.svg $RPM_BUILD_ROOT/usr/share/sugar/data/icons

make -C po install DESTDIR="$RPM_BUILD_ROOT"
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/update-desktop-database %{_datadir}/applications &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
	%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README COPYING

%{_bindir}/olpc-switch-to-sugar
%config %{_sysconfdir}/skel/Desktop/olpc-switch-to-sugar.desktop
%attr(0644,-,-) %{_datadir}/icons/hicolor/scalable/apps/olpc-switch-to-sugar.svg
%attr(0644,-,-) %{_datadir}/applications/olpc-switch-to-sugar.desktop
%attr(0644,-,-) %{_datadir}/sugar/data/icons/module-switch-desktop.svg
%{_datadir}/sugar/extensions/cpsection/switchdesktop

%changelog
* Mon Jun 22 2009 Daniel Drake <dsd@laptop.org> - 0.4-1
- Rewrite GNOME app in PyGTK

* Fri Jun 19 2009 Daniel Drake <dsd@laptop.org> - 0.3-1
- Fix Sugar control panel icon installation

* Fri Jun 19 2009 Daniel Drake <dsd@laptop.org> - 0.2-1
- GNOME app: add icon, put launcher on desktop by default, auto-logout after
  change
- Sugar extension: add screenshots, add restart button, don't crash on absence
  of .olpc-active-desktop

* Mon Jun 15 2009 Daniel Drake <dsd@laptop.org> - 0.1-1
- Initial release

