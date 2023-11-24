#!/usr/bin/pup
# installing a package using puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
