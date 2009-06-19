Name:		olpc-switch-desktop
Version:	0.1
Release:	1%{?dist}
Summary:	OLPC desktop switching utilities

Group: System Environment/Base
License: GPL
URL: http://dev.laptop.org/git/users/dsd/olpc-switch-desktop
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: python, sugar, gtk2, desktop-file-utils
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
install -t $RPM_BUILD_ROOT/usr/share/sugar/extensions/cpsection/switchdesktop sugar/__init__.py sugar/view.py sugar/model.py

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/update-desktop-database %{_datadir}/applications &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
	%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%defattr(-,root,root,-)
%doc README COPYING

%{_bindir}/olpc-switch-to-sugar
%config %{_sysconfdir}/skel/Desktop/olpc-switch-to-sugar.desktop
%attr(0644,-,-) %{_datadir}/icons/hicolor/scalable/apps/olpc-switch-to-sugar.svg
%attr(0644,-,-) %{_datadir}/applications/olpc-switch-to-sugar.desktop
%{_datadir}/sugar/extensions/cpsection/switchdesktop

%changelog
* Mon Jun 15 2009 Daniel Drake <dsd@laptop.org> - 0.1-1
- Initial release

