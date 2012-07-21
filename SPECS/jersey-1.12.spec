# Unfortunately, even for noarch builds, a build on a 64-bit host uses lib64
# for _lib. Technically this is correct, as data should go in _datadir, which
# translates to /usr/share. However, it seems weird to put java libraries in
# there, even though they are technically data interpreted by the jvm.
%define libdir %{_exec_prefix}/lib

Summary: JSR311 implementation with Grizzly Server
Name: jersey
Version: 1.12
Release: 1
License: CDDL
URL: http://jersey.java.net/
%define distro %{name}-archive-%{version}
Source0: %{distro}.zip
BuildRoot: %{distro}
BuildArch: noarch
Requires: java >= 1.6


%description
JSR311 RESTful web services support via annotations.

Also includes the Grizzly web server.

This package is installed as a library, leaving it to users to create a
dependent package that runs a server service.

%prep
# we have to give the (non-standard) name of the unzipped directory /w -n
%setup -q -n %{distro}


%build
# the java jars come pre-built, so there's nothing to do here


%install
#rm -rf $RPM_BUILD_ROOT

# copy the unzipped distribution to a reasonable place
%define sdir %{_builddir}/%{distro}
%define tdir %{buildroot}%{libdir}/%{name}
%__install -d %{tdir}
cp -r %{sdir} %{tdir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%attr(0755,root,root) %{libdir}/%{name}


%changelog
* Sat Jul 21 2012 Chris Westin <cwestin@fedora-16-jetty> - 1.12-1
- Initial build.

