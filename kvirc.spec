%define		_beta		beta3
%define		_snap	20031227

Summary:	KDE Enhanced Visual IRC Client
Summary(es):	KVirc - Cliente IRC
Summary(pl):	Wizualny Klient IRC dla KDE
Summary(pt_BR):	KVirc - Cliente IRC
Name:		kvirc
Version:	3.0.0
Release:	0.%{_snap}.1
#%define	fver	%{version}-%{_beta}
License:	GPL
Group:		X11/Applications
Vendor:		Szymon Stefanek <kvirc@tin.it>
##Source0:	ftp://ftp.kvirc.net/kvirc/%{fver}/source/%{name}-%{fver}.tar.bz2
Source0:	ftp://ftp.kvirc.net/pub/kvirc/snapshots/source/kvirc-%{version}-snap%{_snap}.tar.gz
# Source0-md5:	bf1ff20fa62413976c8ac912c044b60d
Patch0:		%{name}-paths.patch
URL:		http://www.kvirc.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
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
%setup -q -n %{name}-%{fver}
%patch -p1

# kill libtool.m4 and co. in acinclude.m4
head -n 2012 acinclude.m4 > acinclude.m4.tmp
mv -f acinclude.m4.tmp acinclude.m4
sed -i -e s,KVIRC_PROG_LIBTOOL,AC_PROG_LIBTOOL, configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Internet/kvirc.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

echo "Categories=Qt;KDE;Network;InstantMessaging;" >> \
	$RPM_BUILD_ROOT%{_desktopdir}/kvirc.desktop

install -d $RPM_BUILD_ROOT%{_mandir}/man1/
mv $RPM_BUILD_ROOT{%{_datadir}/man/kvirc.1,%{_mandir}/man1/}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
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

%dir %{_datadir}/kvirc
%dir %{_datadir}/kvirc/%{fver}
%{_datadir}/kvirc/%{fver}/config
%{_datadir}/kvirc/%{fver}/defscript
%dir %{_datadir}/kvirc/%{fver}/help
%{_datadir}/kvirc/%{fver}/help/en
##%dir %{_datadir}/kvirc/%{fver}/locale
%lang(de) %{_datadir}/kvirc/%{fver}/locale/*_de.mo
%lang(es) %{_datadir}/kvirc/%{fver}/locale/*_es.mo
%lang(fr) %{_datadir}/kvirc/%{fver}/locale/*_fr.mo
%lang(it) %{_datadir}/kvirc/%{fver}/locale/*_it.mo
%lang(nl) %{_datadir}/kvirc/%{fver}/locale/*_nl.mo
%lang(pl) %{_datadir}/kvirc/%{fver}/locale/*_pl.mo
%lang(pt) %{_datadir}/kvirc/%{fver}/locale/*_pt.mo
%lang(pt_BR) %{_datadir}/kvirc/%{fver}/locale/*_pt_BR.mo
%lang(sr) %{_datadir}/kvirc/%{fver}/locale/*_sr.mo
%{_datadir}/kvirc/%{fver}/pics
%{_pixmapsdir}/hicolor/*/*/*.png
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
