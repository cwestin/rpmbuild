Summary: Application for reducing the size of pngs
Name: pngcrush
Version: 1.7.41
Release: 1
License: libpng-derived
URL: http://pmt.sourceforge.net/pngcrush/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
pngcrush is an application for minimizing the size of png files.


%prep
%setup -q


%build
make


%install
rm -rf $RPM_BUILD_ROOT
%__install -d %{buildroot}%{_bindir}
cp %{_builddir}/%{name}-%{version}/%name %{buildroot}%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(655,root,root,755)
%{_bindir}/%{name}


%changelog
* Tue Jan 15 2013 Chris Westin <cwestin@fedora-16-jetty> - 
- Initial build.

