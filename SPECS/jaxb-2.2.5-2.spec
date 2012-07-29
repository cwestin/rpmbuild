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

Summary: Reference implementation of JAXB, JSR-222 (JAXB 2.x) & JSR-31 (JAXB 1.0)
Name: jaxb
Version: 2.2.5
Release: 2
License: CDDL & GPLv2
URL: http://jaxb.java.net/2.2.5-2/
Source0: %{name}-%{version}-%{release}.tar.gz
%define distro jaxb-ri-20120516
BuildRoot: %{distro}
BuildArch: noarch
Requires: java >= 1.6


%description
The goal of the JAXB project is to develop and evolve the code base for the Reference Implementation (RI) of JAXB, the Java Architecture for XML Binding. The JAXB specification is developed through the Java Community Process following the process described at jcp.org. This process involves an Expert Group with a lead that is responsible for delivering the specification, a reference implementation (RI) and a Technology Compatibility Kit (TCK). The primary goal of an RI is to support the development of the specification and to validate it. Specific RIs can have additional goals; the JAXB RI is a production-quality implementation that is used directly in a number of products by Oracle and other vendors.

The JAXB expert group has wide industry participation with Oracle as the EG lead. The initial specification (JAXB 1.0) was JSR-31 and was released in March 2003.

The next versions of the spec (JAXB 2.0/2.1/2.2) are being developed as JSR-222. This release addresses a number of additional requirements in the area, and increases the synergy between the JAXB and JAX-WS specifications.


%prep
# we have to give the (non-standard) name of the unzipped directory /w -n
%setup -q -n %{distro}

%build
# the java jars come pre-built, so there's nothing to do here


%install
rm -rf $RPM_BUILD_ROOT

# At the moment, this includes the whole distro, and should probably be
# cleaned up not to include the zipped sources, or javadoc, which should go
# in other packages, and or be used to build a doc and binary package

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
* Sun Jul 29 2012 Chris Westin <cwestin@fedora-16-jetty> - 2.2.5-2
- Initial build.

