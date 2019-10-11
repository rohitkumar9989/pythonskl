# Ansible playbook example

## Ansible docs

https://docs.ansible.com/

## Install

```
pip install ansible ansible-lint
```

## Lint for ansible playbooks

```
ansible-lint playbook.yml
ansible-playbook -i hosts playbook.yml --list-hosts
```

## Run playbook

```
ansible-playbook -i hosts playbook.yml
ansible-playbook -i hosts ping.yml
ansible-playbook -i hosts ping.yml  -c local -u test -k
```
