Name: umockdev
Version: 0.12
Release: 1%{?dist}
Summary: Mock hardware devices for creating unit tests and bug reporting

License: LGPLv2+
URL: https://github.com/martinpitt/umockdev
Source: https://github.com/martinpitt/umockdev/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: libgudev1-devel
BuildRequires: libtool
BuildRequires: libudev-devel
BuildRequires: vala

%description
TODO

%prep
%setup -q


%build
./autogen.sh
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog
* Fri Sep 21 2018 Frantisek Sumsal <frantisek@sumsal.cz> - 0.12-1
- Initial spec


