%define name kvirc
%define version 0.9.0
%define release 2
%define prefix /opt/kde

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: KDE Enhanced Visual IRC Client
Name: %{name}
Version: %{version}
Release: %{release}
Prefix: %{prefix}
Group: X11/KDE/Internet
Distribution: KDE
Copyright: GPL
Vendor: Szymon Stefanek <kvirc@tin.it>
Packager: Troy Engel <tengel@sonic.net>
Source: %{name}-%{version}.tar.gz
URL: http://www.kvirc.org/
Requires: qt >= 1.40 kdelibs > 1.0
BuildRoot: /tmp/build-%{name}-%{version}
Patch: kvi_sparser.cpp.patch

%description
KVIrc is an enchanced visual irc client.
Features:
        -MDI interface
        -CTCP's
        -DCC CHAT SEND/GET
        -Individual queries
        -Scripting
        -Aliases
        -Events (remote)
        -Complete color,background and behavior configuration.
        -Socks V4 support
        -... just compile it and see :)
 

%changelog
* Sun Apr 04 1999 - Troy Engel <tengel@sonic.net>
  - Removed some bad uid/gid stuff from files
  - Removed exec-prefix (now uses automatic setting)
  - Relocateable packaging

%prep
%setup
%patch -p1

%build
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=%{prefix} --with-install-root=$RPM_BUILD_ROOT
make

%install
rm -rf $RPM_BUILD_ROOT
make install

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%files
%defattr(-,root,root)
%{prefix}/bin/kvidns
%{prefix}/bin/kviphone
%{prefix}/bin/kvirc
%{prefix}/share/applnk/Internet/kvirc.kdelnk
%{prefix}/share/apps/kvirc/*
%{prefix}/share/doc/HTML/de/kvirc/*
%{prefix}/share/doc/HTML/en/kvirc/*
%{prefix}/share/icons/kvirc.xpm
%{prefix}/share/icons/mini/kvirc.xpm
%{prefix}/share/locale/de/LC_MESSAGES/kvirc.mo
%{prefix}/share/locale/it/LC_MESSAGES/kvirc.mo
