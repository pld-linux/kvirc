# TODO:
# - check if the following still occurs:
#   file /usr/share/services/irc.protocol from install of
#   kvirc-3.0.0-0.20040211.4 conflicts with file from package
#   kdenetwork-kopete-protocol-irc-3.3.2-1

%define		_ver	3.2.0
#define		_snap	20040211
%define		_snap	%nil
Summary:	KDE Enhanced Visual IRC Client
Summary(es):	KVirc - Cliente IRC
Summary(pl):	Wizualny Klient IRC dla KDE
Summary(pt_BR):	KVirc - Cliente IRC
Name:		kvirc
Version:	%{_ver}
#Release:	0.%{_snap}.4.5
Release:	0.1
License:	GPL
Group:		X11/Applications
Vendor:		Szymon Stefanek <kvirc@tin.it>
Source0:	ftp://ftp.kvirc.net/pub/kvirc/%{_ver}/source/%{name}-%{_ver}.tar.bz2
# Source0-md5:	e783827fda3832fc3fb50e7a41ed627d
##Source0:	ftp://ftp.kvirc.net/pub/kvirc/snapshots/source/kvirc-%{_ver}-snap%{_snap}.tar.gz
##Source0:	%{name}-snap%{_snap}.tar.bz2
Patch0:		%{name}-paths.patch
Patch1:		%{name}-build.patch
URL:		http://www.kvirc.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libgsm-devel
BuildRequires:	libjpeg-devel
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	rpmbuild(macros) >= 1.129
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
embasado en Qt.

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
X-Window, baseado no excelente toolkit gráfico Qt.

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
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .niedakh
%patch1 -p1

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

%configure \
	--with-pipes \
	--with-aa-fonts \
	--with-big-channels \
	--with-pizza \
%ifarch %{ix86}
	--with-i386-asm \
	--with-ix86-asm \
%endif
	--with-charset-translation \
	kde_icondir=%{_iconsdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_datadir}/locale/{de,es,fr,it,nl,pl,pt,pt_BR,sr}/LC_MESSAGES

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	applnkdir=%{_desktopdir} \

echo "Categories=Qt;KDE;Network;X-Communication;IRCClient;" >> $RPM_BUILD_ROOT%{_desktopdir}/kvirc.desktop

install -d $RPM_BUILD_ROOT%{_mandir}/man1/

mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/kvirc_de.mo	$RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/dcc_de.mo      $RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/dcc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/about_de.mo      $RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/about.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/kvirc_es.mo      $RPM_BUILD_ROOT%{_datadir}/locale/es/LC_MESSAGES/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/about_es.mo      $RPM_BUILD_ROOT%{_datadir}/locale/es/LC_MESSAGES/about.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/kvirc_fr.mo      $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/kvirc_it.mo      $RPM_BUILD_ROOT%{_datadir}/locale/it/LC_MESSAGES/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/dcc_it.mo      $RPM_BUILD_ROOT%{_datadir}/locale/it/LC_MESSAGES/dcc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/about_it.mo      $RPM_BUILD_ROOT%{_datadir}/locale/it/LC_MESSAGES/about.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/logview_it.mo      $RPM_BUILD_ROOT%{_datadir}/locale/it/LC_MESSAGES/logview.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/kvirc_nl.mo      $RPM_BUILD_ROOT%{_datadir}/locale/nl/LC_MESSAGES/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/kvirc_pl.mo      $RPM_BUILD_ROOT%{_datadir}/locale/pl/LC_MESSAGES/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/kvirc_pt.mo      $RPM_BUILD_ROOT%{_datadir}/locale/pt/LC_MESSAGES/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/kvirc_pt_BR.mo      $RPM_BUILD_ROOT%{_datadir}/locale/pt_BR/LC_MESSAGES/kvirc.mo
mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/kvirc_sr.mo      $RPM_BUILD_ROOT%{_datadir}/locale/sr/LC_MESSAGES/kvirc.mo

%find_lang	kvirc	--with-kde
%find_lang	about	--with-kde
cat about.lang >> kvirc.lang
%find_lang	logview	--with-kde
cat logview.lang >> kvirc.lang
%find_lang	dcc	--with-kde
cat dcc.lang >> kvirc.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO doc/scriptexamples/{*.kvs,*/*.kvs,*/*.png}
%dir %{_datadir}/kvirc/%{_ver}/help
%dir %{_datadir}/kvirc/%{_ver}/help/en
%doc %{_datadir}/kvirc/%{_ver}/help/en/*
%attr(755,root,root) %{_bindir}/kvi_*.sh
%attr(755,root,root) %{_bindir}/kvirc
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/kvirc
%dir %{_libdir}/kvirc/%{_ver}
%dir %{_libdir}/kvirc/%{_ver}/modules
%{_libdir}/kvirc/%{_ver}/modules/caps
%attr(755,root,root) %{_libdir}/kvirc/%{_ver}/modules/*.so
# needed or not?
%{_libdir}/kvirc/%{_ver}/modules/*.la

%dir %{_datadir}/kvirc
%dir %{_datadir}/kvirc/%{_ver}
%{_datadir}/kvirc/%{_ver}/config
%{_datadir}/kvirc/%{_ver}/defscript
%{_datadir}/kvirc/%{_ver}/pics
%{_datadir}/kvirc/%{_ver}/locale/*.mo
%{_datadir}/kvirc/%{_ver}/msgcolors/*.msgclr
%{_datadir}/kvirc/%{_ver}/themes/*/*.kvc
%{_datadir}/mimelnk/text/*.desktop
%{_datadir}/services/*
# initial kvirc run complained on missing COPYING file
# it's having additional clause to GPL allowing distributing binaries for win32
%dir %{_datadir}/kvirc/%{_ver}/license
%{_datadir}/kvirc/%{_ver}/license/COPYING

%{_iconsdir}/hicolor/*/*/*.png
%{_desktopdir}/*.desktop
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kvirc-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
