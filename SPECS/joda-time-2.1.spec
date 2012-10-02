# Unfortunately, even for noarch builds, a build on a 64-bit host uses lib64
# for _lib. Technically this is correct, as data should go in _datadir, which
# translates to /usr/share. However, it seems weird to put java libraries in
# there, even though they are technically data interpreted by the jvm.
%define libdir %{_exec_prefix}/lib


Summary: joda-time java date and time library
Name: joda-time
Version: 2.1
Release: 1
License: Apache 2.0
URL: http://joda-time.sourceforge.net/
Source0: %{name}-%{version}-dist.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: java >= 1.6


%description
Joda-Time provides a quality replacement for the Java date and
time classes. The design allows for multiple calendar systems,
while still providing a simple API. The 'default' calendar is the
ISO8601 standard which is used by XML. The Gregorian, Julian,
Buddhist, Coptic, Ethiopic and Islamic systems are also included,
and we welcome further additions. Supporting classes include time
zone, duration, format and parsing.


%prep
%setup -q


%build
# the java jars come pre-built, so there's nothing to do here


%install
rm -rf $RPM_BUILD_ROOT

# copy the unzipped distribution files to a reasonable place
%define sdir %{_builddir}/%{name}-%{version}
%define tdir %{buildroot}%{libdir}/%{name}/%{name}-%{version}
%__install -d %{tdir}
cp %{sdir}/LICENSE.txt %{tdir}
cp %{sdir}/NOTICE.txt %{tdir}
cp %{sdir}/%{name}-%{version}.jar %{tdir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/LICENSE.txt
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/NOTICE.txt
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/%{name}-%{version}.jar


%changelog
* Tue Oct  2 2012 Chris Westin <cwestin@fedora-16-jetty> - time-2.1
- Initial build.

