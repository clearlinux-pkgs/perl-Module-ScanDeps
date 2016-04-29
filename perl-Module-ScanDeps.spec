#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-ScanDeps
Version  : 0.54
Release  : 3
URL      : http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/Module-ScanDeps-0.54.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/Module-ScanDeps-0.54.tar.gz
Summary  : Recursively scan Perl code for dependencies
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Module-ScanDeps-bin
Requires: perl-Module-ScanDeps-doc

%description
scan Perl programs for dependencies.
An application of Module::ScanDeps is to generate executables from scripts
that contains necessary modules; this module supports two such projects,
PAR and App::Packer.  Please see their respective documentations on CPAN
for further information.

%package bin
Summary: bin components for the perl-Module-ScanDeps package.
Group: Binaries

%description bin
bin components for the perl-Module-ScanDeps package.


%package doc
Summary: doc components for the perl-Module-ScanDeps package.
Group: Documentation

%description doc
doc components for the perl-Module-ScanDeps package.


%prep
%setup -q -n Module-ScanDeps-0.54

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/Module/ScanDeps.pm
/usr/lib/perl5/site_perl/5.22.0/Module/ScanDeps/DataFeed.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/scandeps.pl

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
