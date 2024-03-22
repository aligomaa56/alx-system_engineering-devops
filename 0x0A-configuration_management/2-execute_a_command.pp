# Puppet manifest to kill a process named killmenow
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => ['/usr/bin', '/bin'],
  refreshonly => true,
}
