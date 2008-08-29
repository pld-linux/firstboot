Summary:	Initial system configuration utility
Summary(pl.UTF-8):	Narzędzie do początkowej konfiguracji systemu
Name:		firstboot
Version:	1.99
Release:	1
License:	GPL
Group:		Base
# https://fedorahosted.org/releases/f/i/firstboot/ (not yet)
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	8883a4e5b1eb6ddc121741b467fd3760
Patch0:		%{name}-python.patch
URL:		http://fedoraproject.org/wiki/FirstBoot
BuildRequires:	gettext-devel
Requires:	python-pygtk-gtk
Requires:	python-rhpl
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
Summary(pl.UTF-8):	Tekstowy interfejs programu firstboot
Group:		Base

%description tui
firstboot-tui is a text interface for initial system configuration.

%description tui -l pl.UTF-8
firstboot-tui to tekstowy interfejs do początkowej konfiguracji
systemu.

%prep
%setup -q
%patch0 -p1
rm po/ilo.po

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_sbindir}/firstboot
%attr(754,root,root) /etc/rc.d/init.d/firstboot
%dir %{_datadir}/firstboot
%dir %{_datadir}/firstboot/modules
%{_datadir}/firstboot/modules/*.py[co]
%{_datadir}/firstboot/themes
%dir %{py_sitedir}/firstboot
%{py_sitedir}/firstboot/*.py[co]
%{py_sitedir}/%{name}-%{version}-py*.egg-info
