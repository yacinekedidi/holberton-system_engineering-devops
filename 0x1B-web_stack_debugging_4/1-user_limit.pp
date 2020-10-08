#  User limit
exec { 'OS config':
command => 'sudo echo "fs.file-max = 65536" >> /etc/sysctl.conf ; sudo sysctl -p',
path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
