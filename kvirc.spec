Summary:	KDE Enhanced Visual IRC Client
Name:		kvirc
Version:	0.9.0
Release:	1
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Copyright:	GPL
Vendor:		Szymon Stefanek <kvirc@tin.it>
Source:		%{name}-%{version}.tar.gz
Patch:		kvi_sparser.cpp.patch
URL:		http://www.kvirc.org/
BuildRequires:	qt-devel >= 1.40
BuildRequires:	kdelibs-devel > 1.0
BuildRoot:	/tmp/%{name}-%{version}-root

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
 
%prep
%setup -q
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
