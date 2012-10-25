# Unfortunately, even for noarch builds, a build on a 64-bit host uses lib64
# for _lib. Technically this is correct, as data should go in _datadir, which
# translates to /usr/share. However, it seems weird to put java libraries in
# there, even though they are technically data interpreted by the jvm.
%define libdir %{_exec_prefix}/lib

Summary: httpcomponents HTTP client library
Name: httpcomponents-client
Version: 4.2.1
Release: 1
License: Apache 2
URL: http://hc.apache.org/index.html
Source0: %{name}-%{version}-bin.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: java >= 1.6


%description
See http://hc.apache.org/index.html .


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
cp %{sdir}/README.txt %{tdir}
cp %{sdir}/RELEASE_NOTES.txt %{tdir}

%__install -d %{tdir}/lib
cp %{sdir}/lib/commons-codec-1.6.jar %{tdir}/lib
cp %{sdir}/lib/commons-logging-1.1.1.jar %{tdir}/lib
cp %{sdir}/lib/fluent-hc-%{version}.jar %{tdir}/lib
cp %{sdir}/lib/httpclient-%{version}.jar %{tdir}/lib
cp %{sdir}/lib/httpclient-cache-%{version}.jar %{tdir}/lib
cp %{sdir}/lib/httpcore-%{version}.jar %{tdir}/lib
cp %{sdir}/lib/httpmime-%{version}.jar %{tdir}/lib


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/LICENSE.txt
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/NOTICE.txt
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/README.txt
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/RELEASE_NOTES.txt

%attr(555,root,root) %{libdir}/%{name}/%{name}-%{version}/lib
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/lib/commons-codec-1.6.jar
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/lib/commons-logging-1.1.1.jar
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/lib/fluent-hc-%{version}.jar
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/lib/httpclient-%{version}.jar
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/lib/httpclient-cache-%{version}.jar
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/lib/httpcore-%{version}.jar
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/lib/httpmime-%{version}.jar


%changelog
* Thu Oct 25 2012 Chris Westin <cwestin@fedora-16-jetty> - client-4.2.1
- Initial build.

