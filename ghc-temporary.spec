# generated by cabal-rpm-0.12.5
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name temporary
%global pkgver %{pkg_name}-%{version}

%ifnarch s390x
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           ghc-%{pkg_name}
Version:        1.2.1.1
Release:        4%{?dist}
Summary:        Portable temporary file and directory support

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
%if %{with tests}
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
%endif
# End cabal-rpm deps

%description
The functions for creating temporary files and directories in the base library
are quite limited. The unixutils package contains some good ones,
but they aren't portable to Windows. This library just repackages the
Cabal implementations of its own temporary file and folder functions
so that you can use them without linking against Cabal or depending on
it being installed.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install


%check
%cabal_test


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc CHANGELOG.md


%changelog
* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 1.2.1.1-4
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 1.2.0.4-1
- update to 1.2.1.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Jens Petersen <petersen@redhat.com> - 1.2.0.4-3
- refresh to cabal-rpm-0.11.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 26 2016 Jens Petersen <petersen@redhat.com> - 1.2.0.4-1
- update to 1.2.0.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 27 2014 Jens Petersen <petersen@redhat.com> - 1.2.0.3-1
- update to 1.2.0.3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul  8 2014 Jens Petersen <petersen@redhat.com> - 1.1.2.4-5
- update to cblrpm-0.8.11

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Jens Petersen <petersen@redhat.com> - 1.1.2.4-3
- update to new simplified Haskell Packaging Guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 08 2012 Jens Petersen <petersen@redhat.com> - 1.1.2.4-1
- update to 1.1.2.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 23 2012 Jens Petersen <petersen@redhat.com> - 1.1.2.3-2
- add license to ghc_files

* Tue Feb  7 2012 Jens Petersen <petersen@redhat.com> - 1.1.2.3-1
- BSD license

* Tue Feb  7 2012 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- spec file template generated by cabal2spec-0.25.4
