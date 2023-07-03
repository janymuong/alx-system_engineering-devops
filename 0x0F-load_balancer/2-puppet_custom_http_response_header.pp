# script add a custom HTTP header with Puppet

$x_header = "add_header X-Served-By ${hostname};"

exec { 'update':
  command => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  ensure  => installed,
  require => Exec['update']
}
-> file_line { 'redirection, 301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me  https://stackoverflow.com/ permanent;',
}
-> file_line { 'custom HTTP response Header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => $x_header,
}
-> file { '/var/www/html/index.html':
  content => 'Hello World!',
}
-> service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
