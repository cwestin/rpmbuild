# Unfortunately, even for noarch builds, a build on a 64-bit host uses lib64
# for _lib. Technically this is correct, as data should go in _datadir, which
# translates to /usr/share. However, it seems weird to put java libraries in
# there, even though they are technically data interpreted by the jvm.
%define libdir %{_exec_prefix}/lib

# The distribution of this available from the URL below comes as a
# self-extracting jar that pops up a dialog box that must be clicked to
# signify acceptance of the license. This can't be done on hosts without a
# window manager, nor can it be scripted. In order to build this rpm, you
# must first obtain that jar (JAXB2_20120516.jar), and go through those
# operations, and then create the tarball named (implicitly) below
# (jaxb-2.2.5-2.tar.gz) from the resulting directory. Place that in the SOURCES
# directory, and let rpmbuild do the rest.

Summary: Trove, a java library that doesn't require boxing primitive types
Name: trove
Version: 3.0.3
Release: 1
License: GPLv2.1 & CERN
URL:  http://trove.starlight-systems.com/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: java >= 1.6

%description
The Trove library provides high speed regular and primitive collections for
Java. 

The GNU Trove library has two objectives: 
(1) Provide "free" (as in "free speech" and "free beer"), fast, lightweight
implementations of the java.util Collections API. These implementations are
designed to be pluggable replacements for their JDK equivalents.

(2) Provide primitive collections with similar APIs to the above. This gap in
the JDK is often addressed by using the "wrapper" classes (java.lang.Integer,
java.lang.Float, etc.) with Object-based collections. For most applications,
however, collections which store primitives directly will require less space
and yield significant performance gains.

Trove allows both server-side and client applications to work faster and use
less memory. Give it a try and discover a library you can't live without!

%prep
# the tarball doesn't have a single top-level directory, so create one for it
%setup -q -c %{name}-%{version}


%build
# the java jars come pre-built, so there's nothing to do here


%install
rm -rf $RPM_BUILD_ROOT

# copy the unzipped distribution files to a reasonable place
%define sdir %{_builddir}/%{name}-%{version}/%{version}
%define tdir %{buildroot}%{libdir}/%{name}/%{name}-%{version}
%__install -d %{tdir}
cp %{sdir}/AUTHORS.txt %{tdir}
cp %{sdir}/CHANGES.txt %{tdir}
cp %{sdir}/LICENSE.txt %{tdir}
cp %{sdir}/README-license.txt %{tdir}
cp %{sdir}/README.txt %{tdir}

%__install -d %{tdir}/lib
cp %{sdir}/lib/%{name}-%{version}.jar %{tdir}/lib


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/AUTHORS.txt
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/CHANGES.txt
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/LICENSE.txt
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/README-license.txt
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/README.txt

%attr(555,root,root) %{libdir}/%{name}/%{name}-%{version}/lib
%attr(444,root,root) %{libdir}/%{name}/%{name}-%{version}/lib/%{name}-%{version}.jar


%changelog
* Mon Aug 20 2012 Chris Westin <cwestin@fedora-16-jetty.domain_not_set.invalid> - 3.0.3-1
- Initial build.
