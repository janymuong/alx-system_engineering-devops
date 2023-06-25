# puppet script - configure ssh authentication:

file_line { 'Turn off passwd auth':
  ensure => 'present',
  path  => '/etc/ssh/sshd_config',
  line  => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => 'present',
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
}

service { 'ssh':
  ensure => running,
  enable => true,
}
