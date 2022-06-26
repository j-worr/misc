# Github CLI & API one-liners

## gh list all Org repos in Github to file
Requires gh (https://github.com/cli/cli#installation)

```
gh repo list ORG_NAME -L300 --json name --jq '.[].name' > current_repos_in_github
```
Adding -L300 for 300 repo limit as default is only 30, adjust as necessary

## gh list all repos in Org, pushed at time, and languages and output as CSV

```
gh repo list ORG_NAME -L300 --json name,pushedAt,languages | jq -j '("repo",",","pushedAt",",","languages","\n",(.[]|.name,",",.pushedAt,",",(.languages[]|.node.name," "),"\n"))' > github_all_repo_list.csv
```

## API List Org Repos (all Repo data)

```
curl   -H "Accept: application/vnd.github.v3+json"  -H "Authorization: token PERSONAL_ACCESS_TOKEN"   https://api.github.com/orgs/ORG/repos
```

## API Org List Repo Names

```
curl   -H "Accept: application/vnd.github.v3+json"  -H "Authorization: token PERSONAL_ACCESS_TOKEN"   https://api.github.com/orgs/ORG/repos | jq -r '.[].name'
```

Sample output:

repo1
repo2


## API Org List Repo Name and Main Language

```
curl   -H "Accept: application/vnd.github.v3+json"  -H "Authorization: token PERSONAL_ACCESS_TOKEN"   https://api.github.com/orgs/ORG/repos | jq -r '.[]|"\(.name) \(.language)"'
```
