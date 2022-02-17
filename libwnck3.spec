%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define oname libwnck
%define api_version 3
%define major 0
%define api %{api_version}.0

%define libname %mklibname wnck %{api_version} %{major}
%define girname %mklibname wnck-gir %{api}
%define devname %mklibname -d wnck %{api_version}

Summary:	Libwnck is Window Navigator Construction Kit
Name:		libwnck3
Version:	40.1
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libwnck/%{url_ver}/%{oname}-%{version}.tar.xz

BuildRequires:	meson
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
Suggests:	%{name} = %{version}-%{release}

%description -n %{libname}
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{devname}
Summary:	Development libraries and include files for %{name}
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}

%description -n %{devname}
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%prep
%setup -qn %{oname}-%{version}

%build
%meson
%meson_build

%install
%meson_install

rm -rf %{buildroot}%{_datadir}/locale/{io,be@latin,bn_IN,si,uz@cyrillic}
%find_lang libwnck-3.0

%files -f libwnck-3.0.lang
%{_bindir}/wnckprop
%{_bindir}/wnck-urgency-monitor

%files -n %{libname}
%{_libdir}/libwnck-%{api_version}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Wnck-%{api}.typelib

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Wnck-%{api}.gir

