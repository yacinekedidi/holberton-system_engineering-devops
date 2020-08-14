#  custom HTTP header response, but with Puppet.
exec {'header':
command  => 'sudo apt-get update -y; 
sudo apt-get install nginx -y; 
echo "ENABLED=1" >> /etc/default/haproxy;
printf %s "frontend load_balancer
    bind *:80
    mode http
    default_backend holb
    
backend holb
    balance roundrobin
    server 1432-web-01 35.190.159.176:80 check
    server 1432-web-02 35.229.61.48:80 check" >> /etc/haproxy/haproxy.cfg;
service nginx restart;',
provider => "shell",
}
