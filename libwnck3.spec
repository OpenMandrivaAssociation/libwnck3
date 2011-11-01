%define oname		libwnck

%define api_version	3
%define lib_major	0
%define api		%{api_version}.0
%define libname		%mklibname wnck %{api_version} %{lib_major}
%define gi_name		%mklibname wnck-gir %{api}
%define libnamedev	%mklibname -d wnck %{api_version}

Summary:	Libwnck is Window Navigator Construction Kit
Name:		libwnck3
Version:	3.2.1
Release:	%mkrel 1
Source0:	http://download.gnome.org/sources/%{oname}/3.2/%{oname}-%{version}.tar.xz
License:	LGPLv2+
URL:		http://www.gnome.org/
Group:		System/Libraries
BuildRequires:	pkgconfig(glib-2.0) >= 2.16.0
BuildRequires:	pkgconfig(gobject-2.0) >= 2.13.0
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.6.14
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(libstartup-notification-1.0) >= 0.4
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xres)
BuildRequires:	pkgconfig(libpng12)
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	gnome-common
Conflicts:	libwnck < 2.30.6-5

%description
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Requires:	%{name} >= %{version}
Obsoletes:	%{_lib}wnck-3_0 < 3.1.5

%description -n %{libname}
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{gi_name}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{gi_name}
GObject Introspection interface library for %{name}.

%package -n %{libnamedev}
Summary:	Development libraries and include files for %{name}
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}-%{api_version}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	%{gi_name} = %{version}
Conflicts:	%mklibname -d wnck-1_ 4
Conflicts:	%mklibname -d wnck-1_ 16
Conflicts:	%mklibname -d wnck-1_ 18
Obsoletes:	%{_lib}wnck-3-devel < 3.1.5

%description -n %{libnamedev}
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x --disable-static
%make 

%install
rm -rf %{buildroot}
%makeinstall_std

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_datadir}/locale/{io,be@latin,bn_IN,si,uz@cyrillic}

%find_lang libwnck-3.0

%files -f libwnck-3.0.lang
%defattr(-,root,root)
%{_bindir}/wnckprop
%{_bindir}/wnck-urgency-monitor

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libwnck-%{api_version}.so.%{lib_major}*

%files -n %{gi_name}
%{_libdir}/girepository-1.0/Wnck-%{api}.typelib

%files -n %{libnamedev}
%defattr(-,root,root)
%{_includedir}/*
%doc %{_datadir}/gtk-doc/html/libwnck-3.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Wnck-%{api}.gir


