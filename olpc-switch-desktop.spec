Name:		olpc-switch-desktop
Version:	0.5
Release:	1%{?dist}
Summary:	OLPC desktop switching utilities

License:	GPLv2+
Group:		System Environment/Base
URL:		http://dev.laptop.org/git/users/dsd/olpc-switch-desktop
Source0:	http://dev.laptop.org/~dsd/olpc-switch-desktop/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

BuildRequires:	gettext
Requires:		python, sugar, gtk2, desktop-file-utils, dbus


%description
This package contains a Sugar control panel extension for switching to GNOME,
and a GNOME program for switching back to Sugar.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/olpc-switch-to-sugar.desktop


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
%attr(0644,-,-) %{_datadir}/icons/hicolor/scalable/apps/olpc-switch-to-sugar.svg
%attr(0644,-,-) %{_datadir}/applications/olpc-switch-to-sugar.desktop
%attr(0644,-,-) %{_datadir}/sugar/data/icons/module-switch-desktop.svg
%{_datadir}/sugar/extensions/cpsection/switchdesktop


%changelog
* Thu Jul  9 2009 Daniel Drake <dsd@laptop.org> - 0.5-1
- Initial import

