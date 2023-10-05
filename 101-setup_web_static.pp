# 101-setup_web_static.pp

# Ensure Nginx is installed
package { 'nginx':
  ensure => 'installed',
}

# Create necessary directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
}

# Create a fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n',
}

# Ensure ownership is set to ubuntu
exec { 'set_ownership':
  command => 'chown -R ubuntu:ubuntu /data',
  path    => ['/bin', '/usr/bin'],
  creates => '/data/web_static/releases/test/index.html',
}

# Configure Nginx to serve the content
file { '/etc/nginx/sites-available/default':
  ensure => 'file',
  content => template('path/to/your/nginx-config-file.erb'), # Replace with the actual path to your Nginx config file
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  require => File['/data/web_static/releases/test/index.html'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}

