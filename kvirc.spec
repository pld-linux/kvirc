#
# TODO:
# - do something about the conflicting file /usr/share/services/irc.protocol
# - installed but unpackaged: /usr/share/locale/{de,it}/LC_MESSAGES/perlcore.mo

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
Release:	1
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
BuildRequires:	sed >= 4.0
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
%setup -q
%patch0 -p1
%patch1 -p1

# kill libtool.m4 and co. in acinclude.m4
# head -n 2012 acinclude.m4 > acinclude.m4.tmp
# mv -f acinclude.m4.tmp acinclude.m4
# sed -i -e s,KVIRC_PROG_LIBTOOL,AC_PROG_LIBTOOL, configure.in

# fix for (wrong) hardcoded path
%{__sed} -i 's:/usr/lib/kvirc/3.0.0-beta3:%{_libdir}/kvirc/3.2.0:g' src/kvirc/kernel/kvi_app_fs.cpp

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
install -d $RPM_BUILD_ROOT%{_datadir}/locale/{bg,ca,cs,de,es,fr,it,nl,pl,pt,pt_BR,ru,sr}/LC_MESSAGES

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	applnkdir=%{_desktopdir} \

echo "Categories=Qt;KDE;Network;X-Communication;IRCClient;" >> $RPM_BUILD_ROOT%{_desktopdir}/kvirc.desktop

install -d $RPM_BUILD_ROOT%{_mandir}/man1/

for lang in bg ca cs de es fr it nl pl pt pt_BR ru sr; do
	for mofile in about dcc editor filetransferwindow kvirc logview notifier perl perlcore sharedfileswindow; do
		[ -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/${mofile}_${lang}.mo ] && \
		mv -f $RPM_BUILD_ROOT%{_datadir}/kvirc/%{_ver}/locale/${mofile}_${lang}.mo \
		      $RPM_BUILD_ROOT%{_datadir}/locale/${lang}/LC_MESSAGES/${mofile}.mo
	done
done

%find_lang	kvirc	--with-kde
for foo in about dcc editor filetransferwindow logview notifier perl perlcore sharedfileswindow; do
	%find_lang	$foo	--with-kde
	cat $foo.lang >> kvirc.lang
done

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
