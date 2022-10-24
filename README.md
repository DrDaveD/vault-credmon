# HTCondor Vault CredMon

NOTE: This is obsolete.  This code has been integrated into HTCondor and
  development continued there.

The HTCondor Vault CredMon monitors and refreshes credentials
that are being managed by the HTCondor CredD. 
The CredMon will then monitor and refresh these tokens by reading from
Vault, and HTCondor can use and/or send the tokens with users' jobs as
requested by the user.

### Prerequisites

* HTCondor 8.8.2+
* Python 2.6+

## Installation

On a RHEL-based Linux distributions (RHEL7 only at this time), we
recommend installing the Vault CredMon by first
[installing and enabling an OSG 3.5+ yum repository](https://opensciencegrid.org/docs/common/yum/),
and then using `yum` to install the CredMon:
```sh
yum install python3-vault-credmon
```
Or you can grab and install the latest RPM
[from our GitHub releases](../../releases).

If you use yum or an RPM, example configuration and submit files will
be stored under
`/usr/share/doc/python3-vault-credmon-%{version}/`.

For other distributions, you can use `pip` to install the latest
version from GitHub and refer to the
[example configuration and submit files](examples) inside the GitHub
repository:
```sh
pip install git+https://github.com/htcondor/vault-credmon
```
Be sure to read the note below about the credential directory.

### Note about the credential directory

If you are installing the CredMon using `pip`, the credential directory
(`SEC_CREDENTIAL_DIRECTORY_OAUTH = /var/lib/condor/oauth_credentials`
in the example config file) may need to be manually created and should
be owned by the group condor with the SetGID bit set and group write
permissions:
```sh
mkdir -p /var/lib/condor/oauth_credentials
chown root:condor /var/lib/condor/oauth_credentials
chmod 2770 /var/lib/condor/oauth_credentials
```
```
# ls -ld /var/lib/condor/oauth_credentials
drwxrws--- 3 root condor 4096 May  8 10:05 /var/lib/condor/oauth_credentials
```

### Note about daemon-to-daemon encryption

For *both submit and execute hosts*, HTCondor must be configured to
use encryption for daemon-to-daemon communication. You can check this
by running `condor_config_val SEC_DEFAULT_ENCRYPTION` on each host,
which will return `REQUIRED` or `PREFERRED` if encryption is enabled.
If encryption is not enabled, you should add the following to your HTCondor
configuration:
    ```
    SEC_DEFAULT_ENCRYPTION = REQUIRED
    ```

### Submit Host Admin Configuration

See the
[example HTCondor 50-vault-credmon.conf config file](examples/config/condor/50-vault-credmon.conf)
for configuring HTCondor with the CredD and CredMon.

