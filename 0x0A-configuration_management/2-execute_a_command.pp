# kill process
exec { 'killmenow'
command => 'pkill -f killmenow',
path    => '/usr/bin/env',
}
