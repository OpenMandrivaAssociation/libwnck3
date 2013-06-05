%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define oname libwnck
%define api_version 3
%define major 0
%define api %{api_version}.0

%define libname %mklibname wnck %{api_version} %{major}
%define girname %mklibname wnck-gir %{api}
%define develname %mklibname -d wnck %{api_version}

Summary:	Libwnck is Window Navigator Construction Kit
Name:		libwnck3
Version:	3.4.5
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libwnck/%{url_ver}/%{oname}-%{version}.tar.xz

BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xres)
BuildRequires:	pkgconfig(libpng)
Conflicts:	libwnck < 2.30.6-5

%description
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}

%description -n %{libname}
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{develname}
Summary:	Development libraries and include files for %{name}
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}

%description -n %{develname}
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x \
	--disable-static

%make 

%install
%makeinstall_std

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_datadir}/locale/{io,be@latin,bn_IN,si,uz@cyrillic}

%find_lang libwnck-3.0

%files -f libwnck-3.0.lang
%{_bindir}/wnckprop
%{_bindir}/wnck-urgency-monitor

%files -n %{libname}
%{_libdir}/libwnck-%{api_version}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Wnck-%{api}.typelib

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Wnck-%{api}.gir
%doc %{_datadir}/gtk-doc/html/libwnck-3.0



%changelog
* Tue Nov 13 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.4.4-1
- update to 3.4.4

* Tue May 15 2012 Götz Waschk <waschk@mandriva.org> 3.4.2-1
+ Revision: 798956
- update to new version 3.4.2

* Sat Apr 28 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.0-1
+ Revision: 794327
- new version 3.4.0

* Sat Nov 19 2011 Matthew Dawkins <mattydaw@mandriva.org> 3.2.1-2
+ Revision: 731720
- rebuild for new gobject-introspec
- cleaned up spec

* Tue Nov 01 2011 Matthew Dawkins <mattydaw@mandriva.org> 3.2.1-1
+ Revision: 708126
- imported package libwnck3

