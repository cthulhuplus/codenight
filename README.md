# Code Night
Repo for Code Night projects, planning, and activities.

## Project Ideas
Automate the provisioning of a LAMP stack
* Could be broken down into smaller activities
  * Automate the provisioning of a web server; Apache, Nginx, Litespeed, etc... and PHP
  * Automate the provisioning of a database server; MySQL, MariaDB, PostGres, etc...

Check for system health
 * Get service status (modular)
 * Check pings
 I know this can be done with a billion different programs but imagine you can justify the cost or you are behind a secure network

Python toolkit
 * check for which binary is used
 * check for version
 * check installed modules
 * check module versions
 * install anaconda, miniconda, alternatives

File encrptor 
 * openssl lets you encypt files
  Encrypt:
   openssl aes-256-cbc -a -salt -in secrets.txt -out secrets.txt.enc
  Decrypt:
   openssl aes-256-cbc -d -a -in secrets.txt.enc -out secrets.txt.new

Identify tasks/complex commands in your life/work that could be automated/scripted

## Documentation as Code
Write and comment your code well enough that your peers can understand and follow what your script does.  This will also help reinforce your understanding of what each piece of your code does.
