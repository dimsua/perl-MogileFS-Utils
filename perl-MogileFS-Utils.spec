Name:           perl-MogileFS-Utils
Version:        2.30
Release:        1%{?dist}
Summary:        Utilities for MogileFS
License:        GPL or Artistic
Group:          Development/Libraries
URL:            https://metacpan.org/release/MogileFS-Utils
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DORMANDO/MogileFS-Utils-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-MogileFS-Client
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(LWP::Simple)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Utilities for the MogileFS distributed storage system

%prep
%setup -q -n MogileFS-Utils-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/*
%{_bindir}/mogadm
%{_bindir}/mogtool
%{_bindir}/mogdelete
%{_bindir}/mogfetch
%{_bindir}/mogfiledebug
%{_bindir}/mogfileinfo
%{_bindir}/moglistfids
%{_bindir}/moglistkeys
%{_bindir}/mogrename
%{_bindir}/mogstats
%{_bindir}/mogupload
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Thu Aug 09 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.12-1
- Upstream released new version
* Wed Jun 20 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.11-1
- Initial import
