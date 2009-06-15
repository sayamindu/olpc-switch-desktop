Name:		olpc-switch-desktop
Version:	0.1
Release:	1%{?dist}
Summary:	OLPC desktop switching utilities

Group: System Environment/Base
License: GPL
URL: http://dev.laptop.org/git/users/dsd/olpc-switch-desktop
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: python, sugar
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
install -m755 gnome/olpc-switch-to-sugar $RPM_BUILD_ROOT/usr/bin
install gnome/olpc-switch-to-sugar.desktop $RPM_BUILD_ROOT/usr/share/applications

install -d $RPM_BUILD_ROOT/usr/share/sugar/extensions/cpsection/desktopswitch
install -t $RPM_BUILD_ROOT/usr/share/sugar/extensions/cpsection/desktopswitch sugar/__init__.py sugar/view.py sugar/model.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING

/usr/bin/olpc-switch-to-sugar
/usr/share/applications/olpc-switch-to-sugar.desktop
/usr/share/sugar/extensions/cpsection/desktopswitch

%changelog
* Mon Jun 15 2009 Daniel Drake <dsd@laptop.org> - 0.1-1
- Initial release

