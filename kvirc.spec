%define		_snap	20040211
%define 	fver	3.0.0-beta3
Summary:	KDE Enhanced Visual IRC Client
Summary(es):	KVirc - Cliente IRC
Summary(pl):	Wizualny Klient IRC dla KDE
Summary(pt_BR):	KVirc - Cliente IRC
Name:		kvirc
Version:	3.0.0
Release:	0.%{_snap}.2
License:	GPL
Group:		X11/Applications
Vendor:		Szymon Stefanek <kvirc@tin.it>
##Source0:	ftp://ftp.kvirc.net/kvirc/%{fver}/source/%{name}-%{fver}.tar.bz2
##Source0:	ftp://ftp.kvirc.net/pub/kvirc/snapshots/source/kvirc-%{version}-snap%{_snap}.tar.gz
Source0:	%{name}-snap%{_snap}.tar.bz2
# Source0-md5:	a1b31ac966d9d35c392631d41e2b506e
Patch0:		%{name}-paths.patch
Patch1:		%{name}-optw_irc.patch
URL:		http://www.kvirc.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libjpeg-devel
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	openssl-devel
BuildRequires:	libgsm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

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
Summary:	Header files for KVirc library
Summary(pl):	Pliki nag³ówkowe biblioteki KVirc
Group:		X11/Development
Requires:	%{name} = %{version}

%description devel
Header files for KVirc library.

%description devel -l pl
Pliki nag³ówkowe biblioteki KVirc.

%prep
%setup -q -n kvirc
%patch0 -p2
%patch1 -p0

# kill libtool.m4 and co. in acinclude.m4
# head -n 2012 acinclude.m4 > acinclude.m4.tmp
# mv -f acinclude.m4.tmp acinclude.m4
# sed -i -e s,KVIRC_PROG_LIBTOOL,AC_PROG_LIBTOOL, configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
#charmapsdir="%{_datadir}/kvirc/charmaps"; export charmapsdir
%configure \
	--with-pipes \
	--with-aa-fonts \
	--with-big-channels \
	--with-pizza \
%ifarch %{ix86}
	--with-i386-asm \
	--with-ix86-asm \
%endif
	--with-charset-translation
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kvirc
install -d $RPM_BUILD_ROOT%{_datadir}/locale/{de,es,fr,it,nl,pl,pt,pt_BR,sr}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

mv -f $RPM_BUILD_ROOT%{_applnkdir}/Internet/kvirc.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

echo "Categories=Qt;KDE;Network;X-Communication;" >> $RPM_BUILD_ROOT%{_desktopdir}/kvirc.desktop

install -d $RPM_BUILD_ROOT%{_mandir}/man1/
mv $RPM_BUILD_ROOT{%{_datadir}/man/kvirc.1*,%{_mandir}/man1/}

mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/kvirc_de.mo	$RPM_BUILD_ROOT%{_datadir}/locale/de/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/dcc_de.mo      $RPM_BUILD_ROOT%{_datadir}/locale/de/dcc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/about_de.mo      $RPM_BUILD_ROOT%{_datadir}/locale/de/about.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/kvirc_es.mo      $RPM_BUILD_ROOT%{_datadir}/locale/es/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/about_es.mo      $RPM_BUILD_ROOT%{_datadir}/locale/es/about.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/kvirc_fr.mo      $RPM_BUILD_ROOT%{_datadir}/locale/fr/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/kvirc_it.mo      $RPM_BUILD_ROOT%{_datadir}/locale/it/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/dcc_it.mo      $RPM_BUILD_ROOT%{_datadir}/locale/it/dcc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/about_it.mo      $RPM_BUILD_ROOT%{_datadir}/locale/it/about.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/logview_it.mo      $RPM_BUILD_ROOT%{_datadir}/locale/it/logview.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/kvirc_nl.mo      $RPM_BUILD_ROOT%{_datadir}/locale/nl/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/kvirc_pl.mo      $RPM_BUILD_ROOT%{_datadir}/locale/pl/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/kvirc_pt.mo      $RPM_BUILD_ROOT%{_datadir}/locale/pt/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/kvirc_pt_BR.mo      $RPM_BUILD_ROOT%{_datadir}/locale/pt_BR/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{fver}/locale/kvirc_sr.mo      $RPM_BUILD_ROOT%{_datadir}/locale/sr/kvirc.mo

%find_lang	kvirc	--with-kde
%find_lang      about   --with-kde
cat about.lang >> kvirc.lang
%find_lang      logview   --with-kde
cat logview.lang >> kvirc.lang
%find_lang      dcc   --with-kde
cat dcc.lang >> kvirc.lang

mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc $RPM_BUILD_ROOT%{_datadir}/apps/kvirc
install -d $RPM_BUILD_ROOT%{_iconsdir}
mv -f $RPM_BUILD_ROOT{%{_pixmapsdir}/*,%{_iconsdir}}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kvirc.lang 
%defattr(644,root,root,755)
%doc README TODO doc/scriptexamples/{*.kvs,*/*.kvs,*/*.png}
%attr(755,root,root) %{_bindir}/kvi_*.sh
%attr(755,root,root) %{_bindir}/kvirc
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/kvirc
%dir %{_libdir}/kvirc/%{fver}
%dir %{_libdir}/kvirc/%{fver}/modules
%{_libdir}/kvirc/%{fver}/modules/caps
%attr(755,root,root) %{_libdir}/kvirc/%{fver}/modules/*.so
# needed or not?
%{_libdir}/kvirc/%{fver}/modules/*.la
%{_datadir}/apps/kvirc
%{_iconsdir}/hicolor/*/*/*.png
%{_desktopdir}/*.desktop
%{_datadir}/mimelnk/text/*.desktop
%{_mandir}/man1/*
%{_datadir}/services/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kvirc-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
