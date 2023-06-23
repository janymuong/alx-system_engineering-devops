# pip install Python Flask package from PIP

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
