# Unfortunately, even for noarch builds, a build on a 64-bit host uses lib64
# for _lib. Technically this is correct, as data should go in _datadir, which
# translates to /usr/share. However, it seems weird to put java libraries in
# there, even though they are technically data interpreted by the jvm.
%define libdir %{_exec_prefix}/lib

Summary: urlrewritefilter - A Java servlet container filter similar to Apache mod_rewrite
Name: urlrewritefilter
Version: 4.0.3
Release: 1
License: BSD
URL: http://tuckey.org/urlrewrite/
Source0: %{name}-%{version}.jar
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: java >= 1.6


%description
urlrewritefilter is a Java servlet container filter that provides capabilities
comparable to Apache's mod_rewrite module.


%prep
# there's nothing to unpack
# %setup -q

%build
# the java jars come pre-built, so there's nothing to do here


%install
rm -rf $RPM_BUILD_ROOT

# copy the unzipped distribution files to a reasonable place
%define sdir %{_sourcedir}
%define tdir %{buildroot}%{libdir}/%{name}/%{name}-%{version}
%__install -d %{tdir}
cp %{sdir}/%{name}-%{version}.jar %{tdir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(444,root,root,555)
%{libdir}/%{name}/%{name}-%{version}/%{name}-%{version}.jar


%changelog
* Sat Feb  9 2013 Chris Westin <cwestin@fedora-16-jetty> - 4.0.3-1
- Initial build.
