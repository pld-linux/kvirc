%define		_beta		beta2
Summary:	KDE Enhanced Visual IRC Client
Summary(es):	KVirc - Cliente IRC
Summary(pl):	Wizualny Klient IRC dla KDE
Summary(pt_BR):	KVirc - Cliente IRC
Name:		kvirc
Version:	3.0.0
Release:	0.%{_beta}.1
License:	GPL
Group:		X11/Applications
Vendor:		Szymon Stefanek <kvirc@tin.it>
Source0:	ftp://ftp.kvirc.net/kvirc/%{version}-%{_beta}/source/%{name}-%{version}-%{_beta}.tar.bz2
URL:		http://www.kvirc.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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

%description -l es
KVirc es un poderoso cliente de IRC en sistema UNIX com X-Window,
embasado en QT.

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

%description -l pt_BR
KVirc é um poderoso cliente livre de IRC para sistemas UNIX com
X-Window, baseado no excelente toolkit gráfico QT.

%package devel
Summary:	KDE Enhanced Visual IRC Client development files
Group:		X11/Development
Requires:	%{name} = %{version}

%description devel
KDE Enhanced Visual IRC Client development files

%prep
%setup -q -n %{name}-%{version}-%{_beta}

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
#charmapsdir="%{_datadir}/kvirc/charmaps"; export charmapsdir

%configure \
	--with-pipes \
	--with-ipv6-support \
%ifarch %{ix86}
	--with-i386-asm \
%endif
	--with-charset-translation
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

%{__make} DESTDIR=$RPM_BUILD_ROOT install

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Internet/kvirc.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/
rm -rf $RPM_BUILD_ROOT%{_datadir}/applnk

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO doc/scriptexamples/{*.kvs,*/*.kvs,*/*.png}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%attr(755,root,root) %{_datadir}/kvirc/%{version}-%{_beta}/modules/*.so
%{_datadir}/kvirc/%{version}-%{_beta}/modules/*.la
%{_datadir}/kvirc/%{version}-%{_beta}/modules/caps
%{_datadir}/kvirc/%{version}-%{_beta}/config/*.kvc
%{_datadir}/kvirc/%{version}-%{_beta}/config/modules/*.kvc
%{_datadir}/kvirc/%{version}-%{_beta}/defscript/*.kvs
%{_datadir}/kvirc/%{version}-%{_beta}/defscript/pics/*.png
%{_datadir}/kvirc/%{version}-%{_beta}/help/*/*.html
%{_datadir}/kvirc/%{version}-%{_beta}/help/*/*.png
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/kvirc/%{version}-%{_beta}/locale/*.mo
%{_datadir}/kvirc/%{version}-%{_beta}/pics/*.png
%{_applnkdir}/Network/Communications/*.desktop
%{_datadir}/mimelnk/text/*.desktop
%dir %{_datadir}/kvirc/%{version}-%{_beta}/modules
%dir %{_datadir}/kvirc/%{version}-%{_beta}/config/modules
%dir %{_datadir}/kvirc/%{version}-%{_beta}/config
%dir %{_datadir}/kvirc/%{version}-%{_beta}/defscript
%dir %{_datadir}/kvirc/%{version}-%{_beta}/help
%dir %{_datadir}/kvirc/%{version}-%{_beta}/locale
%dir %{_datadir}/kvirc/%{version}-%{_beta}/pics
%dir %{_datadir}/kvirc
%{_mandir}/man1/*
%{_datadir}/services

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}/%{version}-%{_beta}/*
