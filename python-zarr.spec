%global _empty_manifest_terminate_build 0
Name:		python-zarr
Version:	2.4.0
Release:	2
Summary:	An implementation of chunked, compressed, N-dimensional arrays for Python.
License:	MIT
URL:		https://github.com/zarr-developers/zarr-python
Source0:	https://files.pythonhosted.org/packages/a3/87/383d77399148ef0772da3472b513ecf143252e7c365c51b0f06714800366/zarr-2.4.0.tar.gz
BuildArch:	noarch


%description
Zarr is a Python package providing an implementation of compressed, chunked, N-dimensional arrays, designed for use in parallel computing. See the [documentation](https://zarr.readthedocs.io) for more information.

%package -n python3-zarr
Summary:	An implementation of chunked, compressed, N-dimensional arrays for Python.
Provides:	python-zarr
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%description -n python3-zarr
python3 package for zarr

%package help
Summary:	Development documents and examples for zarr
Provides:	python3-zarr-doc
%description help
help package for zarr

%prep
%autosetup -n zarr-2.4.0

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-zarr -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Tue May 24 2022 YukariChiba <i@0x7f.cc>
- Add missing dependency

* Wed Jun 24 2020 BruceGW <gyl93216@163.com>
- init package
