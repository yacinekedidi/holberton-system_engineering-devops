# Add HTTP header Puppet

exec { 'Nginx Header':
command => 'sudo apt-get -y install haproxy;
echo "ENABLED=1" >> /etc/default/haproxy;
printf %s "listen holb
    bind *:80
    mode http
    balance roundrobin
    server 1432-web-01 35.190.159.176:80 check
    server 1432-web-02 35.229.61.48:80 check
" >> /etc/haproxy/haproxy.cfg;
sudo service haproxy restart;
',
provider   => 'shell',
}
