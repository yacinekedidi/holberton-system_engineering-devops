# make changes to our configuration file
file_line { 'add_line':
    ensure => 'present',
    line   => 'IdentityFile ~/.ssh/holberton\nPasswordAuthentication no',
    path   => '/etc/ssh/ssh_config',
}
