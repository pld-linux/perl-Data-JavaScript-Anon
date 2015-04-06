#
# Conditional build:
%bcond_without	tests		# perform "make test" (require Internet connection)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	JavaScript-Anon
Summary:	Data::JavaScript::Anon - dump big dumb Perl structs to anonymous JavaScript structs
Summary(pl.UTF-8):	Data::JavaScript::Anon - konwersja dużych prostych struktur Perla do anonimowych struktur JavaScript
Name:		perl-Data-JavaScript-Anon
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6808b24eaa719b9303f904e0388f3ce3
URL:		http://search.cpan.org/dist/Data-JavaScript-Anon/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Class::Default)
BuildRequires:	perl(Params::Util)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::JavaScript::Anon provides the ability to dump large simple data
structures to JavaScript. That is, things that don't need to be
a class, or have special methods or whatever.

%description -l pl.UTF-8
Data::JavaScript::Anon pozwala na konwersję dużych struktur danych
na format JavaScriptowy. Możliwe jest konwertowanie tych struktur,
które nie są klasami, nie mają specjalnych metod itp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Data/JavaScript
%{perl_vendorlib}/Data/JavaScript/Anon.pm
%{_mandir}/man?/*
