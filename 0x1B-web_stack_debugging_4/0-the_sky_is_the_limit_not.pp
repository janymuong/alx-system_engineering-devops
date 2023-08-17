# manifest file: 0-the_sky_is_the_limit_solved.pp
# increase the open file limit for Nginx using the exec resource:

exec { 'fix--for-nginx':
  onlyif  => 'test -e /etc/default/nginx',
  command => 'sed -i "5s/[0-9]\+/$( ulimit -n )/" /etc/default/nginx; service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
