# Puppet manifest to install Flask package

package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}