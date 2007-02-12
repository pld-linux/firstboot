Summary:	Initial system configuration utility
Summary(pl.UTF-8):   Narzędzie do początkowej konfiguracji systemu
Name:		firstboot
Version:	1.4.6
Release:	0.1
License:	GPL
Group:		Base
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	bea227cd82be988b9638e239f3380dfb
URL:		http://fedora.redhat.com/projects/config-tools/
BuildRequires:	gettext-devel
#Requires:	/etc/init.d
#Requires:	authconfig-gtk
#Requires:	chkconfig
#Requires:	firstboot-tui
#Requires:	libuser
#Requires:	metacity
Requires:	python-pygtk-gtk
Requires:	python-rhpl
Requires:	python-rhpxl
#Requires:	redhat-artwork
#Requires:	redhat-logos
#Requires:	system-config-date >= 1.7.9
#Requires:	system-config-display
#Requires:	system-config-keyboard
#Requires:	system-config-language
#Requires:	system-config-network
#Requires:	system-config-securitylevel
#Requires:	system-config-soundcard
#Requires:	system-config-users
ExcludeArch:	s390 s390x ppc64
ExclusiveOS:	Linux
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The firstboot utility runs after installation. It guides the user
through a series of steps that allows for easier configuration of the
machine.

%description -l pl.UTF-8
Narzędzie firstboot uruchamia się po instalacji. Prowadzi użytkownika
poprzez serię kroków umożliwiających łatwą konfigurację maszyny.

%package tui
Summary:	A text interface for firstboot
Summary(pl.UTF-8):   Tekstowy interfejs programu firstboot
Group:		Base
#Requires:	/etc/init.d
#Requires:	authconfig
#Requires:	chkconfig
#Requires:	netconfig
#Requires:	ntsysv
#Requires:	python
#Requires:	python-rhpl
#Requires:	system-config-securitylevel-tui
#Requires:	usermode >= 1.36

%description tui
firstboot-tui is a text interface for initial system configuration.

%description tui -l pl.UTF-8
firstboot-tui to tekstowy interfejs do początkowej konfiguracji
systemu.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTROOT=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT/usr/share/firstboot
%py_ocomp $RPM_BUILD_ROOT/usr/share/firstboot
%py_postclean /usr/share/firstboot

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post tui
#/sbin/chkconfig --add firstboot

%preun tui
if [ "$1" = 0 ]; then
	/sbin/chkconfig --del firstboot
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir /usr/share/firstboot
%dir /usr/share/firstboot/modules
%dir /usr/share/firstboot/pixmaps
/usr/share/firstboot/exceptionWindow.py[co]
/usr/share/firstboot/firstbootWindow.py[co]
/usr/share/firstboot/firstboot_module_window.py[co]
/usr/share/firstboot/xfirstboot.py[co]
/usr/share/firstboot/modules/*
/usr/share/firstboot/pixmaps/*

%files -f %{name}.lang tui
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/firstboot
%dir /usr/share/firstboot/
%attr(755,root,root) %{_sbindir}/firstboot
/usr/share/firstboot/constants_text.py[co]
/usr/share/firstboot/eula_strings.py[co]
/usr/share/firstboot/firstboot.py[co]
/usr/share/firstboot/firstbootBackend.py[co]
/usr/share/firstboot/functions.py[co]
/usr/share/firstboot/textWindow.py[co]
