#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-bleach
Version  : 6.0.0
Release  : 71
URL      : https://files.pythonhosted.org/packages/7e/e6/d5f220ca638f6a25557a611860482cb6e54b2d97f0332966b1b005742e1f/bleach-6.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/7e/e6/d5f220ca638f6a25557a611860482cb6e54b2d97f0332966b1b005742e1f/bleach-6.0.0.tar.gz
Summary  : An easy safelist-based HTML-sanitizing tool.
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: pypi-bleach-license = %{version}-%{release}
Requires: pypi-bleach-python = %{version}-%{release}
Requires: pypi-bleach-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(six)
BuildRequires : pypi(webencodings)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
======
Bleach
======
.. image:: https://github.com/mozilla/bleach/workflows/Test/badge.svg
:target: https://github.com/mozilla/bleach/actions?query=workflow%3ATest

%package license
Summary: license components for the pypi-bleach package.
Group: Default

%description license
license components for the pypi-bleach package.


%package python
Summary: python components for the pypi-bleach package.
Group: Default
Requires: pypi-bleach-python3 = %{version}-%{release}

%description python
python components for the pypi-bleach package.


%package python3
Summary: python3 components for the pypi-bleach package.
Group: Default
Requires: python3-core
Provides: pypi(bleach)
Requires: pypi(six)
Requires: pypi(webencodings)

%description python3
python3 components for the pypi-bleach package.


%prep
%setup -q -n bleach-6.0.0
cd %{_builddir}/bleach-6.0.0
pushd ..
cp -a bleach-6.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1674525557
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-bleach
cp %{_builddir}/bleach-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-bleach/2712eb1e3c7cc1e80a68d7eea6acb5299222f242 || :
cp %{_builddir}/bleach-%{version}/bleach/_vendor/html5lib-1.1.dist-info/LICENSE %{buildroot}/usr/share/package-licenses/pypi-bleach/5bd527c7e2297d365b33ea67a400b6ba995e3705 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-bleach/2712eb1e3c7cc1e80a68d7eea6acb5299222f242
/usr/share/package-licenses/pypi-bleach/5bd527c7e2297d365b33ea67a400b6ba995e3705

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
