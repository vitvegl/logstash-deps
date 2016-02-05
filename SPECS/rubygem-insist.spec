%global gem_name  insist

Name:             rubygem-%{gem_name}
Version:          1.0.0
Release:          1%{?dist}.qg
Summary:          A simple block-driven assertion library for both testing and for production code

Group:            Logstash/Dependencies
License:          Apache v2.0
URL:              https://rubygems.org/downloads/%{gem_name}-%{version}.gem
Source0:          https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:          %{gem_name}.gemspec
#Patch0:           %{gem_name}-gemspec.patch

Requires:         ruby(release)
Requires:         ruby(rubygems)
Requires:         rubygem(diff-lcs) >= 1.1.2
Requires:         rubygem(rspec) >= 2.8.0
Requires:         rubygem(rspec-core) >= 2.8.0
Requires:         rubygem(rspec-expectations) >= 2.8.0
Requires:         rubygem(rspec-mocks) = 2.8.0
BuildRequires:    rubygem(rspec) >= 2.8.0
BuildArch:        noarch

%if 0%{?fc20} || 0%{?el7}
Provides:         rubygem(%{gem_name}) = %{version}
%endif

%global __requires_exclude ^/usr/bin/ruby$

%description
A simple block-driven assertion library for
both testing and for production code

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
#gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
#sed -i "s|\"Rakefile\",||g" %{gem_name}.gemspec
cp -v %{SOURCE1} %{gem_name}.gemspec
#%patch0
%{__git} init %{-q}

%build
make package
%make_install
#gem build %{gem_name}.gemspec
#%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
%make_install

%files
%{!?_licensedir:%global license %%doc}
%{gem_dir}
#%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}

%changelog
* Wed Feb 3 2016 <vitvegl@quintagroup.org> - 1.0.0-1
- initial build
- patching gemspec
