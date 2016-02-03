%global gem_name

Name:             rubygem-%{gem_name}
Version:          0.0.1
Release:          1%{?dist}
Summary:

Group:            Logstash/Dependencies
License:          Apache v2.0
URL:
Source0:          https://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fc20} || 0%{?el7}
Requires:         ruby(release)
Requires:         ruby(rubygems)
%endif

BuildRequires:    rubygems-devel
BuildArch:        noarch

%if 0%{?fc20} || 0%{?el7}
Provides:         rubygem(%{gem_name}) = %{version}
%endif

%global __requires_exclude ^/usr/bin/ruby$

%description

%package doc
Summary:          Documentation for %{name}
Group:            Documentation
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch

%description doc
Documentation for %{name}.

%prep
#%setup -q
gem unpack %{SOURCE0}

%setup -q -D -T -n %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# shebang fix
sed -i -e 's/#!/usr/bin/env ruby|#!/usr/bin/ruby|' bin/%{gem_name}

# clean up development-only file
rm Rakefile
sed -i "s|\"Rakefile\",||g" %{gem_name}.gemspec

%build
#%configure
#make %{?_smp_mflags}
gem build %{gem_name}.gemspec

%gem_install

# remove unneccessary gemspec
rm .%{gem_instdir}/%{gem_name}.gemspec

%install
#%make_install

mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* %{buildroot}%{_bindir}/

# set executable
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
  ruby -I"lib:." test/*.rb
popd

%files
#%doc
%{!?_licensedir:%global license %%doc}
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%{_bindir}/%{gem_name}
%{gem_instdir}/bin
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.rdoc
%exclude %{gem_instdir}/test

%changelog

