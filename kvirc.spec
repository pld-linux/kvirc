Summary:	KDE Enhanced Visual IRC Client
Summary(pl):	Wizualny Klient IRC dla KDE
Name:		kvirc
Version:	3.0.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Vendor:		Szymon Stefanek <kvirc@tin.it>
Source0:	ftp://ftp.kvirc.net/kvirc/%{version}xmas/source/%{name}-%{version}-xmas.tar.gz
URL:		http://www.kvirc.net/
BuildRequires:	qt-devel >= 3.0
BuildRequires:	kdelibs-devel >= 3.0
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
KVIrc jest rozszerzonym, wizualnym klientem irc. Jego mo¿liwo¶ci i
zalety to:
 - interfejs MDI
 - CTCP
 - DCC CHAT SEND/GET
 - indywidualne zapytania
 - skrypty
 - aliasy
 - zdarzenia
 - kompletne wsparcie dla kolorów
 - obs³uga IPv6

%prep
%setup -q -n %{name}-%{version}-xmas

%build
#charmapsdir="%{_datadir}/kvirc/charmaps"; export charmapsdir
#kdeicondir="%{_pixmapsdir}/hicolor/48x48"; export kdeicondir

aclocal
%{__autoconf}
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
#%{__make} \
#    charmapsdir="%{_datadir}/kvirc/charmaps" \
#    kdeicondir="%{_pixmapsdir}/hicolor/48x48" \
#    mandir="%{_mandir}/man1" \
%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

mv -f $RPM_BUILD_ROOT/usr/X11R6/share/kvirc/3.0.0-xmas/applnk/kvirc.desktop \
   $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/kvirc.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%dir %{_datadir}/kvirc
%dir %{_datadir}/kvirc/%{version}-xmas/modules
%{_datadir}/kvirc/%{version}-xmas/config
%{_datadir}/kvirc/%{version}-xmas/defscript
%{_datadir}/kvirc/%{version}-xmas/help
%{_datadir}/kvirc/%{version}-xmas/icons
%{_datadir}/kvirc/%{version}-xmas/license
%{_datadir}/kvirc/%{version}-xmas/locale
%attr(755,root,root) %{_datadir}/kvirc/%{version}-xmas/modules/*
%{_datadir}/kvirc/%{version}-xmas/pics
%{_datadir}/kvirc/%{version}-xmas/protocols
%{_applnkdir}/Network/Communications/kvirc.desktop
