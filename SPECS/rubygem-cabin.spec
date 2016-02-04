%global gem_name  cabin

Name:             rubygem-%{gem_name}
Version:          0.8.1
Release:          1%{?dist}.qg
Summary:          Structured+contextual logging experiments in Ruby

Group:            Logstash/Dependencies
License:          Apache v2.0
URL:              https://github.com/jordansissel/ruby-cabin
#Source0:          https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source0:          %{gem_name}-%{version}.gem

%if 0%{?fc20} || 0%{?el7}
Requires:         ruby(release)
Requires:         ruby(rubygems)
Requires:         rubygem-json
Requires:         rubygem-ffi = 1.0.11
Requires:         rubygem-ffi-rzmq = 0.9.3
Requires:         rubygem-minitest
Requires:         rubygem-simplecov
%endif

BuildRequires:    rubygem-rake >= 10.4.2
BuildRequires:    rubygems-devel
BuildRequires:    rubygem-minitest
BuildArch:        noarch

%if 0%{?fc20} || 0%{?el7}
Provides:         rubygem(%{gem_name}) = %{version}
%endif

%global __requires_exclude ^/usr/bin/ruby$

%description
This is an experiment to try and make logging more flexible and more consumable.
Plain text logs are bullshit, let's emit structured and contextual logs.
Metrics, too!

%package doc
Summary:          Documentation for %{name}
Group:            Documentation
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

sed -i "s|\"Rakefile\",||g" %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* %{buildroot}%{_bindir}/

# set executable
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

#%check
#pushd .%{gem_instdir}
#  ruby -I"lib:." test/test_helper.rb
#popd

%files
#%{!?_licensedir:%global license %%doc}
#%dir %{gem_instdir}
#%license %{gem_instdir}/LICENSE
%{_bindir}/rubygems-%{gem_name}-test
#%{gem_instdir}/bin
#%{gem_libdir}
%{gem_dir}
%exclude %{gem_cache}
#%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/test

%changelog
* Wed Feb 3 2016 <vitvegl@quintagroup.org> - 0.8.1-1
- initial build
- https://github.com/vitvegl/ruby-cabin/commit/17f6afdb83fa57bea7eead116ddc77561a8262a3
