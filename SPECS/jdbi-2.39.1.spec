# Unfortunately, even for noarch builds, a build on a 64-bit host uses lib64
# for _lib. Technically this is correct, as data should go in _datadir, which
# translates to /usr/share. However, it seems weird to put java libraries in
# there, even though they are technically data interpreted by the jvm.
%define libdir %{_exec_prefix}/lib

Summary: JDBI - A convenience library that wraps JDBC
Name: jdbi
Version: 2.39.1
Release: 1
License: Apache 2
URL: http://www.jdbi.org
Source0: %{name}-%{version}.jar
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: java >= 1.6


%description
JDBI is a SQL convenience library for Java. It attempts to expose relational
database access in idiommatic Java, using collections, beans, and so on, while
maintaining the same level of detail as JDBC. It exposes two different style
APIs, a fluent style and a sql object style.


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
* Tue Nov 20 2012 Chris Westin <cwestin@fedora-16-jetty> - 2.39.1-1
- Initial build.
