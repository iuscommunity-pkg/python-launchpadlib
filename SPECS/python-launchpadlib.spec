%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

#python major version
%{expand: %%define pyver %(%{__python} -c 'import sys;print(sys.version[0:3])')}

Name:		python-launchpadlib	
Version:	1.9.8
Release:	1.ius%{?dist}
Summary:	A free Python library for scripting Launchpad through its web services interface.

Group:		Applicatons/System
License:	GPLv3
URL:		https://launchpad.net/launchpadlib
Source0:	http://launchpad.net/launchpadlib/trunk/1.9.8/+download/launchpadlib-1.9.8.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	python, python-setuptools
Requires:	python, python-oauth, python-httplib2	

%description
A free Python library for scripting Launchpad through its web services interface.

%prep
%setup -q -n launchpadlib-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 \
		    --skip-build \
	     --root %{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc PKG-INFO README.txt COPYING.txt HACKING.txt
%{python_sitelib}/launchpadlib-%{version}-py%{pyver}.egg-info/
%{python_sitelib}/launchpadlib/

%changelog
* Tue Jun 07 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.9.8-1.ius
- Initial spec
