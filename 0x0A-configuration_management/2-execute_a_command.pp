# kill process
exec { 'kill_process'
command => 'pkill -f killmenow',
path    => ['/usr/bin/', '/usr/local/bin/', '/bin/'],
}
