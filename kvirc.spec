Summary:	KDE Enhanced Visual IRC Client
Summary(pl):	Wizualny Klient IRC dla KDE
Name:		kvirc
Version:	2.1.0
Release:	3
License:	GPL
Group:		X11/Applications
Vendor:		Szymon Stefanek <kvirc@tin.it>
Source0:	ftp://ftp.kvirc.net/kvirc/%{version}/source/%{name}-%{version}.tar.gz
URL:		http://www.kvirc.net/
BuildRequires:	qt-devel >= 2.0
BuildRequires:	kdelibs-devel >= 2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libjpeg-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
KVIrc is an enchanced visual irc client. Features:
 - MDI interface
 - CTCP's
 - DCC CHAT SEND/GET
 - Individual queries
 - Scripting
 - Aliases
 - Events (remote)
 - Complete color,background and behavior configuration
 - IPv6 support

%description -l pl
KVIrc jest rozszerzonym, wizualnym klientem irc. Jego mo�liwo�ci i
zalety to:
 - interfejs MDI
 - CTCP
 - DCC CHAT SEND/GET
 - indywidualne zapytania
 - skrypty
 - aliasy
 - zdarzenia
 - kompletne wsparcie dla kolor�w
 - obs�uga IPv6

%prep
%setup -q

%build
charmapsdir="%{_datadir}/kvirc/charmaps"; export charmapsdir
kdeicondir="%{_pixmapsdir}/hicolor/48x48"; export kdeicondir

aclocal
autoconf
%configure \
	--prefix=%{_prefix} \
	--with-pipes \
	--with-ipv6-support \
%ifarch %{ix86}
	--with-i386-asm \
%endif
	--with-charset-translation
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
    charmapsdir="%{_datadir}/kvirc/charmaps" \
    kdeicondir="%{_pixmapsdir}/hicolor/48x48" \
    mandir="%{_mandir}/man1" \
    DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

mv -f $RPM_BUILD_ROOT%{_applnkdir}/Internet/kvirc.desktop \
   $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/kvirc.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%dir %{_datadir}/kvirc
%attr(755,root,root) %{_datadir}/kvirc/plugins/*
%{_datadir}/kvirc/charmaps
%{_datadir}/kvirc/config
%{_datadir}/kvirc/help
%{_datadir}/kvirc/locale
%{_datadir}/kvirc/msgcolors
%{_datadir}/kvirc/pics
%{_mandir}/man1/*
%{_applnkdir}/Network/Communications/kvirc.desktop
%{_pixmapsdir}/hicolor/48x48/kvirc.png
