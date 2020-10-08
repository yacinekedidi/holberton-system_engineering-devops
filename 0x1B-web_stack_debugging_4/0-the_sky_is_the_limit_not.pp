#  Sky is the limit, let's bring that limit higher
exec { 'nginx':
command => 'sed -i "5s/[0-9]\+/4096/" /etc/default/nginx; sudo service nginx restart',
path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
