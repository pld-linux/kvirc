Summary:	KDE Enhanced Visual IRC Client
Name:		kvirc
Version:	2.0.0
Release:	1
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Copyright:	GPL
Vendor:		Szymon Stefanek <kvirc@tin.it>
Source:		ftp://ftp.kvirc.net/kvirc/%{version}/source/%{name}-%{version}.tar.gz
#Patch:		kvi_sparser.cpp.patch
URL:		http://www.kvirc.net/
BuildRequires:	qt-devel >= 2.0
BuildRequires:	kdelibs-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
#%patch -p1

%build
charmapsdir="%{_datadir}/kvirc/charmaps"; export charmapsdir
kdeicondir="%{_pixmapsdir}/hicolor/48x48"; export kdeicondir

%configure \
	--prefix=%{prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
    charmapsdir="%{_datadir}/kvirc/charmaps" \
    kdeicondir="%{_pixmapsdir}/hicolor/48x48" \
    mandir="%{_mandir}/man1" \
    DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%attr(755,root,root) %{_datadir}/kvirc/plugins/*
%{_datadir}/kvirc/charmaps
%{_datadir}/kvirc/config
%{_datadir}/kvirc/help
%{_datadir}/kvirc/locale
%{_datadir}/kvirc/msgcolors
%{_datadir}/kvirc/pics
%{_mandir}/man1/*
%{_applnkdir}/Internet/kvirc.desktop
%{_pixmapsdir}/hicolor/48x48/kvirc.png
