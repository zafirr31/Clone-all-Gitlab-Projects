

from requests import get, post
import sys
import json
import os

token = ''

def list_all_groups():
	headers = {"Content-Type": "application/json", "PRIVATE-TOKEN": token}

	r = get('https://gitlab.com/api/v4/groups/', headers=headers)
	parsed = json.loads(r.text)
	for i in parsed:
		print("Name: {}\nID: {}\n".format(i["full_name"], i["id"]))


def clone_by_group_id(path='.', group_id = -1, per_page = 1):
	number_of_pages = ((per_page-1) // 100) + 1
	if(group_id == -1):
		print("Group id is required")
		return
	headers = {"Content-Type": "application/json", "PRIVATE-TOKEN": token}
	# Get all projects in group
	projects = []
	for i in range(number_of_pages):
		r = get('https://gitlab.com/api/v4/groups/{}/projects?per_page=100&include_subgroups=1&page={}'.format(group_id, i), headers=headers)
		parsed = json.loads(r.text)
		for j in parsed:
			projects.append({"name": j["path"], "url": j["ssh_url_to_repo"]})

	for i in projects:
		os.system('mkdir {}/{} ; git clone {} {}/{} ;'.format(path, i["name"], i["url"], path, i["name"]))

def print_menu():
	print("Choice List:")
	print("1. List all Groups")
	print("2. Clone all repos in group")
	print("3. Exit")
	return int(input("Choice: "))

def menu():
	while(True):
		choice = print_menu()
		if(choice == 1):
			list_all_groups()
		elif(choice == 2):
			path = input("Input directory to clone to: ")
			group_id = int(input("Input group id: "))
			per_page = int(input("Number of repos to clone (upper bound): "))
			clone_by_group_id(path, group_id, per_page)
		elif(choice == 3):
			break
		else:
			print("Unknown choice")


if __name__ == '__main__':
	while(token == ''):
		token = input("Input gitlab api token: ")
	menu()
	print("Goodbye~")