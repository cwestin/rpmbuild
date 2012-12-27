# Unfortunately, even for noarch builds, a build on a 64-bit host uses lib64
# for _lib. Technically this is correct, as data should go in _datadir, which
# translates to /usr/share. However, it seems weird to put java libraries in
# there, even though they are technically data interpreted by the jvm.
%define libdir %{_exec_prefix}/lib

# before running this, rename the downloaded javamail1_4_5.zip to javamail-1.4.5.zip

Summary: JavaMail library
Name: javamail
Version: 1.4.5
Release: 1
License: Oracle Binary Code License Agreement for Java EE Technologies
URL: http://www.oracle.com/technetwork/java/javamail/index.html
Source0: %{name}-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildArch: noarch
Requires: java >= 1.6


%description
JavaMail Library for sending and receiving email.


%prep
%setup -q


%build
# the java jars come pre-built, so there's nothing to do here


%install
#rm -rf $RPM_BUILD_ROOT

# copy the unzipped distribution to a reasonable place
%define sdir %{_builddir}/%{name}-%{version}
%define tdir %{buildroot}%{libdir}/%{name}/%{name}-%{version}
%__install -d %{tdir}
cp %{sdir}/COPYRIGHT.txt %{tdir}
cp %{sdir}/LICENSE.txt %{tdir}
cp %{sdir}/README.txt %{tdir}
cp %{sdir}/distributionREADME.txt %{tdir}
cp %{sdir}/mail.jar %{tdir}
cp -r %{sdir}/lib %{tdir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(0644,root,root,0755)
%{libdir}/%{name}/%{name}-%{version}


%changelog
* Thu Dec 27 2012 Chris Westin <cwestin@fedora-16-jetty> - 1.4.5-1
- Initial build.
