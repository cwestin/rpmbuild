# Unfortunately, even for noarch builds, a build on a 64-bit host uses lib64
# for _lib. Technically this is correct, as data should go in _datadir, which
# translates to /usr/share. However, it seems weird to put java libraries in
# there, even though they are technically data interpreted by the jvm.
%define libdir %{_exec_prefix}/lib

Summary: Akka library and microkernel from Typesafe
Name: akka
Version: 2.0.3
Release: 1
License: Apache 2
URL: http://akka.io/
Source0: %{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: java >= 1.6


%description
Library supports Actors in Java or Scala, and includes a microkernel that can
be used as an application server. See the Akka site above.

This package does not include the documentation or windows batch file that
comes in the distribution tarball. Only the bin and lib directories are
present.

This package does include the config and deploy directories within the
distribution, as the current tarball expects you to drop your application in
there if you are using the application server option; I'm not familiar enough
with this yet to know if you can set up an environment where those live outside
this package, so they are there for now (I'm only using the actor library
embedded in an existing application). If you're using the microkernel
application server, I recommend starting it as a service from another package
that includes your jars.


%prep
%setup -q


%build
# the java jars come pre-built, so there's nothing to do here


%install
rm -rf $RPM_BUILD_ROOT

# copy the unzipped distribution files to a reasonable place
# this doesn't include the documentation
%define sdir %{_builddir}/%{name}-%{version}
%define tdir %{buildroot}%{libdir}/%{name}/%{name}-%{version}
%__install -d %{tdir}
%__install -d %{tdir}/bin
cp %{sdir}/bin/akka %{tdir}/bin

%__install -d %{tdir}/config
cp %{sdir}/config/application.conf %{tdir}/config

%__install -d %{tdir}/deploy

%__install -d %{tdir}/lib
cp -r %{sdir}/lib/* %{tdir}/lib


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(444,root,root,755)
%define akkadir %{libdir}/%{name}/%{name}-%{version}
%attr(555,root,root) %{akkadir}/bin/akka
%config %{akkadir}/config/application.conf
%dir %{akkadir}/deploy
%{akkadir}/lib


%changelog
* Sun Oct 28 2012 Chris Westin <cwestin@fedora-16-jetty> - 2.0.3-1
- Initial build.
