#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v2
# autospec commit: 250a666
#
Name     : perl-Module-ScanDeps
Version  : 1.35
Release  : 49
URL      : https://cpan.metacpan.org/authors/id/R/RS/RSCHUPP/Module-ScanDeps-1.35.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RS/RSCHUPP/Module-ScanDeps-1.35.tar.gz
Summary  : 'Recursively scan Perl code for dependencies'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Module-ScanDeps-bin = %{version}-%{release}
Requires: perl-Module-ScanDeps-license = %{version}-%{release}
Requires: perl-Module-ScanDeps-man = %{version}-%{release}
Requires: perl-Module-ScanDeps-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(IPC::Run3)
BuildRequires : perl(Module::Install)
BuildRequires : perl(Test::Requires)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
scan Perl programs for dependencies.
An application of Module::ScanDeps is to generate executables from scripts
that contains necessary modules; this module supports two such projects,
PAR and App::Packer.  Please see their respective documentations on CPAN
for further information.

%package bin
Summary: bin components for the perl-Module-ScanDeps package.
Group: Binaries
Requires: perl-Module-ScanDeps-license = %{version}-%{release}

%description bin
bin components for the perl-Module-ScanDeps package.


%package dev
Summary: dev components for the perl-Module-ScanDeps package.
Group: Development
Requires: perl-Module-ScanDeps-bin = %{version}-%{release}
Provides: perl-Module-ScanDeps-devel = %{version}-%{release}
Requires: perl-Module-ScanDeps = %{version}-%{release}

%description dev
dev components for the perl-Module-ScanDeps package.


%package license
Summary: license components for the perl-Module-ScanDeps package.
Group: Default

%description license
license components for the perl-Module-ScanDeps package.


%package man
Summary: man components for the perl-Module-ScanDeps package.
Group: Default

%description man
man components for the perl-Module-ScanDeps package.


%package perl
Summary: perl components for the perl-Module-ScanDeps package.
Group: Default
Requires: perl-Module-ScanDeps = %{version}-%{release}

%description perl
perl components for the perl-Module-ScanDeps package.


%prep
%setup -q -n Module-ScanDeps-1.35
cd %{_builddir}/Module-ScanDeps-1.35
pushd ..
cp -a Module-ScanDeps-1.35 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Module-ScanDeps
cp %{_builddir}/Module-ScanDeps-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Module-ScanDeps/724e019aadc4cc1b851dc94c40ca66972aaaaaed || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/scandeps.pl

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::ScanDeps.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Module-ScanDeps/724e019aadc4cc1b851dc94c40ca66972aaaaaed

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/scandeps.pl.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
