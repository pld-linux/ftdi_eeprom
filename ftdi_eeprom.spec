Summary:	EEPROM creation and upload utility for the FTDI chips
Summary(pl.UTF-8):	Narzędzie do tworzenia i nagrywania EEPROM-ów w układach FTDI
Name:		ftdi_eeprom
Version:	0.2
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.intra2net.com/de/produkte/opensource/ftdi/TGZ/%{name}-%{version}.tar.gz
# Source0-md5:	d133e77f625c496ae9d58629d7443596
URL:		http://www.intra2net.com/de/produkte/opensource/ftdi/
BuildRequires:	libconfuse-devel
BuildRequires:	libftdi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ftdi_eeprom is a tool for creating and uploading the configuration
EEPROM for the FTDI chip. An example configuration file is included.

%description -l pl.UTF-8
ftdi_eeprom to narzędzie do tworzenia i nagrywania EEPROM-ów
konfiguracyjnych w układach FTDI. Załączony jest przykładowy plik
konfiguracyjny.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ftdi_eeprom/example.conf
%attr(755,root,root) %{_bindir}/ftdi_eeprom
