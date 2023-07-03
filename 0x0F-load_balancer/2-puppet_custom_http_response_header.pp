# script add a custom HTTP header with Puppet

class { 'nginx':
  # Install Nginx package
}

# Install required puppet modules
package { 'puppet-nginx':
  ensure => installed,
}

# create index.html file served out by the server
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

# create 404.html file
file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
}

# configure Nginx with custom response header
nginx::resource::server { 'default':
  ensure       => present,
  listen_port  => '80',
  root         => '/var/www/html',
  index_files  => ['index.html', 'index.htm'],
  server_name  => '_',
  location_cfg => [
    {
      'location' => '/redirect_me',
      'return'   => '301 https://stackoverflow.com/',
    },
    {
      'location' => '/404',
      'root'     => '/var/www/html',
      'internal' => true,
    },
  ],
  add_header   => {
    'X-Served-By' => '$hostname',
  },
}
