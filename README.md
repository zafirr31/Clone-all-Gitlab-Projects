

## Clone all Gitlab Projects

Usage: `python main.py`

You must set gitlab ssh key to use. You can set it [here](https://gitlab.com/profile/keys).

You must also set ssh config file. Example:

```
Host gitlab.com
	Hostname altssh.gitlab.com
	Port 443
	Identityfile ~/.ssh/id_rsa
```