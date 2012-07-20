# Unfortunately, even for noarch builds, a build on a 64-bit host uses lib64
# for %_lib. Technically this is correct, as data should go in %_datadir, which
# translates to /usr/share. However, it seems weird to put java libraries in
# there, even though they are technically data interpreted by the jvm.
%define libdir %{_exec_prefix}/lib

Summary: Jetty Java web server library
Name: jetty
Version: 8.1.4
%define vtag v20120524
Release: 1
License: APACHE and ECLIPSE
#Group: 
URL: http://wiki.eclipse.org/Jetty
%define distro %{name}-distribution-%{version}.%{vtag}
Source0: %{distro}.tar.gz
#BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRoot: %{distro}
BuildArch: noarch


%description
Jetty is a Java web server packaged in such a way that it can be embedded in
other projects, as well as used as a servlet container in the traditional way.

This package contains all the jetty jars and structure, but does not have any
server management scripts; those would go in a jetty-server package that
would depend on this one.


%prep
# we have to give the (non-standard) name of the unzipped directory /w -n
%setup -q -n %{distro}


%build
# The jars come pre-built from the jetty site, so there's nothing to build
# here


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
* Fri Jul 20 2012 Chris Westin <cwestin@fedora-16-jetty> - 8.1.4-1
- Initial build from v20120524.

