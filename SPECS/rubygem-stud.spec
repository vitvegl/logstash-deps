%global gem_name  stud

Name:             rubygem-%{gem_name}
Version:          0.0.22
Release:          1%{?dist}.qg
Summary:          Common software patterns

Group:            Logstash/Dependencies
License:          Apache v2.0
URL:              https://github.com/jordansissel/ruby-stud
Source0:          https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:         ruby(release)
Requires:         ruby(rubygems)

Requires:         rubygem(diff-lcs) >= 1.2.0
Requires:         rubygem(diff-lcs) < 2.0

Requires:         rubygem(insist) = 1.0.0
Requires:         rubygem(rspec) = 3.1.0
Requires:         rubygem(rspec-core) >= 3.1.0
Requires:         rubygem(rspec-expectations) >= 3.1.0
Requires:         rubygem(rspec-mocks) >= 3.1.0

BuildRequires:    rubygem-rspec
BuildArch:        noarch

%if 0%{?fc20} || 0%{?el7}
Provides:         rubygem(%{gem_name}) = %{version}
%endif

%global __requires_exclude ^/usr/bin/ruby$

%description
Ruby's stdlib is missing many things I use to solve most of my software problems.
Things like like retrying on a failure, supervising workers, resource pools, etc.

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
#bundle install

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%{!?_licensedir:%global license %%doc}
%{gem_dir}
#%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}

%changelog
* Wed Feb 3 2016 <vitvegl@quintagroup.org> - 0.0.22-1
- initial build
