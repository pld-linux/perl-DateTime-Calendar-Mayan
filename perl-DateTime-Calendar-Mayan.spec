#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Calendar-Mayan
Summary:	DateTime::Calendar::Mayan - The Mayan Long Count, Haab, and Tzolkin calendars
Name:		perl-%{pdir}-%{pnam}
Version:	0.0601
Release:	1
# as perl itself
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9ed964ceadee297770be4ef7778e090c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-DateTime
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An implementation of the Mayan Long Count, Haab, and Tzolkin
calendars as defined in "Calendrical Calculations The Millennium
Edition". Supplemented by "Frequently Asked Questions about Calendars".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT
./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo
%{perl_vendorlib}/DateTime/Calendar/Mayan.pm
# not sure if that should be or should not be included..
# i rather would like to include it
#%{perl_vendorlib}/DateTime/Calendar/Mayan.pod
%{_mandir}/man3/*
