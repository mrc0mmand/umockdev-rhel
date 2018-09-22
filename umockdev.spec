Name: umockdev
Version: 0.12
Release: 2%{?dist}
Summary: Mock hardware devices for creating unit tests and bug reporting

License: LGPLv2+
URL: https://github.com/martinpitt/%{name}
Source: https://github.com/martinpitt/umockdev/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: chrpath
BuildRequires: git
BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: libgudev1-devel
BuildRequires: libtool
BuildRequires: libudev-devel
BuildRequires: vala

Patch0: 0001-Fix-missing-O_TMPFILE-on-some-systems.patch

%description
With this program and libraries you can easily create mock udev objects.
This is useful for writing tests for software which talks to
hardware devices.

%package devel
Summary: Development packages for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the libraries to develop
using %{name}.

%prep
%autosetup -n %{name}-%{version} -S git

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static --enable-gtk-doc

make %{?_smp_mflags}

%install

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

#nuke the .la file(s)
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Remove rpath
chrpath --delete %{buildroot}%{_bindir}/umockdev-record \
	%{buildroot}%{_bindir}/umockdev-run
chrpath --delete %{buildroot}%{_libdir}/libumockdev.so.*
chrpath --delete %{buildroot}%{_libdir}/libumockdev-preload.so.*

rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/umockdev

%check

# Disabled for now, as the Xorg tests don't pass
# https://github.com/martinpitt/umockdev/issues/47
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README.rst
%{_bindir}/umockdev-*
%{_libdir}/libumockdev.so.*
%{_libdir}/libumockdev-preload.so.*
%{_libdir}/girepository-1.0/UMockdev-1.0.typelib

%files devel
%doc docs/script-format.txt docs/examples/battery.c docs/examples/battery.py
%{_libdir}/libumockdev.so
%{_libdir}/pkgconfig/umockdev-1.0.pc
%{_datadir}/gir-1.0/UMockdev-1.0.gir
%{_includedir}/umockdev-1.0
%{_datadir}/gtk-doc/html/umockdev/
%{_datadir}/vala/vapi/umockdev-1.0.vapi

%changelog
* Fri Sep 21 2018 Frantisek Sumsal <frantisek@sumsal.cz> - 0.12-2
- Use specfile structure from the Fedora package (by Bastien Nocera)
- Patch for missing O_TMPFILE on some systems

* Fri Sep 21 2018 Frantisek Sumsal <frantisek@sumsal.cz> - 0.12-1
- Initial spec

