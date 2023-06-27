# puppet: install and configure Ngin

class { 'nginx':
  ensure  => installed,
  require => Package['nginx'],
}

file_line { 'Add redirection, 301':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://stackoverflow.com/ permanent;',
  require => Class['nginx'],
  notify  => Service['nginx'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
