%define name	sound-monitor
%define version	1.99.0
%define release %mkrel 5

Name: 	 	%{name}
Summary: 	Audio panel accessories for GNOME2
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://gqapplets.sourceforge.net/
License:	GPL
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig GConf2 libgnomeui2-devel libpanel-applet-2-devel gettext

%description
Sound Monitor is a GNOME panel applet, it displays the current Volume output
of the Esound daemon, also, optionally shows the Esound status: Off(error),
Standby, Ready. The esound server information can be displayed, the balance
and volume can be also be adjusted for streams and samples. An extra program,
esdpvd is included that will allow saving of stream volumes between sessions.

%prep
%setup -q

%build
%configure
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
#rm -fr $RPM_BUILD_ROOT/etc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING ChangeLog NEWS TODO
%{_bindir}/esdpvd2
%{_libdir}/sound-monitor_applet2
%{_sysconfdir}/gconf/schemas/*.schemas
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/pixmaps/*.png
%{_datadir}/sound-monitor2

