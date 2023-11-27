#!/usr/bin/env bash
#Practice with puppet

file { '/etc/ssh/ssh_config':
	ensure => present,
	content =>"
	#SSH client config
	Host*
	IdentityFile ~/.ssh/school
	PasswordAuthenticate no
	",
}
