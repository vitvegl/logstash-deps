Gem::Specification.new do |spec|
  spec.name = "insist"
  spec.version = "1.0.0"
  spec.summary = "A simple block-driven assertion library for both testing and for production code"
  spec.description = "This gem provides simple block-driven assertion library for both testing and for production code"
  spec.license = "Apache 2"
  spec.add_dependency "cabin", "~> 0.7", ">= 0.7.0"

  files = []
  dirs = %w{lib}
  dirs.each do |dir|
    files += Dir["#{dir}/**/*"]
  end

  files << 'lib/insist.rb'

  spec.files = files
  spec.require_paths << 'lib'
  spec.bindir = 'bin'
  spec.authors = ["Jordan Sissel"]
  spec.email = ["jls@semicomplete.com"]
  #spec.homepage = "..."
end
