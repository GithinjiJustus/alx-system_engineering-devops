# 100-puppet_ssh_config.pp

# Configure the SSH client to use the private key and refuse password authentication
file_line { 'Declare identity file':
  path  => $file_path,
  line  => '    IdentityFile ~/.ssh/school',
  match => '    IdentityFile',
}

file_line { 'Turn off passwd auth':
  path  => $file_path,
  line  => '    PasswordAuthentication no',
  match => '    PasswordAuthentication',
}
